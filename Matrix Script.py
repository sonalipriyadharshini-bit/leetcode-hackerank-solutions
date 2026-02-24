import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
decoded_string = "".join([matrix[i][j] for j in range(m) for i in range(n)])
print(re.sub(r'(?<=[\w])[^\w]+(?=[\w])', ' ', decoded_string))
