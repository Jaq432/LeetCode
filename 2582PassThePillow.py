def passThePillow(n: int, time: int) -> int:
    print(f"New Run: n = {n} time = {time}")
    
    if n == time:
        return time-1

    forward = True
    pointer = 1
    while time > 0:
        if forward and pointer == n:
            pointer -= 1
            time -= 1
            forward = False
            print("Reached the end, returning...")
            continue
            
        elif not forward and pointer == 1:
            pointer += 1
            time -= 1
            forward = True
            print("Reached the beginning, advancing...")
            continue
            
        elif forward:
            pointer += 1
            time -= 1
            print("Advancing...")
            continue
            
        elif not forward:
            pointer -= 1
            time -= 1
            print("Returning...")
            continue
    
    return pointer
    
    '''
    time += 1
    
    forward = True
    while True:
        if time > n:
            time -= n
            forward = not forward
        else:
            if forward:
                return time
            else:
                return n - time
    '''

def main():
    print(f"Result: {passThePillow(4,5)} Expected: 2")
    print(f"Result: {passThePillow(3,2)} Expected: 3")
    print(f"Result: {passThePillow(3,3)} Expected: 3")
    print(f"Result: {passThePillow(18,38)} Expected: 5")
    print(f"Result: {passThePillow(2,341)} Expected: 2")

main()