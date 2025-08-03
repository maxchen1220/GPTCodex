"""News analyzer agent using sample headlines."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from .base import Analysis, Agent

SAMPLE_NEWS: Dict[str, List[str]] = {
    "AAPL": [
        "Apple releases new product line to strong reviews",
        "Investors optimistic about upcoming earnings report",
    ],
    "TSLA": [
        "Tesla faces safety probe after recent recalls",
        "Analysts question valuation amid market volatility",
    ],
    "BTC-USD": [
        "Bitcoin holds steady as market awaits regulatory clarity",
        "Major bank announces crypto custody service",
    ],
}

POSITIVE_WORDS = {"strong", "optimistic", "steady", "announces"}
NEGATIVE_WORDS = {"probe", "question", "volatility", "recall"}


def _headline_sentiment(headlines: List[str]) -> int:
    score = 0
    for line in headlines:
        words = {w.strip('.,').lower() for w in line.split()}
        score += len(words & POSITIVE_WORDS)
        score -= len(words & NEGATIVE_WORDS)
    return score


@dataclass
class NewsAnalyzerAgent:
    name: str = "news_analyzer"

    def analyze(self, symbol: str) -> Analysis:
        headlines = SAMPLE_NEWS.get(symbol.upper(), [])
        score = _headline_sentiment(headlines)
        sentiment = "positive" if score > 0 else "negative" if score < 0 else "neutral"
        data = {"headlines": headlines, "sentiment": sentiment, "score": score}
        return Analysis(agent=self.name, data=data)
