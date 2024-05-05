
"""
arithmetic
comparison or relational
logical
Bitwise
Ternary
"""

print("Arithematic Operator".center(60, "-"))
a = 10
b = 3
print(f"a, b :{a, b}")
print(f"addtion         : a + b = {a + b}")
print(f"subtraction     : a - b = {a - b}")
print(f"multiplication  : a * b = {a * b}")
print(f"division        : a / b = {a / b}")
print(f"floor division  : a // b = {a // b}")
print(f"modulus         : a % b = {a % b}")
print(f"exponential     : a ** b = {a ** b}")

print("Augmentor".center(60, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")

x += 5          # x = x + 5
print(f"x :{x}")

x /= 3          # x = x / 3
print(f"x :{x}")

print("comparison".center(60, "-"))
# ==, >, <, !=, >=, <=
a = 10
b = 3
print(f"a == b :{a == b}")
print(f"a != b :{a != b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")

print("logical operator".center(60, "-"))
# and, or, not
print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")

print("-" * 60)
print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")

print("-" * 60)
print(f"not(1 == 1 and 2 == 2) :{not(1 == 1 and 2 == 2)}")
print(f"not(1 == 1 and 2 == 1) :{not(1 == 1 and 2 == 1)}")

print("-" * 60)
# integer representation of unicode characters (ascii values)
print(f"ord('a') :{ord('a')}")
print(f"ord('z') :{ord('z')}")

print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print("apple" > "orange")
print("orange" > "apple")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")

print(f"ternary operator".center(60, "-"))
a = 18
print("eligible" if a > 17 else "not eligible")

