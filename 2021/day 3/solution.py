with open("puzzleinput") as file:
    data = [int(x.strip("\n")) for x in file.readlines()]

# Part 1
sums = []
new_sum = 0
for binary in data:
    new_sum += binary
    if "9" in str(new_sum):
        sums.append(str(new_sum))
        new_sum = 0
sums.append(str(new_sum))

most_common_digit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for sum in sums:
    for index, digit in enumerate(sum):
        most_common_digit[index] += int(digit)

half = len(data)/2
gamma_rate = ""
epsilon_rate = ""

for total in most_common_digit:
    if total > half:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print("Part 1: " + str(gamma_rate * epsilon_rate))

# Part 2

with open("puzzleinput") as file:
    data_2 = [x.strip("\n") for x in file.readlines()]

oxygen = data_2.copy()
oxygen_generator_rating = 0

for index in range(0, len(data_2[0])):
    count_1 = 0
    count_0 = 0
    new = []
    for binary in oxygen:
        if binary[index] == "1":
            count_1 += 1
        else:
            count_0 += 1
    if count_1 >= count_0:
        most_common = "1"
    else:
        most_common = "0"
    for binary in oxygen:
        if binary[index] == most_common:
            new.append(binary)
    if len(new) == 1:
        oxygen_generator_rating = int(new[0], 2)
        break
    oxygen = new

co2 = data_2.copy()
co2_scrubber_rating = 0

for index in range(0, len(data_2[0])):
    count_1 = 0
    count_0 = 0
    new = []
    for binary in co2:
        if binary[index] == "1":
            count_1 += 1
        else:
            count_0 += 1
    if count_1 >= count_0:
        least_common = "0"
    else:
        least_common = "1"
    for binary in co2:
        if binary[index] == least_common:
            new.append(binary)
    if len(new) == 1:
        co2_scrubber_rating = int(new[0], 2)
        break
    co2 = new

print("Part 2:", str(oxygen_generator_rating * co2_scrubber_rating))