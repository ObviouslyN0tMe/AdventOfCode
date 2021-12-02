with open("puzzle input 4") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
testdata = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
            "",
            "hcl:#ae17e1 iyr:2013",
            "eyr:2024",
            "ecl:brn pid:760753108 byr:1931",
            "hgt:179cm",
            "",
            "hcl:#cfa07d eyr:2025 pid:166559648",
            "iyr:2011 ecl:brn hgt:59in"]


# byr (Birth Year) - at least 1920 and at most 2002
def validateByr(fieldcontent):
    if 1920 <= int(fieldcontent) <= 2002:
        return True
    else:
        return False


# iyr (Issue Year) - at least 2010 and at most 2020.
def validateIyr(fieldcontent):
    if 2010 <= int(fieldcontent) <= 2020:
        return True
    else:
        return False


# eyr (Expiration Year) - at least 2020 and at most 2030.
def validateEyr(fieldcontent):
    if 2020 <= int(fieldcontent) <= 2030:
        return True
    else:
        return False


# hgt (Height) - a number followed by either cm or in:
def validateHgt(fieldcontent):
    valid = False
    if fieldcontent.endswith("cm"):
        #   If cm, the number must be at least 150 and at most 193.
        height = fieldcontent.strip("cm")
        if 150 <= int(height) <= 193:
            valid = True
    elif fieldcontent.endswith("in"):
        #   If in, the number must be at least 59 and at most 76.
        height = fieldcontent.strip("in")
        if 59 <= int(height) <= 76:
            valid = True
    return valid


# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def validateHcl(fieldcontent):
    contains = ["a", "b", "c", "d", "e", "f", "#"]
    valid = False
    if fieldcontent.startswith("#") and len(fieldcontent) == 7:
        for x in contains:
            fieldcontent = fieldcontent.replace(x, "")
        for x in range(0, 10, 1):
            fieldcontent = fieldcontent.replace(str(x), "")
        if len(fieldcontent) == 0:
            valid = True
    return valid


# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def validateEcl(fieldcontent):
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    valid = False
    for x in eye_colors:
        if fieldcontent == x:
            valid = True
    return valid


# pid (Passport ID) - a nine-digit number, including leading zeroes.
def validatePid(fieldcontent):
    valid = False
    if len(fieldcontent) == 9:
        for x in range(0, 10, 1):
            fieldcontent = fieldcontent.replace(str(x), "")
        if len(fieldcontent) == 0:
            valid = True
    return valid


# cid (Country ID) - we dont care about that
def validateCid(fieldcontent):
    return True


# each passport becomes one item in a list
def formatPassports(data):
    passport = ""
    formated_passports = []
    last_index = len(data) - 1
    # making sure last passport gets appended
    if data[last_index] != "":
        data.append("")
    for x in data:
        if x != "":
            passport += x
            passport += " "
        else:
            passport = passport.strip()
            formated_passports.append(passport)
            passport = ""
    return formated_passports


def validatePassport(passport):
    validatefunctions = {"byr": validateByr, "iyr": validateIyr, "eyr": validateEyr, "hgt": validateHgt,
                         "hcl": validateHcl, "ecl": validateEcl, "pid": validatePid, "cid": validateCid}

    validated = {"byr": False, "iyr": False, "eyr": False, "hgt": False,
                 "hcl": False, "ecl": False, "pid": False, "cid": True}

    fields = passport.split(" ")

    # check which fields are valid
    for field in fields:
        field_name = field.split(":")[0]
        field_content = field.split(":")[1]
        valid = validatefunctions[field_name](field_content)
        validated[field_name] = valid

    # return
    if False not in validated.values():
        return True
    else:
        return False


def countValidPassports(passport_list):
    valid_passports = 0
    for passport in passport_list:
        if validatePassport(passport):
            valid_passports += 1
    return valid_passports


passports = formatPassports(rawdata)
validPassports = countValidPassports(passports)
print("There are " + str(validPassports) + " out of " + str(len(passports)) + " valid.")
