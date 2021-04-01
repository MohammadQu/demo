# Mohammad Qureshi
#PSID: 1789301
#10.19


class ItemToPurchase:
    def init(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = 'none'
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@ $', self.item_price, '=',
              (self.item_price * self.item_quantity))
    def print_item_description(self):
        print(self.item_name, ':', self.item_description, '.')


class ShoppingCart:
    def init(self):
        self.customer_name = 'none'
        self.current_date = 'January 1, 2016'
        self.cart_items = []

    def add_items(self):

    def remove_items(self):

    def modify_itens(self):

    def get_num_items_in_cart(self):

    def get_cost_of_cart(self):

    def print_total(self):

    def print_descriptions(self):



FirstItem = ItemToPurchase()
SecItem = ItemToPurchase()

FirstItem.item_name = str(input())
FirstItem.item_price = int(input())
FirstItem.item_quantity = int(input())

SecItem.item_name = str(input())
SecItem.item_price = int(input())
SecItem.item_quantity = int(input())

Total = (FirstItem.item_price * FirstItem.item_quantity) + (SecItem.item_price * SecItem.item_quantity)

print('TOTAL COST')
FirstItem.print_item_cost()
SecItem.print_item_cost()

print('Total: $', Total)

print('')
print('MENU')
print('a - Add item to cart')
print('r - Remove item from cart')
print('c - Change item quantity')
print("i - Output items' descriptions")
print('o - Output shopping cart')
print("q - Quit")
print('')
print('Choose an option:')
