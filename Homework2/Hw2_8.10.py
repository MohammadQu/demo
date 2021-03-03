# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


Words = input()
New = Words.replace(" ", "")

fail = True

start = 0
end = len(New) - 1

while(start < end):
    if(New[start] != New[end]):
        fail = False
        break
    else:
        start = start + 1
        end = end - 1

if(fail):
    print(Words, 'is a palindrome')
else:
    print(Words, 'is not a palindrome')