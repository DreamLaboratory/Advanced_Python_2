"""
collections.OrderedDict – Remember the Insertion Order of Keys
"""

from collections import  OrderedDict

d = OrderedDict(four=4, one=1, two=2, three=3)
print(d)  # OrderedDict([('four', 4), ('one', 1), ('two', 2), ('three', 3)])

d['five'] = 5
print(d)  # OrderedDict([('four', 4), ('one', 1), ('two', 2), ('three', 3), ('five', 5)])

d.popitem(last=False)

print(d)  # OrderedDict([('four', 4), ('one', 1), ('two', 2), ('three', 3)])

d.move_to_end('three', last=False)
print(d)  # OrderedDict([('three', 3), ('four', 4), ('one', 1), ('two', 2)])