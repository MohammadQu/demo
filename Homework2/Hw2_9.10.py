# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import csv

NewFile = input()
frequency = {}
with open(NewFile, 'r') as myfile:
  csvfile = csv.reader(myfile)
  for row in csvfile:
    for test in row:
        if test not in frequency.keys():
            frequency[csvfile] = 1
        else:
            frequency[csvfile] += 1
for key in frequency.keys():
    print(key, frequency[csvfile])

