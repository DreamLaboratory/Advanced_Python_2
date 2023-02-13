from time import perf_counter
list_of_numbers = list(range(1_000_000)) # list of numbers []


start = perf_counter()

# def evens(list_of_numbers):
#     return [i for i in list_of_numbers if i % 2 == 0]

evens = list(filter(lambda x: x % 2 == 0, list_of_numbers))

end = perf_counter()

# evens(list_of_numbers)
print(evens)
print(end - start)
