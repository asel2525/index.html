# from time import time


# def decor(func):
#     def wrapper():
#         a = time()
#         func()
#         b = time()
#         print(b - a)
#     return wrapper

# @decor
# def func():
#     return 5 + 7

# func()


# def decor(func):
#     def wrapper(*args):
#         a = func(*args)
#         return a*2
#     return wrapper


# @decor
# def sum_args(*args):
#     return sum(args)

# print(sum_args(2, 2))


from time import time
def decor(func):
    def wrapper(*args):
        a = func(*args)
        return a*2
    return wrapper


print(decor(time)())
