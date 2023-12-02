def countCharacters(words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """

    count = 0

    # go over each word
    for i in range(len(words)):
        charsDisposible = chars
        tempCounter = 0
        # go over each letter of each word
        for j in range(len(words[i])):
            # if the word's letter isn't in the char list
            if words[i][j] not in charsDisposible:
                # go to the next word
                print("breaking")
                break
            # if the word's letter is in the char list
            if words[i][j] in charsDisposible:
                # count it and remove the letter from the chars list
                print("counting")
                charsDisposible.replace(words[i][j], "")
                tempCounter += 1
        count += tempCounter

    return count



print(countCharacters(["cat","bt","hat","tree"], "atach"))
#print(countCharacters(["hello","world","leetcode"], "welldonehoneyr"))