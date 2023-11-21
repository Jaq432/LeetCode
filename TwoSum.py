
def twoSum(nums, target):

    inputNumsLen = len(nums)

    for i in range(inputNumsLen):
        for j in range(i+1, inputNumsLen):
            if nums[i] + nums[j] == target:
                return [i,j]

print(twoSum([2,7,11,15], 9)) #[0,1]
print(twoSum([3,2,4], 6)) #[1,2]
print(twoSum([3,3], 6)) #[0,1]
print(twoSum([1,5,5,9]), 10)