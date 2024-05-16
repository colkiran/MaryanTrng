"""
sort    - sort will sort the original array
sorted  - sorted will take a copy of the list and sorts it and returns it
"""

l1 = [9, 3, 7, 1, 10, 2, 5, 6, 4, 8]
print(f"l1 :{l1}")

asc_res = sorted(l1)
print(f"ascending :{asc_res}")

desc_res = sorted(l1, reverse=True)
print(f"Descending :{desc_res}")

print("-" * 60)

l1 = [9, 'zebra', 'apple', 3, 'yellow', 'blue', 7, 'violet', 'green',  1, 'white', 'pink', 10, 'orange', 'cat', 2, 'dog', 'fox', 5, 'egg', 'frog', 6, 4, 8, 192, 1038, 27, 215, 2089]

print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(f"res :{res}")

x = 0
for i in range(0, len(res)):
    if type(res[i]) == int:
        print(i)
        x = i
        break

print(res[:x] + sorted(res[x:]))

print("-" * 60)
cities = ['thiruvananthapuram', 'delhi', 'chennai', 'vishakapatnam', 'bangalore', 'ooty', 'pune', 'mysore', 'mumbai', 'hyderabad']

print(f"cities :{cities}")
res = sorted(cities, key=len)
print(f"res :{res}")

months = ['dec', 'apr', 'aug', 'nov', 'mar', 'jan', 'jun', 'feb', 'sep', 'oct', 'may', 'jul']
print(len(months))
# sort the months - calendar dates

print("-" * 60)
l1 = [9, 3, 7, 1, 10, 2, 5, 6, 4, 8]
print(f"l1 :{l1}")

print(f"l1 :{l1}")
print(list(reversed(l1)))
