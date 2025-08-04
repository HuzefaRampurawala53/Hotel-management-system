menu = {
    'Pizza': 100,
    'Burger': 55,
    'Pasta': 80,
    'Salad': 30,
    'Soda': 20,
    'Coffee': 25,
    'Tea': 15,
}

print("👋 HELLO WELCOME TO OUR RESTAURANT 🍽️")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: {price} RS 🥘")

order_total = 0
item = input("Enter the dish name: ").capitalize().strip()

if item in menu:
    order_total += menu[item]
    print(f"✅ Your {item} has been added.")
else:
    print("❌ Sorry, that item is not on the menu.")
while True:
    another_item = input("Do you want to order another dish? (yes/no): ").strip().lower()
    if another_item == 'yes':
        item = input("Enter the dish name: ").capitalize().strip()
        if item in menu:
            order_total += menu[item]
            print(f"✅ Your {item} has been added.")
        else:
            print(f"❌ Ordered item '{item}' is not on the menu.")
    elif another_item == 'no':
        break
    else:
        print("🤔 Please answer with 'yes' or 'no'.")
another_order = input("Do you want to order another dish? (yes/no): ").strip().lower()
if another_order == 'yes':
    item2 = input("Enter the dish name: ").capitalize().strip()
    if item2 in menu:
        order_total += menu[item2]
        print(f"✅ Your {item2} has been added.")
    else:
        print(f"❌ Ordered item '{item2}' is not on the menu.")
else:
    print("🙏 Thank you for your order!")

print(f"🧾 Your total bill is: {order_total} RS")
print(f"💵 Please pay {order_total} RS at the counter.")
print("😊 Thank you ")