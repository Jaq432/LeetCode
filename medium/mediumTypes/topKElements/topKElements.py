'''
Given an array of integers and a value k. Return the k-th largest element.
Solve it without sorting.
'''

def topKElements(arr: list[int], k: int):
    kLargestElements = []
    for i in arr:
        if len(kLargestElements) < k:
            kLargestElements.append(i)
            continue
        for i in kLargestElements:
            if 



print(topKElements([3,2,1,5,6,4], 2))       # 5
print(topKElements([3,2,3,1,2,4,5,5,6], 4)) # 4