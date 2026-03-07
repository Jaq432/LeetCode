def intToRoman(num: int) -> str:
    romanMap={
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    inputStr = str(num)
    inputStrRev = inputStr[::-1]
    # Forward
    for i in inputStr:
        
        print(i)

    return ""


print(intToRoman(3749)) # MMMDCCXLIX
print(intToRoman(58))   # LVIII
print(intToRoman(1994)) # MCMXCIV