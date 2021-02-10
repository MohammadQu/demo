# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


print('Enter amount of lemon juice (in cups):')
Lemon = int(input())
print('Enter amount of water (in cups):')
Water = int(input())
print('Enter amount of agave nectar (in cups):')
Nectar = float(input())
print('How many servings does this make?')
Servings = int(input())
print()
print('Lemonade ingredients - yields', ('{:.2f}'.format(Servings)),'servings')
print(('{:.2f}'.format(Lemon)), 'cup(s) lemon juice')
print(('{:.2f}'.format(Water)), 'cup(s) water')
print(('{:.2f}'.format(Nectar)), 'cup(s) agave nectar')
print()

print('How many servings would you like to make?')
print()

ServingsWanted = int(input())
Difference = ServingsWanted / Servings

print('Lemonade ingredients - yields', ('{:.2f}'.format(ServingsWanted)),'servings')
print(('{:.2f}'.format(Lemon*Difference)), 'cup(s) lemon juice')
print(('{:.2f}'.format(Water*Difference)), 'cup(s) water')
print(('{:.2f}'.format(Nectar*Difference)), 'cup(s) agave nectar')
print()


LemonGallon = (Lemon*Difference)/16
WaterGallon = (Water*Difference)/16
NectarGallon = (Nectar*Difference)/16
print('Lemonade ingredients - yields', ('{:.2f}'.format(ServingsWanted)),'servings')
print(('{:.2f}'.format(LemonGallon)), 'gallon(s) lemon juice')
print(('{:.2f}'.format(WaterGallon)), 'gallon(s) water')
print(('{:.2f}'.format(NectarGallon)), 'gallon(s) agave nectar')