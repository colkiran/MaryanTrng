
st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 60)
print(f"st[0]  :{st[0]}")       # indexing - strings are stored like an array or list
print(f"st[6]  :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

print("-" * 60)
# reverse indexing
print(f"st[-1]  :{st[-1]}")
print(f"st[-5]  :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 60)
# slicing
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

st = "malayalam"
print("palindrome" if st[:] == st[::-1] else "Not a palindrome")   # ternary

print("-" * 60)
# strings are immutable
st = "hello"
print(f"st :{st}")
# st[0] = "H"

print("-" * 60)
# string functions to manipulate it
st = "abc"
print(dir(st))