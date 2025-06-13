import time

class CoffeeMachine:
    def __init__(self):
        self._turned_on = True
        self._money = 0 # dollars
        self._resources = {
            "water": [300, "ml"],
            "coffee": [100, "g"],
            "milk": [200, "ml"],
        }
        self._drinks = {
            "espresso": {
                "water": [50, "ml"],
                "coffee": [18, "g"],
                "milk": [0, "ml"],
            }, 
            "latte": {
                "water": [200, "ml"],
                "coffee": [24, "g"],
                "milk": [150, "ml"],
            }, 
            "cappuccino": {
                "water": [250, "ml"],
                "coffee": [24, "g"],
                "milk": [100, "ml"],
            },
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
            return self.check_resources_sufficient(user_choice)
        
        elif user_choice == "report": 
            self.print_report()
        elif user_choice == "off": 
            self.turn_off()
    
    def check_resources_sufficient(self, drink: str) -> bool:
        print()
        print("=" * 68)
        print("||" + (" " * 21) + " CHECKING RESOURCES..." + (" " * 21) + "||")
        print("=" * 68)

        print()

        for resource, quantity_and_unit in self._drinks[drink].items():
            quantity, unit = quantity_and_unit[0], quantity_and_unit[1]
            print(f"\t\tDrink requires {quantity} {unit} of {resource}...", end="\t")
            if self._resources[resource][0] >= quantity:
                print("🗹")
            else: 
                print("⛝ [INSUFFICIENT]")
        return True
    
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
        print("||" + (" " * 19) + "MACHINE POWERING DOWN..." + (" " * 19) + "||")
        print("=" * 68)
        return self._turned_on
        
        