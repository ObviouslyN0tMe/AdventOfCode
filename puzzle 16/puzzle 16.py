# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip("\n") for x in file.readlines()]


def formatData(data):
    rules = {}
    my_ticket = []
    nearby_tickets = []
    step = 0
    for line in data:
        if line == "":
            step += 1
        # rules
        elif step == 0:
            rule = line. split(": ")
            ranges = rule[1].split(" or ")
            range1 = ranges[0].split("-")
            range2 = ranges[1].split("-")
            rules[rule[0]] = [range1, range2]
        # my ticket
        elif step == 1:
            my_ticket = line.split(",")
        # nearby tickets
        else:
            nearby_tickets.append(line.split(","))
    nearby_tickets.remove(nearby_tickets[0])
    return rules, my_ticket, nearby_tickets


def getValidValues(rule):
    valid_values = []
    range1 = rule[0]
    range2 = rule[1]
    for i in range(int(range1[0]), int(range1[1]) + 1, 1):
            valid_values.append(i)
    for i in range(int(range2[0]), int(range2[1]) + 1, 1):
            valid_values.append(i)
    return valid_values


def getAllValidValues(rules):
    all_valid_values = []
    for rule in rules.values():
        valid_values = getValidValues(rule)
        all_valid_values += valid_values
    return all_valid_values


def getTSER(valid_numbers, nearby_tickets):  # ticket scanning error rate
    tser = 0
    for ticket in nearby_tickets:
        for field in ticket:
            if int(field) not in valid_numbers:
                tser += int(field)
    return tser


def getValidTickets(valid_values, nearby_tickets):
    valid_tickets = []
    for ticket in nearby_tickets:
        valid = True
        for field in ticket:
            if int(field) not in valid_values:
                valid = False
        if valid:
            valid_tickets.append(ticket)
    return valid_tickets


def asignPossibleFields(rules, nearby_tickets):
    possible_fields = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for name, value in rules.items():
        valid_values = getValidValues(value)
        for i in range(0, len(nearby_tickets[0]), 1):
            could_be = True
            for ticket in nearby_tickets:
                if int(ticket[i]) not in valid_values:
                    could_be = False
                    break
            if could_be:
                possible_fields[i].append(name)
    return possible_fields


def asignCorrectFields(rules, possible_fields):
    for i in range(0, len(possible_fields)):
        for name in rules.keys():
            count = 0
            position_correct = 0
            name_correct = ""
            for position in possible_fields:
                if name in position:
                    count += 1
                    position_correct = possible_fields.index(position)
                    name_correct = name
            if count == 1:
                possible_fields[position_correct] = name_correct
    return possible_fields


def getSolution(correct_fields, my_ticket):
    solution = 1
    for index, field in enumerate(correct_fields):
        if field.startswith("departure"):
            solution *= int(my_ticket[index])
    return solution


rules, my_ticket, nearby_tickets = formatData(rawdata)
valid_values = getAllValidValues(rules)
valid_tickets = getValidTickets(valid_values, nearby_tickets)
print(getTSER(valid_values, nearby_tickets))
possible_fields = asignPossibleFields(rules, valid_tickets)
correct_fields = asignCorrectFields(rules, possible_fields)
print(getSolution(correct_fields, my_ticket))
