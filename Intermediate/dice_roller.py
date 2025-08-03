import random

def show_dice(no):
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    elif no == 3:
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")
    elif no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif no == 6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")

def main():
    print("🎲 Welcome to Dice Roller Simulator 🎲\n")
    while True:
        input("Press Enter to roll the dice...")
        no = random.randint(1, 6)
        print(f"\n🎲 You rolled: {no}")
        show_dice(no)
        
        again = input("\nRoll again? (y/n): ").lower()
        if again != "y":
            print("\nThanks for playing! Goodbye 👋")
            break
        print("\n" + "-"*30 + "\n")

if __name__ == "__main__":
    main()
