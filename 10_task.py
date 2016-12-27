"""
https://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


def prime_sum(limit):
    count = 0
    # Sieve of Eratosthenes 
    a = [True] * limit
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a): 
        if is_prime:
            count += i
            for n in range(i*i, limit, i):
                a[n] = False
    return count


if __name__ == '__main__':
    import time
    start = time.time()
    print(prime_sum(2000000))
    print("Calculation took {0} seconds".format(int(time.time() - start)))
