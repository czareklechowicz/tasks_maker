from utils import utils_user_choice
import time

def second_task():
    utils_user_choice(get_user_input, self_divisible_a, self_divisible_b, self_divisible_c, 2)

def get_user_input():
    n = int(input("Enter a number: "))
    return n

def self_divisible_a(input):
    start = time.time()
    result = all([int(digit) != 0 and input % int(digit) == 0 for digit in str(input)]) 

    if result == False:
        print(input, "is not divisible")
    else:
        print(input, "is self-divisible")
    return start


def self_divisible_b(input):
    start = time.time()
    string_input = str(input)
    if '0' in string_input:
        print(input, "is not self-divisible")
    number_of_digits = len(string_input)
    i = 0

    while i < number_of_digits:
        if input % int(string_input[i]) != 0:
            print(input, "is not self-divisible")
            return start
        i+=1

    print(f"{input} is self-divisible")
    return start

def self_divisible_c(input):
    start = time.time()
    for digit in str(input):
        if digit == '0' or input % int(digit) != 0:
            print(input, "is not self-divisible")
            return start
    print(input, "is self-divisible")
    return start

