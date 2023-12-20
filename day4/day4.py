def main():
    input = readFile("input.txt")
    # challenge1Result = challenge1(input)
    # print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge2(input)
    print("Challenge 2: ", challenge2Result)


def challenge1(input):
    total = 0
    for index, line in enumerate(input):
        card = line.split(":")[1].split("|")

        first_list = list(filter(lambda x: x.isnumeric(), card[0].split(" ")))
        second_list = list(filter(lambda x: x.isnumeric(), card[1].split(" ")))

        num_of_hits = 0
        
        for num in first_list:
            if num in second_list:
                num_of_hits += 1

        if num_of_hits > 0:
            total += pow(2, num_of_hits - 1)
    return total


def challenge2(input):
    total = 0
    
    return total


def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read().splitlines()
    file.close()
    return inputLines


if __name__ == "__main__":
    main()
