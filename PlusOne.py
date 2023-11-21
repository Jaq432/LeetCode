def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    numAsString = ""
    # convert the list of nums into a string
    for num in digits:
        numAsString += str(num)

    # change the string into an int
    numAsInt = int(numAsString)
    # increment the integer
    numAsInt += 1
    # convert back to a string
    numAsString = str(numAsInt)

    returnList = []
    # convert it back into a list
    for char in numAsString:
        returnList.append(int(char))

    return returnList

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))