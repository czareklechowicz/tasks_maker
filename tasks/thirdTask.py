from collections import OrderedDict
from utils import utils_user_choice
import time

def third_task():
    utils_user_choice(get_user_input, remove_duplicate_a, remove_duplicate_b, remove_duplicate_c, 2)

def get_user_input():
  n = input(str("Enter:"))
  return n

def remove_duplicate_a(input):
    start = time.time() 
    print("Result:", "".join(OrderedDict.fromkeys(input)))
    return start

def remove_duplicate_b(input): 
    start = time.time()
    print("Result:", set(input))
    return start


def remove_duplicate_c(input): 
    start = time.time()
    t=""
    for i in input:
        if(i in t):
            pass
        else:
            t=t+i
    print("Result:",t)
    return start
