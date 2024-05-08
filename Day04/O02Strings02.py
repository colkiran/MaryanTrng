
print("find".center(60, "-"))
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(F"st1 :{st1}")
print(st1.find("w"))       # returns the index of w

print(st1.find("l"))
print(st1.find("l", st1.find("l") + 1))
print(st1.find("l", st1.find("l", st1.find("l") + 1) + 1))

print("-" * 60)
st1 = "lolndonlondon"
print(st1.find("l"))
print(st1.find("l",3))                # hard code
print(st1.find("l", st1.find("l") + 1))     # generic code

print("-" * 60)
print(f"st2 :{st2}")
print(f"dog :{st2.find('dog')}")
print(f"the :{st2.find('the')}")
print(f"the :{st2.find('the', st2.find('the') + 1)}")

print("replace".center(60, "-"))
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1 :{st1}")
res = st1.replace("h", 'H')
print(f"res :{res}")
# print(f"st1 :{st1}")

res = st1.replace("l", "L")
print(f"res :{res}")

res = st1.replace("l", "L", 1)
print(f"res :{res}")

res = st1.replace("l", "L", 2)
print(f"res :{res}")

print("-" * 60)
print(f"st2 :{st2}")
res = st2.replace("fox", "tiger")
print(f"res :{res}")

res = st2.replace("the", "The")
print(f"res: {res}")

res = st2.replace("the", "The", 1)
print(f"res: {res}")
