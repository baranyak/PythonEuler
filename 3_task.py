"""
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

#
In number theory, the prime factors of a positive integer are the prime numbers that divide that integer exactly.
The prime factorization of a positive integer is a list of the integer's prime factors, together with their
multiplicities; the process of determining these factors is called integer factorization.
The fundamental theorem of arithmetic says that every positive integer has a single unique prime factorization.

"""


def prime_number_generator():
    n = 1
    while True:
        n += 1
        flag = True
        for divisor in range(2, n):
            if n % divisor == 0:
                flag = False
        if flag:
            yield n


def get_largest_prime_number(input_number):
    largest_prime = 1
    for prime in prime_number_generator():
        if input_number % prime == 0:
            largest_prime = prime
            input_number /= prime
        if prime >= input_number:
            break
    return largest_prime


if __name__ == '__main__':
    import time
    start = time.time()
    print(get_largest_prime_number(600851475143))
    print("Calculation took {0} seconds".format(int(time.time() - start)))
