import sys

def getMarker(s, markerLength):
    for i in range(markerLength, len(s)):
        substr = s[i - markerLength:i]
        if not hasRepeatingCharacters(substr):
            return i
    return None

def hasRepeatingCharacters(s):
    for character in s:
        if s.count(character) > 1:
            return True
    return False

def Puzzle1(filePath):
    f = open(filePath)
    marker = getMarker(f.read().strip("\n"), 4)
    f.close()
    return marker

def Puzzle2(filePath):
    f = open(filePath)
    marker = getMarker(f.read().strip("\n"), 14)
    f.close()
    return marker

if __name__ == '__main__':
    print(f"Day 6 Puzzle 1: {Puzzle1(sys.argv[1])}")
    print(f"Day 6 Puzzle 2: {Puzzle2(sys.argv[1])}")