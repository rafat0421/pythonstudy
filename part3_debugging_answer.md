# Part 3 — Debugging the Broken Calculator Code

## 1. What is wrong with this code?

The main problem is that `num1` and `num2` are collected with `input()`, so they are stored as text strings rather than numbers. The code also only handles addition. It does not include subtraction, multiplication, division, division-by-zero handling, or invalid-operation handling.

Another problem is that `result` may never be created. If the user selects an operation other than `+`, the `if` condition is skipped, but the code still tries to print `result`. This would cause an error because the variable has not been assigned.

## 2. What happens if the user enters 10 and 5?

If the user selects `+`, the program prints:

```text
Result: 105
```

This happens because `"10"` and `"5"` are text strings, and the `+` operator joins strings together.

If the user selects another operation, the program attempts to print `result` even though it has not been created, causing an error.

## 3. Why is `num1 + num2` not safe here?

It is not safe because both variables contain text from `input()`. With strings, `+` means concatenation, not arithmetic addition. The program needs to convert the input values to numeric types before calculating.

## 4. How should the input values be converted?

The values should be converted when they are collected:

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
```

`float()` is suitable because it accepts both whole numbers and decimal numbers.

## 5. What operations are missing?

The code is missing:

- subtraction (`-`)
- multiplication (`*`)
- division (`/`)

It also needs conditional branches for those operations.

## 6. What other error handling should be added?

The program should check for division by zero before dividing. It should also handle invalid operations with an `else` branch. A stronger version can use `try` and `except` to handle invalid number input, such as when a user enters a word instead of a number.

## Corrected version

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ").strip()

if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    if num2 == 0:
        print("Error: division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid operation.")
```
