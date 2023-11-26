def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 2:
        return str(x)
    i = 2
    while i*i <= x:
        i += 1
    return str(i-1)
    

# mySqrt(4)
# mySqrt(8)
# mySqrt(0)
# mySqrt(1)
# mySqrt(2)
'''
with open("output.txt", "w") as file:
    outputString = ""
    outputString += mySqrt(4) + "\n"
    outputString += mySqrt(8) + "\n"
    outputString += mySqrt(0) + "\n"
    outputString += mySqrt(1) + "\n"
    outputString += mySqrt(2) + "\n"
    outputString += mySqrt(2147395599) + "\n"
    file.write(outputString)
    
    print(mySqrt(4))
    print(mySqrt(8))
    print(mySqrt(0))
    print(mySqrt(1))
    print(mySqrt(2))
    print(mySqrt(2147395599))
'''