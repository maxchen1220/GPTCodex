"""Market scanner agent using sample data.

This agent simulates scanning the market for the given symbol. In a real-world
scenario this would pull data from a market data provider.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .base import Analysis, Agent

# Sample static market data for demonstration purposes.
SAMPLE_MARKET_DATA: Dict[str, Dict[str, float]] = {
    "AAPL": {"price": 189.25, "volume": 150_000},
    "TSLA": {"price": 247.59, "volume": 98_000},
    "BTC-USD": {"price": 101_500.0, "volume": 3_200},
}


@dataclass
class MarketScannerAgent:
    name: str = "market_scanner"

    def analyze(self, symbol: str) -> Analysis:
        data = SAMPLE_MARKET_DATA.get(symbol.upper(), {"price": 0.0, "volume": 0.0})
        return Analysis(agent=self.name, data=data)
