"""
https://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


def find_prime(prime_index):
    prime_list = [2]
    i = 3
    while True:
        flag = True
        for divisor in prime_list:
            if i % divisor == 0:
                flag = False
                break
        if flag:
            prime_list.append(i)
        i += 2

        if len(prime_list) == prime_index:
            return prime_list[-1]

if __name__ == '__main__':
    import time
    start = time.time()
    print(find_prime(10001))
    print("Calculation took {0} seconds".format(int(time.time() - start)))
