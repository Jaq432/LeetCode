def findMaxK(nums) -> int:
    biggestNum = -1
    for num in nums:
        if num > biggestNum:
            if -num in nums:
                biggestNum = num
    
    if biggestNum == -1:
        return -1
    return biggestNum

print(findMaxK([-1,2,-3,3]))
print(findMaxK([-1,10,6,7,-7,1]))
print(findMaxK([-10,8,6,7,-2,-3]))