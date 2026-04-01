from math import atan, sqrt
import sys

lines = [line.rstrip() for line in sys.stdin.readlines()]

d, r, x, y = [float(n) for n in lines[0].split()]
a, b, c = [float(n) for n in lines[1].split()]
