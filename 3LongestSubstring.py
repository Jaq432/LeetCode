def lengthOfLongestSubstring(s: str) -> int:

    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    
    longestSubstrings = []
    
    for k,i in enumerate(s):
        
        charString = ""
        counter = 0
        for j in s[k:]:
            if j in charString:
                longestSubstrings.append(counter)
                break
            else:
                charString = charString+str(j)
                counter += 1
        else:
            longestSubstrings.append(counter)
    
    print(longestSubstrings)

    return sorted(longestSubstrings,reverse=True)[0]


print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("bbbbb"))    # 1
print(lengthOfLongestSubstring("pwwkew"))   # 3
print(lengthOfLongestSubstring(" "))        # 1
print(lengthOfLongestSubstring("au"))       # 2
