#!/bin/python3

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    maxArr = arr[0]
    minArr = arr[0]
    sumArr = 0
    for num in arr:
        sumArr += num
        if (num > maxArr):
            maxArr = num
        if (minArr > num):
            minArr = num
    print(sumArr - maxArr, sumArr - minArr)
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
