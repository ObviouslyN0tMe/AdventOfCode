# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip(")\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip(")\n") for x in file.readlines()]

food_list = {}
all_ingredients = {}
allergens_apperiance = {}
ingredients_apperiance = {}
all_allergens = {}


# format food list
def formatData(data):
    global food_list, all_ingredients, allergens_apperiance, ingredients_apperiance
    for line in data:
        line = line.split(" (contains ")
        line_ingredients = line[0].split(" ")
        line_allergens = line[1].split(", ")
        # save line in a dict
        food_list[tuple(line_allergens)] = line_ingredients
        # save every ingredient with all lines it appears in and create a dict to save the matching allergen later
        for ingredient in line_ingredients:
            if ingredient not in ingredients_apperiance:
                all_ingredients[ingredient] = []
                ingredients_apperiance[ingredient] = [tuple(line_allergens)]
            else:
                ingredients_apperiance[ingredient].append(tuple(line_allergens))
        # save every allergen with all lines it appears in
        for allergen in line_allergens:
            if allergen not in allergens_apperiance:
                all_allergens[allergen] = []
                allergens_apperiance[allergen] = [tuple(line_allergens)]
            else:
                allergens_apperiance[allergen].append(tuple(line_allergens))


# remove all allergenfree ingredients
def getAllergenFreeIngredients():
    global food_list, all_ingredients, allergens_apperiance, ingredients_apperiance
    for allergen, apperiance in allergens_apperiance.items():
        food_counter = 0
        possible_ing = []
        for food in apperiance:
            possible_ing += food_list[food]
            food_counter += 1
        for ingredient in possible_ing:
            if possible_ing.count(ingredient) == food_counter:
                if allergen not in all_ingredients[ingredient]:
                    all_ingredients[ingredient].append(allergen)
                if ingredient not in all_allergens[allergen]:
                    all_allergens[allergen].append(ingredient)
    allergen_free_counter = 0
    to_pop = []
    for ingredient, possible_allergens in all_ingredients.items():
        if not possible_allergens:
            allergen_free_counter += len(ingredients_apperiance[ingredient])
            to_pop.append(ingredient)
    for ingredient in to_pop:
        all_ingredients.pop(ingredient)
    return allergen_free_counter


# match all allergens to the right ingredient
def matchAllergensToIngredients():
    global all_allergens
    matched_ingredients = {}
    while True:
        for allergen, possible_ingredients in all_allergens.items():
            if len(possible_ingredients) == 1:
                matched_ingredients[possible_ingredients[0]] = allergen
            else:
                for ingredient in matched_ingredients:
                    if ingredient in possible_ingredients:
                        possible_ingredients.remove(ingredient)
        if len(all_allergens) == len(matched_ingredients):
            return


# canonical dangerous ingredient list
def getCDIL():
    global all_allergens
    all_allergens_sorted = sorted(list(all_allergens.keys()))
    cdil_list = [all_allergens[allergen] for allergen in all_allergens_sorted]
    cdil = cdil_list[0]
    for ingredient in cdil_list[1:]:
        cdil += "," + ingredient
    return cdil


# Part 1
formatData(rawdata)
print("Part 1:", getAllergenFreeIngredients())
# Part 2
print(all_allergens)
matchAllergensToIngredients()
print("Part 2:", getCDIL())
