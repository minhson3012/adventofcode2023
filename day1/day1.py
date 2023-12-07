def main():
    input = readFile("input.txt")
    challenge1Result = challenge1(input)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge2(input)
    print("Challenge 2: ", challenge2Result)


def challenge1(input):
    numbers = []
    total = 0
    for line in input:
        currentNum = []
        for i in line:
            if(i.isnumeric()):
                currentNum.append(i)
        if len(currentNum) > 1:
            numbers.append(int(currentNum[0] + currentNum[len(currentNum) - 1]))
        else:
            numbers.append(int(currentNum[0] + currentNum[0]))

    for num in numbers:
        total += num
    return total


def challenge2(input):
    numbers = []
    total = 0
    for line in input:
        currentNum = []

        currentNum += [{"value": "1", "index": idx} for idx in range(len(line)) if line.startswith("one", idx)]
        currentNum += [{"value": "2", "index": idx} for idx in range(len(line)) if line.startswith("two", idx)]
        currentNum += [{"value": "3", "index": idx} for idx in range(len(line)) if line.startswith("three", idx)]
        currentNum += [{"value": "4", "index": idx} for idx in range(len(line)) if line.startswith("four", idx)]
        currentNum += [{"value": "5", "index": idx} for idx in range(len(line)) if line.startswith("five", idx)]
        currentNum += [{"value": "6", "index": idx} for idx in range(len(line)) if line.startswith("six", idx)]
        currentNum += [{"value": "7", "index": idx} for idx in range(len(line)) if line.startswith("seven", idx)]
        currentNum += [{"value": "8", "index": idx} for idx in range(len(line)) if line.startswith("eight", idx)]
        currentNum += [{"value": "9", "index": idx} for idx in range(len(line)) if line.startswith("nine", idx)]

        for index, i in enumerate(line):
            if(i.isnumeric()):
                currentNum.append({"value": i, "index": index})
        
        currentNum = sorted(currentNum, key=lambda x:x["index"])

        newNum = 0
        if len(currentNum) > 1:
            newNum = int(currentNum[0]["value"] + currentNum[len(currentNum) - 1]["value"])
            numbers.append(newNum)
        else:
            newNum = int(currentNum[0]["value"] + currentNum[0]["value"])
            numbers.append(newNum)

    for num in numbers:
        total += num
    return total


def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read().splitlines()
    file.close()
    return inputLines


if __name__ == "__main__":
    main()
