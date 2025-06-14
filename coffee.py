class CoffeeMachine:
    def __init__(self):
        self._turned_on = True
        self._resources = {
            "water": [300, "ml"],
            "coffee": [100, "g"],
            "milk": [200, "ml"],
            "money": [0, "$"],
        }
        self._drinks = {
            "espresso": {
                "water": [50, "ml"],
                "coffee": [18, "g"],
                "milk": [0, "ml"],
                "price": [1.50, "$"],
            }, 
            "latte": {
                "water": [200, "ml"],
                "coffee": [24, "g"],
                "milk": [150, "ml"],
                "price": [2.50, "$"],
            }, 
            "cappuccino": {
                "water": [250, "ml"],
                "coffee": [24, "g"],
                "milk": [100, "ml"],
                "price": [3.00, "$"],
            },
        }
        self._coins = {
            "quarters": 0.25,
            "dimes": 0.10,
            "nickels": 0.05,
            "pennies": 0.01,
        }
        self._actions = ["off", "report"]
        
    
    def prompt_user(self) -> str:
        # User choices are: espresso, latte, cappuccino, off, report
        user_choice = ""
        while not (user_choice in self._drinks or user_choice in self._actions):
            user_choice = input("\nWhat would you like (espresso/latte/cappuccino)?\n> ").lower()
            if not (user_choice in self._drinks or user_choice in self._actions):
                print()
                print("=" * 100)
                print("ERROR: Please specify a valid drink or action (e.g. 'espresso')")
                print("=" * 100)
                print()

        if user_choice in self._drinks:
            if self.check_resources_sufficient(user_choice):
                drink_price = self._drinks[user_choice]["price"][0]
                if self.complete_transaction(drink_price):
                    print()
                    print("=" * 68)
                    print()
                    print(f"Enjot your {user_choice} ☕️!".center(68))
                    print()
                    print("=" * 68)
                    print()
                else:
                    # FIXME: Make this work later
                    print("FAILLL")
                    
        elif user_choice == "report": 
            self.print_report()
        elif user_choice == "off": 
            self.turn_off()
    
    def check_resources_sufficient(self, drink: str) -> bool:
        """
        Checks that there enough resources to make the given drink.
        """

        sufficient_resources = True

        print()
        print("=" * 68)
        print("||" + (" " * 21) + " CHECKING RESOURCES..." + (" " * 21) + "||")
        print("=" * 68)
        print()

        for resource, quantity_and_unit in self._drinks[drink].items():
            if resource == "price":
                continue

            quantity, unit = quantity_and_unit[0], quantity_and_unit[1]
            
            description = f"Drink requires {quantity} {unit} of {resource}..."
            
            print(f"\t\t{description:<40}", end="")
            
            if self._resources[resource][0] >= quantity:
                print("🗹")
            else: 
                print("⛝ [INSUFFICIENT]")
                sufficient_resources = False

        return sufficient_resources

    
    def complete_transaction(self, price: float) -> bool:
        """
        Attempts a monetary transaction based on the price and the coins the user inserts.
        """
        transaction_successful = False
        transaction_total = 0.00

        print()
        print("=" * 68)
        print("||" + (" " * 22) + "PLEASE INSERT COINS." + (" " * 22) + "||")
        print("=" * 68)

        for coin, value in self._coins.items():
            print()
            print(f"How many {coin}: ".center(68))
            print()
            try:
                transaction_total += int(input("".center(32))) * value
            except ValueError:
                print()
                print("=" * 100)
                print("ERROR: Please enter a whole number (e.g. '1', '2'))")
                print("=" * 100)
                print()
                print(f"How many {coin}: ".center(68))
                print()
                transaction_total += float(input("".center(32))) * value
            print()
            print(("*" * 34).center(68))
            print()
            print(f"YOUR TOTAL SO FAR: ${transaction_total:.2f}".center(68))
            print()
            print(("*" * 34).center(68))
            print()
        
        if transaction_total >= price:
            print()
            print("=" * 68)
            print("||" + (" " * 21) + "TRANSACTION SUCCESSFUL" + (" " * 21) + "||")
            print("=" * 68)
            transaction_successful = True
        else:
            print()
            print("=" * 68)
            print("||" + (" " * 21) + "⛝ TRANSACTION FAILED ⛝" + (" " * 21) + "||")
            print("=" * 68)

        self.calculate_change(price, transaction_total, transaction_successful)

        return transaction_successful

    def calculate_change(self, price: float, transaction_total: float, transaction_successful: bool) -> None:
        """
        Calculates and prints change to be returned to user.
        """
        if not transaction_successful:
            print("=" * 68)
            print("||" + (" " * 20) + f"HERE IS ${transaction_total:.2f} IN CHANGE" + (" " * 20) + "||")
            print("=" * 68)
        elif (transaction_successful and transaction_total > price):
            change = transaction_total - price
            print("=" * 68)
            print("||" + (" " * 20) + f" HERE IS ${change:.2f} IN CHANGE" + (" " * 20) + "||")
            print("=" * 68)
        else:
            print("=" * 68)
            print("||" + (" " * 27) + "NO CHANGE." + (" " * 27) + "||")
            print("=" * 68)

    
    def print_report(self) -> None:
        """
        Prints out a report of the remaining resources and cash in the machine.
        """

        print(("=" * 30) + " REPORT " + ("=" * 30))
        print()
        print(f"WATER: {self._water}ml".center(68))
        print()
        print(f"MILK: {self._milk}ml".center(68))
        print()
        print(f"COFFEE: {self._coffee}g".center(68))
        print()
        print(f"MONEY: ${self._money:.2f}".center(68))
        print()
        print("=" * 68)
    
    def turn_off(self) -> bool:
        """
        Turns off the machine and prints a depowering message
        """

        self._turned_on = False
        print()
        print("=" * 68)
        print("||" + (" " * 20) + "MACHINE POWERING DOWN..." + (" " * 20) + "||")
        print("=" * 68)
        return self._turned_on
        
        