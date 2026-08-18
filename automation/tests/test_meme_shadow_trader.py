import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "automation"))

from meme_shadow_trader import (
    MarketSnapshot,
    MemeShadowTrader,
    ShadowJournal,
    SignalState,
)


def snapshot(**overrides):
    values = dict(
        token="TEST",
        timestamp="2026-08-18T11:00:00Z",
        price_usd=0.01,
        liquidity_usd=500_000,
        market_cap_usd=2_000_000,
        social_acceleration=0.8,
        unique_author_acceleration=0.75,
        buyer_acceleration=0.85,
        volume_acceleration=0.8,
        liquidity_growth=0.7,
        holder_quality=0.8,
        deployer_quality=0.85,
        manipulation_risk=0.12,
        insider_distribution_risk=0.10,
        estimated_slippage_pct=0.6,
        price_extension_pct=18,
    )
    values.update(overrides)
    return MarketSnapshot(**values)


class MemeShadowTraderTests(unittest.TestCase):
    def test_attention_leading_price_can_be_actionable(self):
        decision = MemeShadowTrader().decide(snapshot())
        self.assertEqual(SignalState.ACTIONABLE, decision.state)
        self.assertEqual(0.01, decision.simulated_entry_price_usd)
        self.assertGreaterEqual(decision.opportunity_score, 68)

    def test_low_liquidity_is_invalidated_even_with_strong_social_signals(self):
        decision = MemeShadowTrader().decide(snapshot(liquidity_usd=20_000))
        self.assertEqual(SignalState.INVALIDATED, decision.state)
        self.assertIsNone(decision.simulated_entry_price_usd)
        self.assertTrue(any("liquidity" in reason for reason in decision.thesis))

    def test_distribution_after_large_extension_is_exit(self):
        decision = MemeShadowTrader().decide(snapshot(
            insider_distribution_risk=0.55,
            price_extension_pct=100,
            manipulation_risk=0.20,
        ))
        self.assertEqual(SignalState.EXIT, decision.state)
        self.assertIsNone(decision.simulated_entry_price_usd)

    def test_excessive_slippage_is_hard_failure(self):
        decision = MemeShadowTrader().decide(snapshot(estimated_slippage_pct=5.0))
        self.assertEqual(SignalState.INVALIDATED, decision.state)

    def test_shadow_journal_is_append_only_and_replayable(self):
        trader = MemeShadowTrader()
        with tempfile.TemporaryDirectory() as tmp:
            journal = ShadowJournal(Path(tmp) / "shadow.jsonl")
            journal.append(trader.decide(snapshot(token="ONE")))
            journal.append(trader.decide(snapshot(token="TWO", liquidity_usd=50_000)))
            rows = journal.read_all()
            self.assertEqual(2, len(rows))
            self.assertEqual("ONE", rows[0]["token"])
            self.assertEqual("ACTIONABLE", rows[0]["state"])
            self.assertEqual("INVALIDATED", rows[1]["state"])


if __name__ == "__main__":
    unittest.main()
