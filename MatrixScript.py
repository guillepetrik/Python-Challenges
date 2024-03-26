# Matrix Script

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

string = "".join([matrix[j][i] for i in range(m) for j in range(n)])
# Concatenates characters from j rows and i columns

pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
# Regular expression pattern using a raw string. 

print(re.sub(pat,' ',string))
# Re module function to substitute matches from pattern pat in the string.
# It replaces the matched non-alphanumeric characters with a blank space

