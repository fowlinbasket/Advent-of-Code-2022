import sys

def splitCompartments(s):
    splitPoint = (len(s) // 2)
    return s[:splitPoint], s[splitPoint:]

def getSharedItems(c1, c2):
    sharedItems = []
    for item in c1:
        if item in c2 and not item in sharedItems:
            sharedItems.append(item)
    return sharedItems

def getCommonItems(r1, r2, r3):
    commonItems = []
    for item in r1:
        if item in r2 and item in r3 and not item in commonItems:
            commonItems.append(item)
    return commonItems

def getPriority(s):
    if (s.islower()):
        return ord(s) - 96
    else:
        return ord(s) - 38

def Puzzle1(filePath):
    f = open(filePath)
    total = 0
    for line in f.readlines():
        line = line.strip("\n")
        if len(line) > 0:
            c1, c2 = splitCompartments(line)
            for item in getSharedItems(c1, c2):
                total += getPriority(item)
    f.close()
    return total

def Puzzle2(filePath):
    f = open(filePath)
    total = 0
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        bag1, bag2, bag3 = lines[i].strip("\n"), lines[i + 1].strip("\n"), lines[i + 2].strip("\n")
        for item in getCommonItems(bag1, bag2, bag3):
            total += getPriority(item)
    f.close()
    return total
        
if __name__ == '__main__':
    print(f"The solution to Day 3 Puzzle 1 is {Puzzle1(sys.argv[1])}")
    print(f"The solution to Day 3 Puzzle 2 is {Puzzle2(sys.argv[1])}")

