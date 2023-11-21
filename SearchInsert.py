def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    # writing this in O(log(n))
    # that means we have to split our search in half each time
    # we want to implement a binary search

    # Get the left and the right
    left = 0
    right = len(nums) - 1

    # Make sure that our left is always smaller than (or equal to) our right
    while left <= right:
        # Calculate the middle of our search
        # // is floor division
        mid = left + (right - left) // 2

        # if we are at the target, return the mid index
        if nums[mid] == target:
            return mid
        # if our mid index value is less than the target 
        elif nums[mid] < target:
            # move the left pointer to be right of the mid
            left = mid + 1
        # if our mid index value is greater than the target
        else:
            # move the right pointer to be left of the mid
            right = mid - 1

    return left




print(searchInsert([1,3,5,6],5)) # 2
print(searchInsert([1,3,5,6],2)) # 1
print(searchInsert([1,3,5,6],7)) # 4