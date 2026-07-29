# Playbook: Trading-System Research and Risk Review

## Purpose

Evaluate an algorithmic or agent-driven trading system as a research system before any real-money use, without assuming profitability from a repository, backtest, or demonstration.

## Inputs

Strategy definition, markets, instruments, data sources, execution venue, code, costs, latency, capital limits, jurisdiction, account permissions, backtests, paper results, and risk constraints.

## Workflow

1. Define the hypothesis, signal, universe, holding period, execution, benchmark, and invalidation criteria.
2. Review data provenance, survivorship, look-ahead, leakage, selection, corporate actions, time zones, missing data, and licensing.
3. Reproduce backtests with realistic fees, spread, slippage, liquidity, latency, borrow, taxes where relevant, and failed orders.
4. Test out-of-sample, walk-forward, regime, stress, parameter sensitivity, and capacity.
5. Review position sizing, concentration, leverage, drawdown, kill switch, custody, credentials, reconciliation, and incident response.
6. Compare the candidate repo with simpler baselines and no-trade.
7. Permit only isolated simulation, then paper trading with fixed limits and independent monitoring.
8. Require a separate explicit decision before any live trading.

## Outputs

Strategy specification, data audit, reproduced results, bias findings, risk metrics, selected research resources, operational controls, paper-trading plan, and no-go criteria.

## Verification

Independently reproduce calculations; reconcile positions and fills; compare expected and observed costs; test exchange failures, stale data, duplicate orders, partial fills, clock drift, credential loss, and kill switch.

## Stop conditions

Stop before live trading, leverage, derivatives, transfers, account changes, credential entry, or presenting profitability as guaranteed. Reject systems whose central performance cannot be reproduced.

## Human review

Qualified financial, legal, tax, compliance, security, and quantitative professionals must review live-trading proposals, regulated activity, customer funds, investment advice, leverage, derivatives, market access, and material capital risk.
