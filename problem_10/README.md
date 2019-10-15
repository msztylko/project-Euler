## Problem 10 - Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Initial solution with standard `is_prime()` function.
```
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
```
It run for 15 seconds

```
         2148938 function calls in 14.611 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   14.611   14.611 {built-in method builtins.exec}
        1    0.000    0.000   14.611   14.611 <string>:1(<module>)
        1    0.000    0.000   14.611   14.611 p010.py:22(solution)
        1    0.040    0.040   14.611   14.611 {built-in method builtins.sum}
   148934    0.405    0.000   14.571    0.000 p010.py:23(<genexpr>)
  1999999   14.166    0.000   14.166    0.000 p010.py:15(is_prime)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

Changing the algorithm based on the information from https://en.wikipedia.org/wiki/Primality_test

```
def is_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

was enough to improve the performance:

```      
2148938 function calls in 7.392 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    7.392    7.392 {built-in method builtins.exec}
        1    0.000    0.000    7.392    7.392 <string>:1(<module>)
        1    0.000    0.000    7.392    7.392 p010.py:16(solution)
        1    0.020    0.020    7.392    7.392 {built-in method builtins.sum}
   148934    0.314    0.000    7.371    0.000 p010.py:17(<genexpr>)
  1999999    7.057    0.000    7.057    0.000 p010.py:1(is_prime)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
