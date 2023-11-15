def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Sort the words
    strs.sort()

    # Get the first and last words
    firstStr = strs[0]
    lastStr = strs[-1]

    prefix = []

    # Compare the first word prefix to that of the last word
    # Keep within word lengths to not get index errors
    for i in range(len(firstStr)):
        # Add the letters to a list if they match
        if i < len(lastStr) and firstStr[i] == lastStr[i]:
            prefix.append(firstStr[i])
        else:
            break

    # Put the letters back into a string
    return ''.join(prefix)

print(longestCommonPrefix(["flower","flow","flight"])) # fl
print(longestCommonPrefix(["dog","racecar","car"])) # 