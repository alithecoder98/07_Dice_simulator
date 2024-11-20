import random

side = 6

def dice():
    die1 = random.randint(1, side)
    die2 = random.randint(1, side)
    # Optional: Use die3 if needed
    die3 = random.randint(1, side)
    print(f"The sum of two dice is: {die1 + die2}")

if __name__ == "__main__":
    dice()
