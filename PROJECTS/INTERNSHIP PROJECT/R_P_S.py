import random


comp_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I Dont't understand, try again.")
        Choose_Option()
    return user_choice


def Computer_Option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You Choose Rock. The Computer Choose Rock.. You Tied.")
        elif comp_choice == "p":
            print("You Choose Rock. The Computer Choose Paper... You Lose.")
            comp_wins += 1

        elif comp_choice == "s":
            print("You Choose Rock. The Computer Choose Scissors. You Win..")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("You Choose Rock. The Computer Choose Rock. You Win.")
            player_wins += 1

        elif comp_choice == "p":
            print("You Choose Paper. The Computer Choose Paper. You Tied.")

        elif comp_choice == "s":
            print("You Choose Paper. The Computer Choose Scissors. You Lose.")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("You Choose Scissors. The Computer Choose Rock. You Lose.")
            comp_wins += 1

        elif comp_choice == "p":
            print("You Choose Scissors. The Computer Choose Paper. You Win.")
            player_wins += 1

        elif comp_choice == "s":
            print("You Choose Scissors. The COmputer Choose Scissors. You Tied.")

    print("")
    print("Player Wins: " + str(player_wins))
    print("Computer Wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
            
