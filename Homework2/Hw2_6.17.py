# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


password = input()
new_pass = ""
i=0
while (i < len(password)):
    letter = password[i]
    if(letter == "i"):
        new_pass = new_pass + '!'
    elif(letter == 'a'):
        new_pass = new_pass + '@'
    elif (letter == 'm'):
        new_pass = new_pass + 'M'
    elif (letter == 'B'):
        new_pass = new_pass + '8'
    elif (letter == 'o'):
        new_pass = new_pass + '.'
    else:
        new_pass = new_pass + letter
    i = i + 1

new_pass = new_pass + "q*s"
print(new_pass)

