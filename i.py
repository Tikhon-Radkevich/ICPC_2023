import math

MAXN = 10**6

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# Function to find k-remarkable set
def find_k_remarkable(k):
    remarkable_set = []
    if k % 2 == 0:
        if is_prime(k - 2):
            remarkable_set.append(2)
            remarkable_set.append(k - 2)
            return remarkable_set
        elif is_prime(2):
            remarkable_set.append(2)
            remarkable_set.append(2)
            remarkable_set.append(2)
            return remarkable_set

    remarkable_set.append(2)
    remarkable_set.append(2)
    remarkable_set.append(2)
    remarkable_set.append(k - 6)
    return remarkable_set

n = int(input())
for _ in range(n):
    k = int(input())

    if k == 1:
        print("-1")  # No 1-remarkable sets
    elif is_prime(k):
        print("-2")  # k is prime, can't be represented as bitwise OR of primes
    else:
        remarkable_set = find_k_remarkable(k)
        s = len(remarkable_set)
        print(s, *remarkable_set)
