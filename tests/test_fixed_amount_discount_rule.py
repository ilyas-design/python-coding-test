from pricing.rules.fixed_amount_discount_rule import FixedAmountDiscountRule


class TestFixedAmountDiscountRule:
    def test_smoke_keeps_constructor_value(self) -> None:
        rule = FixedAmountDiscountRule(amount=12.5)
        assert rule.amount == 12.5

    def test_common_cases(self) -> None:
        # TODO(candidate): Add nominal tests for fixed amount discount behavior.
        pass

    def test_edge_cases(self) -> None:
        # TODO(candidate): Add boundary/invalid input tests.
        pass

