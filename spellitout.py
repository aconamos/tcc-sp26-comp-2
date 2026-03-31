import sys


lines = [line.rstrip() for line in sys.stdin.readlines()]

n = int(lines[0])

ones = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]

twos = [
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
]

others = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

if n <= 10:
    print(ones[n])
elif n <= 20:
    print(twos[n - 11])
else:
    first = (n - (n % 10)) // 10
    second = n % 10

    first = others[first - 2]
    second = ones[second]
    print(f"{first}-{second}")
