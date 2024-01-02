def arrayStringsAreEqual(word1, word2):
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """
    string1 = ""
    string2 = ""

    for a in word1:
        #print(f"Adding {a} to string1")
        string1 += a
    for b in word2:
        #print(f"Adding {b} to string2")
        string2 += b

    #print(f"Checking that {string1} is the same as {string2}")
    return string1 == string2


print(arrayStringsAreEqual(["ab", "c"],["a", "bc"]))
