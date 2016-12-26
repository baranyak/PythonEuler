"""
https://projecteuler.net/problem=4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools


def is_palindromic(input_number):
    return str(input_number) == "".join(str(input_number)[::-1])


def find_palindrome():
    largest_palindrome = 0
    for i, j in itertools.product(range(100, 1000), range(100, 1000)):
        res = i * j
        if res > largest_palindrome and is_palindromic(res):
            largest_palindrome = res
    return largest_palindrome

if __name__ == '__main__':
    import time
    start = time.time()
    print(find_palindrome())
    print("Calculation took {0} seconds".format(int(time.time() - start)))
