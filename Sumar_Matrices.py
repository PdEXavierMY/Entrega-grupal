import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    suma = 0
    for i in ar:
        suma += i
    return suma

if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)