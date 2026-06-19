from pricing.rules.pricing_rule import PricingRule


class ThresholdDiscountRule(PricingRule):
    def __init__(self, threshold: float, percent: float) -> None:
        # threshold and percent must be valid
        if threshold < 0:
            raise ValueError("threshold must always be >= 0")
        if percent < 0 or percent > 100:
            raise ValueError("percent must always be between 0 and 100")
        # Set threshold and percent
        self.threshold = threshold
        self.percent = percent

    def apply(self, subtotal: float) -> float:
        # Error if subtotal is negative
        if subtotal < 0:
            raise ValueError("subtotal must always be >= 0")
        # Apply threshold discount
        if subtotal >= self.threshold:
            # Apply percentage discount
            return subtotal * (1 - self.percent / 100)
        return subtotal
