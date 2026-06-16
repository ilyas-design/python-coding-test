from pricing.models.line_item import LineItem
from pricing.rules.no_discount_rule import NoDiscountRule
from pricing.models.order import Order
from pricing.pricing_engine import PricingEngine


def main() -> None:
    order = Order(
        items=(
            LineItem(name="notebook", unit_price=5.0, quantity=3),
            LineItem(name="pen", unit_price=2.5, quantity=2),
        )
    )

    engine = PricingEngine(rule=NoDiscountRule())
    total = engine.calculate_total(order)

    print(f"Order total (no discount): {total:.2f}")


if __name__ == "__main__":
    main()

