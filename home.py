from collections  import Counter
y = [(1920, 1938), (1911, 1944), (1920, 1955), (1938, 1939), (1900,2000), (1900,2000), (1900,2000), (1900,2000), (1900,2000)]

a = []
for i in y:
    list_of_nums = list(range(i[0],i[1]+1))
    a.extend(list_of_nums)
d=Counter(a)
print(d.most_common(1))
