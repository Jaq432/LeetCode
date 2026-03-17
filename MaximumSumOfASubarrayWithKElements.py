'''
Input  : arr[] = [5, 2, -1, 0, 3], k = 3
Output : 6
Explanation : We get maximum sum by considering the subarray [5, 2 , -1]

Input  : arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4 
Output : 39
Explanation : We get maximum sum by adding subarray [4, 2, 10, 23] of size 4.
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

#print(maximumSum([5, 2, -1, 0, 3], 3))
#print(maximumSum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
print(maxSum([5, 2, -1, 0, 3], 3))
print(maxSum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))