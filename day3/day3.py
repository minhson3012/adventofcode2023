import re

def main():
    input = readFile("input.txt")
    # challenge1Result = challenge1(input)
    # print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge2(input)
    print("Challenge 2: ", challenge2Result)



def challenge1(input):
    total = 0
    for index, line in enumerate(input):
        new_line = line
        values = list(filter(lambda x: x, re.sub("[^0-9]", " ", new_line).split(" ")))
        current_index = 0

        for num in values:
            is_part = False
            num_index = line.index(num)

            if num_index <= current_index and current_index != 0:
                num_index = line.find(num, current_index)

            current_index = num_index + len(num)

            start_index = num_index if num_index == 0 else (num_index - 1)
            end_index = (num_index + len(num) - 1) if (num_index + len(num) - 1) == (len(line) - 1) else (num_index + len(num))

            vertical_indexes = list(range(start_index, end_index + 1))

            if index > 0 and not is_part:
                for sub_index in vertical_indexes:
                    symbol = input[index - 1][sub_index]
                    if symbol != '.' and not symbol.isnumeric():
                        total += int(num)
                        is_part = True
                        print(index, num)
                        break
            
            if index < 139 and not is_part:
                for sub_index in vertical_indexes:
                    symbol = input[index + 1][sub_index]
                    if symbol != '.' and not symbol.isnumeric():
                        total += int(num)
                        is_part = True
                        print(index, num)
                        break
            
            if num_index != 0 and line[num_index - 1] != '.' and not is_part and not line[num_index - 1].isnumeric():
                total += int(num)
                print(index, num)
                is_part = True

            if (num_index + len(num) - 1) < len(line) - 1 and line[num_index + len(num)] != '.' and not is_part and not line[num_index + len(num)].isnumeric():
                total += int(num)
                print(index, num)
                is_part = True

    return total


def challenge2(input):
    total = 0

    num_list = []
    asterisk_list = []
    for index, line in enumerate(input):
        new_line = line
        values = list(filter(lambda x: x, re.sub("[^0-9*]", " ", new_line).split(" ")))
        current_index = 0

        current_num_list = []
        current_ast_list = []

        for item in values:
            num_index = line.index(item)

            if num_index <= current_index and current_index != 0:
                num_index = line.find(item, current_index)

            current_index = num_index + len(item)
            if item.isnumeric():
                current_num_list.append(num_index)
            else:
                current_ast_list.append(num_index)

        num_list.append(current_num_list)
        asterisk_list.append(current_ast_list)
    print(num_list)
    return total


def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read().splitlines()
    file.close()
    return inputLines


if __name__ == "__main__":
    main()
