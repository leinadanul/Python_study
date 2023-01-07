user_option = input("rock, paper or scissor =>")
computer_option = "paper"

if user_option == computer_option:
    print("Draw")
elif user_option == "rock":
    if computer_option == "scissor":
        print("Your Win!!")
    else:
        print("Your lose") 
elif user_option == "paper":
    if computer_option == "scissor":
        print( "Your lose ")
    else :
        print("Your win!!") 
elif user_option == "scissor":
    if computer_option == "rock":
        print("your lose ")   
    else:
        print("your win!!")        