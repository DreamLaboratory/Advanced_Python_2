# Nested Lambda Function

# BU Nomsiz fuksiya

# Why ?

# def func(x, y):
#     return lambda z: x + y

# def find_top(list_num, func):
#     top = list_num[0]
#     for i in list_num:
#         if func(i, top):
#             top = i
#     return top

# # 1. Lambda function

# def func(x, y):
#     return x+y

# sum_lamb = lambda x, y: x + y

# print(sum_lamb(2, 3))

# Nested Lambda Function


# if_then_else = lambda cond, x, y: x if cond else y # if_then_else(True, 1, 2) = 1

# print(if_then_else(1>2, 1, 2))

# def if_then_else(cond, x, y):
#     return x if cond else y
    
# print(if_then_else(1>2, 1, 2))

# if_then_else = lambda cond: lambda then_do: lambda else_do: cond(then_do)(else_do)

# troo = lambda then_do: lambda else_do: then_do
# fals = lambda then_do: lambda else_do: else_do

# coffees_today =  if_then_else(fals)("Yes")("No")
# print(coffees_today)

#TODO  f = lambda x: 1*x**2 + 2*x + 2

