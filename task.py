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

left_right = input("The tunnel before you splits. Turn Left or Right. Type L or R \n").upper().strip()
if left_right != "L":
    print("You fell of a cliff. Game over")
    exit()

swim_wait = input("You reach a lake. Swim or Wait for a boat? Type S or W \n").upper().strip()
if swim_wait != "W":
    print("You have been eaten by Piranhas. Game over.")
    exit()

which_door = input("You come to three doors painted Red, Yellow and Blue. Pick the door color by typing R, Y or B \n").upper().strip()
if which_door == "Y":
    print("You found the treasure! You win the game!")
elif which_door == "R":
        print("You have walked into a room of fire. Game over.")
elif which_door == "B":
        print("You have fallen into a pit of daggers. Game over.")
else:
    print("You have chosen a door that does not exist. Game over.")

# Twitter post
"""
Day 3 of #100DaysOfCode: The Complete Python Pro Bootcamp, Conditional statements, 
logical operators, code blocks and scope, the modulo operator
"""

