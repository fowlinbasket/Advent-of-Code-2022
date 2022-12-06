import sys

def Puzzle1(filePath):
    stack = {
        "1" : ["H", "C", "R"],
        "2" : ["B", "J", "H", "L", "S", "F"],
        "3" : ["R", "M", "D", "H", "J", "T", "Q"],
        "4" : ["S", "G", "R", "H", "Z", "B", "J"],
        "5" : ["R", "P", "F", "Z", "T", "D", "C", "B"],
        "6" : ["T", "H", "C", "G"],
        "7" : ["S", "N", "V", "Z", "B", "P", "W", "L"],
        "8" : ["R", "J", "Q", "G", "C"],
        "9" : ["L", "D", "T", "R", "H", "P", "F", "S"]
    }
    f = open(filePath)
    for line in f.readlines():
        command = line.strip("\n").split(" ")
        count = int(command[1])
        fromStack = command[3]
        toStack = command[5]
        for _ in range(count):
            stack[toStack].append(stack[fromStack].pop())
    f.close()
    # get the crate on top of each stack
    result = ""
    for i in range(1, len(stack) + 1):
        result += stack[str(i)][len(stack[str(i)]) - 1]
    return result

def Puzzle2(filePath):
    stack = {
        "1" : ["H", "C", "R"],
        "2" : ["B", "J", "H", "L", "S", "F"],
        "3" : ["R", "M", "D", "H", "J", "T", "Q"],
        "4" : ["S", "G", "R", "H", "Z", "B", "J"],
        "5" : ["R", "P", "F", "Z", "T", "D", "C", "B"],
        "6" : ["T", "H", "C", "G"],
        "7" : ["S", "N", "V", "Z", "B", "P", "W", "L"],
        "8" : ["R", "J", "Q", "G", "C"],
        "9" : ["L", "D", "T", "R", "H", "P", "F", "S"]
    }
    f = open(filePath)
    for line in f.readlines():
        command = line.strip("\n").split(" ")
        count = int(command[1])
        fromStack = command[3]
        toStack = command[5]
        movedItems = []
        for _ in range(count):
            movedItems.append(stack[fromStack].pop())
        movedItems.reverse()
        for element in movedItems:
            stack[toStack].append(element)

    f.close()
    # get the crate on top of each stack
    result = ""
    for i in range(1, len(stack) + 1):
        result += stack[str(i)][len(stack[str(i)]) - 1]
    return result

if __name__ == '__main__':
    print(f"The solution to Day 5 Puzzle 1 is {Puzzle1(sys.argv[1])}")
    print(f"The solution to Day 5 Puzzle 2 is {Puzzle2(sys.argv[1])}")