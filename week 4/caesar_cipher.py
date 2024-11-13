#!/bin/python3

import os

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    original = 'abcdefghijklmnopqrstuvwxyz'
    k = k % 26
    cipher = original[k:] + original[0:k]
    res = ''
    for t in s:
        if t.isalpha():
            tmp = cipher[original.index(t.lower())]
            res += (tmp if t.islower() else tmp.upper())
        else:
            res += t
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
