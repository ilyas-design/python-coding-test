from pricing.rules.percentage_discount_rule import PercentageDiscountRule


class TestPercentageDiscountRule:
    def test_smoke_keeps_constructor_value(self) -> None:
        rule = PercentageDiscountRule(percent=10)
        assert rule.percent == 10

    def test_common_cases(self) -> None:
        # TODO(candidate): Add nominal tests for percentage discount behavior.
        pass

    def test_edge_cases(self) -> None:
        # TODO(candidate): Add boundary/invalid input tests.
        pass

