import time

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


# Functions are First-Class Objects -  can be passed around as arguments e.g. int, str, float ect.
def calculate(calc_func, n1, n2):
    return calc_func(n1, n2)


result = calculate(mult, 5, 4)


# Nested Functions
# def outer_function():
#     print("OUTER")
#
#     def inner_function():
#         print("inner")
#
#     inner_function()

# Functions can be RETURNED
# def outer_function():
#     print("OUTER")
#
#     def inner_function():
#         print("inner")
#
#     return inner_function
#
#
# call_inner = outer_function() # assigns the outer functions output to call_inner
# call_inner()    # take our new variable and add parenthesis to call inner_function
#                 # which is embedded in the outer func return
#
#
# # DECORATORS
# def delay_decorator(func):
#
#     def wrapper_func():
#         time.sleep(2)
#         func()
#     return wrapper_func
#
# @delay_decorator
# def say_hello():
#     print("hello")
#
# @delay_decorator
# def say_goodbye():
#     print("goodbye")
#
# @delay_decorator
# def greeting():
#     print("How are you?")





def speed_calc_decorator(func):
    def get_speed():
        func()
        speed = time.time()
        return speed
    return get_speed

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i



fast = fast_function()
slow = slow_function()
print(f"fast took {fast} seconds")
print(f"slow took {slow} seconds")
print(f"The difference in speed is {slow - fast:.2f} seconds")
