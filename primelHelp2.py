import random, os
from turtle import position
from prime_nums import prime_nums


def convert(string):
    li = list(string.split(" "))
    return li


def check_pres(sub, test_str):
    for ele in sub:
        if ele in test_str:
            return 0
    return 1


def removeNum(digit):
    print(f"Removing all the numbers with {digit}...")
    return [ele for ele in prime_number_list if check_pres(ele, digit)]


def forSureNumsPosition(digit, position):
    print(f"Looking for all the numbers with {digit} at position {position+1}...")
    return [ele for ele in prime_number_list if digit == ele[position] in ele]


def removeNumsPosition(digit, position):
    print(f"Removing all the numbers with {digit} at position {position+1}...")
    li = [ele for ele in prime_number_list if digit != ele[position] in ele]
    return [ele for ele in li if digit in ele]


prime_number_list = convert(prime_nums)

# welcome msg and first input
print(
    """╭―――――――――――――――――――――――╮
│       WELCOME!        │
╰―――――――――――――――――――――――╯"""
)
print("I'll help you with guessing todays number for Primel.")

# 69677 --> let say that the number doesn't have any 7 and has a 9 in correct place you would write it like this -9-xx


choice = input(
    "------MENU------\n1 --> Random number\n2 --> Choose what digits are in and which are not\n3 --> Print out the list or length of list of remaning numbers\nq --> Quit\n"
).lower()
skip = []
while choice != "q":

    if choice == "1":
        num = random.choice(prime_number_list)
        print("\nTry with: ", num)
        # TODO ask if the number is used if yes remove it from the list if not leave it give a msg that it wil be removed if used

    elif choice == "2":
        used_number = 0
        used_number_choice = input(
            "Did you use the random choice number? y/n: "
        ).lower()
        if used_number_choice == "y":
            used_number = num
        elif used_number_choice == "n":
            while used_number not in prime_number_list:
                used_number = input("What number did you use? \n").lower()

        for ind in range(5):
            if ind not in skip:
                is_used = input(
                    f"\nIs {used_number[ind]} in today's number? y/n: "
                ).lower()

                while is_used != "y" and is_used != "n":
                    is_used = input(
                        f"\nIs {used_number[ind]} in today's number? y/n: "
                    ).lower()

                if is_used == "n":
                    prime_number_list = removeNum(used_number[ind])
                elif is_used == "y":
                    is_correct_position = input(
                        "Is it at correct position? y/n "
                    ).lower()
                    if is_correct_position == "y":
                        prime_number_list = forSureNumsPosition(used_number[ind], ind)
                        skip.append(ind)
                    elif is_correct_position == "n":
                        prime_number_list = removeNumsPosition(used_number[ind], ind)
            else:
                print(f"\n{used_number[ind]} is in today's number at position {ind+1}")

        if len(prime_number_list) == 1:
            print("\nToday number is:")
            print("╭――――――――――╮")
            print(f"│{str(prime_number_list[0])} │")
            print("╰――――――――――╯")

    elif choice == "3":
        dec = input("1 --> Whole list\n2 --> Length of list\n")
        if dec == "1":
            print(prime_number_list)
        elif dec == "2":
            print(len(prime_number_list))
        else:
            print("Error, wrong input")

    else:
        print("Error, wrong input")

    choice = input(
        "\n------MENU------\n1 --> Random number\n2 --> choose what digits are in and which are not\n3 --> Print out the list or length of list of remaning numbers\nq --> Quit\n".lower()
    )


print(
    """╭―――――――――――――――――――――――╮
│Goodbye! Hope I helped.│
╰―――――――――――――――――――――――╯"""
)
