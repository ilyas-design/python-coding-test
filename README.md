# Python Exercise Template

This repository contains a **small coding exercise**.

## Goal of the exercise

Build and test a small pricing system using object-oriented design.

**Note:** You may use online resources or AI tools (though this is neither required nor particularly encouraged). Be
prepared to discuss your implementation in detail during the interview, and to explain and justify your choices as if
the work were entirely your own.

## Business context

A shop computes an order total from line items.

A pricing rule can transform the subtotal into a final total.

- The system already has a `PricingEngine` that accepts any rule inheriting from `PricingRule`.
- Two rule classes are intentionally incomplete:
    - `PercentageDiscountRule`
    - `FixedAmountDiscountRule`

Your work is to implement these classes and test them correctly.

## What you need to do

1. Implement the missing methods in:
    - `pricing/rules/percentage_discount_rule.py`
    - `pricing/rules/fixed_amount_discount_rule.py`
2. Complete tests in:
    - `tests/test_percentage_discount_rule.py`
    - `tests/test_fixed_amount_discount_rule.py`
    - `tests/test_pricing_engine.py`
3. Add at least one additional rule class that **inherits from `PricingRule`**.
    - Place it in its own file (same style as the template)
    - Example ideas: `CapAtMinimumRule`, `BuyOneGetOneRule`, `ThresholdDiscountRule`
4. Add tests for your additional rule in a new `tests/test_<your_rule_name>.py` file, following the same naming convention.
5. Add `pylint` dependency and run it on your code to ensure good code quality.
6. Fill in the "Candidate section" below with instructions on how to run the program, run tests, and explain your design
   choices.

**Note:** The `tests/` folder does not contain an `__init__.py` file. This is intentional — pytest
discovers tests without it. You do not need to add one, but you are free to discuss the trade-offs.

## Functional expectations

- `PercentageDiscountRule(10)` means 10% off (100 -> 90)
- `FixedAmountDiscountRule(15)` means subtract 15 (100 -> 85)
- Totals should never be negative
- Invalid inputs should be handled clearly

---

## Candidate section (to fill)

### How to run the program (including setup instructions if needed)

```bash
python -m venv venv
source venv/Scripts/activate   # Windows
pip install -r requirements.txt
python main.py
```

### How to run tests

```bash
pip install -r requirements.txt
python -m pytest -v
python -m pylint pricing/ tests/ main.py
```

### Design choices

- One class per discount type. All extend `PricingRule` and have an `apply()` method.
- `PricingEngine` adds up the order price, then runs the rule you chose.
- Bad values (negative price, percent over 100…) raise a `ValueError`.
- Only the engine stops the total from going below 0. The rules do not do that.

### What I would improve with more time

- Apply more than one discount on the same order.
- Check that items have valid price and quantity.

