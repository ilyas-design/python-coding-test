import pytest

from pricing.rules.threshold_discount_rule import ThresholdDiscountRule


class TestThresholdDiscountRule:
    def test_smoke_keeps_constructor_values(self) -> None:
        rule = ThresholdDiscountRule(threshold=100, percent=10)
        assert rule.threshold == 100
        assert rule.percent == 10

    def test_common_cases(self) -> None:
        rule = ThresholdDiscountRule(threshold=100, percent=10)
        assert rule.apply(100) == 90   # reached threshold, 10% off
        assert rule.apply(150) == 135  # above threshold, 10% off
        assert rule.apply(50) == 50    # below threshold, no discount

    def test_edge_cases(self) -> None:
        rule = ThresholdDiscountRule(threshold=100, percent=10)
        assert rule.apply(0) == 0  # below threshold

        with pytest.raises(ValueError):
            ThresholdDiscountRule(threshold=-1, percent=10)  # negative threshold

        with pytest.raises(ValueError):
            ThresholdDiscountRule(threshold=100, percent=101)  # over 100%

        with pytest.raises(ValueError):
            rule.apply(-5)  # negative subtotal
