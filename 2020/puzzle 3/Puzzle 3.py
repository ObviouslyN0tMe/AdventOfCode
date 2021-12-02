with open("puzzle input 3") as file:
    data = [x for x in file.readlines()]

# Variablen und Listen
trees = 1
tree = 0
position = 0
pattern = [1, 3, 5, 7, 9]
right = 1
second = False

for p in pattern:
    if p != 9:
        right = p
        for x in data:
            if x[position % 31] == "#":
                tree += 1
            position += right
    else:
        for x in data:
            second = not second
            if second:
                if x[position % 31] == "#":
                    tree += 1
                position += right
    position = 0
    print("Bäume: ", tree)
    trees *= tree
    tree = 0
    right = 1
print("Bäume Produkt: ", trees)
