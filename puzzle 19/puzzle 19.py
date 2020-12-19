# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip("\n") for x in file.readlines()]


def formatData(data):
    rules = {}
    messages = []
    rules_done = False
    for line in data:
        if line == "":
            rules_done = True
        elif rules_done:
            messages.append(line)
        else:
            rule = line.split(": ")
            rule_nr = rule[0]
            subrules = rule[1].split(" | ")
            for subrule in subrules:
                subrule = subrule.split(" ")
                if tuple(subrule) not in rules.keys():
                    rules[tuple(subrule)] = [rule_nr]
                else:
                    rules[tuple(subrule)].append(rule_nr)
    return rules, messages


def checkIfValid(message, rules):
    message_list = []
    for letter in message:
        message_list.append(letter)
    for index, letter in enumerate(message_list):
        if letter == "a":
            message_list[index] = "99"
        else:
            message_list[index] = "36"
    done = False
    results = [message_list]
    valid = False
    while not done:
        new_results = []
        used = []
        for result in results:
            for key in rules.keys():
                if len(key) == 1:
                    if key in result:
                        index = result.index(key)
                        result_copy = result.copy()
                        result_copy[index] = rules[key]
                        if result_copy not in results:
                            new_results.append(result_copy)
                        if result not in used:
                            used.append(result)
                else:
                    try:
                        index0 = result.index(key[0])
                        index1 = result.index(key[1])
                    except ValueError:
                        index0 = 0
                        index1 = 0
                    if index1 - index0 == 1:
                        for rule_nr in rules[key]:
                            result_copy = result.copy()
                            result_copy[index0] = rule_nr
                            result_copy.pop(index1)
                            if result_copy not in results:
                                new_results.append(result_copy)
                        if result not in used:
                            used.append(result)
        results = []
        for new_result in new_results:
            results.append(new_result)
        for used_result in used:
            results.append(used_result)
        if not results:
            done = True
        if ["0"] in results:
            done = True
            valid = True
    return valid


def validateMessages(messages, rules):
    count = 0
    for message in messages:
        valid = checkIfValid(message, rules)
        if valid:
            count += 1
    return count


rules, messages = formatData(testdata)
print(validateMessages(messages, rules))
