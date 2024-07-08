## CSC500 Module 8 - Project Portfolio
## Sonya Bourgeois
## 07/07/2024

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                cart_item.item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}\n")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print()  # Add a blank line before printing item descriptions  
            print("ITEM DESCRIPTIONS:")
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")

def print_menu(cart):
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    choice = input("Choose an option: ").lower()
    return choice

def main():
    customer_name = input("\nEnter customer's name: ")
    current_date = input("Enter today's date: ")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    shopping_cart = ShoppingCart(customer_name, current_date)

    while True:
        choice = print_menu(shopping_cart)
        if choice == 'q':
            break
        elif choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            shopping_cart.add_item(new_item)
        elif choice == 'r':
            item_name = input("Enter name of item to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            item_to_modify = ItemToPurchase(item_name, 0, new_quantity)
            shopping_cart.modify_item(item_to_modify)
        elif choice == 'i':
            print()  # Add a blank line before printing item descriptions        
            shopping_cart.print_descriptions()
        elif choice == 'o':
            print()  # Add a blank line before printing the shopping cart
            shopping_cart.print_total()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
