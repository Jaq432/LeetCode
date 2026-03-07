def letterCombinations(digits: str) -> list[str]:
    
    numberLetterMap = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",
    }
    
    combinations = []
    outputCombinations = []
    for i in digits:
        #print(numberLetterMap[i])
        combinations.append(numberLetterMap[i])

    print(f"Output Combinations{combinations}")

    if len(digits) == 1:
        for i in combinations[0]:
            outputCombinations.append(i)

    if len(digits) == 2:
        for i in combinations[0]:
            for j in combinations[1]:
                outputCombinations.append(f"{i}{j}")

    if len(digits) == 3:
        for i in combinations[0]:
            for j in combinations[1]:
                for k in combinations[2]:
                    outputCombinations.append(f"{i}{j}{k}")

    if len(digits) == 4:
        for i in combinations[0]:
            for j in combinations[1]:
                for k in combinations[2]:
                    for l in combinations[3]:
                        outputCombinations.append(f"{i}{j}{k}{l}")

    return outputCombinations





    #num1 = "abc"
    #num2 = "def"
    #num3 = "ghi"
    #num4 = "jkl"
    #num5 = "mno"
    #num6 = "pqrs"
    #num7 = "tuv"
    #num8 = "wxyz"
    

print(letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letterCombinations("2"))  # ["a","b","c"]
print(letterCombinations("248"))

#letterCombinations("23")
#letterCombinations("2")
#letterCombinations("248")