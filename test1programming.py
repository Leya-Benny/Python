shoppingCart = {}
#menu
def display_menu():
    print("\nWELCOME TO THE AMANDO SHOPPING SITE")
    print("1. Add a product to the cart.")
    print("2. Search for a product.")
    print("3. Delete a product from the cart.")
    print("4. Display the contents of the cart.")
    print("5. Purchase items.")
    print("6. Quit.")
#add
def add_product():
    if len(shoppingCart) >= 5:
        print("Cart is full.")
    else:
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))
        brand = input("Enter product brand: ")
        shoppingCart[product_name] = {"product-price": product_price, "brand": brand}
        print(f"{product_name} has been added to the cart.")
#search
def search_product():
    product_name = input("Enter product name to search: ")
    if product_name in shoppingCart:
        product = shoppingCart[product_name]
        print(f"Product: {product_name}\nPrice: {product['product-price']}\nBrand: {product['brand']}")
    else:
        print("No product exists with this name.")
#delete
def delete_product():
    if not shoppingCart:
        print("Cart is empty, no item is found.")
    else:
        product_name = input("Enter product name to delete: ")
        if product_name in shoppingCart:
            del shoppingCart[product_name]
            print(f"{product_name} has been removed from the cart.")
        else:
            print("Product not found in cart.")
#view
def display_cart():
    if not shoppingCart:
        print("Cart is empty.")
    else:
        for product_name, details in shoppingCart.items():
            print(f"Product: {product_name}, Price: {details['product-price']}, Brand: {details['brand']}")
#purchase
def purchase_items():
    if not shoppingCart:
        print("Cart is empty, please select an item before completing purchase.")
    else:
        total_price = sum(item['product-price'] for item in shoppingCart.values())
        print(f"Total: ${total_price:.2f}")
        choice = input("Complete purchase (Y/N)? ").strip().lower()
        if choice == "y":
            print("Thank you for your business.")
            shoppingCart.clear()
        elif choice == "n":
            print("Please continue shopping.")
        else:
            print("Please answer either Y or N.")
#main 
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            search_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            display_cart()
        elif choice == '5':
            purchase_items()
        elif choice == '6':
            print("Thank you for visiting the Amando Shopping Site.")
            break
        else:
            print("Invalid choice, please enter a valid option.")

if __name__ == "__main__":
    main()
