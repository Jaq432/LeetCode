def countCharacters(words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """

    sumOfLength = 0

    for word in words:
        characters = list(chars)
        wordLength = len(word)
        goodLetterCount = 0
        for letter in word:
            if letter in characters:
                characters.remove(letter)
                goodLetterCount += 1
            else:
                pass
        if wordLength == goodLetterCount:
            sumOfLengths += wordLength
    return sumOfLength




    '''
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
                tempCounter = 0
                break
            # if the word's letter is in the char list
            if words[i][j] in charsDisposible:
                # count it and remove the letter from the chars list
                charsDisposible.replace(words[i][j], "")
                tempCounter += 1
                break
        count += tempCounter

    
    return count
    '''


#print(countCharacters(["cat","bt","hat","tree"], "atach")) # 6
#print(countCharacters(["hello","world","leetcode"], "welldonehoneyr")) # 10
print(countCharacters(["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin","ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb","ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl","boygirdlggnh","xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx","nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop","hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx","juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr","lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo","oxgaskztzroxuntiwlfyufddl","tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp","qnagrpfzlyrouolqquytwnwnsqnmuzphne","eeilfdaookieawrrbvtnqfzcricvhpiv","sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz","yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue","hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv","cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo","teyygdmmyadppuopvqdodaczob","qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs","qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"], "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp")) # 0