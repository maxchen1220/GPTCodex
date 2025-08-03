"""Social media sentiment agent using rudimentary analysis.

The agent looks up predefined sentiment values for the symbol. In production,
this would connect to social media APIs and perform NLP-based sentiment
analysis.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .base import Analysis, Agent

# Simple sentiment dictionary: 1 = positive, -1 = negative, 0 = neutral
SAMPLE_SENTIMENT: Dict[str, int] = {
    "AAPL": 1,
    "TSLA": -1,
    "BTC-USD": 0,
}

SENTIMENT_LABEL = {1: "positive", -1: "negative", 0: "neutral"}


@dataclass
class SocialMediaAgent:
    name: str = "social_media"

    def analyze(self, symbol: str) -> Analysis:
        score = SAMPLE_SENTIMENT.get(symbol.upper(), 0)
        data = {"sentiment": SENTIMENT_LABEL[score], "score": score}
        return Analysis(agent=self.name, data=data)
