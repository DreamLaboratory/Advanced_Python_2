from functools import reduce
import operator

list_of_number = list(range(1, 5))
print(list_of_number)
sum_of_number = reduce(lambda x, y: operator.mul(x, y), list_of_number)
print(sum_of_number)



# Path: 1-day/reduce_adv.py