#!/bin/python3

import os

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr_sort = sorted(arr)
    difference_dict = {}

    for i in range(len(arr_sort) - 1):
        difference = abs(arr_sort[i] - arr_sort[i + 1])
        if difference not in difference_dict:
            difference_dict[difference] = []
        difference_dict[difference].append((arr_sort[i], arr_sort[i + 1]))

    min_difference = min(difference_dict.keys())

    closest_pairs = difference_dict[min_difference]

    result = [num for pair in closest_pairs for num in pair]

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
