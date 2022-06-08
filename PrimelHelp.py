import random
from prime_nums import prime_nums

exclude_list = []


def convert(string):
    li = list(string.split(" "))
    return li


def check_pres(sub, test_str):
    for ele in sub:
        if ele in test_str:
            return 0
    return 1


# function that is looking for all the numbers that have a given digit in them and removing them from the list
def removeNum(li, digit):
    print("removing numbers...")
    return [ele for ele in li if check_pres(ele, digit)]


# function that is looking for all the numbers that have a given digit in them and is adding them to a list
def forSureNums(li, digit):
    print("Looking for all the numbers with that digit...")
    return [ele for ele in li if digit in ele]


def forSureNumsPosition(li):
    digit = input("What digit is definitely in the number?\n")
    position = int(
        input(
            "And at what position? (eg. I guessed 21193 and I know that number 3 is definitely at last place, the input would be 5.)\n"
        )
    )
    return [ele for ele in li if digit == ele[position - 1] in ele]


prime_number_list = convert(prime_nums)

# welcome msg and first input
print(
    """╭―――――――――――――――――――――――╮
│       WELCOME!        │
╰―――――――――――――――――――――――╯"""
)
print("I'll help you with guessing todays number for Primel.")
choice = input(
    "------MENU------\n1 --> Random number\n2 --> Remove all numbers with given digit\n3 --> The given digit is definitely in the number\n4 --> Print out the list or length of list of remaning numbers\nq --> Quit\n"
).lower()


while choice != "q":
    if choice == "1":
        print("\nTry with: ", random.choice(prime_number_list))
        # TODO ask if the number is used if yes remove it from the list if not leave it give a msg that it wil be removed if used

    elif choice == "2":
        num = input("What digit do you want to remove?\n")
        prime_number_list = removeNum(prime_number_list, num)
        # print(prime_number_list)

    elif choice == "3":
        decision = input(
            "Do you know at what position the digit is definitely on? y or n\n"
        )
        if decision == "y":
            prime_number_list = forSureNumsPosition(prime_number_list)

        elif decision == "n":
            num = input(
                "What digit is definitely in the number but you don't know the position?\n"
            )
            prime_number_list = forSureNums(prime_number_list, num)
            # print(prime_number_list)
        else:
            print("Error, wrong input")

    elif choice == "4":
        dec = input("1 --> Whole list\n2 --> Length of list")
        if dec == "1":
            print(prime_number_list)
        elif dec == "2":
            print(len(prime_number_list))
        else:
            print("Error, wrong input")

    else:
        print("Error, wrong input")
    choice = input(
        "\n------MENU------\n1 --> Random number\n2 --> Remove all numbers with given digit\n3 --> The given digit is definitely in the number\n4 --> Print out the list or length of list of remaning numbers\nq --> Quit\n".lower()
    )

print(
    """╭―――――――――――――――――――――――╮
│Goodbye! Hope I helped.│
╰―――――――――――――――――――――――╯"""
)
