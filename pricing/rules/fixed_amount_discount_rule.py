from pricing.rules.pricing_rule import PricingRule


class FixedAmountDiscountRule(PricingRule):
    def __init__(self, amount: float) -> None:
        # amount must be strictly positive
        if amount < 0:
            raise ValueError("amount must always be >= 0")
        # Set amount
        self.amount = amount

    def apply(self, subtotal: float) -> float:
        # Error if subtotal is negative
        if subtotal < 0:
            raise ValueError("subtotal must always be >= 0")
        # Apply fixed amount discount
        return subtotal - self.amount

