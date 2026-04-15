'''
Input  : arr[] = [5, 2, -1, 0, 3], k = 3
Output : 6
Explanation : We get maximum sum by considering the subarray [5, 2 , -1]

Input  : arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4 
Output : 39
Explanation : We get maximum sum by adding subarray [4, 2, 10, 23] of size 4.
'''

def maxSum(arr: list[int], subLength: int) -> int:
    arrLen = len(arr)
    largestValue = 0
    for i in range(arrLen-subLength):
        currentVal = 0
        for j in range(i,i+subLength):
            currentVal += arr[j]
        largestValue = max(largestValue, currentVal)
    return largestValue

def maxSum3(arr: list[int], subLength: int) -> int:
    arrlen = len(arr)
    maxSum = 0
    for i in range(arrlen-subLength):
        currentSum = 0
        for j in range(subLength):
            currentSum += arr[i+j]
        maxSum = max(maxSum, currentSum)

    return maxSum

def maxSum2(arr: list[int], subLength: int) -> int:
    arrlen = len(arr)
    largestSum = 0
    for i in range(arrlen-subLength+1):
        currentSum = 0
        for j in range(i,i+subLength):
            currentSum += arr[j]
        largestSum = max(largestSum, currentSum)
    
    return largestSum

print(maxSum([5, 2, -1, 0, 3], 3)) # 6
print(maxSum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)) # 39


'''
def maxSum(arr: list[int], subLength: int) -> int:
    arrLen = len(arr)
    maxValue = 0
    for i in range(arrLen - subLength + 1):
        currentValue = 0
        for j in range(subLength):
            currentValue += arr[i+j]
        maxValue = max(maxValue, currentValue)
    return maxValue
'''
'''
def maxSum(arr: list[int], subLength: int) -> int:
    maxVal = 0
    lenArr = len(arr)

    for i in range(lenArr - subLength + 1):
        currentVal = 0
        for j in range(subLength):
            currentVal += arr[i+j]
        if currentVal > maxVal:
            maxVal = currentVal
    return maxVal
'''
#print(maximumSum([5, 2, -1, 0, 3], 3))
#print(maximumSum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
