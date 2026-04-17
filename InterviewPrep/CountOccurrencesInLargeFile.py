'''def countOccurrences(fileDir: str, pattern, chunkSize):
    count = 0
    with open(fileDir, "r") as openFile:
        for line in openFile:
            count += line.count(pattern)

    return count'''


# Tried to load by memory size
def countOccurrences(fileDir: str, pattern, chunkSize):
    count = 0
    overlap = len(pattern) - 1
    prev_chunk = ""

    with open(fileDir, "r") as f:
        while True:
            chunk = f.read(chunkSize)
            if not chunk:
                break

            # Combine with previous tail
            combined = prev_chunk + chunk

            combined = combined.replace("\n", "")

            count += combined.count(pattern)

            # Keep last part for overlap
            prev_chunk = combined[-overlap:]
    
    return count

if __name__ == "__main__":
    print(countOccurrences("CountOccurrencesInLargeFile.txt", "about", 1000))

# Generate the file
#with open("CountOccurrencesInLargeFile.txt", "w") as openFile:
#    for i in range(5000):
#        openFile.write("ut Filling this file with things we care abo\n")