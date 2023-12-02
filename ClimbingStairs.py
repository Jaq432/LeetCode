def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    
    # Return the number unique ways that we can get to the top of the stairs
    # We are only able to take 1 or 2 step increments

    # Assuming that the answer is the fibonnacci sequence
    num1 = 0
    num2 = 1
    next_number = num2
    count = 1
    rollingTotal = 0

    while count <= n:
        rollingTotal += next_number
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2

    return rollingTotal

    '''
    1 -> 1
    2 -> 2
    3 -> 3
    4 -> 5
    5 -> 8
    6 -> 13?
    111111
    11112
    11121
    11211
    12111
    21111
    1122
    1212
    1221
    2112
    
    
    
    
    
    '''

print(climbStairs(2))