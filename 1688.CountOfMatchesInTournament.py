def numberOfMatches(n):
    """
    :type n: int
    :rtype: int
    """
    matchCount = 0
    i = n
    while i != 1:
        # odd number of teams
        if i % 2 != 0:
            matchCount += (i - 1) / 2
            i = (i - 1) / 2 + 1
        else:
            matchCount += i / 2
            i = i / 2
    
    return int(matchCount)

print(numberOfMatches(7))
print(numberOfMatches(14))