# lst = [4, "hello", (55, 33, ), 33, 65.01, ('kkk', 'kkk'), ]
# def func(lst):
#     sum = 0
#     for i in lst:
#         try:
#             sum += i
#         except TypeError:
#             continue
#     return sum       
# print(func(lst))
# func(lst)


# def func():   
#     while True:
#         num = input("Enter sum: ")
#         try:
#             num = int(num)
#             s =  num * 0.3
#             break
#         except:
#             continue
#     return s
# print(func())

a = {
    'John': 150,
    'Kate': 200,
    'Beka': 250
}

def func ():
    name = input("Enter your name: ")
    try:
        print(a['John'])
    except:
        print 