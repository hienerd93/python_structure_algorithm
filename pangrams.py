#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def replace_uppercase(match):
    return match.group(0).lower()

def pangrams(s):
    # Write your code here
    result = re.sub(r'[A-Z]', replace_uppercase, s)
    result = re.sub(r'\s+', '', result)
    result = [x for x in result]
    return 'pangram' if len(set(result)) == 26 else 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()