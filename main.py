import math
from collections import Counter

min_value = 2

def smallest_prime_divisor(n):

    divisor = n
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            divisor = i
            break

    return divisor

def factorize(n):

    factors = []
    m = n
    while (div := smallest_prime_divisor(m)) < m:
        factors.append(div)
        m //= div
    factors.append(div)

    return factors

n = input("Enter positive integer to factorize: ")
try:
    n = int(n)
    assert n >= min_value

    factorization_dict = Counter(factorize(n))
    result = ''
    for factor, exponent in factorization_dict.items():
        result += str(factor)
        if exponent > 1:
            result += f'^{str(exponent)}'
        result += ' * '
    result = result[:-3] # remove last ' * '
    print(result)

except:
    print(f'Error: input must be integer >= {min_value}!')

