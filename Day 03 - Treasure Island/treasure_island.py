print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input("You are at cross road. Choose either \"left\" or \"right\"\n").lower()

wrong_choice = 0
if choice == "right":
    print("You fell in a hole.\nGAME OVER")
elif choice == "left":
    print("You are now at the shore.")
    choice = input("Do you want to wait for a boat or swim away? Choose either \"wait\" or \"swim\"\n").lower()

    if choice == "swim":
        print("Oops! You were eaten by a crocodile.\nGAME OVER")
    elif choice == "wait":
        print("You safely cross the sea.")
        choice = input("Now there are three doors in front of you. Choose \"red\" or \"yellow\" or \"blue\"\n").lower()

        if choice == "red" or choice == "blue":
            print(f"Wrong Door. {choice.title()} monster kills you.\nGAME OVER")
        elif choice == "yellow":
            print("Congratulations! You found the treasure.\nYOU WIN")
        else:
            wrong_choice = 1
    else:
        wrong_choice = 1
else:
    wrong_choice = 1

if wrong_choice == 1:
    print("You chose unknown option.\nGAME OVER")