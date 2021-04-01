# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Mohammad Qureshi
# 1789301
# 10.17

class ItemToPurchase:
    def init(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@ ${}'.format(self.item_price), '= ${}'.format(self.item_price * self.item_quantity))

FirstItem = ItemToPurchase()
SecItem = ItemToPurchase()
print('Item 1')
FirstItem.item_name = str(input('Enter the item name:\n'))
FirstItem.item_price = int(input('Enter the item price:\n'))
FirstItem.item_quantity = int(input('Enter the item quantity:\n'))
print('')
print('Item 2')
SecItem.item_name = str(input('Enter the item name:\n'))
SecItem.item_price = int(input('Enter the item price:\n'))
SecItem.item_quantity = int(input('Enter the item quantity:\n'))

print('')
Total = (FirstItem.item_price * FirstItem.item_quantity) + (SecItem.item_price * SecItem.item_quantity)

print('TOTAL COST')
FirstItem.print_item_cost()
SecItem.print_item_cost()
print('')
print('Total: ${}'.format(Total))
