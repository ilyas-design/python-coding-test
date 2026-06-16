from pricing.models.order import Order
from pricing.rules.pricing_rule import PricingRule


class PricingEngine:
    def __init__(self, rule: PricingRule) -> None:
        self.rule = rule

    @staticmethod
    def calculate_subtotal(order: Order) -> float:
        return sum(item.unit_price * item.quantity for item in order.items)

    def calculate_total(self, order: Order) -> float:
        subtotal = self.calculate_subtotal(order)
        total = self.rule.apply(subtotal)
        # Safety net: the engine guarantees the final total is never negative,
        # regardless of what any rule returns. Rules themselves should NOT
        # duplicate this clamping — leave that responsibility here.
        return max(total, 0.0)

