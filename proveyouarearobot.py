import sys


def isprime(n):
    n = int(n)
    if n <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime


lines = [line.rstrip() for line in sys.stdin.readlines()]

n, m = [int(x) for x in lines[0].split(" ")]

for i in range(0, n):
    line = lines[i + 1]
    nums = line.split(" ")
    for num in nums:
        if isprime(num):
            print("1", end="")
        else:
            print("0", end="")
    print("")
