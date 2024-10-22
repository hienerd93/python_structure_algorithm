#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    isAm = s[8:10] == 'AM'
    hour = s[0:2]
    if hour == '12' and isAm:
        hour = '00'
    if hour != '12':
        hour = hour if isAm else int(hour) + 12
    return str(hour) + s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
