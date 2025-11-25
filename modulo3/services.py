
def pp_menu():
    print("""
1. Add product
2. Show inventory
3. Stats
4. Search Product
5. Update product
6. Delete product
7. Save CSV
8. Load CSV
9. Exit
""")

def add_product(inventory):
    validation_name = True
    validation_price = True
    validation_quanty = True
    add_product = True
    while add_product:
        while validation_name:
        #request name of product
            product_name = input("Insert the name of the product: ").lower()
        #Is allow the use of numbers and letters for productos like H20
            if product_name.isalnum():
                validation_name = False
        #return to the cycle until the name get correct.
            else:
                print("Don't use Special Characters or Spaces, Try Again. (just integer numbers allowed).")
            while validation_price:
            #request the price of the product
                product_price = input("Insert the price of the product: ")
                if not product_price.isdigit():
                    print("Just integers numbers allowed, Try again.")
                    continue
                else:
                    validation_price = True
                product_price = int(product_price)
                if product_price < 0:
                    print("Just integer number allowed.")
                else:
                    validation_price = False
            while validation_quanty:
                #Request quantity of product
                product_quanty = input("Insert the quanty of your product: ")
                if not product_quanty.isdigit():
                    print("Just numbers allowed, Try again.")
                    continue
                else:
                    validation_quanty = True
                product_quanty = int(product_quanty)
                if product_quanty <= 0:
                    print("Insert a valid number.")
                else:
                    validation_quanty = False
    #reserv total cost of the product here
            total_cost = product_price * product_quanty
            inventory.append({
                "name": product_name,
                "price": product_price,
                "quanty": product_quanty
            })
            print("\n--Product Added on inventory successfully--")
            print("" + "="*15)
            print("Product Info Added")
            print("="*15)
            print(f"Name: {product_name} | Price: {product_price} | Quanty: {product_quanty} | Total cost: ${total_cost}")
            add_product = False
        return

def show_inventory(inventory):
    print("----Inventory----")
    if len(inventory) == 0:
        print("Inventory Empty")
        return
    for i in inventory:
        print(f"""
product: {i['name']}
price: ${i['price']}
quanty: {i['quanty']}
----------------------------------------""")
    return

def calculate_stats(inventory):
    total_value = 0
    total_quanty = 0
    for i in inventory:
        total_value += i['price'] * i['quanty']
        total_quanty += i['quanty']
    return total_value, total_quanty
def show_stats(inventory):
    if len(inventory) == 0:
        print("Inventory is empty. No stats.")
        return
    total_value, total_quanty = calculate_stats()
    print(f"""
    total value: ${total_value}
    total quantity: {total_quanty}
    """)
    return



