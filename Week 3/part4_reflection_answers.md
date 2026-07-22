# Part 4 — Reflection on ChatGPT Use

## 1. Did ChatGPT help you understand lists, loops, counters, or tracing?

ChatGPT mostly helped me verify my reasoning about loop tracing and accumulator behavior. I already understood the basic syntax of lists and `for` loops, but I used ChatGPT to confirm that my explanation of counter updates and running sums was clear enough.

## 2. Did you ask ChatGPT to trace your loop step by step?

Yes, I asked ChatGPT to trace one loop iteration and then compare it with my own explanation. I wanted to make sure I was describing the loop state accurately, especially how `positive_count`, `negative_count`, `zero_count`, and `total_sum` change after each iteration.

## 3. Did ChatGPT help you understand how the variable values changed during the loop, or did it mainly give you code?

It mainly helped with verification and explanation. It did not mainly give me code. I already wrote the main program, then used ChatGPT to check whether my tracing explanation was correct and whether the debugging answer was precise.

## 4. Which loop concept was most difficult?

The most difficult concept was explaining loop state clearly in writing. Writing the code was straightforward, but describing how each variable changes after each iteration required more careful thinking.

## 5. Could you explain one loop iteration without ChatGPT now?

Yes. For example, if the current number is `-1`, the program first adds `-1` to `total_sum`. Then it checks `number > 0`, which is false. It checks `number < 0`, which is true, so `negative_count` increases by 1. The other counters do not change during that iteration.

## 6. What would you try alone before asking ChatGPT next time?

Next time, I would first write a small trace table myself. I would include the current number, the counter that changes, and the new total sum after each iteration. Then I would ask ChatGPT only to verify the trace if I was unsure.
