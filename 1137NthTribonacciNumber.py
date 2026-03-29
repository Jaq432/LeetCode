def main():
    print(tribonacci(4))
    print(tribonacci(25))

def tribonacci(inputNum: int):

    if inputNum == 0:
        return 0
    elif inputNum == 1:
        return 1
    elif inputNum == 2:
        return 1

    # Make a starting list with the first 3
    tribonacciList = [0,1,1]
    
    # Numbers bigger than 2
    for i in range(3, inputNum+1):
        numToAddToList = tribonacciList[-1]+tribonacciList[-2]+tribonacciList[-3]
        tribonacciList.append(numToAddToList)
        if i == inputNum:
            return tribonacciList[-1]
    
    return 0

main()