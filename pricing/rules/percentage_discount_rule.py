from pricing.rules.pricing_rule import PricingRule


class PercentageDiscountRule(PricingRule):
    def __init__(self, percent: float) -> None:
        # percent between 0 and 100
        if percent < 0 or percent > 100:
            # Error if percent is not between 0 and 100
            raise ValueError("percent must always be between 0 and 100")
        # Set percent
        self.percent = percent

    def apply(self, subtotal: float) -> float:
        if subtotal < 0:
            # Error if subtotal is negative
            raise ValueError("subtotal must always be >= 0")
        # Apply percentage discount
        return subtotal * (1 - self.percent / 100)

