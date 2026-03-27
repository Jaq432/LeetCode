'''
You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.
'''
from collections import defaultdict


def longestBalancedString2(s: str) -> int:
    slen = len(s)
    longestLen = 0
    pointer1 = 0
    pointer2 = 0
    for i in range(slen):
        while 













def longestBalancedSubstring(s: str) -> int:
    sLen = len(s)
    longestBalancedLength = 0
    for i in range(sLen):
        letterCountDict = defaultdict(int)
        for j in range(i,sLen):
            letterCountDict[s[j]] += 1
        if len(set(letterCountDict.values())) == 1:
            longestBalancedLength = max(longestBalancedLength, j-i+1)
    return longestBalancedLength




def longestBalanced(s: str) -> int:
    sLen = len(s)
    longestStringNum = 0
    for i in range(sLen):
        holdingDict = defaultdict(int)
        for j in range(i,sLen):
            holdingDict[s[j]] += 1
        if len(set(holdingDict.values())) == 1:
            longestStringNum = max(longestStringNum, j-i+1)
    return longestStringNum



print(longestBalanced("abbac"))     # 4
print(longestBalanced("zzabccy"))   # 4
print(longestBalanced("aba"))       # 4

'''
def longestBalanced(s: str) -> int:
    sLen = len(s)
    longestBalancedLength = 0

    for i in range(sLen):
        print("a")
        currentLength = 0
        currentCharMap = {}
        isBalanced = False

        remainingS = len(s[i:])
        # Go through all of the possible substrings and add their char and repeat value to dict
        for j in range(remainingS):
            print("b")
            if s[i+j] not in currentCharMap.keys():
                print("new char")
                currentCharMap[s[i+j]] = 1
            else:
                print(f"existing char {s[i+j]}")
                currentCharMap[s[i+j]] += 1

        referenceVal = currentCharMap[s[i+j]]

        print(f"currentCharMap: {currentCharMap}")

        print(f"reference val: {referenceVal}")

        # check all l values to make sure they are the same
        for l in currentCharMap.values():
            if l != referenceVal:
                print("broke")
                break
        else:
            print("is balanced")
            isBalanced = True

        if currentLength > longestBalancedLength and isBalanced:
            print("updating longestBalancedLength")
            longestBalancedLength = currentLength

    return longestBalancedLength

print(longestBalanced("abbac"))     # 4
print(longestBalanced("zzabccy"))   # 4
print(longestBalanced("aba"))       # 4'''