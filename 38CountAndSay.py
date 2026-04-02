def countAndSay(n: int) -> str:
    strN = str(n)
    outputString = ""
    
    pointer = 0
    currentLetterCount = 0
    
    currentChar = strN[0]
    previousChar = strN[0]

    while pointer < len(strN):
        #print(f"Pointer: {pointer}")
        # Capture the current character
        currentChar = strN[pointer]
        # If the character is a repeat
        if currentChar == previousChar:
            currentLetterCount += 1
        # If it is a new character
        else:
            outputString += f"{currentLetterCount}{previousChar}"
            currentLetterCount = 1
        # Reset the previousChar value
        previousChar = currentChar
        pointer += 1

    outputString += f"{currentLetterCount}{previousChar}"

    return int(outputString)

print(countAndSay(1))
print(countAndSay(4))
print(countAndSay(3322251))