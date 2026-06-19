import pytest

from pricing.rules.percentage_discount_rule import PercentageDiscountRule


class TestPercentageDiscountRule:
    def test_smoke_keeps_constructor_value(self) -> None:
        rule = PercentageDiscountRule(percent=10)
        assert rule.percent == 10

    def test_common_cases(self) -> None:
        rule = PercentageDiscountRule(percent=10)
        assert rule.apply(100) == 90  # 10% off 100
        assert rule.apply(0) == 0     # discount on 0 stays 0

        no_discount = PercentageDiscountRule(percent=0)
        assert no_discount.apply(50) == 50  # 0% = no change

    def test_edge_cases(self) -> None:
        full_discount = PercentageDiscountRule(percent=100)
        assert full_discount.apply(50) == 0  # 100% off = free

        with pytest.raises(ValueError):
            PercentageDiscountRule(percent=-1)  # negative percent

        with pytest.raises(ValueError):
            PercentageDiscountRule(percent=101)  # over 100%

        rule = PercentageDiscountRule(percent=10)
        with pytest.raises(ValueError):
            rule.apply(-5)  # negative subtotal

