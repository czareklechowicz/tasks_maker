from tasks.secondTask import second_task 
from tasks.firstTask import first_task 
from tasks.thirdTask import third_task 


def task_choice():
    print("Choose your task number")
    print("1 - 'sum of pairs in function")
    print("2 - 'self-dividing number'")
    print("3 - 'duplication remover'")
    x = input()
    
    if x != '0':
        if x == '1':
            first_task()
        if x == '2':
            second_task()
        if x == '3':
            third_task()
            

    once_more = input("Do you want to try another task? Type 'yes'. If you don't want type 'no'")
    if once_more == "yes":
        task_choice()
    if once_more == "no":
        return


