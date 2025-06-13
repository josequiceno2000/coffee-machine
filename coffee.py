class CoffeeMachine:
    def __init__(self):
        self._water = 300 # ml
        self._milk = 200 # ml
        self._coffee = 100 # ml
        self._money = 0 # dollars
    
    def prompt_user(self) -> str:
        user_choice = input("What would you like (espresso/latte/cappuccino)?\n> ").lower()
        return user_choice