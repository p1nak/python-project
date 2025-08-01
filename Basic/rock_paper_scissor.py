import random
def game(user,comp):
    if(user == comp):
        return "tie"
    elif(user == "stone" and comp == "scissor") or \
        (user == "paper" and comp == "stone") or \
        (user == "scissor" and comp == "paper"):
        return "you win!"
    else:
        return "you loss!"
print("welcome to play stone, paper , scissor")

user_choice = input("your choice : ").lower()
comp_choice = random.choice(["stone","paper","scissor"])

print(f"comp choice : {comp_choice}")

result = game(user_choice,comp_choice) 

print(f"the final result : {result}")
