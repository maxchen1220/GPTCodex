"""Technical analysis agent using basic moving averages."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from .base import Analysis, Agent

# Sample closing price history (last 9 days) for selected symbols
SAMPLE_PRICE_HISTORY: Dict[str, List[float]] = {
    "AAPL": [187.2, 188.5, 189.0, 188.0, 189.4, 190.1, 189.8, 189.5, 189.25],
    "TSLA": [255.0, 253.4, 250.0, 248.9, 249.5, 247.0, 248.0, 247.8, 247.59],
    "BTC-USD": [100_500, 100_800, 101_200, 101_500, 101_700, 101_300, 101_400, 101_450, 101_500],
}


def _ema(prices: List[float], period: int) -> float:
    """Compute exponential moving average for the given ``period``."""
    k = 2 / (period + 1)
    ema = prices[0]
    for price in prices[1:]:
        ema = price * k + ema * (1 - k)
    return ema


@dataclass
class TechnicalAnalysisAgent:
    name: str = "technical_analysis"

    def analyze(self, symbol: str) -> Analysis:
        prices = SAMPLE_PRICE_HISTORY.get(symbol.upper())
        if not prices:
            data = {"ema9": 0.0, "trend": "unknown"}
        else:
            ema9 = _ema(prices[-9:], 9)
            current_price = prices[-1]
            trend = "bullish" if current_price > ema9 else "bearish"
            data = {"ema9": round(ema9, 2), "trend": trend, "price": current_price}
        return Analysis(agent=self.name, data=data)
