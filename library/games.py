
import datetime
import time
from datetime import datetime
import numerguess
import quizgame
current_time = datetime.now().replace(microsecond=0)
print(current_time)
MAX_TIME = 5
MAX_PERSONS = 10

start_time = time.time() + MAX_TIME
time_limit = 15

games = ["quiz", "number_guess"]

game1="quiz"
game2 ="number_guess"
print("available games are....")
for i in games:
    print(i)
    

def check():
    
    print("....game going to start in 5 sec....")
    print("you have only 15sec to complete ... then only u will get score")
                        
    start_time = time.time() 
    while (time.time() - start_time) < MAX_TIME:
            time.sleep(1)
    print("Quiz started!")

     # Update start_time after the initial 5 seconds

    while (time.time() - start_time) < time_limit:
        while True:
            k = input("Enter existed game name from list...")
            if all(item in games for item in k):
                break
            if (game1 in k):
                print(quizgame.quiz_game())
            else:
                print(numerguess.number())
                
            # else:
            #     print("Please enter existing game name...")
        return k
    end_time = time.time()
    elapsed_time = end_time - start_time

    if elapsed_time > time_limit:
        print("Time's up! You hav took too long.....so no score better luck next time ")
                        
    else:
        print("In time")   
                

              
a = check()
print(a)
    
    

    




