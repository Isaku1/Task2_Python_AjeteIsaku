# Task 2 – Python Exercises
**Author:** Ajete Isaku  
**Repository:** [Task2_Python_AjeteIsaku](https://github.com/Isaku1/Task2_Python_AjeteIsaku.git)

---

## Overview

This project contains 7 Python tasks plus a Bonus task, covering core programming concepts such as data filtering, input validation, exception handling, text analysis, file I/O, and decorators.

---

## Tasks

### Task 1 – Shipment Processing
Filters a list of shipment dictionaries, returning only those with a positive weight **and** a `"delivered"` status.

```python
get_valid_shipments(shipments)
# Returns shipments where weight > 0 AND status == "delivered"
```

---

### Task 2 – Clean Numeric Input
Parses a mixed list of strings and returns only the valid integers, silently skipping non-numeric values like `"NaN"` or `"error"`.

```python
clean_numeric_values(["100", "200", "NaN", "50", "error", "300"])
# Returns: [100, 200, 50, 300]
```

---

### Task 3 – Custom Validation Exception
Defines a custom exception `InvalidWeightError` and a `validate_weight()` function that raises it when the weight is ≤ 0 or > 500.

```python
validate_weight(70)    # → "Valid weight"
validate_weight(-5)    # → raises InvalidWeightError
validate_weight(600)   # → raises InvalidWeightError
```

---

### Task 4 – Text Analysis
Counts word frequencies in a given string using a dictionary, after lowercasing and splitting the text.

```python
text = "Data science is evolving and data is becoming more important in science"
# Output: {'data': 2, 'science': 2, 'is': 2, ...}
```

---

### Task 5 – List Filtering
Uses `filter()` with a lambda to return numbers divisible by 3 **and** greater than 10.

```python
numbers = [3, 6, 9, 12, 15, 18]
# Output: [12, 15, 18]
```

---

### Task 6 – File Handling with Validation
Reads a text file and reports total lines and empty lines. Handles three edge cases gracefully:
- File not found → prints an error message
- Empty file → prints an error message
- Unexpected errors → prints the exception

```python
analyze_file('test.txt')    # Normal analysis
analyze_file('empty.txt')   # Reports empty file error
analyze_file('missing.txt') # Reports file not found
```

---

### Task 7 – Data Integrity Check
Validates a list of product dictionaries and returns all records that fail one or more of these rules:
- `id` must not be `None`
- `name` must not be empty
- `price` must be positive

```python
validate_products(products)
# Returns a list of {"record": ..., "issues": [...]} for each invalid entry
```

---

### Bonus – Timer Decorator + Generator
Combines two Python features:

- **`divisible_by_five(n)`** – a generator that yields integers divisible by 5 in range `[1, n]`
- **`@timer`** decorator – wraps a function and prints its execution time using `time.perf_counter()`
- **`squared_multiples_of_five(n)`** – uses `map()` + the generator to return a list of squares

```python
squared_multiples_of_five(50)
# [25, 100, 225, 400, 625, 900, 1225, 1600, 2025, 2500]
# [timer] 'squared_multiples_of_five' ran in 0.000012s
```

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Isaku1/Task2_Python_AjeteIsaku.git
   cd Task2_Python_AjeteIsaku
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

> **Note:** For Task 6, make sure `test.txt` and `empty.txt` exist in the same directory before running. `missing.txt` is intentionally absent to test the error handler.

---

## Requirements

- Python 3.10 or higher (Task 7 uses `list[dict]` type hints which require 3.9+)
- No external libraries required — standard library only (`os`, `time`, `functools`)

---

## Project Structure

```
Task2_Python_AjeteIsaku/
│
├── main.py          # All tasks in a single file
├── test.txt         # Sample file for Task 6
├── empty.txt        # Empty file for Task 6 edge case
└── README.md        # This file
```
