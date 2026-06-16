from pricing.models.line_item import LineItem
from pricing.rules.no_discount_rule import NoDiscountRule
from pricing.models.order import Order
from pricing.pricing_engine import PricingEngine


class TestPricingEngine:
    def test_smoke_no_discount_rule(self) -> None:
        order = Order(items=(LineItem(name="book", unit_price=10.0, quantity=2),))
        engine = PricingEngine(rule=NoDiscountRule())
        assert engine.calculate_total(order) == 20.0

    def test_common_cases(self) -> None:
        # TODO(candidate): Add nominal tests for subtotal/total behavior.
        pass

    def test_edge_cases(self) -> None:
        # TODO(candidate): Add boundary/invalid input tests.
        pass


