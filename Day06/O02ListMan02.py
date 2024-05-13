
print('append'.center(60, "-"))
l1 = list(range(1, 6))
print(f'l1 :{l1}')
print(type(l1))

l1.append(6)
l1.append(7)
l1.append(8)

print(f'l1 :{l1}')
l1.append([9, 10, 11])
print(f'l1 :{l1}')

print(f"l1[8] :{l1[8]}")
print(f"l1[8][1] :{l1[8][1]}")

print("extend".center(60, "-"))
l2 = list(range(6, 11))
print(f"l2 :{l2}")
print(type(l2))

l2.extend([11, 12, 13, 14, 15])
print(f"l2 :{l2}")

print("insert".center(60, "-"))
l3 = list(range(1, 11, 2))
print(f"l3 :{l3}")

l3.insert(1, 2)
l3.insert(3, 4)
l3.insert(5, 6)
l3.insert(7, 8)
l3.insert(9, [10, 11, 12, 13])

print(f"l3 :{l3}")

print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop()              # removes the last element from the list
print(f"res :{res}")

# res = l1.pop(9)
# print(f"res :{res}")

print(f"l1 :{l1}")

print("remove".center(60, "-"))
# remove will work based on the values present in the list

l1 = [1, 2, 1, 2, 2, 2, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]
print(f"l1 :{l1}")

l1.remove(3)        # removes the first 3 from the left
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

print("clear".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")
