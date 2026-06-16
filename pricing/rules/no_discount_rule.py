from pricing.rules.pricing_rule import PricingRule


class NoDiscountRule(PricingRule):
    def apply(self, subtotal: float) -> float:
        return subtotal

