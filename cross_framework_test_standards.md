# Cross-Framework Test Standards – Knowledge Base

## 1️⃣ Naming Conventions

### PyTest (Python)
- File names: `test_<module_name>.py`
- Function names: `test_<functionName>_<scenario>`

### Jest (JavaScript)
- File names: `<module_name>.test.js`
- Use `describe()` blocks for grouping.
- Test names should read like sentences: `should <do something>`.

---

## 2️⃣ PyTest Template
```python
import pytest
from app.example import my_function

def test_my_function_valid_case():
    result = my_function("input")
    assert result == "expected"

@pytest.mark.parametrize("input_val,expected", [
    ("case1", "expected1"),
    ("case2", "expected2"),
])
def test_my_function_parameterized(input_val, expected):
    assert my_function(input_val) == expected
```

---

## 3️⃣ Jest Template
```javascript
const { myFunction } = require('../src/example');

test('myFunction valid case', () => {
  expect(myFunction("input")).toBe("expected");
});

describe('myFunction parameterized', () => {
  test.each([
    ["case1", "expected1"],
    ["case2", "expected2"],
  ])('myFunction(%s) should return %s', (input, expected) => {
    expect(myFunction(input)).toBe(expected);
  });
});
```

---

## 4️⃣ Conversion Guidelines

### PyTest → Jest
- `assert x == y` → `expect(x).toBe(y)`
- Use `test.each` for parameterization.
- Replace `pytest.raises` with `expect(() => fn()).toThrow()`.

### Jest → PyTest
- `expect(x).toBe(y)` → `assert x == y`
- Replace `test.each` with `@pytest.mark.parametrize`.
- Replace `toThrow` with `pytest.raises`.

---

## 5️⃣ Assertion Best Practices
- Use specific assertions (`assert x == y` / `expect(x).toBe(y)`).
- Avoid ambiguous truthy checks.
- Test edge cases as well as normal cases.

---

## 6️⃣ PR Review Checklist
- Equivalent coverage exists in both frameworks.
- Naming follows respective framework rules.
- Assertions match KB patterns.
- Parameterization applied where relevant.
- Test logic matches across frameworks.

---
