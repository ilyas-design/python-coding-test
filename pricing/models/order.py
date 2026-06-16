from dataclasses import dataclass

from pricing.models.line_item import LineItem


@dataclass(frozen=True)
class Order:
    items: tuple[LineItem, ...]

