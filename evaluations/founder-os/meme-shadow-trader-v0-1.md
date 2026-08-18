# Meme Shadow Trader v0.1

## Goal

Build a research-only memecoin momentum system that can discover and score candidate opportunities, reject unsafe setups, record simulated entries and exits, and generate an evidence base for later strategy evaluation without connecting to a wallet or moving money.

## Selected playbook

`playbooks/trading-system-research.md`

## Project assessment

- product type: fintech / trading research
- initial market: Solana memecoin spot markets
- stage: shadow trading only
- risk class: high
- capital at risk in v0.1: zero
- external execution authority: none

## Required capabilities

- market-data ingestion
- social-signal ingestion
- on-chain risk signals
- deterministic opportunity scoring
- explicit state machine
- manipulation and liquidity hard stops
- append-only decision journal
- outcome labeling
- backtesting and paper-trading adapters
- audit logging and reproducibility
- kill conditions before any future execution layer

## Initial resource selection

Internet-Well's existing trading fixture identifies LEAN, Freqtrade, Hummingbot, NautilusTrader, vectorbt, QuantStats, pytest, Docker Compose, and Testcontainers as research candidates according to actual requirements. v0.1 deliberately avoids binding the core scoring engine to any one framework so that its decisions can be replayed in multiple research environments.

## State machine

`IGNORE -> WATCH -> PRIME -> ACTIONABLE -> EXIT`

Any state may transition to `INVALIDATED` when a hard risk limit is breached.

## Hard no-trade conditions in v0.1

The research engine invalidates a candidate when any configured hard limit is breached, including minimum liquidity, maximum estimated slippage, manipulation risk, insider-distribution risk, or excessive price extension.

These thresholds are research defaults and must be calibrated from historical and shadow data before being treated as meaningful trading parameters.

## Implementation slice 1

`automation/meme_shadow_trader.py` provides:

- typed market snapshots;
- bounded alpha and risk scoring;
- deterministic opportunity states;
- explicit hard-failure rules;
- simulated entry recording only for `ACTIONABLE` decisions;
- append-only JSONL shadow journal;
- stream evaluation for replay/backtesting adapters.

The module intentionally contains no wallet, private key, signing, RPC submission, exchange, broker, leverage, or money-movement capability.

## Verification

Focused unit tests cover:

1. attention acceleration leading price can reach `ACTIONABLE`;
2. low liquidity invalidates a candidate even with strong social momentum;
3. insider distribution after material extension produces `EXIT`;
4. excessive slippage produces `INVALIDATED`;
5. the shadow journal records and replays decisions deterministically.

## Next slices

1. normalize DEX Screener market snapshots behind a read-only adapter;
2. define X/social feature contracts without embedding provider-specific logic in the scorer;
3. add Solana on-chain holder/deployer/manipulation feature adapters;
4. add outcome labeling at +1m, +5m, +15m, +1h, +6h, and +24h;
5. connect vectorbt/LEAN/Freqtrade adapters for replay and paper evaluation;
6. build strategy metrics for precision, expectancy, maximum adverse excursion, drawdown, and slippage-adjusted returns;
7. keep all wallet and execution capabilities out of scope until a separate explicit live-trading authorization and review.

## No-go gates

Do not add wallet credentials, deposit flows, transaction signing, autonomous swaps, leverage, derivatives, or live order routing in this phase. Historical or paper performance must not be represented as guaranteed future profitability.
