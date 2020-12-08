import sys
resource_water = 3000
resource_milk = 2000 
resource_coffee = 500 
while(True):
    def start():
        global resource_coffee
        global resource_milk
        global resource_water
        choice = input("what would you like to have?\n1.Espresso\n2.latte\n3.cappuccino") 
        report=input("If you want to print the report?\n1.Yes\n2.No")
        if choice== '1':
            resource_water-=50
            resource_coffee-=15
            if report=='1':
                print("water: 50ml\ncoffee: 15g\namount: $2")
            else:
                pass
        elif choice == '2':
            resource_water -= 25    
            resource_milk -=30 
            resource_coffee-=20
            if report=='1':
                print("water:25ml\nmilk:30ml\ncoffee:20g,\namount:$3")
            else:
                pass
        elif choice=='3':
            resource_coffee-=10
            resource_water-=30
            resource_milk-=25
            if report=='1':
                print("water:25ml\nmilk:30ml\ncoffee:10g,\namount:$3.5")
            else:
                pass
        else:
            print("Resource is unavailable")

        def process_coins():
            print("Please insert coins.")
            total = int(input("how many quarters?: ")) * 0.25
            total += int(input("how many dimes?: ")) * 0.1
            total += int(input("how many nickles?: ")) * 0.05
            total += int(input("how many pennies?: ")) * 0.01
            x=int(round(total,5))
            print(x)
            if choice=='1':
                if x==1:
                    print("Transaction successful")
                else:
                    print("enter the correct amount")
            if choice=='2':
                if x==3:
                    print("Transaction successful")
                else:
                    print("enter the correct amount")
            if choice=='3':
                if x==3.5:
                    print("Transaction successful")
                else:
                    print("enter the correct amount")
            return x
        process_coins()
    status=input("Do you want to stop the machine\n1.yes\n2.No")
    if status=='1':
        sys.exit()
    else:
        start()
    print("The available water is",resource_water)
    print("The available milk is",resource_milk)
    print("The avaiable coffee is",resource_coffee)


