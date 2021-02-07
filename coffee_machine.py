def sell(buy, water, milk, beans, cups, money):
    if buy == "1":
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
        return water, milk, beans, cups, money

    elif buy == "2":
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        money += 7
        return water, milk, beans, cups, money

    elif buy == "3":
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6
        return water, milk, beans, cups, money



def it_has(water, milk, beans, cups, money):
    print(f'''The coffee machine has:
          {water} of water
          {milk} of milk
          {beans} of coffee beans
          {cups} of disposable cups
          {money} of money''')


def action():
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    it_has(water, milk, beans, cups, money)

    act = input("Write action (buy, fill, take): ")
    if act == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        buy = input()
        water, milk, beans, cups, money = sell(buy, water, milk, beans, cups, money)
        it_has(water, milk, beans, cups, money)


    elif act == "fill":
        w = int(input("Write how many ml of water do you want to add: "))
        m = int(input("Write how many ml of milk do you want to add: "))
        b = int(input("Write how many grams of coffee beans do you want to add: "))
        c = int(input("Write how many disposable cups of coffee do you want to add: "))

        water += w
        milk += m
        beans += b
        cups += c
        it_has(water, milk, beans, cups, money)


    elif act == "take":
        print(f"I gave you ${money}")
        money -= money
        it_has(water, milk, beans, cups, money)



action()
















