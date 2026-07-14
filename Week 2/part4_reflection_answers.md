# Part 4 — Reflection on ChatGPT Use

## 1. Did ChatGPT help you with boundaries, syntax, debugging, or explanation?

ChatGPT helped me mostly with explanation and boundary logic. I used it to understand why the grade conditions should be ordered from the highest score to the lowest score. It also helped me understand the syntax problem in the broken code, especially the difference between `=` and comparison operators.

## 2. Did you test the conditions yourself before asking ChatGPT?

Yes, I tested some conditions myself first. I tried normal values like `82` and `55`, then I tested boundary values such as `90`, `89`, `80`, `79`, `60`, and `59`. After that, I asked ChatGPT to help me confirm whether the condition order was correct.

## 3. Which condition was hardest to understand?

The hardest condition was the boundary logic around grade changes. For example, I had to think carefully about why `90` should be A but `89` should be B. I also had to understand why the condition `score >= 90` must come before `score >= 80`.

## 4. Could you write a similar `if`/`elif`/`else` program without ChatGPT now?

Yes, I think I could write a similar program without ChatGPT now. I understand how to take input, convert it to a number, compare it with boundaries, and use `else` for values that do not match earlier conditions. I may still need help for more complex validation, but I understand the basic structure.

## 5. What would you try independently before asking ChatGPT next time?

Next time, I would first write the possible ranges on paper or in comments. Then I would turn each range into an `if` or `elif` condition. I would also test the boundary values myself before asking ChatGPT for verification.

## 6. Did ChatGPT change your original condition structure? If yes, how?

Yes, slightly. My first idea was to write the grade conditions without thinking much about the order. After using ChatGPT, I understood that the conditions should be checked from highest to lowest. It also reminded me to check invalid scores before assigning a grade.
