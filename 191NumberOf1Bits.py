def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    binN = bin(n)[1:]
    weight = 0
    for i in binN:
        if i != "0":
            weight += 1
    return weight

print(hammingWeight(00000000000000000000000000001011))
