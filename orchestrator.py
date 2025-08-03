"""Orchestrates communication between trading agents."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from agents import (
    Analysis,
    MarketScannerAgent,
    NewsAnalyzerAgent,
    SocialMediaAgent,
    TechnicalAnalysisAgent,
)


@dataclass
class TradingOrchestrator:
    """Coordinate multiple agents to produce a trade recommendation."""

    agents: List = field(
        default_factory=lambda: [
            MarketScannerAgent(),
            SocialMediaAgent(),
            TechnicalAnalysisAgent(),
            NewsAnalyzerAgent(),
        ]
    )

    def gather(self, symbol: str) -> Dict[str, Analysis]:
        """Run all agents for ``symbol`` and return a mapping of results."""
        results: Dict[str, Analysis] = {}
        for agent in self.agents:
            results[agent.name] = agent.analyze(symbol)
        return results

    def build_strategy(self, symbol: str) -> str:
        """Create a simple trading strategy using gathered data."""
        data = self.gather(symbol)
        market = data["market_scanner"].data
        tech = data["technical_analysis"].data

        price = market["price"]
        volume = market["volume"]
        ema9 = tech.get("ema9", 0)
        trend = tech.get("trend", "unknown")

        sector_links = {
            "AAPL": "QQQ",  # Technology sector
            "MSFT": "QQQ",  # Technology sector
            "TSLA": "XLY",  # Consumer discretionary sector
        }
        benchmark = sector_links.get(symbol.upper(), "SPY")

        primary_entry = round(price * 1.03, 2)
        secondary_entry = round(price * 0.98, 2)
        stop_loss = round(price * 0.97, 2)
        final_target = round(price * 1.08, 2)

        strategy = f"""ENTRY CRITERIA:
- Primary entry: ${primary_entry} on break of resistance with volume > {int(volume)} shares
- Secondary entry: ${secondary_entry} on pullback to VWAP if initial breakout occurs
- Entry time window: First 20 minutes of trading session

POSITION SIZING:
- 3% account risk
- 120 shares at primary entry
- Stop distance: ${round(primary_entry - stop_loss,2)} per share

RISK MANAGEMENT:
- Initial stop loss: ${stop_loss}
- Break-even stop: Move stop to entry once price reaches ${round(primary_entry*1.02,2)}

EXIT STRATEGY:
- Partial take profit (50%): When price crosses 9_ema ({ema9}) on 5 minute chart
- Final take profit: ${final_target} (measured move target) OR
- Time-based exit: Close position at market close if targets not reached

TRADE MANAGEMENT:
- Reduce position by 50% if {benchmark} breaks below its opening range low during the trade
- Trend according to technical analysis: {trend}
- DO NOT move stop loss downwards
"""
        return strategy
