print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

first_choice = input("You're at a cross road. Where do you want to go? " 'Type "left" or "right"\n').lower()

if first_choice == "left":
    second_choice = input("You've to a lake. There is an island in the middle of the lake.\n" 'Type "wait" to wait for a boat. Type "swim" to swim across.\n ').lower()
    if second_choice == "wait":
        third_choice = input("You arrive at the island unharmed.\n There is a house with 3 doors. \n One red, one yellow and one blue \n Which color door do you choose?\n").lower()
        if third_choice == "red":
            print("Burned by fire. GAME OVER!")
        elif third_choice == "blue":
            print("Eaten by beasts. GAME OVER!")
        elif third_choice == "yellow":
            print("YOU WIN!")
        elif third_choice == "abbey road":
            print("HOW DID YOU GET HERE! ANYWAYS AND IN THE END THE LOVE YOU TAKE IS EQUAL TO THE LOVE YOU MAKE!")
        else:
            print("GAME OVER!")
    else:
        print("Attacked by Sea Monster. GAME OVER!")
else:
    print("Fell into a hole. GAME OVER!")