#creating a guessing game

import random
t=0
try:
  total_guess= int(input("Enter the number of guess:  "))
  low= int(input("Enter the lower range:   "))
  high=int(input("Enter the high range:   "))
  random_number=random.randint(low,high)
  actual_guess=int(input("Enter a guess number that matches with random_number:  "))
  print("int")
except:
    print("only integers are allowed")

finally:("Please behave and type integers only")   
while (random_number != 'actual_guess'):
    
           
    if (actual_guess not in range(low,high)):
      raise Exception("Number out of Range")
    if(t<(total_guess-1)):
       if actual_guess < random_number:
       
           print("The number guessed is low")
       
           t+=1
           actual_guess=int(input("Enter a guess number that matches with random_number:  "))
 
       elif(actual_guess > random_number):
           print("The number guessed is high")
           t+=1
           actual_guess=int(input("Enter a guess number that matches with random_number:  "))
       else:
           print("The number guessed is right")
           print("Total guesses taken: ",t+1)
           break
    else:
        print("Ran out of tries")
        break
