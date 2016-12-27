"""
https://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def main(input_sum):
    limit = int(input_sum / 2)
    for i in range(1, limit):
        for j in range(i+1, limit):
            for k in range(j+1, limit):
                if i + j + k == input_sum and i**2 + j**2 == k**2:
                    print(i*j*k)
                    return i, j, k

if __name__ == '__main__':
    import time
    start = time.time()
    print(main(1000))
    print("Calculation took {0} seconds".format(int(time.time() - start)))
