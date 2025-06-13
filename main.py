from coffee import CoffeeMachine

def main():
    coffee_machine = CoffeeMachine()
    while True:
        coffee_machine.prompt_user()
        if not coffee_machine._turned_on:
            break

if __name__ == "__main__":
    main()