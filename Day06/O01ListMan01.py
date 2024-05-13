
l1 = list()   # list function
print(f"l1 :{l1}")
print(type(l1))
print("-" * 60)

l2 = [1, 2, 3, 4, 5.3, 6.2, 7.1, 8.0, 9+2j, 10-3j, 'eleven', 'twelve', 'thirteen', True, False ]
print(f"l2 :{l2}")
print(type(l2))
print("-" * 60)

l3 = list(range(1, 6))
print(f"l3 :{l3}")
print(type(l3))
print("-" * 60)

#CRUD
#Create
l1 = list(range(1, 6))
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
# Read
# read the list by using its indexes

print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")
print(f"l1[-1] :{l1[-1]}")
print(f"l1[0:4] :{l1[0:4]}")
print(f"l1[-1:-4:-1] :{l1[-1:-4:-1]}")

for i in l1:
    print(i, end=" ")
print()

print("-" * 60)
# update  - modify the existing value or add a new element into the list

print(f"l1 :{l1}")
# lists will not allow to insert new values - static
l1[3] = 300
l1[1] = 500
# l1[5] = "new element"       # cannot add a new element
print(f"l1 :{l1}")

print("-" * 60)
# delete
print(f"l1 :{l1}")
del l1[2]
del l1[3]

print(f"l1 :{l1}")
print("-" * 60)
print(dir(l1))
