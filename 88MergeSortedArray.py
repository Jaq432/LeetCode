def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # Remove 0s
    try:
        while nums1[-1] == 0:
            nums1.pop()
    except:
        pass
    try:
        while nums2[-1] == 0:
            nums2.pop()
    except:
        pass

    holdThis = []

    while nums1 != []:
        holdThis.append(nums1.pop())
    while nums2 != []:
        holdThis.append(nums2.pop())

    holdThis = sorted(holdThis, reverse=True)

    while holdThis != []:
        nums1.append(holdThis.pop())

    while len(nums1) < (m + n):
        nums1.append(0)

    print(nums1)

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
merge([1], 1, [], 0)
merge([0], 0, [1], 1)