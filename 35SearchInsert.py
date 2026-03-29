def searchInsert(nums: List[int], target: int) -> int:
    #left=nums[0]
    #right=nums[len(nums)/2]
    answerFound = False
    pointer = nums[len(nums/2)]
    pointerMoveDistance = len(nums/2)
    while not answerFound:
        if nums[pointer] > target:
            pointer -= pointer - (pointerMoveDistance)
            pointerMoveDistance = pointerMoveDistance / 2
            continue
        if nums[pointer] < target:
            pointer += pointer + (pointerMoveDistance)
            pointerMoveDistance = pointerMoveDistance / 2
            continue
        if nums[pointer] == target:
            return pointer
        
        nums.index()
    pass

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))