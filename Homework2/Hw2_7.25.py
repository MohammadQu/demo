# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def exact_change(user_total):
    total = user_total
    num_dollars = user_total // 100
    user_total = user_total % 100

    num_quarters = user_total // 25
    user_total = user_total % 25

    num_dimes = user_total // 10
    user_total = user_total % 10

    num_nickels = user_total // 5
    user_total = user_total % 5

    num_pennies = user_total//1
    user_total = user_total % 1


    if(total > 0):
        if(num_dollars > 1):
            print(num_dollars, "dollars")
        elif(num_dollars == 1):
            print(num_dollars, "dollar")

        if(num_quarters > 1):
            print(num_quarters, "quarters")
        elif(num_quarters == 1):
            print(num_quarters, "quarter")

        if(num_dimes > 1):
            print(num_dimes, "dimes")
        elif(num_dimes == 1):
            print(num_dimes, "dime")

        if(num_nickels > 1):
            print(num_nickels, "nickels")
        elif(num_dollars == 1):
            print(num_nickels, "nickel")

        if(num_pennies > 1):
            print(num_pennies, "pennies")
        elif(num_pennies == 1):
            print(num_pennies, "penny")

    else:
        print("no change")



print(exact_change(int(input())))