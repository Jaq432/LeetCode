def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    lastWordLength = 0
    wordFlag = False
    for letter in s[::-1]:
        if letter == " " and wordFlag:
            break
        elif letter == " ":
            continue
        elif letter != " ":
            wordFlag = True
            lastWordLength += 1
    return lastWordLength

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))