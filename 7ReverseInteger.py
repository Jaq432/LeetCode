def reverse(x: int) -> int:
    lowBound = -2**31
    highBound = (2**31)-1
    stringifiedInput = str(x)
    sign = ""
    if "-" in stringifiedInput:
        sign = "-"
        stringifiedInput = stringifiedInput.replace("-","")
    stringifiedInputReversed = int(sign + stringifiedInput[::-1])
    
    if stringifiedInputReversed > highBound or stringifiedInputReversed < lowBound:
        return 0
    return int(stringifiedInputReversed)

print(reverse(123))
print(reverse(-123))
print(reverse(120))