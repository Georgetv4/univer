import pandas as pd


class Market:

    def __init__(self, name, balance, products, cart):
        self.name = name
        self.balance = balance
        self.products = products
        self.cart = cart

    def add_product(self, product_num, cart, balance):  # Function for adding products to cart
        product_frame = pd.DataFrame(products.iloc[[product_num]])
        updated_cart = pd.concat([cart, product_frame], ignore_index=True)
        balance -= float(products.iloc[[product_num], 1])
        print("Your cart:", '\n', updated_cart)
        print("Your balance:", balance)
        if balance < 0:
            print("Attention! Your balance is negative!")
        return updated_cart, balance

    def delete_product(self, product_num, cart, balance):   # Function for deleting products from cart
        updated_cart = cart.drop(index=product_num)
        balance += float(cart.iloc[[product_num], 1])
        print("Your cart:", '\n', updated_cart)
        print("Your balance:", balance)
        return updated_cart, balance


# Executable code
if __name__ == '__main__':
    print("Input your name and balance")
    name = str(input("Name:"))
    balance = float(input("Balance:"))
    products = pd.read_csv('products.csv')
    cart = pd.DataFrame({
        "product_name": [],
        "price": []
    })
    market = Market(name, balance, products, cart)
    print("This is our product range:", '\n', products)
    print("You can use commands like: Add, Delete, Exit")

    while True:
        user_input = input("You:")
        if user_input.lower() == 'exit' and balance > 0:
            break
        elif user_input.lower() == 'exit' and balance < 0:
            print("You can't end session because your balance is negative.", '\n', "Delete some products from your cart!")
            print("Your balance:", balance)
        elif user_input.lower() == "add":
            product_num = int(input("Input number of product:"))
            cart, balance = market.add_product(product_num, cart, balance)
        elif user_input.lower() == "delete":
            product_num = int(input("Input number of product:"))
            cart, balance = market.delete_product(product_num, cart, balance)
        else:
            print("Invalid input! Try again!")
