#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary_string = bin(n)[2:]
    consecutive_groups = binary_string.split('0')
    max_consecutive_ones = len(max(consecutive_groups))
    print(max_consecutive_ones)
