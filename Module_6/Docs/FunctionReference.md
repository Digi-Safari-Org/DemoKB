<!-- Explain the selected function as documentation for a project wiki. Provide:
- Short summary
- Purpose
- Inputs (types and example)
- Outputs (types and example)
- Example call with expected output
- Complexity and edge cases / gotchas
Format as markdown suitable to save in docs/FunctionReference.md. -->


## Function: display_product

### Short Summary
Formats a product's name and price for display using input sanitization, uppercase conversion, and currency formatting.

---

### Purpose
To generate a clean, standardized string representation of a product by:
- Removing unwanted whitespace and characters from the name,
- Converting the name to uppercase,
- Formatting the price as a currency string.

---

### Inputs

| Name   | Type   | Description                                 | Example                |
|--------|--------|---------------------------------------------|------------------------|
| name   | str    | The raw product name (may include whitespace or newlines) | `"   deluxe Chair\n"`  |
| price  | float  | The product price                           | `129.95`               |

---

### Outputs

| Type   | Description                       | Example                        |
|--------|-----------------------------------|--------------------------------|
| str    | Formatted product string          | `"DELUXE CHAIR - $129.95"`     |

---

### Example Call

```python
display_product("   deluxe Chair\n", 129.95)
# Output: "DELUXE CHAIR - $129.95"