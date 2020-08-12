import time
import random
import operator
from colorama import Fore, init
start_time = time.time()
score = 0
run = True
init(autoreset=True)

while run == True :

#smt
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    num_3 = random.randint(3, 10)
    num_4 = random.randint(3, 10)
    num_5 = random.randint(2,4)

    operator_choice = random.randint(1, 4)


    if operator_choice == 1 :
        result = operator.add(num_1, num_2)
        print(num_1, end=' ')
        print('+', end=' ')
        print(num_2)
    if operator_choice == 2 :
        result = operator.sub(num_1, num_2)
        print(num_1, end=' ')
        print('-', end=' ')
        print(num_2)
    if operator_choice == 3 :
        result = operator.mul(num_3, num_4)
        print(num_3, end=' ')
        print('*', end=' ')
        print(num_4)
    if operator_choice == 4 :
        result = operator.pow(num_3, num_5)
        print(num_3, end=' ')
        print('^', end=' ')
        print(num_5)
    while True :
        try :
            answer = int(input("What is your answer? :  "))
            break
        except ValueError :
            print("Oops... That was not valid number. Try again please ")





    if int(answer) == int(result) :
        print(Fore.GREEN + "That's a good answer")

        score += 1
    else :
        print(Fore.RED + "That's a bad answer")
    end_time = time.time()

    if end_time - start_time >= 60 :
        run = False
else :
    print("Your score is", end=' ')
    print(score)































