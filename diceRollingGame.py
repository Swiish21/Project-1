import random

def roll_dice(num_dice):
    """Rolls the specified number of dice and returns the total result."""
    return sum(random.randint(1, 6) for _ in range(num_dice))

def main():
    while True:
        user_input = input("How many dice would you like to roll? (1-6): ")
        if user_input.isdigit() and 1 <= int(user_input) <= 6:
            num_dice = int(user_input)
            result = roll_dice(num_dice)
            print(f"You rolled {num_dice} dice and got a total of: {result}")
        else:
            print("Please input a number between 1 and 6.")
            

if __name__ == "__main__":
    main()