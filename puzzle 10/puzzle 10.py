# puzzle input
with open("puzzle input 10") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input 10") as file:
    testdata = [x.strip("\n") for x in file.readlines()]

def formatData(data):
    formated_data = [0]
    for x in data:
        formated_data.append(int(x))
    formated_data.sort()
    highest = formated_data[-1]
    formated_data.append(highest + 3)
    return formated_data


def countDiffs(adapters):
    diff1 = 0
    diff3 = 0
    missingfirst = adapters.copy()
    missingfirst.pop(0)
    for index, adapter in enumerate(missingfirst):
        diff = adapter - adapters[index]
        if diff == 3:
            diff3 += 1
        elif diff == 1:
            diff1 += 1
    return diff1, diff3


def findFixAdapters(adapters):
    diff3 = [0]
    missingfirst = adapters.copy()
    missingfirst.pop(0)
    for index, adapter in enumerate(missingfirst):
        diff = adapter - adapters[index]
        if diff == 3:
            if adapter not in diff3:
                diff3.append(adapter)
            if adapters[index] not in diff3:
                diff3.append(adapters[index])
    diff3.sort()
    return diff3


def findMaxGapDiff(fix_adapters):
    missingfirst = fix_adapters.copy()
    missingfirst.pop(0)
    maxdiff = 0
    for index, adapter in enumerate(missingfirst):
        diff = adapter - fix_adapters[index]
        if diff > maxdiff:
            maxdiff = diff
    return maxdiff


def countOptions(fix_adapters, adapters):
    missingfirst = adapters.copy()
    missingfirst.pop(0)
    max_in_gap = 0
    options = 1
    # calculate options per gap
    for index, adapter in enumerate(missingfirst):
        if adapter not in fix_adapters:
            max_in_gap += 1
        elif max_in_gap != 0:
            option_in_gap = 2**max_in_gap
            max_in_gap = 0
            fix_index = fix_adapters.index(adapter)
            fix_diff = adapter - fix_adapters[fix_index-1]
            if fix_diff >= 4:
                option_in_gap -= 1
            options *= option_in_gap
    return options


all_adapters = formatData(rawdata)
fix_adapters = (findFixAdapters(all_adapters))
# print(findMaxGapDiff(fix_adapters))    max = 4 so min_in_gap is always 1
all_options = countOptions(fix_adapters, all_adapters)
print("Total options:", all_options)
