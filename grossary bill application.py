# Grocery={
#
#     product_id :1  product_name:Maggie stock:200 price:23
#     product_id:2  product_name:Biscuits stock:1000 price:50
#
# }
# menu -
#      1. Add new Product
#      2. show all product
#      3. Update specific product
#      4. Delete product
#      5. purchase product
#
# 5. which product u want -- product_id  -- 2
# how many qty u want - 20
# price - 200
# pay - 200
# message -- Thanks for Visit our shop. Kindly collect your product
#     do u want to continue -- Y  then again display Menu otherwise
# exit from program
grocery = {
    '1': {'name': 'Maggie', 'stock': 200, 'price': 10},
    '2': {'name': 'Biscuit', 'stock': 300, 'price': 10},
    '3': {'name': 'Soap', 'stock': 400, 'price': 40},
    '4': {'name': 'Toothpaste', 'stock': 100, 'price': 30},
    '5': {'name': 'Hand wash', 'stock': 300, 'price': 90}
}
while True:
    menu = {
        1: 'Add new Product',
        2: 'Show all products',
        3: 'Update specific product',
        4: 'Delete product',
        5: 'Purchase product'
    }

    for k, v in menu.items():
        print(f"{k}: {v}")

    a = int(input("Enter your choice: "))

    if a == 1:
        for key, val in grocery.items():
            print(f"{key}\t{val['name']}\t{val['stock']}\t{val['price']}")
            print("-----------------------------------")

        key = input("Enter product id to add: ")

        if key not in grocery:
            name = input("Enter new product name: ")
            stock = int(input("Enter new product stock: "))
            price = float(input("Enter new product price: "))

            new_product = {
                'name': name,
                'stock': stock,
                'price': price
            }

            grocery[key] = new_product
            print("Product added successfully.")

        for key, val in grocery.items():
            print(f"{key}\t{val['name']}\t{val['stock']}\t{val['price']}")
            print("----------------------------------------")

    elif a == 2:
        print("product id   product  stock  price")
        print("--------------------------------------")
        for key, val in grocery.items():
            print(f"\t{key}\t  {val['name']}\t  {val['stock']}\t{val['price']}\t")
            print("--------------------------------------")

    elif a == 3:
        for key, val in grocery.items():
            print(f"{key}\t{val['name']}\t{val['stock']}\t{val['price']}\t")
            print("----------------------------------------------------------------------")

        key = input("Enter product id to update: ")
        if key in grocery:
            name = input("Enter new product name: ")
            stock = int(input("Enter new product stock: "))
            price = int(input("Enter new product price: "))
            grocery[key]['name'] = name
            grocery[key]['stock'] = stock
            grocery[key]['price'] = price
            print("Product updated successfully.")
            for key, val in grocery.items():
                print(f"{key}\t{val['name']}\t{val['stock']}\t{val['price']}\t")
                print("----------------------------------------------------------------------")
        else:
            print("Product not found.")

    elif a == 4:

        for key, val in grocery.items():
            print(f"{key}\t{val['name']}\t{val['stock']}\t{val['price']}\t")
            print("----------------------------------------------------------------------")

        key = input("Which product do you want to delete? Enter the key: ")

        if key in grocery:
            grocery.pop(key)
        else:
            print("Invalid key. Product not found.")

        for key, val in grocery.items():
            print(f"{key}\t{val['name']}\t{val['stock']}\t{val['price']}\t")
            print("----------------------------------------------------------------------")

    elif a == 5:
        for key, val in grocery.items():
            print(f"{key}\t{val['name']}\t{val['stock']}\t{val['price']}\t")
            print("----------------------------------------------------------------------")

        key = input("Which product do you want to buy? ")
        if key in grocery:
            product = grocery[key]
            n = int(input(f"How many packets of {product['name']} do you want to buy? "))
            amount = product['price'] * n
            print(f"Total amount: {amount}")

            pay_amount = int(input("Pay Amount: "))
            if pay_amount == amount:
                print("Your payment is successful!!!")
                print("Thanks for visiting our shop.")
                print("Kindly collect your product.")

            elif pay_amount < amount:
                amount1 = amount - pay_amount
                print(f"This amount is less than our amount. Please add amount: {amount1}")
                add_amount = int(input("Add amount: "))
                total_amount = add_amount + pay_amount

                if total_amount == amount:
                    print("Your payment is successful!!!")
                    print("Thanks for visiting our shop.")
                    print("Kindly collect your product.")
                elif total_amount > amount:
                    change = total_amount - amount
                    print(f"Your change is {change}\n")

                elif total_amount < amount:
                    print("payment is not sufficient")

            elif pay_amount > amount:
                change = pay_amount - amount
                print(f"Your change is {change}")
                print("Your payment is successful!!!")
                print("Thanks for visiting our shop.")
                print("Kindly collect your product.")

            grocery[key]['stock'] = grocery[key]['stock'] - n
            print("\nUpdated stock")
            for key, val in grocery.items():
                print(f"{key}\t{val['name']}\t{val['stock']}\t{val['price']}\t")
                print("----------------------------------------------------------------------")

        else:
            print("Invalid product key. Please try again.")

    else:
        print("Invalid choice.")
    n = input("Do you want to continue? (yes/no): ")
    if n == 'yes':
        continue
    elif n == 'no':
        print("Exit")
        break

