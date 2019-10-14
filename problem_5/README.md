## Problem 5 - Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

My first brute force soultion run for 170 seconds and I decided to optimize it with the help of cProfile module. The output from the profiler:

```
         232792564 function calls in 168.962 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  168.962  168.962 {built-in method builtins.exec}
        1    0.000    0.000  168.961  168.961 <string>:1(<module>)
        1   44.883   44.883  168.961  168.961 p005.py:10(solution)
232792560  124.079    0.000  124.079    0.000 p005.py:1(evenly_divisible)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
```
