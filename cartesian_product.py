import itertools

def cartesian_product():
    print("CARTESIAN PRODUCT")
    print("-----------------")
    print()
    while True:
        num_of_sets = input("Number Of Sets: ")
        if num_of_sets.isdigit():
            break
    num_of_sets = int(num_of_sets)

    userSets = [[] for _ in range(num_of_sets)]


    for i in range(num_of_sets):
        setNames = input(f"Set {i+1}: ")
        # CONVERT USER ELEMENTS INTO AN ARRAY
        userElements = setNames.replace(',', '').split()
        # ADD THE USER SETS INTO A LIST OF ALL THE SETS
        userSets[i] = userElements


    combination_string = ""
    for i in range(num_of_sets):
        combination_string += f"combination[{i}], "
    combination_string = combination_string[:-2]

    # COMPUTE THE CARTESIAN PRODUCT
    cartesianProduct = [eval(combination_string) for combination in itertools.product(*userSets)]

    print()
    print(f"{cartesianProduct}")

    while True:
        print()
        back = input("Press (R) To Restart Program: ").lower()
        if back == "r":
            cartesian_product()





cartesian_product()

