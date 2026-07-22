# Part 2 — Loop Trace Explanation

## 1. What values are stored in your list?

My list stores these values:

```python
[3, -1, 0, 8, -4, 15, -7, 0]
```

The list includes positive numbers, negative numbers, and zeros. This is useful because the program needs to test all three classification cases.

## 2. Which counters did you create and why?

I created three counters:

```python
positive_count = 0
negative_count = 0
zero_count = 0
```

`positive_count` counts values greater than zero.  
`negative_count` counts values less than zero.  
`zero_count` counts values equal to zero.

All counters start at `0` because no list items have been processed before the loop begins.

## 3. What happens during the first loop iteration?

During the first iteration, the first value in the list is processed:

```python
number = 3
```

The program first adds `3` to `total_sum`, so the sum changes from `0` to `3`.

Then the condition checks whether `3` is positive, negative, or zero. Since `3 > 0` is true, the program increases `positive_count` by 1.

After the first iteration:

```text
positive_count = 1
negative_count = 0
zero_count = 0
total_sum = 3
```

## 4. How does the program decide whether a number is positive, negative, or zero?

The program uses `if`, `elif`, and `else` inside the loop:

```python
if number > 0:
    positive_count += 1
elif number < 0:
    negative_count += 1
else:
    zero_count += 1
```

If the number is greater than zero, it is positive.  
If the number is less than zero, it is negative.  
If neither condition is true, the number must be zero.

## 5. How does the total sum change during the loop?

The variable `total_sum` works as an accumulator. It starts at `0`, and each number is added during the loop:

```python
total_sum += number
```

For my list, the sum changes like this:

```text
Start: 0
After 3: 3
After -1: 2
After 0: 2
After 8: 10
After -4: 6
After 15: 21
After -7: 14
After 0: 14
```

So the final sum is `14`.

## 6. Why is the final print statement usually outside the loop?

The final print statements are outside the loop because I only want to print the final summary after all numbers have been processed.

If the print statements were inside the loop, the program would print intermediate results after every number. That can be useful for tracing, but it is not ideal for the final summary.
