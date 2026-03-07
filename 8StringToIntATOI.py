def myAtoi(s: str) -> int:
    upperBound = (2**31)-1
    lowerBound = (-2**31)
    sign = ""
    outputNum = "0"
    firstPass = True

    s = s.strip()

    for i in s:
        #print(f"Checking character: {i}")
        # look at each char 1 by 1
        try:
            # Get sign, only do this once
            if firstPass:
                if i == "-" or i == "+":
                    sign = i
                else:
                    int(i)
                    outputNum = i
                firstPass = False
                continue
            # Add each number we see
            # Break out of loop if not number
            int(i)
            outputNum += i
        except:
            break

    outputNum = sign + outputNum
    print(f"Trying to turn this into an int: {outputNum}")
    outputNum = int(outputNum)
    if outputNum > upperBound:
        outputNum = upperBound
    elif outputNum < lowerBound:
        outputNum = lowerBound

    return outputNum

#print(myAtoi("42"))             # 42
#print(myAtoi("-042"))           # -42
#print(myAtoi("1337c0d3"))       # 1337
#print(myAtoi("0-1"))            # 0
#print(myAtoi("words and 987"))  # 0
#print(myAtoi("-91283472332"))
print(myAtoi("+1"))