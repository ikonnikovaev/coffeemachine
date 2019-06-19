
#For the espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
#For the latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
#And for the cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.

water_per_cup = [250, 350, 200]
milk_per_cup = [0, 75, 100]
beans_per_cup = [16, 20, 12]
cost_per_cup = [4, 7, 6]

#At the moment, the coffee machine has $550, 
#1200 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.

available_water = 400
available_milk = 540
available_beans = 120
available_cups = 9
money = 550

def work():    
    action = ""
    while (action != "exit"):
        action = input("Write action (buy, fill, take, remaining, exit): ").strip()
        if (action == "buy"):
            buy()
        elif (action == "fill"):
            fill()
        elif (action == "take"):
            take()
        elif (action == "remaining"):
            print_remaining()
        

def buy():
    global available_water
    global available_milk
    global available_beans
    global available_cups
    global money

    answer = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ").strip()
    if (answer != "back"):
        drink = int(answer) - 1
        if (available_water < water_per_cup[drink]):
            print("Sorry, not enough water!")
        elif (available_milk < milk_per_cup[drink]):
            print("Sorry, not enough milk!")
        elif (available_beans < beans_per_cup[drink]):
            print("Sorry, not enough coffee beans!")
        elif (available_cups < 1):
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            available_water -= water_per_cup[drink]
            available_milk -= milk_per_cup[drink]
            available_beans -= beans_per_cup[drink]
            available_cups -= 1
            money += cost_per_cup[drink]


def fill():
    global available_water
    global available_milk
    global available_beans
    global available_cups
    
    available_water += int(input("Write how many ml of water do you want to add: "))
    available_milk += int(input("Write how many ml of milk do you want to add: "))
    available_beans += int(input("Write how many grams of coffee beans do you want to add: "))
    available_cups += int(input("Write how many disposable cups of coffee  do you want to add: "))

def take():
    global money
    print("I gave you $" + str(money))
    money = 0


def print_remaining():

    global available_water
    global available_milk
    global available_beans
    global available_cups
    global money

    print("The coffee machine has:")
    print(str(available_water) + " of water")
    print(str(available_milk) + " of milk")
    print(str(available_beans) + " of coffee beans")
    print(str(available_cups) + " of disposable cups")
    if (money == 0):
        print("0 of money")
    else:
        print("$" + str(money) + " of money")


work()

'''water_per_cup = 200
milk_per_cup = 50
beans_per_cup = 15'''

''' print("Write how many ml of water the coffee machine has:")
available_water = int(input())
print("Write how many ml of milk the coffee machine has:")
available_milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
available_beans = int(input())

print("Write how many cups of coffee you will need:")
needed_cups = int(input())

possible_cups = min(available_water // water_per_cup, available_milk // milk_per_cup, available_beans // beans_per_cup)
if (possible_cups < needed_cups):
    print("No, I can make only " + str(possible_cups) + " cups of coffee")
elif (possible_cups == needed_cups):
    print("Yes, I can make that amount of coffee")
else:
    print("Yes, I can make that amount of coffee (and even " + str(possible_cups - needed_cups) + " more than that)")'''

'''print("For", n_cups, "cups of coffee you will need:")
print(water_per_cup * n_cups, " ml of water")
print(milk_per_cup * n_cups, " ml of milk")
print(beans_per_cup * n_cups, "g of beans")'''

