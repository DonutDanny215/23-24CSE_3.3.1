order = []

pizza = input("What choice of Pizza Topping would you like?: Cheese ($7.99), Pepperoni ($8.99), Supreme ($9.99)")
drink = input("Would you like a drink?")
drink_size = "No"
wings = input("Do you want wings as well?")
wings_size = "None"

total_cost = 0

if pizza == "Cheese":
    order.append("Cheese_Pizza")
elif pizza == "Pepperoni":
    order.append("Pepperoni_Pizza")
elif pizza == "Supreme":
    order.append("Supreme_Pizza")

if drink == "Yes":
    drink_size = input("What size of your bottled beverage would you like: Small ($2.99), Medium ($3.99), Large ($4.99)")

if drink_size == "Small":
    order.append("Small_Bottle")
elif drink_size == "Medium":
    order.append("Medium_Bottle")
elif drink_size == "Large":
    order.append("Large_Bottle")
else:
    drink = "No Beverage"

if wings == "Yes":
    wings_size = input("What size of wings would you like: Small ($9.99), Medium ($19.99), Large ($29.99): ")
    if wings_size == "Small":
        super_size = input("Would you like to super-size the amount of wings?: ")
        if super_size == "Yes":
            wings_size = "Large"
            order.append("Large_Wings")
    elif wings_size == "Medium":
        order.append("Medium_Wings")
    elif wings_size == "Large":
        order.append("Large_Wings")
    else:
        order.append("Small_Wings")

if "Cheese Pizza" in order:
    total_cost += 7.99

if "Supreme Pizza" in order:
    total_cost += 9.99

if "Pepperoni_Pizza" in order:
    total_cost += 8.99

if "Small Drink" in order:
    total_cost += 2.99

if "Medium Drink" in order:
    total_cost += 3.99

if "Large Drink" in order:
    total_cost += 4.99

if "Small Wings" in order:
    total_cost += 9.99

if "Medium Wings" in order:
    total_cost += 19.99

if "Large Wings" in order:
    total_cost += 29.99

bleucheese = float(input("How many cups of Bleu Cheese do you want? ($1.00 per packet): "))
order.append(str(bleucheese))

bleucheese_price = bleucheese * 1.00
total_cost += bleucheese_price

if drink == "Yes":
    if wings == "Yes":
        total_cost = total_cost - 1.00

print(str(order) + "Cups of Bleu Cheese")
print("Your order will cost $" + str(total_cost))