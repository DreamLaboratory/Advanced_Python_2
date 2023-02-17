list_other = range(1000000)

#iter() is a built-in function that returns an iterator from an iterable.

inter_list = iter(list_other)
# print(next(inter_list))
# print(next(inter_list))
# print(next(inter_list))
# print(next(inter_list))
# print(next(inter_list))
# print(next(inter_list))


# An infinite generator function that prints
# next square number. It starts with 1
 
 
def nextSquare(nums:list):
    counter = 0
    # An Infinite loop to generate squares
    for i in nums:
        yield counter # yield is a keyword that is used like return, except the function will return a generator.
        counter = i**2 #

# Driver code to test above generator
# function
# for num in nextSquare():
#     if num > 100:
#         break
#     print(num)

numbers = nextSquare([1,2,3,4,5,6,7,8,9,10])
# print(list(numbers))


#yield is a keyword that is used like return, except the function will return a generator.


#range() is a generator, so it doesn't create a list of 1 million items in memory. It creates them one at a time, and only when you ask for them. This is a huge advantage when you're working with large datasets.



# Example 2: Using yield in Python

class N_Even_Number:
    def __init__(self, num) -> None:
        self.num = num

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.num:
            self.counter += 1
            return self.counter * 2
        else:
            raise StopIteration
    
# for i in N_Even_Number(10):
#     print(type(i), i)

even_nums = N_Even_Number(10)
even_nums = iter(even_nums)
print(next(even_nums))
print(next(even_nums))
print(next(even_nums))
print(next(even_nums))

import types, collections

issubclass(types.GeneratorType, collections.Iterable) #