print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

# Cross Road
print("You're at a cross road. Where do you want to go?")
crossroad_turn = input("\tType \"left\" or \"right\": ")

if crossroad_turn == "left":
    # Go to lake
    print("\nYou've come to an lake with a island in the middle of it. Where do you want to go?")
    lake_turn = input("\tType \"swim\" or \"wait\": ")
    if lake_turn == "swim":
        print("\nGame Over!")
    elif lake_turn == "wait":
        # Go to Island
        print("\nA boat appears and you arrive to the island unharmed. \nThere is a single building with three doors painted in different colors.")
        entrance = input("\tEnter through the \"blue\",\"yellow\", or \"red\" entrance?")
        if entrance == "yellow":
            print("\nYou Win!")
        elif entrance == "blue" or "red":
            print("\nGame Over!")

elif crossroad_turn == "right":
    print("\nGame Over!")
