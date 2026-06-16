from pricing.rules.pricing_rule import PricingRule


class PercentageDiscountRule(PricingRule):
    def __init__(self, percent: float) -> None:
        self.percent = percent

    def apply(self, subtotal: float) -> float:
        # TODO(candidate): Implement validation + percentage discount logic.
        pass

