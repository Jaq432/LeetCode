def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    parTypes = {"(":0,
                ")":0,
                "[":0,
                "]":0,
                "{":0,
                "}":0,
                }
    
    parCompliments = {")":"(",
                      "]":"[",
                      "}":"{",}
    
    charStack = []

    for index, char in enumerate(s):
        if (parTypes[")"] > parTypes["("]) or (parTypes["]"] > parTypes["["]) or (parTypes["}"] > parTypes["{"]):
           return False
        # Add up the quantities of each char
        parTypes[char] += 1

        if char in parCompliments.values():
            charStack.append(char)
            continue

        # If the char is a closing paranthesis
        if char in parCompliments.keys():
            if len(charStack) == 0:
                return False
            # Check if it is the same as the previous opening
            previousChar = charStack.pop()
            if parCompliments[char] != previousChar:
                #print("ParCompliment: " + str(parCompliments[char]) + " prevChar: " + str(previousChar))

                return False


    return (parTypes[")"] == parTypes["("]) and (parTypes["]"] == parTypes["["]) and (parTypes["}"] == parTypes["{"])

print(isValid("()")) # true
print(isValid("()[]{}")) # true
print(isValid("(]")) # false
print(isValid("[()]{}")) # true
print(isValid("([]{})")) # true
print(isValid("([)]")) # should be false
# if an outer parenthesis is closed before an inner, it will cause an issue