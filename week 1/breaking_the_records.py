#!/bin/python3

import os

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    breakingMost = 0
    breakingLeast = 0
    minScore = scores[0]
    maxScore = scores[0]
    for score in scores:
        if score > maxScore:
            breakingMost += 1
            maxScore = score
        if score < minScore:
            breakingLeast += 1
            minScore = score
    return [breakingMost, breakingLeast]
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()