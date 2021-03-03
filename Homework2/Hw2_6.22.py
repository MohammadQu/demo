# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


first_x = int(input())
first_y = int(input())

first_ans = int(input())

sec_x = int(input())
sec_y = int(input())
sec_ans = int(input())

first_sol = 0
sec_sol = 0
NoSol = False
for i in range(-10, 10):
    for y in range(-10, 10):
        if((first_x * i) + (first_y * y) - first_ans == 0):
            if((sec_x * i) + (sec_y * y) - sec_ans == 0):
                first_sol = i
                sec_sol = y
                print(first_sol, sec_sol)
                NoSol = True
    if NoSol:
        break
else:
    print('No solution')
