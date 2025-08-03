"""Base classes for trading agents."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Protocol


@dataclass
class Analysis:
    """Structured output from an agent."""

    agent: str
    data: Dict[str, Any]


class Agent(Protocol):
    """Trading agent interface."""

    name: str

    def analyze(self, symbol: str) -> Analysis:  # pragma: no cover - interface
        """Run analysis for ``symbol`` and return structured data."""
        ...
