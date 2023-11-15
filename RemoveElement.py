def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    for i,num in enumerate(nums):
        if num == val:
            nums[i] = None

    return sum(x is not None for x in nums)

print(removeElement([0,1,2,2,3,0,4,2],2))