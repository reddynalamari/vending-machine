''' 
Name        : N. Shashidhar Reddy
Topic       : Food Vending Machine
Discription : This a simulation of a vending machine. This code will take input from user to buy items and 
              The amount should be entered and the process will be continued until the user exit.
              When the user exits the code it will print the total money, total bill, remaining change.
              Here in this code I used Functions to organize my code properly.'''


menu = '''
1 >  chocolate   10rs
2 >  chips       20rs
3 >  milkshake   30rs
4 >  water       15rs
5 >  options
6 >  exit'''

revisite = "Thankyou for shopping and please visit again!!"

amount = 0
total = 0
t_cash = 0
print(menu)

def a(t_cash,total,amount):
    print(f"Total money entered : {t_cash}")
    print(f"Total bill          : {total}")
    print(f"Your change         : {amount}\n{revisite}")
    exit("byee :)")


def chocolate(amount,total,t_cash):
        if amount < 10:
            cash = int(input("It costs 10rs: "))
            amount += cash
            t_cash += cash


        if amount > 10:
            print("You got chocolate!!")
            amount -= 10
            total += 10
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash
            

        elif amount == 10:
            print("You got chocolate!!")
            amount -= 10
            total+=10
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash
            

        elif amount < 10:
            print("Insuficient money!!")
            print(f"Your money: {amount}")
            amount -= cash
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash

def chips(amount,total,t_cash):
        if amount < 20:
            cash = int(input("It costs 20rs: "))
            amount += cash
            t_cash += cash


        if amount > 20:
            print("You got chips!!")
            amount -= 20
            total+=20
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash
            

        elif amount == 20:
            print("You got chips!!")
            amount -= 20
            total+=20
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash
            

        elif amount < 20:
            print("Insuficient money!!")
            print(f"Your money: {amount}")
            amount -= cash
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash
            
def milkshake(amount,total,t_cash):
        if amount < 30:
            cash = int(input("It costs 30rs: "))
            amount += cash
            t_cash += cash


        if amount > 30:
            print("You got milkshake!!")
            amount -= 30
            total+=30
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash
            

        elif amount == 30:
            print("You got mikshake!!")
            amount -= 30
            total+=30
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash
            

        elif amount < 30:
            print("Insuficient money!!")
            print(f"Your money : {amount}")
            amount -= cash
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash

def water(amount,total,t_cash):
        if amount < 15:
            cash = int(input("It costs 15rs: "))
            amount += cash
            t_cash += cash


        if amount > 15:
            print("You got water!!")
            amount -= 15
            total+=15
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash
            

        elif amount == 15:
            print("You got water!!")
            amount -= 15
            total+=15
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash
            

        elif amount < 15:
            print("Insuficient money!!")
            print(f"Your money             : {amount}")
            amount -= cash
            ch = input("Do you want any other items(y/n): ")
            if ch.lower()=='n':
                a(t_cash,total,amount)
            elif ch.lower()=='y':
                return amount,total,t_cash

while True:
    op = int(input("Enter the option: "))
    if op == 1:
        amount,total,t_cash = chocolate(amount,total,t_cash)

    elif op == 2:
        amount,total,t_cash = chips(amount,total,t_cash)

    elif op == 3:
        amount,total,t_cash = milkshake(amount,total,t_cash)

    elif op == 4:
       amount,total,t_cash = water(amount,total,t_cash)

    elif op == 5:
        print(menu)
    
    elif op == 6:
        a(t_cash,total,amount)

    else:
        print("Choose the correct option!!")
