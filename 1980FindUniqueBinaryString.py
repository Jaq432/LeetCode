def findDifferentBinaryString(nums: list[str]) -> str:
    possibleNums = 2 ** len(nums[0])
    for i in range(possibleNums):
        
        binI = str(bin(i)).replace("0b","")
        
        # Add leading zeros
        binI = ("0"*(len(nums[0]) - len(binI))) + binI
        
        #print(f"binI: {binI}")
        #print(f"Nums: {nums}")
        
        if binI in nums:
            continue
        return binI
    
    return ""



print(findDifferentBinaryString(["01","10"]))
print(findDifferentBinaryString(["00","01"]))
print(findDifferentBinaryString(["111","011","001"]))

#findDifferentBinaryString(["01","10"])
#findDifferentBinaryString(["00","01"])
#findDifferentBinaryString(["111","011","001"])