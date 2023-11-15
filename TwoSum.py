
def twoSum(nums, target):
    # Input types
    '''
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    '''
    inputNums = nums
    inputTarget = target
    outputIndexes = []

    inputNumsLen = len(inputNums)

    for i in range(0, inputNumsLen):
        for j in range(i+1, inputNumsLen):
            if inputNums[i] + inputNums[j] == inputTarget:
                outputIndexes.append(i)
                outputIndexes.append(j)
                return outputIndexes

print(twoSum([2,7,11,15], 9)) #[0,1]
print(twoSum([3,2,4], 6)) #[1,2]
print(twoSum([3,3], 6)) #[0,1]
