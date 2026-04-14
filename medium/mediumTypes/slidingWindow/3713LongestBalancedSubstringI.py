'''
You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.
'''
from collections import defaultdict

def longestBalanced(s: str) -> int:
    lenS = len(s)
    longestSubstring = 0
    for i in range(lenS):
        currentLongest = 0
        letterDict = defaultdict(int)
        for j in range(i,lenS):
            letterDict[s[j]] += 1
            currentLongest += 1
            if len(set(letterDict.values())) == 1:
                longestSubstring = max(longestSubstring, currentLongest)
    return longestSubstring






def longestBalanced3(s: str) -> int:
    slen = len(s)
    longestBalancedLen = 0
    for i in range(slen):
        charDict = defaultdict(int)
        for j in range(i,slen):
            charDict[s[j]] += 1
            if len(set(charDict.values())) == 1:
                longestBalancedLen = max(longestBalancedLen, j-i+1)
    return longestBalancedLen


def longestBalanced2(s: str) -> int:
    sLen = len(s)
    longestStringNum = 0
    # Go over the string of chars
    for i in range(sLen):
        # Create an empty dictionary with built in features
        holdingDict = defaultdict(int)
        # Go over all of the remaining characters
        for j in range(i,sLen):
            # Add all of the characters to the dictionary
            holdingDict[s[j]] += 1
            # If all of the values are the same
            if len(set(holdingDict.values())) == 1:
                # Check if the latest version of the dict is balanced
                longestStringNum = max(longestStringNum, j-i+1)
    return longestStringNum



print(longestBalanced("abbac"))     # 4
print(longestBalanced("zzabccy"))   # 4
print(longestBalanced("aba"))       # 2