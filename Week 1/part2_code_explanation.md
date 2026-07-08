# Part 2 — Code Explanation

## 1. What variables did you use, and what does each variable store?

I used three main variables:

- `first_number` stores the first number entered by the user.
- `second_number` stores the second number entered by the user.
- `operation` stores the selected arithmetic symbol, such as `+`, `-`, `*`, or `/`.

When a valid operation is selected, the variable `result` stores the calculated answer before it is printed.

## 2. Why do you need to convert input values using `float()` or `int()`?

Python treats everything entered through `input()` as text. For example, if a user enters `10` and `5`, Python initially stores them as `"10"` and `"5"`. If the program adds those text values directly, it would join them into `"105"` instead of calculating `15`.

Using `float()` converts the input into a number that can be used in arithmetic. I chose `float()` because it allows both whole numbers and decimal values, such as `10.5`.

## 3. How does your `if`, `elif`, and `else` structure decide which operation to run?

The program compares the value stored in `operation` with each supported symbol. If the value is `+`, the program adds the two numbers. The `elif` branches handle subtraction, multiplication, and division. If none of the supported symbols match, the final `else` branch displays an invalid-operation message.

## 4. How does your program handle division by zero?

Inside the division branch, the program checks whether `second_number == 0`. If it is zero, the program prints an error message instead of trying to divide. If it is not zero, the program performs the division normally.

## 5. How does your program handle an invalid operation?

The final `else` branch handles unsupported operations. For example, if a user enters `%`, `^`, or a word, the program prints: `Invalid operation. Please choose +, -, *, or /.`

## 6. Which part of your code shows that you understand the task?

The division section shows my understanding most clearly because it combines conditional logic with error handling. I needed to recognize that division is different from the other operations because dividing by zero causes an error. The use of `float()` also shows that I understand the difference between text input and numeric data.
