from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Iterable


class SignalState(str, Enum):
    IGNORE = "IGNORE"
    WATCH = "WATCH"
    PRIME = "PRIME"
    ACTIONABLE = "ACTIONABLE"
    EXIT = "EXIT"
    INVALIDATED = "INVALIDATED"


@dataclass(frozen=True)
class MarketSnapshot:
    token: str
    timestamp: str
    price_usd: float
    liquidity_usd: float
    market_cap_usd: float
    social_acceleration: float
    unique_author_acceleration: float
    buyer_acceleration: float
    volume_acceleration: float
    liquidity_growth: float
    holder_quality: float
    deployer_quality: float
    manipulation_risk: float
    insider_distribution_risk: float
    estimated_slippage_pct: float
    price_extension_pct: float


@dataclass(frozen=True)
class ScoreBreakdown:
    alpha_score: float
    risk_penalty: float
    opportunity_score: float
    state: SignalState
    reasons: tuple[str, ...]


@dataclass(frozen=True)
class ShadowDecision:
    token: str
    timestamp: str
    state: SignalState
    opportunity_score: float
    simulated_entry_price_usd: float | None
    thesis: tuple[str, ...]


@dataclass(frozen=True)
class RiskLimits:
    min_liquidity_usd: float = 100_000.0
    max_slippage_pct: float = 3.0
    max_manipulation_risk: float = 0.55
    max_insider_distribution_risk: float = 0.60
    max_price_extension_pct: float = 250.0


class MemeShadowTrader:
    """Research-only scoring engine.

    This module deliberately has no wallet, signing, RPC submission, exchange,
    broker, or money-movement capability. It produces shadow decisions only.
    """

    def __init__(self, limits: RiskLimits | None = None) -> None:
        self.limits = limits or RiskLimits()

    @staticmethod
    def _bounded(value: float) -> float:
        return max(0.0, min(1.0, value))

    def score(self, snapshot: MarketSnapshot) -> ScoreBreakdown:
        reasons: list[str] = []

        hard_failure = self._hard_failure(snapshot)
        if hard_failure:
            return ScoreBreakdown(
                alpha_score=0.0,
                risk_penalty=100.0,
                opportunity_score=0.0,
                state=SignalState.INVALIDATED,
                reasons=tuple(hard_failure),
            )

        alpha_components = {
            "social acceleration": (snapshot.social_acceleration, 18.0),
            "unique author acceleration": (snapshot.unique_author_acceleration, 12.0),
            "buyer acceleration": (snapshot.buyer_acceleration, 20.0),
            "volume acceleration": (snapshot.volume_acceleration, 16.0),
            "liquidity growth": (snapshot.liquidity_growth, 10.0),
            "holder quality": (snapshot.holder_quality, 12.0),
            "deployer quality": (snapshot.deployer_quality, 12.0),
        }
        alpha = sum(self._bounded(value) * weight for value, weight in alpha_components.values())

        risk = (
            self._bounded(snapshot.manipulation_risk) * 35.0
            + self._bounded(snapshot.insider_distribution_risk) * 30.0
            + self._bounded(snapshot.estimated_slippage_pct / self.limits.max_slippage_pct) * 20.0
            + self._bounded(snapshot.price_extension_pct / self.limits.max_price_extension_pct) * 15.0
        )

        score = max(0.0, min(100.0, alpha - risk * 0.55))

        if snapshot.social_acceleration >= 0.65 and snapshot.price_extension_pct <= 40:
            reasons.append("attention is accelerating before extreme price extension")
        if snapshot.buyer_acceleration >= 0.65 and snapshot.volume_acceleration >= 0.65:
            reasons.append("buyer and volume acceleration confirm market participation")
        if snapshot.liquidity_growth >= 0.50:
            reasons.append("liquidity is improving")
        if snapshot.insider_distribution_risk >= 0.45:
            reasons.append("insider distribution risk is elevated")
        if snapshot.manipulation_risk >= 0.40:
            reasons.append("manipulation risk is elevated")
        if snapshot.price_extension_pct >= 120:
            reasons.append("price is already materially extended")

        state = self._state_for(score, snapshot)
        return ScoreBreakdown(
            alpha_score=round(alpha, 2),
            risk_penalty=round(risk, 2),
            opportunity_score=round(score, 2),
            state=state,
            reasons=tuple(reasons),
        )

    def _hard_failure(self, snapshot: MarketSnapshot) -> list[str]:
        failures: list[str] = []
        if snapshot.liquidity_usd < self.limits.min_liquidity_usd:
            failures.append("liquidity below minimum research threshold")
        if snapshot.estimated_slippage_pct > self.limits.max_slippage_pct:
            failures.append("estimated slippage exceeds limit")
        if snapshot.manipulation_risk > self.limits.max_manipulation_risk:
            failures.append("manipulation risk exceeds limit")
        if snapshot.insider_distribution_risk > self.limits.max_insider_distribution_risk:
            failures.append("insider distribution risk exceeds limit")
        if snapshot.price_extension_pct > self.limits.max_price_extension_pct:
            failures.append("price extension exceeds chase limit")
        return failures

    @staticmethod
    def _state_for(score: float, snapshot: MarketSnapshot) -> SignalState:
        if snapshot.insider_distribution_risk >= 0.50 and snapshot.price_extension_pct >= 80:
            return SignalState.EXIT
        if score >= 68 and snapshot.price_extension_pct <= 80:
            return SignalState.ACTIONABLE
        if score >= 52:
            return SignalState.PRIME
        if score >= 32:
            return SignalState.WATCH
        return SignalState.IGNORE

    def decide(self, snapshot: MarketSnapshot) -> ShadowDecision:
        scored = self.score(snapshot)
        entry = snapshot.price_usd if scored.state is SignalState.ACTIONABLE else None
        return ShadowDecision(
            token=snapshot.token,
            timestamp=snapshot.timestamp,
            state=scored.state,
            opportunity_score=scored.opportunity_score,
            simulated_entry_price_usd=entry,
            thesis=scored.reasons,
        )


class ShadowJournal:
    """Append-only JSONL journal for reproducible shadow decisions."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def append(self, decision: ShadowDecision) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = asdict(decision)
        payload["state"] = decision.state.value
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, sort_keys=True) + "\n")

    def read_all(self) -> list[dict]:
        if not self.path.exists():
            return []
        records: list[dict] = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                records.append(json.loads(line))
        return records


def evaluate_stream(
    snapshots: Iterable[MarketSnapshot],
    trader: MemeShadowTrader | None = None,
) -> list[ShadowDecision]:
    engine = trader or MemeShadowTrader()
    return [engine.decide(snapshot) for snapshot in snapshots]
