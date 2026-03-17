def restoreIpAddresses(s: str) -> list[str]:
    print(f"Testing: {s}")
    highVal = 255

    possibleFirstIPs = []
    possibleSecondIPs = []
    possibleIPs = []

    if len(s) == 4:
        return f"{s[0]}.{s[1]}.{s[2]}.{s[3]}"

    # Get possible first nums
    for i in range(1,4):
        if int(s[:i]) <= highVal:
            possibleFirstIPs.append(s[:i])
    
    for i in possibleFirstIPs:
        sClone = s
        sClone.replace(i,"")
        # Get possible second nums
        for j in range(1,4):
            if int(sClone[:j]) <= highVal:
                possibleSecondIPs.append(sClone[:j])

    print(f"First: {possibleFirstIPs}")
    print(f"Second: {possibleSecondIPs}")



print(restoreIpAddresses("25525511135"))
print(restoreIpAddresses("0000"))
print(restoreIpAddresses("101023"))