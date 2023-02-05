from utils import utils_user_choice
import time

def first_task():
    utils_user_choice(get_user_input, sum_of_pairs_a, sum_of_pairs_b, sum_of_pairs_c, 1)


def get_user_input():
    user_input = input("Enter a list of numbers separated by commas: ")
    my_list = [int(x) for x in user_input.split(",")]

    if (len(my_list)) % 2 != 0:
        print("Please enter even amount of numbers.")
        return get_user_input()
    
    return my_list
    

def sum_of_pairs_a(input):
    start = time.time()
    i = 0
    sumArr = []

    while i < (len(input)):
        if i == (len(input)-1):
            return 
        sumArr.append(input[i] + input[i+1])
        i += 2

    print('Result: ', sumArr)
    return start

def sum_of_pairs_b(input):
    start = time.time() 
    result = []

    for i in range(0, len(input), 2):
        result.append(input[i] + input[i+1])

    print('Result: ', result)
    return start

def sum_of_pairs_c(input):
    start = time.time()
    result = [input[i] + input[i+1] for i in range(0, len(input), 2)]
    print('Result: ', result)
    return start
