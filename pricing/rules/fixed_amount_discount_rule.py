from pricing.rules.pricing_rule import PricingRule


class FixedAmountDiscountRule(PricingRule):
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def apply(self, subtotal: float) -> float:
        # TODO(candidate): Implement validation + fixed amount discount logic.
        pass

