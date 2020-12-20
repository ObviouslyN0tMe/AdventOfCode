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
                if subrule not in rules.keys():
                    rules[subrule] = [rule_nr]
                else:
                    rules[subrule].append(rule_nr)
    return rules, messages


def checkIfValid(message, rules):
    message = message.replace("a", rules["a"][0] + " ")
    message = message.replace("b", rules["b"][0] + " ")
    done = False
    results = [message]
    valid = False
    while not done:
        new_results = []
        for result in results:
            for key in rules.keys():
                if key in result:
                    for rule_nr in rules[key]:
                        new_result = result.replace(key, rule_nr, 1)
                        if new_result not in new_results:
                            new_results.append(new_result)
        results = new_results.copy()
        if not results:
            done = True
        if ["0"] in results:
            done = True
            valid = True
        print(len(results))
    return valid


def validateMessages(messages, rules):
    count = 0
    for message in messages:
        valid = checkIfValid(message, rules)
        print(valid)
        if valid:
            count += 1
    return count


rules, messages = formatData(rawdata)
print(validateMessages(messages, rules))
