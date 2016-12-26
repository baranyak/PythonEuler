"""
https://projecteuler.net/problem=5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def find_number():
    divisors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for n in range(20, 670442572800, 20):
        flag = True
        for divisor in divisors:
            if n % divisor != 0:
                flag = False
                break
        if flag:
            return n

if __name__ == '__main__':
    import time
    start = time.time()
    print(find_number())
    print("Calculation took {0} seconds".format(int(time.time() - start)))
