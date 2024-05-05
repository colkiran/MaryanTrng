
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 60)

for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("-" * 60)

for i in range(1, 6):
    # print(i, end= " ")
    for j in range(1, 6):
        print(j, end=" ")
    print()

print("-" * 60)

for i in range(1, 6):
    # print(i, end= " ")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("-" * 60)

for i in range(1, 6):
    for k in range(i, 6):
        print("*", end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


