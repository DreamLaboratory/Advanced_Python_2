from collections import Counter, deque

#################################################### Counter ####################################################

words = ['a', 'b', 'c', 'f', 'c', 'f','c', 'f', 'a']
words_count = Counter(words)

# print(words_count)
# print(words_count.most_common(2))
# print(sorted(words_count.elements()))

#################################################### deque ####################################################

# deque is a double-ended queue. It can be used to add or remove elements from both ends.
# It is thread-safe, which means that multiple threads can access it simultaneously.
# It is faster than the list in terms of execution time for appending and popping elements.

custom_deque = deque([], maxlen=3)

for i in range(1,10):
    custom_deque.append(i)
    print(custom_deque)

# custom_deque.rotate()
custom_deque.rotate(3) # rotate right
print(custom_deque)
