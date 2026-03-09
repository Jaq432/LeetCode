def divide(dividend: int, divisor: int) -> int:
    upperBound = (2 ** 31) - 1
    lowerBound = -(2 ** 31)
    
    wholeNums = 0
    posSign = True
    if (divisor < 0 and not dividend < 0) or (dividend < 0 and not divisor < 0):
        posSign = False

    posDivisor = abs(divisor)
    posDividend = abs(dividend)

    if posDivisor == 1 and posSign:
        print("A")
        if abs(dividend) > upperBound:
            return upperBound
        return abs(dividend)
    elif posDivisor == 1 and not posSign:
        print("B")
        if 0 - abs(dividend) < lowerBound:
            return lowerBound
        return 0 - abs(dividend)

    posDivisorHolder = posDivisor
    posDividendHolder = posDividend

    #print(f"posDivisor: {posDivisorHolder}")
    #print(f"posDividend: {posDividendHolder}")

    while posDividendHolder >= posDivisorHolder:
        wholeNums += 1
        posDividendHolder -= posDivisorHolder
    
    if not posSign:
        wholeNums = 0 - wholeNums

    if wholeNums > upperBound:
        return upperBound
    elif wholeNums < lowerBound:
        return lowerBound
    return wholeNums

#print(divide(10,3)) # 3
#print(divide(7,-3)) # -2
#print(divide(-1,1)) # -1
print(divide(-2147483648,-1))