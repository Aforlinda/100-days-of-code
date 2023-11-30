import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.  "))

if choice == 0:
    print(f" You chose {rock}")
elif choice == 1:
    print(f" You chose {paper}")
elif choice == 2: 
    print(f" You chose {scissors}")
else: 
    print("You selected an invalid option. You lose. ")


computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(f" The computer chose {rock}")
elif computer_choice == 1:
    print(f" The computer chose {paper}")
else: 
    print(f" The computer chose {scissors}")

    
    
if choice == 0 and computer_choice == 1 :
    print("You lost")
elif choice == 0 and computer_choice == 2 :
    print("You won!!!!")
elif choice == 1 and computer_choice == 2 :
    print("You lost")
elif choice == 1 and computer_choice == 0 :
    print("You won")
elif choice == 2 and computer_choice == 1 :
    print("You won!!!!")
elif choice == 2 and computer_choice == 0 :
    print("You lost")
elif choice == computer_choice:
    print("Its a draw") 
else:
    print("You selected an invalid option. You lose. ")
