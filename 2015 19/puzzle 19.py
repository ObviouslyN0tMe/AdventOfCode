# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]

element_to_letter = {"Ca": "A",
                     "B:": "B",
                     "Al": "D",
                     "F" : "E",
                     "H" : "F",
                     "Mg": "G",
                     "N" : "H",
                     "O" : "I",
                     "P" : "J",
                     "Si": "K",
                     "Th": "L",
                     "Ti": "M",
                     "e" : "N",
                     "Rn": "O",
                     "Ar": "P",
                     "Y" : "Q",
                     "C" : "C"}


def changeElementsToLetters(line):
    for old, new in element_to_letter:
        line.replace(old, new)


# TODO: try calc without programm
