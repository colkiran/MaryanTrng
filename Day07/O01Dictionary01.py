
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'sachin', 'runs': 120, 'oppn': 'Aus', 'venue': 'Gabba'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict(name='rahul', age=32, runs=85, oppn="SA")
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d5 = dict([('name', 'virat'), ('age', 29), ('runs', 67), ('oppn', 'pak')])
print(f"d5 :{d5}")
print(type(d5))

print("-" * 60)
# CRUD
player = {'name': 'Sachin', 'Age': 36, 'runs': 97, 'oppn': 'nzl'}
print(f"player :{player}")

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"runs :{player['runs']}")

print("-" * 60)
# iterate
for i in player:
    print(i, "=>", player[i])
print()

print("-" * 60)
# update
print(f"player :{player}")
player['year'] = 2003
player['venue'] = 'Auckland'
player['name'] = "Tendulkar"

print(f"player :{player}")

print("-" * 60)
# delete
print(f"player :{player}")

del player['Age']
del player['year']

print(f"player :{player}")

print(dir(player))
