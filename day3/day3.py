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


def valid_num(ast_index, item):
    if ast_index == item["index"] or abs(ast_index - item["index"]) == 1:
        return True
    if item["index"] < ast_index and ast_index - item["index"] <= len(str(item["num"])):
        return True
    if item["index"] > ast_index and item["index"] - ast_index == 1:
        return True

    return False

def challenge2(input):
    total = 0

    num_list = []
    asterisk_list = []
    line_len = 0
    for index, line in enumerate(input):
        if line_len == 0:
            line_len = len(line)
        new_line = line
        values = list(filter(lambda x: x, re.sub("[^0-9]", " ", new_line).split(" ")))
        ast_values = list(filter(lambda x: x, re.sub("[^*]", " ", new_line).split(" ")))
        current_index = 0
        current_ast_index = 0

        current_num_list = []
        current_ast_list = []

        for item in values:
            num_index = line.index(item)

            if num_index <= current_index and current_index != 0:
                num_index = line.find(item, current_index)

            current_index = num_index + len(item)
            # if item.isnumeric():
            current_num_list.append({"index": num_index, "num": item})
            # else:
                # current_ast_list.append(num_index)
            
        for item in ast_values:
            num_index = line.index(item)

            if num_index <= current_ast_index and current_ast_index != 0:
                num_index = line.find(item, current_ast_index)

            current_ast_index = num_index + len(item)
            current_ast_list.append(num_index)

        num_list.append(current_num_list)
        asterisk_list.append(current_ast_list)
    
    for index, ast in enumerate(asterisk_list):
        for item in ast:
            current_num_list = []

            start_index = item - 1 if item > 0 else item
            end_index = item + 1 if item < line_len - 1 else item
            if index - 1 >= 0:
                gear_list = list(filter(lambda x: valid_num(item, x), num_list[index - 1]))
                # print("upper", gear_list)
                for gear in gear_list:
                    current_num_list.append(gear["num"])
            
            if index + 1 < len(input):
                gear_list = list(filter(lambda x: valid_num(item, x), num_list[index + 1]))
                
                for gear in gear_list:
                    current_num_list.append(gear["num"])

            if item - 1 >= 0:
                gear_list = list(filter(lambda x: (start_index - len(str(x["num"])) + 1) == x["index"], num_list[index]))
                
                if len(gear_list) > 0:
                    current_num_list.append(gear_list[0]["num"])
            
            if item + 1 < line_len:
                gear_list = list(filter(lambda x: x["index"] == end_index, num_list[index]))
                
                if len(gear_list) > 0:
                    current_num_list.append(gear_list[0]["num"])


            print("index " + str(index) + "," + "item " + str(item))
            print(current_num_list)
            if len(current_num_list) == 2:
                total += int(current_num_list[0]) * int(current_num_list[1])
    return total


def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read().splitlines()
    file.close()
    return inputLines


if __name__ == "__main__":
    main()
