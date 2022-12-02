import sys
from queue import PriorityQueue

class Elf:
    def __init__(self, totalCalories=0):
        self.__totalCalories = totalCalories

    def addCalories(self, calories):
        self.__totalCalories += calories

    def getTotalCalories(self):
        return self.__totalCalories

    def __lt__(self, other):
        # This is for the PriorityQueue
        return self.getTotalCalories() > other.getTotalCalories()

def getHighestCalories(filePath):
    f = open(filePath, "r")
    elves = PriorityQueue()
    elf = Elf()
    for line in f.readlines():
        line = line.strip("\n")
        if len(line) == 0:
            elves.put(elf)
            elf = Elf()
            continue
        else:
            elf.addCalories(int(line))
    f.close()
    return elves

def puzzle1(filePath):
    return getHighestCalories(filePath).get().getTotalCalories()

def puzzle2(filePath):
    totalCalories = 0
    elves = getHighestCalories(filePath)
    for _ in range(3):
        totalCalories += elves.get().getTotalCalories()
    return totalCalories

if __name__ == '__main__':
    print(f"The answer to Day 1 Puzzle 1 is {puzzle1(sys.argv[1])}")
    print(f"The answer to Day 1 Puzzle 2 is {puzzle2(sys.argv[1])}")