# Part 3 — Debugging Broken Grade Logic

## Broken code

```python
score = input("Enter score: ")

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score = 70:
    print("C")
else:
    print("F")
```

## 1. Why will this code not run correctly?

The code will not run correctly for two main reasons. First, `score` comes from `input()`, so it is stored as text. The program then tries to compare that text with numbers such as `90` and `80`.

Second, the line `elif score = 70:` is invalid Python syntax. The single equals sign `=` is used for assignment, not comparison.

## 2. What is wrong with comparing score before converting it to a number?

Before conversion, `score` is a string. Comparing a string with numbers like `90` or `80` is not correct. The input should first be converted into a number:

```python
score = float(input("Enter score: "))
```

After that, numeric comparisons can work properly.

## 3. What is wrong with `score = 70` inside `elif`?

`score = 70` tries to assign the value `70` to the variable. It does not check whether the score is 70 or above. In an `elif` condition, the program needs a comparison that becomes either true or false.

For this grade range, the correct condition is:

```python
elif score >= 70:
```

## 4. Which grade ranges are missing?

The D grade range is missing. The code should include:

```python
elif score >= 60:
    print("D")
```

The complete structure should include A, B, C, D, and F.

## 5. How should invalid score values such as -5 or 120 be handled?

Invalid values should be checked before grading. If the score is below `0` or above `100`, the program should print an error message instead of assigning a grade.

## Corrected code

```python
score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a value between 0 and 100.")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```
