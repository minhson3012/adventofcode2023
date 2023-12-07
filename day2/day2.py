def main():
    input = readFile("input.txt")
    # challenge1Result = challenge1(input)
    # print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge2(input)
    print("Challenge 2: ", challenge2Result)


def challenge1(input):
    total = 0
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    for index, line in enumerate(input):
        possible = True
        game = line.split(":")[1].replace(";", ",").split(",")
        for attempts in game:
            roll = attempts.strip().split(" ")
            if((roll[1] == "red" and int(roll[0]) > maxRed) \
                or (roll[1] == "green" and int(roll[0]) > maxGreen) \
                or (roll[1] == "blue" and int(roll[0]) > maxBlue)):
                possible = False
                break
        if (possible):
            total += (index + 1)

    return total


def challenge2(input):
    total = 0
    for line in input:
        maxRed = 0
        maxGreen = 0
        maxBlue = 0

        game = line.split(":")[1].replace(";", ",").split(",")
        for attempts in game:
            roll = attempts.strip().split(" ")
            if(roll[1] == "red" and int(roll[0]) > maxRed):
                maxRed = int(roll[0])
            elif(roll[1] == "green" and int(roll[0]) > maxGreen):
                maxGreen = int(roll[0])
            elif(roll[1] == "blue" and int(roll[0]) > maxBlue):
                maxBlue = int(roll[0])
        
        total += maxRed * maxGreen * maxBlue

    return total


def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read().splitlines()
    file.close()
    return inputLines


if __name__ == "__main__":
    main()
