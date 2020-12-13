with open("my puzzle input 2") as file:
    data = [x for x in file.readlines()]
passwords = []
policys = []
valid_passwords = 0
checked = 0
for x in data:
    splited = x.split(":")
    policys.append(splited[0])
    password = splited[1].strip("\n")
    password = password.strip(" ")
    passwords.append(password)
for index, p in enumerate(passwords):
    policy = policys[index]
    policy_split = policy.split(" ")
    letter = policy_split[1]
    amount = policy_split[0]
    amount_split = amount.split("-")
    position1 = int(amount_split[0]) - 1
    position2 = int(amount_split[1]) - 1
    if (p[position1] == letter) != (p[position2] == letter):
        valid_passwords += 1
print(valid_passwords)
