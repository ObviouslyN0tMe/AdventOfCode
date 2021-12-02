# puzzle input
with open("puzzle input 9") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input 9") as file:
    testdata = [x.strip("\n") for x in file.readlines()]


def formatData(data, preamblelengh):
    formated_preamble = []
    formated_data = []
    for i in range(0, preamblelengh, 1):
        formated_preamble.append(int(data[i]))
    for i in range(preamblelengh, len(data), 1):
        formated_data.append(int(data[i]))
    return formated_preamble, formated_data


def findInvalidNumber(preabmle, numbers):
    valid = False
    for number in numbers:
        # check if 2 of last25 sum up to number
        for x1 in preamble:
            for x2 in preamble:
                if x1 != x2:
                    if number == x1 + x2:
                        valid = True
                        break
            if valid:
                break
        # if number valid
        if valid:
            preamble.remove(preamble[0])
            preamble.append(number)
            valid = False
        # if number invaild
        else:
            return number


def findEncryptionWeakness(invalid, numbers):
    for index, startnumber in enumerate(numbers):
        stop = False
        sum = startnumber
        smallest = startnumber
        largest = startnumber
        while not stop:
            if invalid == sum:
                weakness = smallest + largest
                return weakness
            elif invalid < sum or (index - 1) == len(numbers):
                stop = True
            else:
                index += 1
                sum += numbers[index]
                if numbers[index] < smallest:
                    smallest = numbers[index]
                elif numbers[index] > largest:
                    largest = numbers[index]


# testdata, 5   or  rawdata, 25
preamble, numbers_to_check = formatData(rawdata, 25)
all_numbers = preamble + numbers_to_check
invalid_number = findInvalidNumber(preamble, numbers_to_check)
print(findEncryptionWeakness(invalid_number, all_numbers))