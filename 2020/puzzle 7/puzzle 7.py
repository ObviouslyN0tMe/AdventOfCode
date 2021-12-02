with open("puzzle input 7") as file:
    rawdata = [x.strip(".\n") for x in file.readlines()]

testdata = ["light red bags contain 1 bright white bag, 2 muted yellow bags",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags",
            "bright white bags contain 1 shiny gold bag",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags",
            "faded blue bags contain no other bags",
            "dotted black bags contain no other bags"]


def formatData(data):
    data_important = []
    formated_data = {}
    for x in data:
        x = x.replace(" bags", "")
        x = x.replace(" bag", "")
        data_important.append(x)
    for rule in data_important:
        rule = rule.split(" contain ")
        containing_bag = rule[0]
        contained_bags = rule[1]
        contained_bags = contained_bags.split(", ")
        contained_bags_dict = {}
        for bag in contained_bags:
            if bag[0:2] == "no":
                count = "no"
            else:
                count = int(bag[0])
            color = bag[2:]
            contained_bags_dict[color] = count
        formated_data[containing_bag] = contained_bags_dict
    return formated_data


def findDirectContainers(bagcolor, rules):
    direct_containers = []
    for container, contained in rules.items():
        if bagcolor in contained:
            direct_containers.append(container)
    return direct_containers


def findAllContainers(bagcolor, rules):
    all_containers = []
    direct_containers = findDirectContainers(bagcolor, rules)
    all_next_containers = []
    while direct_containers:
        for container in direct_containers:
            all_containers.append(container)
            if container in rules.keys():
                rules.pop(container)
        for container in direct_containers:
            next_containers = findDirectContainers(container, rules)
            for next_container in next_containers:
                if next_container not in all_next_containers:
                    all_next_containers.append(next_container)
        direct_containers = all_next_containers
        all_next_containers = []
    return all_containers


def content(bagcolor, rules):
    result = 1
    bags = rules[bagcolor]
    for color, amount in bags.items():
        if amount == "no":
            pass
        else:
            result += int(amount) * content(color, rules)
    return result


formated = formatData(rawdata)
all_containers = findAllContainers("shiny gold", formated)
print(content("shiny gold", formated)-1)
