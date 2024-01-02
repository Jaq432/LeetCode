def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        # Make a dict of the numerals and values
        romanDict = {"I":1,
                     "V":5,
                     "X":10,
                     "L":50,
                     "C":100,
                     "D":500,
                     "M":1000,}
        
        reverseInput = s[::-1]
        rollingTotal = 0

        # go through the number in reverse and look at each value
        # if the next value is less than the previous, subtract it from the total
        for letter in reverseInput:
            # First pass
            if rollingTotal == 0:
                rollingTotal += romanDict[letter]
                previousValue = romanDict[letter]
                continue
            if romanDict[letter] < previousValue:
                rollingTotal -= romanDict[letter]
                continue
            rollingTotal += romanDict[letter]
            previousValue = romanDict[letter]

        return rollingTotal

print(romanToInt("III")) # 3
print(romanToInt("LVIII")) # 58
print(romanToInt("MCMXCIV")) # 1994