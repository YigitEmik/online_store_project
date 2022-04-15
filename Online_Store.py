# Item Categories
fruits = [
    ["Banana", 2.99, "1"],
    ["Blueberry", 3.99, "2"],
    ["Apple", 3.99, "3"],
    ["Grape", 5.99, "4"],
    ["Orange", 6.99, "5"],
    ["Strawberry", 2.99, "6"],
    ["Pineapple", 10.99, "7"]
]
personal_care = [
    ["Shampoo", 4.68, "1"],
    ["Conditioner", 6.77, "2"],
    ["Soap", 5.30, "3"],
    ["Deodorant", 6.99, "4"],
    ["Toothpaste", 3.80, "5"],
    ["Dental Floss", 5.70, "6"]

]
beverages = [
    ["Water", 1, "1"],
    ["Coffee", 3, "2"],
    ["Milk", 6, "3"],
    ["Juice", 4, "4"],
    ["Soda", 2, "5"],
    ["Tea", 1.5, "6"]
]
paper_wrap = [
    ["Toilet Paper", 99, "1"],
    ["Paper Towels", 7, "2"],
    ["Tissues", 6, "3"],
    ["Aluminum Foil", 5, "4"]
]

# Variables
cart = []
total = 0
discount = 0
counter = 0

# Monthly Promotion Combos
combos = [
    ["Shampoo", "Soap", 10],
    ["Toilet Paper", "Tissues", 15],
    ["Milk", "Juice", 5],
    ["Banana", "Blueberry", 6]
]

file = open("/Users/Yigit Emik/Desktop/receipt.txt", "+a")


def menu():
    # Menu function
    global total
    print("-" * 9, "Welcome!", "-" * 9)
    print("-" * 10, "MENU", "-" * 11)
    print("| 1- Add Item to your cart | ")
    print("| 2- Show Total Purchase   |")
    print("| 3- Checkout              |")
    print("| 4- Promotions            |")
    print("| 5- Exit                  |")
    print("-" * 27)
    while True:
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Not an integer, Please try again")
            continue
        else:
            break
    if option == 1:
        add_item()
    elif option == 2:
        show_total_purchase()
        ask()
    elif option == 3:
        checkout()
        ask()
    elif option == 4:
        promotion()
    elif option == 5:
        print("Thank you for using our app!")
        exit()
    else:
        print("Selection not in options. Please try again.")
        menu()


def promotion():
    # A function that prints promotions to user to check what are the combos
    print("Here are the promotions of the month:")
    print("Item 1 | Item 2 | Discount for combo")
    for i in combos:
        print(str(i[0]) + " | " + str(i[1]) + " | " + str(i[2]) + "$")
    answer = input("Would you like to go to menu? (Y/N) ")
    if answer.lower() == "y":
        menu()
    else:
        exit()


def show_total_purchase():
    # Show Items in the cart
    print("Name | Price")
    for i in cart:
        for k in i:
            print(k[0], "-", k[1], "$")
    print("Total: ", calculate(), "$")


def buy_item(lst, lst1):
    # This function is to buy an item in any category,
    # First parameter has to be temp_cart list and second one is depends on the category of the item.

    # Display Items in the selected category.
    print("Name - Price - ID")
    for i in lst1:
        print(i)
    print("Which Item would you like to buy?")
    selection = input("Enter Item ID: ")
    while True:
        if selection.isnumeric() == True:
            for index in lst1:
                # Check if selection is valid
                if index[2] == selection:
                    lst.append(index)
            # If it was successfully completed, print user the added item
            print(str(lst) + " " + "Successfully added.")
            # Append temp list to main cart
            cart.append(lst)
            while True:
                selection2 = input("Would you like to buy another item? (Y/N) ")
                if selection2.lower() == "y":
                    add_item()
                elif selection2.lower() == "n":
                    ask()
                else:
                    print("Wrong Input")
                    continue
        else:
            print("Item ID must be a number")
            continue



def add_item():
    # Add item function.
    # Created temp list to add selected items in the temporary file, then we add temp list to the customer's cart.
    temp_cart = []
    print("Please Choose a Category")
    print("1) Fruits")
    print("2) Personal Care")
    print("3) Beverages")
    print("4) Paper Wrap")
    while True:
        try:
            option1 = int(input("Select: "))
        except ValueError:
            print("Not an integer, Please try again")
            continue
        else:
            break
    if option1 == 1:
        buy_item(temp_cart, fruits)
    elif option1 == 2:
        buy_item(temp_cart, personal_care)
    elif option1 == 3:
        buy_item(temp_cart, beverages)
    elif option1 == 4:
        buy_item(temp_cart, paper_wrap)
    else:
        print("Choice not in categories")
        while True:
            a = input("Would you like to go to menu? (Y/N) ")
            if a.lower() == "y":
                menu()
            elif a == "n":
                a = input("Would you like to try again ? (Y/N) ")
                if a.lower() == "y":
                    add_item()
                elif a.lower() == "n":
                    exit()
            else:
                print("Wrong input please try again.")
                continue
        cart.append(temp_cart)


def calculate():
    # Add item's price's to the total variable.
    global total
    global discount
    discount = 0
    total = 0
    for i in cart:
        for k in i:
            total += k[1]
    return float(total)


def calculate_combo():
    # If there is a monthly promotion combo in customer's cart, calculate the discount for that combo and apply it.
    temporary = []
    global discount
    global total
    for c in cart:
        for k in c:
            temporary.append(k[0])
    for i in combos:
        if i[0] and i[1] in temporary:
            total -= i[2]
            discount += i[2]
    return float(total)


def checkout():
    # Printing confirmed check-out and receipt info
    print("Thanks for shopping from us!")
    print("Here is your receipt:")
    print("Name | Price")
    for i in cart:
        for k in i:
            print(k[0], "-", k[1], "$")
    calculate()
    print("Total: ", calculate_combo(), "$")
    print("A total of ", discount, "$ discount has been applied")
    file.write(checkout_file())


def checkout_file():
    # Creating a string to print everything in our file.
    string = ""
    if counter == 0:
        string += "Thanks for shopping from us!\nHere is your receipt:\nName | Price\n"
        for i in cart:
            for k in i:
                string += str(k[0] + "-" + str(k[1]) + "$\n")
        calculate()
        string += ("Total: " + str(calculate_combo()) + "$\n""A total of " + str(discount) +
                   "$ discount has been applied")
        print("Your receipt is successfully printed!")
        return string
    else:
        string += "\nThanks for shopping from us!\nHere is your receipt:\nName | Price\n"
        for i in cart:
            for k in i:
                string += str(k[0] + "-" + str(k[1]) + "$\n")
        calculate()
        string += ("Total: " + str(calculate_combo()) + "$\n""A total of " + str(
            discount) + "$ discount has been applied")
        print("Your receipt is successfully printed!")
        return string



def ask():
    # Ask if the user wants to go to menu.
    while True:
        answer = input("Would you like to go to menu? (Y/N) ")
        if answer.lower() == "y":
            menu()
        elif answer.lower() == "n":
            exit()
        else:
            print("Wrong input, please try again.")
            continue


menu()
