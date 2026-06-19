from pricing.models.line_item import LineItem
from pricing.models.order import Order
from pricing.pricing_engine import PricingEngine
from pricing.rules.fixed_amount_discount_rule import FixedAmountDiscountRule
from pricing.rules.no_discount_rule import NoDiscountRule
from pricing.rules.percentage_discount_rule import PercentageDiscountRule


class TestPricingEngine:
    def test_smoke_no_discount_rule(self) -> None:
        order = Order(items=(LineItem(name="book", unit_price=10.0, quantity=2),))
        engine = PricingEngine(rule=NoDiscountRule())
        assert engine.calculate_total(order) == 20.0

    def test_common_cases(self) -> None:
        order = Order(
            items=(
                LineItem(name="notebook", unit_price=5.0, quantity=3),
                LineItem(name="pen", unit_price=2.5, quantity=2),
            )
        )
        assert PricingEngine.calculate_subtotal(order) == 20.0  # 15 + 5

        engine = PricingEngine(rule=PercentageDiscountRule(percent=10))
        assert engine.calculate_total(order) == 18.0  # 10% off 20

        engine = PricingEngine(rule=FixedAmountDiscountRule(amount=5))
        assert engine.calculate_total(order) == 15.0  # 20 - 5

    def test_edge_cases(self) -> None:
        empty_order = Order(items=())
        engine = PricingEngine(rule=FixedAmountDiscountRule(amount=10))
        assert engine.calculate_total(empty_order) == 0.0  # 0 - 10 clamped to 0

        order = Order(items=(LineItem(name="book", unit_price=10.0, quantity=1),))
        engine = PricingEngine(rule=FixedAmountDiscountRule(amount=50))
        assert engine.calculate_total(order) == 0.0  # discount bigger than subtotal


