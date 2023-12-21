def main():
    input = readFile("input.txt")
    challenge1Result = challenge1(input)
    print("Challenge 1: ", challenge1Result)
    # challenge2Result = challenge2(input)
    # print("Challenge 2: ", challenge2Result)

def challenge1(input):
    data = [[] for _ in range(8)]

    current_region = 0
    for index, line in enumerate(input):
        if not line:
            current_region += 1
            continue
        
        if current_region == 0:
            data[0] = line.split(" ")
        else:
            data[current_region].append(line.split(" "))
    
    lowest_location = -1

    for index, seed in enumerate(data[0]):
        current_value = int(seed)
        current_index = 1

        while current_index <= 7:
            current_list = list(filter(lambda x: (int(x[1]) + int(x[2]) - 1 >= current_value) and current_value >= int(x[1]), data[current_index]))
            
            if len(current_list) == 1:
                arr = current_list[0]
                current_value = current_value - int(arr[1]) + int(arr[0])

            if current_index == 7:
                if lowest_location == -1 or current_value < lowest_location:
                    lowest_location = current_value
            
            current_index += 1
    
    return lowest_location


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
