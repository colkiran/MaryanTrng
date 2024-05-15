
print("clear".center(60, "-"))
player = {'name': 'Tendulkar', 'Age': 36, 'runs': 97, 'oppn': 'nzl'}
print(f"player :{player}")

player.clear()
print(f"player :{player}")

print("items".center(60,"-"))
# items function is a combination of keys and values function

player = {'name': 'Tendulkar', 'Age': 36, 'runs': 97, 'oppn': 'nzl'}
print(f"player :{player}")

itm = player.items()
print(f"items :{itm}")

for k, v in player.items():
    print(k, "=>", v)

print("update".center(60, "-"))
player1 = {'name': 'Tendulkar', 'Age': 36, 'runs': 97, 'oppn': 'nzl'}
player2 = {'name': 'Rahul', 'Age': 28, 'runs': 150, 'year': '2010'}

print(f"player1 :{player1}")
print(f"player2 :{player2}")

# update player1's values with player2's values

player1.update(player2)
print(f"player1 :{player1}")

