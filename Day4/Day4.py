import sys

class Elf:
    def __init__(self, assignment):
        self.assignment = assignment

    def contains(self, other):
        contained = True
        if len(other.assignment) > len(self.assignment):
            return False
        for section in other.assignment:
            contained &= section in self.assignment
        return contained
    
    def overlaps(self, other):
        for section in self.assignment:
            if section in other.assignment:
                return True
        return False

def getAssignment(s):
    dividerIndex = s.find("-")
    start, stop = int(s[0:dividerIndex]), int(s[dividerIndex + 1:])
    return {i for i in range(start, stop + 1)}

def splitAssignments(s):
    return s.split(",")

def Puzzle1(filePath):
    f = open(filePath, "r")
    total = 0
    for line in f.readlines():
        line = line.strip("\n")
        if len(line) > 0:
            assignments = splitAssignments(line)
            elf1 = Elf(getAssignment(assignments[0]))
            elf2 = Elf(getAssignment(assignments[1]))
            if elf1.contains(elf2) or elf2.contains(elf1):
                total += 1
    f.close()
    return total

def Puzzle2(filePath):
    f = open(filePath, "r")
    total = 0
    for line in f.readlines():
        line = line.strip("\n")
        if len(line) > 0:
            assignments = splitAssignments(line)
            elf1 = Elf(getAssignment(assignments[0]))
            elf2 = Elf(getAssignment(assignments[1]))
            if elf1.overlaps(elf2) or elf2.overlaps(elf1):
                total += 1
    f.close()
    return total

if __name__ == '__main__':
    print(f"The solution to Day 4 Puzzle 1 is {Puzzle1(sys.argv[1])}")
    print(f"The solution to Day 4 Puzzle 2 is {Puzzle2(sys.argv[1])}")
