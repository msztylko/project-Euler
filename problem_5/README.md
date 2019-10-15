## Problem 5 - Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

My first brute force solution run for 170 seconds and I decided to optimize it with the help of `cProfile` module. The output from the profiler:

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
In the first solution `evenly_divisible()` function accepted general arguments, but hardcoding its range allowed to speed up the program.

```
         232792564 function calls in 154.530 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  154.530  154.530 {built-in method builtins.exec}
        1    0.000    0.000  154.530  154.530 <string>:1(<module>)
        1   40.863   40.863  154.530  154.530 p005.py:10(solution)
232792560  113.667    0.000  113.667    0.000 p005.py:1(evenly_divisible)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
Since we know that the solution has to be a multiple of 20 we can change the main loop so that it only checks multiples of 20. This change led to significant speed-up as the number of function call was greatly reduced.

```
         11639632 function calls in 8.376 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.376    8.376 {built-in method builtins.exec}
        1    0.000    0.000    8.376    8.376 <string>:1(<module>)
        1    1.959    1.959    8.376    8.376 p005.py:10(solution)
 11639628    6.417    0.000    6.417    0.000 p005.py:1(evenly_divisible)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

Optimization lesson - If the code involves loops try to limit their range and check if it's possible to increament by a number bigger than one. 

