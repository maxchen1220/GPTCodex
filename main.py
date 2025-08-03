"""Example entry point for the agentic trading bot."""

from __future__ import annotations

import argparse

from orchestrator import TradingOrchestrator


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a sample trading strategy")
    parser.add_argument("symbol", nargs="?", default="AAPL", help="Ticker symbol to analyze")
    args = parser.parse_args()

    orchestrator = TradingOrchestrator()
    strategy = orchestrator.build_strategy(args.symbol)
    print(strategy)


if __name__ == "__main__":  # pragma: no cover
    main()
