# puzzle input
with open("puzzle input 8") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input 8") as file:
    testdata = [x.strip("\n") for x in file.readlines()]


# format data
def formatData(data):
    formated_data = []
    for x in data:
        instruction = x.split(" ")
        operation =  instruction[0]
        agrument = instruction [1]
        if agrument.startswith("+"):
            agrument.lstrip("+")
        instruction_list = [operation, int(agrument)]
        formated_data.append(instruction_list)
    return formated_data


def findLoop(code):
    loop = []
    for i in range(0, len(code), 1):
        loop.append(False)
    loop.append(True)
    line = 0
    acc = 0
    while not loop[line]:
        loop[line] = True
        operation = code[line][0]
        argument = code[line][1]
        if operation == "acc":
            acc += argument
        elif operation == "jmp":
            line += (argument-1)
        line += 1
    if line == len(code):
        return True, acc
    else:
        return False, acc

def repairCode(code):
    repaired_code = code
    for index, instruction in enumerate(code):
        operation = instruction[0]
        if operation == "jmp":
            repaired_code[index][0] = "nop"
            worked, acc = findLoop(repaired_code)
            if worked:
                return acc
            else:
                repaired_code[index][0] = "jmp"
        if operation == "nop":
            repaired_code[index][0] = "jmp"
            worked, acc = findLoop(repaired_code)
            if worked:
                return acc
            else:
                repaired_code[index][0] = "nop"
    return "Geht nicht"


handheld_code = formatData(rawdata)
print(repairCode(handheld_code))
