import pytest

from pricing.rules.fixed_amount_discount_rule import FixedAmountDiscountRule


class TestFixedAmountDiscountRule:
    def test_smoke_keeps_constructor_value(self) -> None:
        rule = FixedAmountDiscountRule(amount=12.5)
        assert rule.amount == 12.5

    def test_common_cases(self) -> None:
        rule = FixedAmountDiscountRule(amount=15)
        assert rule.apply(100) == 85  # 100 - 15 = 85
        assert rule.apply(0) == -15   # 0 - 15 = -15

        no_discount = FixedAmountDiscountRule(amount=0)
        assert no_discount.apply(50) == 50  # 0 off = no change

    def test_edge_cases(self) -> None:
        rule = FixedAmountDiscountRule(amount=15)
        assert rule.apply(15) == 0  # 15 - 15 = 0

        with pytest.raises(ValueError):
            FixedAmountDiscountRule(amount=-1)  # negative amount

        with pytest.raises(ValueError):
            rule.apply(-5)  # negative subtotal
