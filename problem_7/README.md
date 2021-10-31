## Problem 7 - 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

My first solution run for 20 seconds and it was mainly due to `is_prime()` function.

```
104745 function calls in 19.353 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   19.353   19.353 {built-in method builtins.exec}
        1    0.000    0.000   19.353   19.353 <string>:1(<module>)
        1    0.046    0.046   19.353   19.353 p007.py:9(nth_prime)
   104741   19.307    0.000   19.307    0.000 p007.py:1(is_prime)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 ```

 As it turned out it was caused by the wrong implementation of this function. Instead of checking factors up to the squar root of a number it was checking for factors up to the half of the number ... Such a silly mistake had a huge impact on performance. Correct implementation:

 ```
 104745 function calls in 0.233 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.233    0.233 {built-in method builtins.exec}
        1    0.000    0.000    0.233    0.233 <string>:1(<module>)
        1    0.021    0.021    0.233    0.233 p007.py:9(nth_prime)
   104741    0.213    0.000    0.213    0.000 p007.py:1(is_prime)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 ```

 Optimization lesson - make sure to use correct implementation of a given algorithm.
