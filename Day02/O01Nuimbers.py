
a = 10
b = -10

#  f string or format string - interpolation - display the value of a variable inside " "
print(f"a :{a}")
print(type(a))          # RTTI - Run time type identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.4
d = -10.4
print(f"c: {c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = +2e3        # exponential format
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 3.14j
h = -3.14j      # x = 10 + 4j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 60)
print(f"max :{max(10, 55, 20, 29, 30, 49, 40)}")
print(f"min :{min(10, 55, 20, 29, 30, 49, 40)}")

print("-" * 60)
x = 2 + 3.5
print(f"x :{x}")
print(type(x))

x = 2
y = 3.5
z = x + y
print(f"x :{x}")
print(f"y :{y}")
print(f"z :{z}")

print(f"x = {type(x)}")
print(f'y = {type(y)}')
print(f"z = {type(z)}")

print("Conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(f"11   :{11}")          # decimal number
print(f"0b11 :{0b11}")        # Binary number
print(f"0b101 :{0b101}")      # Binary Number
print(f"0o11  :{0o11}")       # octal number
print(f"0o101 :{0o101}")      # octal Number
print(f"0xa   :{0xa}")         # hexa decimal
print(f"0xe :{0xe}")

print("Number System Conversion".center(60, "-"))
a = 100
print(bin(a))
print(oct(a))
print(hex(a))