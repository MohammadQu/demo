# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
print('Enter wall height (feet):')
Height = int(input())
print('Enter wall width (feet):')
Width = int(input())
Area = Height * Width
print('Wall area:', Area, 'square feet')

Paint = ('{:.2f}'.format(Area / 350))
print('Paint needed:', Paint, 'gallons')

Cans = float(Paint)
print('Cans needed:', math.ceil(Cans), 'can(s)')
print()
thisdict = {
  "red": "$35",
  "blue": "$25",
  "green": "$23"
}
print('Choose a color to paint the wall:')
Color = str(input())
print('Cost of purchasing', Color, 'paint:', thisdict[Color])