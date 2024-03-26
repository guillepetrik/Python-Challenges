#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    odd = n% 2
    cond_2 = not(n%2) and n in range(2,6)
    cond_3 = not(n%2) and n in range(6,21)
    cond_4 = not(n%2) and n > 20
    
    if odd or cond_3:
        print("Weird")
    elif cond_2 or cond_4:
        print("Not Weird")