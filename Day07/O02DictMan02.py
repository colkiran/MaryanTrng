
print("keys".center(60, "-"))

player = {'name': 'Tendulkar', 'Age': 36, 'runs': 97, 'oppn': 'nzl', 'year': 2003, 'venue': 'Auckland'}
print(f"player :{player}")

k = player.keys()
print(f"keys :{k}")

print("-" * 60)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(60, "-"))

player = {'name': 'Tendulkar', 'Age': 36, 'runs': 97, 'oppn': 'nzl', 'year': 2003, 'venue': 'Auckland'}

print(f"player :{player}")

v = player.values()
print(f"values :{v}")

print("get".center(60, "-"))

player = {'name': 'Tendulkar', 'Age': 36, 'runs': 97, 'oppn': 'nzl', 'year': 2003, 'venue': 'Auckland'}

print(f"player :{player}")

print("-" * 60)
print(f"Name  :{player.get('name', 'Invalid Key, Please enter a valid key.....')}")
print(f"Venue :{player.get('venu', 'Invalid Key, Please enter a valid key.....')}")

print("fromkeys".center(60, "-"))
cities = ['che', 'blr', 'mum', 'hyd', 'del']
print(f"Cities :{cities}")

# convert the list into a dictionary
res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 24)
print(f"res :{res}")

print("setdefault".center(60, "-"))
player = {'name': 'Tendulkar', 'Age': 36, 'runs': 97, 'oppn': 'nzl'}
print(f"player :{player}")

# add only new key values into it
player.setdefault("name", "Sachin")
player.setdefault("Age", 32)

player.setdefault("year", 2010)
player.setdefault('venue', 'auckland')

print(f"player: {player}")

print("pop".center(60, "-"))
player = {'name': 'Tendulkar', 'Age': 36, 'runs': 97, 'oppn': 'nzl'}
print(f"player :{player}")

res = player.pop('Age')
print(f"res: {res}")

res = player.pop('oppn')
print(f"res: {res}")

# res = player.pop('')
# print(f"res: {res}")

print(f"player: {player}")

print("popitem".center(60, "-"))
player = {'name': 'Tendulkar', 'Age': 36, 'runs': 97, 'oppn': 'nzl'}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")
