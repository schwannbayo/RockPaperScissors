import random
option=['R','P','S']


while True:
    to_be_guessed=random.choice(option)
    user_input=input("input your guess:\n R is for Rock\n S is for scissors \n P is for Paper \n")
    if user_input==to_be_guessed:
           print("it's a tie")
    elif user_input=="S" and to_be_guessed=="P":
           print("Player(Scissors) : CPU (Paper)")
           print("Player Won")
           break
    elif user_input=="R" and to_be_guessed=="S" :
           print("Player(Rock) : CPU(Scissors)")
           print("Player Won")
           break
    elif user_input=="P" and to_be_guessed=="R" :
           print("Player(Paper) : CPU(Rock)")
           print("Player Won")
           break
   
    elif user_input=="R" and to_be_guessed=="P" :
           print("Player (Rock) : CPU(Paper)")
           print("Computer Won")
           break
    elif user_input=="P" and to_be_guessed=="S" :
           print("Player(Paper) : CPU(scissors)")
           print("Computer won")
           break
    elif user_input=="S" and to_be_guessed=="R" :
           print("Player(Scissors) : CPU(Rock) ")
           print("computer Won")
           break
    else :
        print("invalid Entry") 
print("Good Bye")        
           
       

       
    
 