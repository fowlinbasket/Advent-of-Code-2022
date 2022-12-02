import sys

MoveScores = {
        "rock" : 1,
        "paper" : 2,
        "scissors" : 3
    }

MoveWins = {
    "rock" : "scissors",
    "paper" : "rock",
    "scissors" : "paper"
}

MoveLosses = {
    "rock" : "paper",
    "paper" : "scissors",
    "scissors" : "rock"
}

PlayerMovesPuzzle1 = {
    "A" : "rock",
    "B" : "paper",
    "C" : "scissors",
    "X" : "rock",
    "Y" : "paper",
    "Z" : "scissors"
}

PlayerMovesPuzzle2 = {
    "A" : "rock",
    "B" : "paper",
    "C" : "scissors",
    "X" : "lose",
    "Y" : "draw",
    "Z" : "win"
}

def getTotalMatchScores(p1, p2):
    p1Score, p2Score = getMatchStatus(p1, p2)
    p1Score += MoveScores[p1]
    p2Score += MoveScores[p2]
    return p1Score, p2Score

def getMatchStatus(p1, p2):
    if MoveWins[p1] == p2:
        # p1 wins
        return 6, 0
    if MoveWins[p2] == p1:
        # p2 wins
        return 0, 6
    else:
        # draw
        return 3, 3

def runStrategyGuidePuzzle1(filePath):
    f = open(filePath, "r")
    p1Total, p2Total = 0, 0
    for line in f.readlines():
        line = line.strip("\n")
        if len(line) == 0:
            continue
        players = line.strip("\n").split(" ")
        if len(players) == 2:
            p1 = PlayerMovesPuzzle1[players[0]]
            p2 = PlayerMovesPuzzle1[players[1]]
            matchScores = getTotalMatchScores(p1, p2)
            p1Total += matchScores[0]
            p2Total += matchScores[1]
        else:
            raise Exception("Too many entries found on one line")
    f.close()
    return p1Total, p2Total

def puzzle2(filePath):
    f = open(filePath, "r")
    p1Total, p2Total = 0, 0
    for line in f.readlines():
        lineList = line.strip("\n").split(" ")
        p1Move = PlayerMovesPuzzle2[lineList[0]]
        p2Strategy = PlayerMovesPuzzle2[lineList[1]]
        match p2Strategy:
            case "lose":
                p2Move = MoveWins[p1Move]
            case "win":
                p2Move = MoveLosses[p1Move]
            case _:
                p2Move = p1Move
        matchScores = getTotalMatchScores(p1Move, p2Move)
        p1Total += matchScores[0]
        p2Total += matchScores[1]
    f.close()
    return p1Total, p2Total
    




if __name__ == '__main__':
    puzzle1 = runStrategyGuidePuzzle1(sys.argv[1])
    print(f"The solution to Day 2 Puzzle 1 is {puzzle1[1]}")
    puzzle2Solution = puzzle2(sys.argv[1])
    print(f"The solution to Day 2 Puzzle 2 is {puzzle2Solution[1]}")


