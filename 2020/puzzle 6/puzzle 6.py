with open("puzzle input 6") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
testdata = ["abc",
            "",
            "a",
            "b",
            "c",
            "",
            "ab",
            "ac",
            "",
            "a",
            "a",
            "a",
            "a",
            "",
            "b"]


def collectGroupanswers(data):
    group_answer = ""
    membercount = 0
    group_answers = {}
    last_index = len(data) - 1
    # making sure last groupanswer gets appended
    if data[last_index] != "":
        data.append("")
    for x in data:
        if x != "":
            group_answer += x
            membercount += 1
        else:
            group_answer = group_answer.strip()
            group_answers[group_answer] = membercount
            group_answer = ""
            membercount = 0
    return group_answers


# if anyone answers
def formatGroupAnswersAnyone(answers):
    formated_answers = []
    for answer in answers:
        contains = ""
        for letter in answer:
            if letter not in contains:
                contains += letter
        formated_answers.append(contains)
    return formated_answers


# if everyone answers
def formatGroupAnswersEveryone(answers):
    formated_answers = []
    for answer, members in answers.items():
        contains = ""
        for letter in answer:
            count = answer.count(letter)
            if count == members and letter not in contains:
                contains += letter
        formated_answers.append(contains)
    return formated_answers


def countAllAnswers(answers):
    totalcount = 0
    for answer in answers:
        totalcount += len(answer)
    return totalcount


x = collectGroupanswers(rawdata)
print(x)
y = formatGroupAnswersEveryone(x)
print(y)
print(countAllAnswers(y))



