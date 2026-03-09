'''
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

# Returning three numbers that don't equal each other but sum to 0
def threeSum(nums: list[int]) -> list[list[int]]:
    numsDict = {}
    returnListIndexes = []
    returnList = []

    for k,num in enumerate(nums):
        numsDict[k] = num
    
    #print(nums)

    # Vars to track loop process
    firstLoopIndex = 0
    secondLoopIndex = 0
    thirdLoopIndex = 0

    # Loop through the dict, getting first sum num
    for i in nums:
        # Loop through the dict, getting second sum num
        for l in nums[firstLoopIndex:]:
            # Loop through the dict, getting third sum num
            for j in nums[secondLoopIndex:]:
                if nums[firstLoopIndex] + nums[secondLoopIndex] + nums[thirdLoopIndex] == 0:
                    if nums[firstLoopIndex] == nums[secondLoopIndex] or nums[firstLoopIndex] == nums[thirdLoopIndex] or nums[secondLoopIndex] == nums[thirdLoopIndex]:
                        #returnList.append([numsDict[firstLoopIndex],numsDict[secondLoopIndex],numsDict[thirdLoopIndex]])
                        returnListIndexes.append([firstLoopIndex,secondLoopIndex,thirdLoopIndex])
                thirdLoopIndex += 1
            secondLoopIndex += 1
            thirdLoopIndex = 0
        firstLoopIndex += 1
        secondLoopIndex = 0
    
    # Go through the list of indexes, split them on commas, sort those in ascending order, reformat back into lists, then into a list of lists
    subSortedListN = []
    for n in returnListIndexes:
        splitN = str(n).replace("[","").replace("]","").replace(" ","").split(",")
        #print(splitN)
        sortedN = sorted(splitN)
        print(sortedN)
        
    
    return returnListIndexes


print(threeSum([-1,0,1,2,-1,-4]))   # The distinct triplets are [-1,0,1] and [-1,-1,2]
#print(threeSum([0,1,1]))            # No solution
#print(threeSum([0,0,0]))            # It is the solution