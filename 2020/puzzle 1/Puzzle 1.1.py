with open("my puzzle input") as file:
    data = [int(x) for x in file.readlines()]
data.sort()
reverse = list(reversed(data))
possible_a = []
possible_b = []
testet = []
stop = 0
stop2 = 0
for a in data:
    b = 2020 - a
    for x in data:
        if x == a:
            break
        for i in reverse:
            if i == a:
                stop2 = 1
                break
            if i == x:
                break
            sum = x + i
            if sum > b:
                testet.append(i)
            if sum == b:
                print(x, i, a, a*x*i)
                stop = 1
                break
            if sum < b:
                break
        if stop2 == 1:
            stop2 = 0
            break
        if stop == 1:
            break
        for t in testet:
            reverse.remove(t)
        testet = []
    if stop == 1:
        break

