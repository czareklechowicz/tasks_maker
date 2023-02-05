import time

def get_execution_time(start, end):
    total_time = end - start
    print('Execution time:', total_time * 1000, 'milliseconds')


def utils_user_choice(userInput, method_a, method_b, method_c, taskNumber):
    print("You have chosen task", taskNumber ,"now choose a method:")
    print("'a' - short way 'first idea'")
    print("'b' - legible way")
    print("'c' - the quickest response of the system")
    x = input("")

    if x != '0':
        if x == 'a':
            start = method_a(userInput())
            end = time.time()
            get_execution_time(start, end)
        elif x == 'b':
            start = method_b(userInput())
            end = time.time()
            get_execution_time(start, end)
        elif x == 'c':
            start = method_c(userInput())
            end = time.time()
            get_execution_time(start, end)
        else:
            print("Unfortunately there is no such way, please try again :D")
            return utils_user_choice(userInput, method_a, method_b, method_b, taskNumber)
        
    once_more = input("Do you want to try another solution? Type 'yes'. If you don't want type 'no' ")
    if once_more == "yes":
        utils_user_choice(userInput, method_a, method_b, method_c, taskNumber)
    if once_more == "no":
        return

