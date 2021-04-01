# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool wiws, actions, and settings.

# Mohammad Qureshi
# PSID: 1789301
# 11.18


user_input = input().split()

list = []


for num in user_input:
    num = int(num)
    if num >= 0:
        list.append(num)

list.sort()
for num in list:
    print(num, end=' ')



