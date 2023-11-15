def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    # Convert the int to a str
    inputText = str(x)

    return inputText == inputText[::-1]

    # Could also do this
    # Faster running, worse memory
    # return str(x) == str(x)[::-1]