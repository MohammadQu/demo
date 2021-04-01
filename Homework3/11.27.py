# Mohammad Qureshi
# PSID: 1789301
# 11.27


NumList = []
RateList = []
#INPUT PLAYER JERSEY NUMBER AND PLAYER RATING/ ADD THEM TO A LIST
jNumber = input("Enter player 1's jersey number:").split()
pRating = input("Enter player 1's rating:").split()
for num in jNumber:
    num = int(num)
    NumList.append(num)
for num in pRating:
    num = int(num)
    RateList.append(num)

jNumber = input("Enter player 2's jersey number:").split()
pRating = input("Enter player 2's rating:").split()
for num in jNumber:
    num = int(num)
    NumList.append(num)
for num in pRating:
    num = int(num)
    RateList.append(num)

jNumber = input("Enter player 3's jersey number:").split()
pRating = input("Enter player 3's rating:").split()
for num in jNumber:
    num = int(num)
    NumList.append(num)
for num in pRating:
    num = int(num)
    RateList.append(num)


jNumber = input("Enter player 4's jersey number:").split()
pRating = input("Enter player 4's rating:").split()
for num in jNumber:
    num = int(num)
    NumList.append(num)
for num in pRating:
    num = int(num)
    RateList.append(num)


jNumber = input("Enter player 5's jersey number:").split()
pRating = input("Enter player 5's rating:").split()
for num in jNumber:
    num = int(num)
    NumList.append(num)
for num in pRating:
    num = int(num)
    RateList.append(num)

print('ROSTER')

NumList.sort()
x = 0
for num in NumList:
        print('Jersey number:', num, 'Rating:', RateList[x])
        x = x + 1

while True:
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print(' ')
    print('Choose an option:')

    option = str(input())
    counter = 5
    if(option == 'o'):
        print('ROSTER')
        NumList.sort()
        x = 0
        for num in NumList:
            print('Jersey number:', num, 'Rating:', RateList[x])
            x = x + 1
    elif(option == 'a'):
        newNum = int(input("Enter a new player's jersey number:"))
        newRate = int(input("Enter the player's rating:"))

        NumList.append(newNum)
        RateList.append(newRate)

    elif (option == 'd'):
        delNum = int(input("Enter a jersey number:"))
        NumList.remove(delNum)

    elif (option == 'r'):
        currNum = int(input("Enter a jersey  number:"))
        updateRate = int(input("Enter a new rating forplayer:"))

        RateList.instert(currNum, updateRate)

    elif (option == 'q'):
        break





