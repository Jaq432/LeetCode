def checkOnesSegment(s: str) -> bool:
    latch = True
    for i in s:
        if i == "0":
            latch = False
        if not latch and i == "1":
            return False
    return True
    
if __name__ == "__main__":
    test1 = "1001"  # false
    test2 = "110"   # true
    test3 = "1"     # true
    test4 = "0"     # true
    test5 = "1111"  # true
    test6 = "110011"# false
    test7 = "101"   # false
    test8 = "10"    # true
    print("Test 1: " + str(checkOnesSegment(test1)))
    print("Test 2: " + str(checkOnesSegment(test2)))
    print("Test 3: " + str(checkOnesSegment(test3)))
    print("Test 4: " + str(checkOnesSegment(test4)))
    print("Test 5: " + str(checkOnesSegment(test5)))
    print("Test 6: " + str(checkOnesSegment(test6)))
    print("Test 7: " + str(checkOnesSegment(test7)))
    print("Test 8: " + str(checkOnesSegment(test8)))