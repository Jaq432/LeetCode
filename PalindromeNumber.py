def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    print(f"Trying {x}")
    inputText = str(x)
    halfLength = len(inputText) // 2
    for i in range(halfLength):
        if inputText[i] != inputText[-i-1]:
            return False
    return True

    # Convert the int to a str
    #inputText = str(x)
    #return inputText == inputText[::-1]

    # Could also do this
    # Faster running, worse memory
    # return str(x) == str(x)[::-1]

print(isPalindrome(121)) # true
print(isPalindrome(122)) # false