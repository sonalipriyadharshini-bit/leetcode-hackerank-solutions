#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    for i in range(len(arr)):
        reversed_array = arr[::-1]
    for i in reversed_array:
        print(i,end = " ")
