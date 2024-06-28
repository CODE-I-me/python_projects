menu = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80,
}

print("wellcome to my mini cafe")
print("pizza: 40\npasta: 50\nburger: 60\nsalad: 70\ncoffee: 80")

order_total = 0
item_1 = input("eneter the name of item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1] #add value of order
    print(f"your item {item_1} has been aded to your order")
else:
    print("enetered order is invalid")    

another_order = input("you want to order something else:(yes/no)")
if another_order == "yes":
    item_2 = input("enter an anoter order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} has been added to your order")
    else:
        print("enetered order is invalid")
elif another_order == "no":
    print(f"your total order is Rs: {order_total}")
else:
    print("invalid input")