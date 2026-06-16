from abc import ABC, abstractmethod


class PricingRule(ABC):
    @abstractmethod
    def apply(self, subtotal: float) -> float:
        """Transform a subtotal into a total."""

