import random

print('Welcome!!!\nThis Game Is Build By : \n\t\t\t\t [ " Ayoub Amer " ]')

repeat  = True

yes_list = ["y", "yes"]

number_of_wins = 0 

number_of_loses = 0 

while repeat : 
  print("We Have Already Choosen A Number Between 1 and 9.Now,It Is Your Turn To Guess What Number We Choose.")
  num = random.randint(1, 9) # a,b are integrated

  allowed_errors = 3 

  done = False 
  
  while not done : 
    guess = int(input("Enter Your Guess : "))
    if guess != num : 
      allowed_errors -= 1 
      if allowed_errors == 0 : 
        number_of_loses += 1
        print("You Lose This Round", end=".")
        repeat_ans = input("Do You Want To Try Again [y or n] : ")
        if repeat_ans.lower() not in yes_list : 
          repeat = False 
          print(f"You Played {number_of_loses + number_of_wins} rounds.You Lose In {number_of_loses} and Win In {number_of_wins}.")
        break
    else : 
      print(f"You Did It.We Choose [ {num} ].You Won This Round", end=".")
      done = True
      number_of_wins += 1
      repeat_ans = input("Do You Want To Try Again [y or n] : ")
      if repeat_ans.lower() not in yes_list : 
        repeat = False
        print(f"You Played {number_of_loses + number_of_wins} rounds.You Lose In {number_of_loses} and Win In {number_of_wins}.")
      
    
