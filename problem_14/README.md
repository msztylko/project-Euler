## Problem 14 - Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

## Solution

First brute force solution gave correct answer in 30 seconds and there were no obvious way to improve its perfomance:
```
         1000049 function calls in 31.972 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   31.972   31.972 {built-in method builtins.exec}
        1    0.000    0.000   31.972   31.972 <string>:1(<module>)
        1    0.216    0.216   31.972   31.972 p014.py:22(solution)
  1000045   31.756    0.000   31.756    0.000 p014.py:10(Collatz_len)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

For this problem memoization gave excellent results and I need to further explore this topic:
```
         1000049 function calls in 0.536 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.536    0.536 {built-in method builtins.exec}
        1    0.000    0.000    0.535    0.535 <string>:1(<module>)
        1    0.212    0.212    0.535    0.535 p014.py:22(solution)
  1000045    0.323    0.000    0.323    0.000 p014.py:3(_f)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

Optimization lesson - if there is a function that many times takes the same argument try to use memoization.
