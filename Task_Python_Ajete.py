# 1.Shipment Processing

def get_valid_shipments(shipments):
    return [
        s for s in shipments
        if s["weight"] > 0 and s["status"] == "delivered"
    ]

shipments = [
    {"shipment_id": 1, "weight": 10, "status": "delivered"},
    {"shipment_id": 2, "weight": -5, "status": "delivered"},
    {"shipment_id": 3, "weight": 8,  "status": "pending"},
    {"shipment_id": 4, "weight": 15, "status": "delivered"},
]

print(get_valid_shipments(shipments))


# 2. Clean Numeric Input

values = ["100", "200", "NaN", "50", "error", "300"]

def clean_numeric_values(values):
    result = []
    for v in values:
        try:
            result.append(int(v))
        except (ValueError, TypeError):
            pass
    return result

print(clean_numeric_values(values))  

#3. Custom Validation Exception

class InvalidWeightError(Exception):
    """Raised when a weight value is outside the acceptable range (0–500)."""
    pass

def validate_weight(weight):
    if weight <= 0:
        raise InvalidWeightError(f"Weight must be greater than 0. Got: {weight}")
    if weight > 500:
        raise InvalidWeightError(f"Weight must not exceed 500. Got: {weight}")
    return "Valid weight"


# --- Test it 3.---
print(validate_weight(70))    
print(validate_weight(500))   

try:
    validate_weight(-5)
except InvalidWeightError as e:
    print(e)                  

try:
    validate_weight(600)
except InvalidWeightError as e:
    print(e)                  

# Task 4: Text Analysis

text = "Data science is evolving and data is becoming more important in science"

word_counts = {}

for word in text.lower().split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)


# Task 5 List filtering

numbers = [3, 6, 9, 12, 15, 18]

filtered = list(filter(lambda x: x % 3 == 0 and x > 10, numbers))

print(filtered)

# Task 6 File Handling with Validation 
import os

def analyze_file(file_path):
    try:
        if os.path.getsize(file_path) == 0:
            print(f"Error: The file '{file_path}' is empty.")
            return

        total_lines = 0
        empty_lines = 0

        with open(file_path, 'r') as file:
            for line in file:
                total_lines += 1
                if not line.strip():
                    empty_lines += 1

        print(f"Analysis for: {file_path}")
        print(f"Total lines: {total_lines}")
        print(f"Empty lines: {empty_lines}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    analyze_file('test.txt')
    print()

    analyze_file('empty.txt')
    print()

    analyze_file('missing.txt')


# Task 7 Data Integrity Check

def validate_products(products: list[dict]) -> list[dict]:
    invalid_records = []

    for product in products:
        issues = []

        if product.get("id") is None:
            issues.append("id must not be None")

        if not product.get("name"):
            issues.append("name must not be empty")

        if product.get("price") is not None and product["price"] <= 0:
            issues.append("price must be positive")

        if issues:
            invalid_records.append({
                "record": product,
                "issues": issues
            })

    return invalid_records

products = [
    {"id": 1,    "name": "Table", "price": 200},
    {"id": 2,    "name": "",      "price": 150},
    {"id": 3,    "name": "Chair", "price": -50},
    {"id": None, "name": "Lamp",  "price": 80},
]

invalid = validate_products(products)

for entry in invalid:
    print(f"Record : {entry['record']}")
    print(f"Issues : {', '.join(entry['issues'])}")
    print()


#Bonus
import time
import functools

def timer(func):
    """Decorator that measures and prints a function's execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timer] '{func.__name__}' ran in {elapsed:.6f}s")
        return result
    return wrapper

def divisible_by_five(n):
    """Generator that yields integers divisible by 5 in the range [1, n]."""
    for i in range(1, n + 1):
        if i % 5 == 0:
            yield i

@timer
def squared_multiples_of_five(n):
    """Returns a list of squares of all numbers divisible by 5 up to N."""
    squares = list(map(lambda x: x ** 2, divisible_by_five(n)))
    return squares

if __name__ == "__main__":
    N = 50
    result = squared_multiples_of_five(N)
    print(f"Squares of multiples of 5 up to {N}:")
    print(result)

