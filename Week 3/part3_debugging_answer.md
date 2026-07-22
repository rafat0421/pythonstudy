# Part 3 — Debugging Broken Loop Code

## Broken code

```python
numbers = [3, -1, 0, 8, -4]
positive_count = 0

for number in numbers:
    if number > 0:
        positive_count + 1

print("Positive numbers:", positive)
```

## 1. Why does `positive_count` not increase?

`positive_count` does not increase because this line calculates a value but does not store it anywhere:

```python
positive_count + 1
```

It creates the result temporarily, but the value of `positive_count` remains unchanged.

## 2. What is missing from `positive_count + 1`?

An assignment is missing. The corrected version should be:

```python
positive_count = positive_count + 1
```

or the shorter version:

```python
positive_count += 1
```

Both versions update the counter properly.

## 3. Why will `print(positive)` cause an error?

`positive` is not defined anywhere in the program. The actual counter variable is named `positive_count`.

This line:

```python
print("Positive numbers:", positive)
```

should be:

```python
print("Positive numbers:", positive_count)
```

Otherwise, Python raises a `NameError`.

## 4. What counters are missing for negative numbers and zeros?

The code only has `positive_count`. It is missing:

```python
negative_count = 0
zero_count = 0
```

The loop should update those counters when the number is less than zero or equal to zero.

## 5. How would you add a running sum?

I would create a variable before the loop:

```python
total_sum = 0
```

Then inside the loop, I would add each number:

```python
total_sum += number
```

This makes `total_sum` an accumulator.

## Corrected code

```python
numbers = [3, -1, 0, 8, -4]

positive_count = 0
negative_count = 0
zero_count = 0
total_sum = 0

for number in numbers:
    total_sum += number

    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)
print("Sum:", total_sum)
```

## Expected output

```text
Positive numbers: 2
Negative numbers: 2
Zeros: 1
Sum: 6
```
