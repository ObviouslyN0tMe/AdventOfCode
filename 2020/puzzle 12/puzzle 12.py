# puzzle input
with open("puzzle input 12") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input 12") as file:
    testdata = [x.strip("\n") for x in file.readlines()]

directions = {"N": 0, "E": 1, "S": 2, "W": 3}


def formatData(data):
    formated_data = []
    for instruction in data:
        operation = instruction[0]
        value = int(instruction.strip(operation))
        formated_data.append([operation, value])
    return formated_data


def turn(operator, value, facing):
    turn_speed = value // 90
    if operator == "L":
        facing -= turn_speed
    else:
        facing += turn_speed
    facing %= 4
    return facing


def move(direction, distance, position):
    if direction == 0:
        position["y"] += distance
    elif direction == 1:
        position["x"] += distance
    elif direction == 2:
        position["y"] -= distance
    else:
        position["x"] -= distance
    return position


def move_waypoint(operator, value, position):
    if operator == "L":
        repeat = value // 90
        while repeat > 0:
            x = position["x"]
            y = position["y"]
            position["x"] = - y
            position["y"] = x
            repeat -= 1
    elif operator == "R":
        repeat = value // 90
        while repeat > 0:
            x = position["x"]
            y = position["y"]
            position["x"] = y
            position["y"] = - x
            repeat -= 1
    else:
        direction = directions[operator]
        position = move(direction, value, position)
    return position


def control(instructions):
    ship_position = {"x": 0, "y": 0}
    waypoint_position_rel = {"x": 10, "y": 1}
    for instruction in instructions:
        operator = instruction[0]
        value = instruction[1]
        if operator == "F":
            ship_position["x"] += waypoint_position_rel["x"]*value
            ship_position["y"] += waypoint_position_rel["y"]*value
        else:
            waypoint_position_rel = move_waypoint(operator, value, waypoint_position_rel)
    return ship_position, abs(ship_position["x"]) + abs(ship_position["y"])


x = formatData(rawdata)

print(control(x))
