def greet():
    print("Hello")
    print("How are you?")
    print("Welcome")


greet()

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Maruthi")
greet_with_name("Kumar")


def life_in_weeks(age):
    total_weeks = 90 * 52
    print(f"You have {total_weeks - age * 52} weeks left")
life_in_weeks(56)



def greet_with_name_and_location(name, location):
    print(f"Hello {name} and {location}")

greet_with_name_and_location("Kumar", "USA")
greet_with_name_and_location(location = "HYD", name ="Kumar")


def calculate_love_score(name1, name2):
    name1 = name1.upper()
    name2 = name2.upper()

    true_occurs = ['T', 'R', 'U', 'E']
    love_occurs = ['L', 'O', 'V', 'E']

    true_count = 0
    love_count = 0

    name1_list = list(name1)
    name2_list = list(name2)

    for item in name1_list:
        if item in true_occurs:
            true_count += 1
    for item in name2_list:
        if item in true_occurs:
            true_count += 1

    for item in name1_list:
        if item in love_occurs:
            love_count += 1
    for item in name2_list:
        if item in love_occurs:
            love_count += 1

    print(F"{true_count}{love_count}")

calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")


def calculate_love_score_sol(name1, name2):
    combined_names = name1 + name2
    lower_name = combined_names.lower()
    print(f"{lower_name}")

    t = lower_name.count("t")
    r = lower_name.count("r")
    u = lower_name.count("u")
    e = lower_name.count("e")

    first_digit = t + r + u + e

    l = lower_name.count("l")
    o = lower_name.count("o")
    v = lower_name.count("v")
    e = lower_name.count("e")

    second_digit = l + o + v + e

    print(f"{first_digit}{second_digit}")

calculate_love_score_sol("Kanye West", "Kim Kardashian")