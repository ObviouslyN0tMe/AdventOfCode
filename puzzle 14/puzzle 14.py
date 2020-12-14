# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip("\n") for x in file.readlines()]


def formatData(data):
    format_data = []
    for line in data:
        if line.startswith("mem"):
            line = line.strip("mem[")
            line_list = line.split("] = ")
            format_data.append(line_list)
        else:
            line_list = line.split(" = ")
            format_data.append(line_list)
    return format_data

def getBinFromDecimal(number):
    bit = ""
    number = int(number)
    for i in range(35, -1, -1):
        if number >= 2**i:
            bit += "1"
            number -= 2**i
        else:
            bit += "0"
    return bit


def applyMask1(mask, number):
    list_number = list(number)
    for index, bit in enumerate(mask):
        if bit != "X":
            list_number[index] = bit
    masked_number = "".join(list_number)
    return masked_number


def runProgramm1(data):
    mask = ""
    result_dict = {}
    result = 0
    for line in data:
        if line[0] == "mask":
            mask = line[1]
        else:
            bin_number = getBinFromDecimal(line[1])
            masked_number = applyMask1(mask, bin_number)
            result_dict[line[0]] = masked_number
    for index, value in result_dict.items():
        result += int(value, 2)
    return result


def getAllIndexes(index):
    all_indexes = [index]
    new_indexes = []
    while all_indexes[0].count("X") != 0:
        occur_index = all_indexes[0].find("X")
        for index in all_indexes:
            list_index = list(index)
            list_index[occur_index] = "0"
            index = "".join(list_index)
            new_indexes.append(index)
            list_index[occur_index] = "1"
            index = "".join(list_index)
            new_indexes.append(index)
        all_indexes = new_indexes
        new_indexes = []
    return all_indexes


def applyMask2(mask, index):
    list_index = list(index)
    for index, bit in enumerate(mask):
        if bit != "0":
            list_index[index] = bit
    masked_index = "".join(list_index)
    return masked_index


def runProgramm2(data):
    mask = ""
    result_dict = {}
    result = 0
    for line in data:
        if line[0] == "mask":
            mask = line[1]
        else:
            bin_index = getBinFromDecimal(line[0])
            masked_index = applyMask2(mask, bin_index)
            all_indexes = getAllIndexes(masked_index)
            for index in all_indexes:
                result_dict[int(index, 2)] = line[1]
    for value in result_dict.values():
        result += value
    return result


code = formatData(testdata)
# Part 1
print(runProgramm1(code))
# Part 2
print(runProgramm2(code))
