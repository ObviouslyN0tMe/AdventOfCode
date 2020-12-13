# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip("\n") for x in file.readlines()]


def formatData(data):
    bus_ids = {}
    arrival_timestamp = int(data[0])
    buses_str = data[1].split(",")
    offset = 0
    for timestamp in buses_str:
        if timestamp != "x":
            bus_ids[int(timestamp)] = offset
        offset += 1
    return arrival_timestamp, bus_ids


# part 1
def findBestBus(arrival, bus_ids):
    best_bus_id = 0
    best_bus_waitingtime = 1000
    for bus_id in bus_ids:
        earlier = arrival % bus_id
        later = bus_id - earlier
        if later < best_bus_waitingtime:
            best_bus_waitingtime = later
            best_bus_id = bus_id
    return best_bus_id, best_bus_waitingtime, best_bus_id*best_bus_waitingtime


# part 2
def calcContestTimestamp(bus_ids, new_start):
    timestamp = new_start
    steps = 1
    for bus_id in bus_ids:
        steps *= bus_id
    steps //= list(bus_ids)[-1]
    won = False
    timestamp -= steps
    ids_to_check = bus_ids.copy()
    ids_to_check.pop(list(bus_ids)[0])
    while not won:
        timestamp += steps
        could_be = True
        for bus_id, offset in ids_to_check.items():
            earlier = timestamp % bus_id
            later = (bus_id - earlier)
            if later != (offset % bus_id):
                could_be = False
        won = could_be
    return timestamp


def winContest(bus_ids):
    ids_checked = {}
    start_timestamp = 0
    for bus_id, offset in bus_ids.items():
        ids_checked[bus_id] = offset
        print(start_timestamp, ids_checked)
        start_timestamp = calcContestTimestamp(ids_checked, start_timestamp)
    return start_timestamp


arrival_time, buses = formatData(rawdata)
print(winContest(buses))
