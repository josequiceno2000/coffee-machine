import time

class CoffeeMachine:
    def __init__(self):
        self._turned_on = True;
        self._water = 300 # ml
        self._milk = 200 # ml
        self._coffee = 100 # g
        self._money = 0 # dollars
        self._drinks = {
            "espresso": {
                "water": 50,
                "coffee": 18,
                "milk": 0,
            }, 
            "latte": {
                "water": 200,
                "coffee": 24,
                "milk": 150,
            }, 
            "cappuccino": {
                "water": 250,
                "coffee": 24,
                "milk": 100,
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

        if user_choice == "espresso": pass
        elif user_choice == "latte": pass
        elif user_choice == "cappuccino": pass
        elif user_choice == "off": self.turn_off()
        elif user_choice == "report": self.print_report()
    
    def check_resources_sufficient(self, drink str) -> bool:
        pass 
    
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
        
        