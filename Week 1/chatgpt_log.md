# ChatGPT Log — Week 1

> Replace or edit this record so it reflects the actual study-related ChatGPT interaction you want to submit. Do not include private or unrelated conversations.

## Study-related use

### Prompt 1
I am learning Python. Explain why values from `input()` need to be converted with `float()` before I use them in a calculator. Do not give a full program yet.

### Summary of AI response
The response explained that `input()` returns strings. It used an example showing that `"10" + "5"` becomes `"105"` rather than the numeric result `15`. It explained that `float()` converts the text input into numeric values and allows decimal numbers.

### Prompt 2
I am writing a beginner calculator with `if`, `elif`, and `else`. Explain where I should check for division by zero and why.

### Summary of AI response
The response explained that the check belongs inside the division branch. The program should first confirm that the selected operation is division and then check whether the second number is zero before calculating.

### Prompt 3
Please review this approach without rewriting everything: I collect two numbers, ask for an operation, use conditional branches for `+`, `-`, `*`, and `/`, and use an `else` branch for invalid input.

### Summary of AI response
The response confirmed that the overall structure is appropriate. It recommended converting input values to numbers, adding a division-by-zero check, and ensuring that invalid operations do not leave `result` undefined.

## How AI assistance was used

The AI was used for explanation, guidance, and verification. The final code and written answers were reviewed and organized after considering the explanations.
