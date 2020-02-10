def main():
    with open("test_input.txt", "r+") as file:
        content = file.readlines()

        recipe_dict = {}

        for line in content:
            recipe = line.split('=>')
            ingredients = recipe[0].strip()
            amount, material = get_specs(recipe[1].strip())
            recipe_dict[material] = (amount, ingredients)

        need_dict = {}
        have_dict = {}

        add_needed('FUEL', need_dict, have_dict, recipe_dict)

        print(need_dict)
        print(have_dict)


def add_needed(chemical, need_dict, have_dict, recipe_dict):
    have_amount = int(recipe_dict[chemical][0])

    # keep track of what materials we have made
    if chemical in have_dict:
        have_dict[chemical] += have_amount
    else:
        have_dict[chemical] = have_amount

    # keep track of materials needed
    for ingredient in recipe_dict[chemical][1].split(','):
        need_amount, need_chemical = get_specs(ingredient.strip())


        # add the materials needed. 
        if need_chemical in need_dict:

            if need_dict[need_chemical] + int(need_amount) > have_dict[need_chemical]:
                need_dict[need_chemical] += int(need_amount)

            if need_chemical == 'ORE':
                continue
            add_needed(need_chemical, need_dict, have_dict, recipe_dict)
            
        else:
            need_dict[need_chemical] = int(need_amount)

            if need_chemical == 'ORE':
                continue
            add_needed(need_chemical, need_dict, have_dict, recipe_dict)


def get_specs(spec):
    return spec.split(' ')[0], spec.split(' ')[1]


if __name__ == "__main__":
    main()
