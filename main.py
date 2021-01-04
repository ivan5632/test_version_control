import math
first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
min_value = 4

def is_prime(n):
    try:
        n = int(n)
        assert n >= min_value

        n_isqrt = math.isqrt(n)
        rest_of_the_list = [i for i in range(max(first_primes) + 1, n_isqrt + 1) if not (i%2==0 or i%3==0 or i%5==0 or i%7==0)]
        list_to_check = [i for i in [*first_primes, *rest_of_the_list] if i<=n_isqrt]
        return list_to_check

    except:
        print(f'Error: input must be integer >= {min_value}!')
        return None


print(is_prime(3))

# n = input("Enter positive integer to factorize: ")
# try:
#     n = int(n)
#     assert n > 0
#
#     n_isqrt = math.isqrt(n)
#     rest_of_the_list = [ i for i in range(max(first_primes) + 1, n_isqrt + 1) if not (i%2==0 or i%3==0 or i%5==0 or i%7==0)]
#
#
#     print ([ *first_primes, *rest_of_the_list ])
#     # print(max(first_primes))
#     # for i in range(1, 10):
#     #     print(i)
#     # print(x)
# except:
#     print('Error: input must be integer > 0!')

