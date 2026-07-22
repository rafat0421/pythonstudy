# ChatGPT Interaction Log — Week 3

## Prompt 1

I am working on a Python loops and lists task. I already wrote the code. Can you help me verify whether my explanation of counters and running sum is correct?

## Answer 1

Yes. A counter usually starts at 0 and increases when a specific condition is met. A running sum also starts at 0 and adds each number during every loop iteration. In your case, `positive_count`, `negative_count`, and `zero_count` are counters, while `total_sum` is an accumulator.

## Prompt 2

Can you trace the first two iterations of this list: `[3, -1, 0, 8, -4]`?

## Answer 2

Start: `positive_count = 0`, `negative_count = 0`, `zero_count = 0`, `total_sum = 0`.

First iteration: `number = 3`. Add `3` to `total_sum`, so `total_sum` becomes `3`. Since `3 > 0`, `positive_count` becomes `1`.

Second iteration: `number = -1`. Add `-1` to `total_sum`, so `total_sum` becomes `2`. Since `-1 < 0`, `negative_count` becomes `1`.

## Prompt 3

Why does `positive_count + 1` not update the counter?

## Answer 3

Because `positive_count + 1` only calculates a new value. It does not save the result back into `positive_count`. You need assignment, such as `positive_count = positive_count + 1`, or the shorthand `positive_count += 1`.

## Prompt 4

Is it okay to find highest and lowest values without using `max()` and `min()` by starting with `None`?

## Answer 4

Yes. Starting with `None` is a common approach when you do not yet have an initial number. During the loop, if `highest_number is None` or the current number is larger, update `highest_number`. The same idea works for `lowest_number`.
