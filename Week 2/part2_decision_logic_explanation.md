# Part 2 — Decision Logic Explanation

## 1. Which variables store the score, username, and password?

The variable `score` stores the score entered by the user. The variable `username` stores the username entered in the login part, and `password` stores the password entered by the user.

I also used `correct_username` and `correct_password` to store the expected login values. These are compared with the user input during the login check.

## 2. Why must the score input be converted to a number?

The score must be converted because `input()` returns text. A value like `82` is first stored as the string `"82"`. The program needs to compare the score with numbers such as `90`, `80`, and `70`, so the value must be converted using `float()` or `int()`.

I used `float()` because it allows both whole numbers and decimal scores.

## 3. What grade boundaries did you choose?

I used these grade boundaries:

- `90` to `100` = A
- `80` to below `90` = B
- `70` to below `80` = C
- `60` to below `70` = D
- below `60` = F

I also treated scores below `0` and above `100` as invalid.

## 4. Why is the order of `if`, `elif`, and `else` important?

The order is important because Python checks conditions from top to bottom and stops at the first true condition. If I check the lower boundary first, a high score could match the wrong grade.

For example, if `score >= 60` came before `score >= 90`, then `95` would be classified as D because it is also greater than 60. That is why the program checks invalid values first and then checks grades from highest to lowest.

## 5. How does the login condition use `and`?

The login condition uses `and` to make sure both the username and password are correct:

```python
if username == correct_username and password == correct_password:
```

This means the login succeeds only when both comparisons are true.

## 6. What would happen if you used `or` instead of `and` in the login check?

If I used `or`, the login would succeed if only one value was correct. For example, a correct username with a wrong password could still log in. That would be unsafe and incorrect for login validation.

## 7. Which boundary case did you test, and what did the result show?

I tested several boundary cases: `90`, `89`, `80`, `79`, `60`, and `59`.

The results showed that `90` becomes A, `89` becomes B, `80` becomes B, `79` becomes C, `60` becomes D, and `59` becomes F. This confirmed that the grade boundaries work correctly.
