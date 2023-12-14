def largestGoodInteger(num):
    """
    :type num: str
    :rtype: str
    """
    biggestGoodInt = ""

    print(f"input: {num} length: {len(num)}")

    if len(num) < 3: 
        return biggestGoodInt

    for i in range(len(num)-2):
        print(f"Checking with {i}")
        if num[i] == num[i+1] and num[i] == num[i+2]:
            if biggestGoodInt == "":
                biggestGoodInt = num[i] + num[i+1] + num[i+2]
                continue
            else:
                if int(biggestGoodInt) < int(num[i] + num[i+1] + num[i+2]):
                    biggestGoodInt = num[i] + num[i+1] + num[i+2]
                    continue

    return biggestGoodInt

print(largestGoodInteger("6777133339"))
print(largestGoodInteger("2300019"))
print(largestGoodInteger("42352338"))
print(largestGoodInteger("333"))