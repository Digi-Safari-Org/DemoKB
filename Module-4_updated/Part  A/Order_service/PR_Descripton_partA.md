# PR: Add tests for order_calculator.py (Part A)

## Summary
This PR adds unit, integration, and regression tests for `order_calculator.py`:
- PyTest parameterized unit tests for `calculate_discount` and `calculate_tax`.
- PyTest parameterized integration tests for `final_price` and cart scenarios.
- unittest-based regression tests for historical bug scenarios.
- Shared test data stored in `order_service/test_data.py` to avoid duplication.

## Files added
- order_service/test_data.py
- order_service/test_order_calculator_pytest.py
- order_service/test_order_calculator_unittest.py

## Reviewer checklist
- [ ] Unit tests cover discount and tax logic with parameterized inputs.
- [ ] Integration tests validate final price and cart totals.
- [ ] Regression tests cover the known bug `final_price(100, 100, 10) → 0.0`.
- [ ] No duplicated test data; all test files import from `test_data.py`.
- [ ] Tests use clear Arrange-Act-Assert structure and Google-style docstrings.
- [ ] Tests run locally with `pytest` and `python -m unittest` and pass.
