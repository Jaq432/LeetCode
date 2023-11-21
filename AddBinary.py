def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # we are given two binary strings
    # we are tasked with adding the binary together
    # what we could do is take these and convert them to integer numbers
    # then convert them back to binary

    return bin(int(a,2) + int(b,2))[2:]

print(addBinary("11","1"))
print(addBinary("1010","1011"))