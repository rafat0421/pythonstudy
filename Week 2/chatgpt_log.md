# ChatGPT Interaction Log — Week 2

## Prompt 1

I am learning Python conditions. Can you explain how grade boundaries should be ordered in an `if`, `elif`, and `else` structure? Do not give me the full code first.

## Answer 1

Grade conditions should usually be ordered from the highest boundary to the lowest boundary. Python checks conditions from top to bottom and stops at the first true condition. If lower boundaries are checked first, high scores may be classified incorrectly.

## Prompt 2

Why should the score input be converted before comparing it with numbers like 90 and 80?

## Answer 2

`input()` returns text. A score typed as `90` is stored as the string `"90"` unless it is converted. To compare it with numeric values, use `float()` or `int()`.

## Prompt 3

Why should a login check use `and` instead of `or`?

## Answer 3

A login check should use `and` because both the username and the password must be correct. If `or` is used, the login might succeed when only one value is correct.

## Prompt 4

In broken code, why is `elif score = 70:` wrong?

## Answer 4

A single equals sign `=` is used for assignment. Conditions need comparison operators. For a grade range, use `score >= 70`. For exact equality, use `score == 70`.
