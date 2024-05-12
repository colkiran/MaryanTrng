
# conversions
print("Conversions".center(60, "-"))
print("{val}  {val}   {val}".format(val = "A"))
print("{val!s}  {val!r}   {val!a}".format(val = "A"))

print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=364645645))

print("Alignment".center(60, "-"))
print("{num:10}Tendulkar".format(num=3))
print("{num:15}Tendulkar".format(num="Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))
from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("alignment".center(60, "-"))
print("{name:>15} Tendulkar".format(name="Sachin"))      # right Align
print("{name:^15} Tendulkar".format(name="Sachin"))      # center Align
print("{name:<15} Tendulkar".format(name="Sachin"))      # left Align

print("-" * 60)
print("one googol is {}".format(10 ** 100))
print("one googol is {:,}".format(10 ** 100))   # thousand seperator

print("-" * 60)
print("{st:*^60}".format(st="Hello World"))
print("Hello World".center(60, "*"))

print("-" * 60)
print("{}".format(pi))
print("{:015.2f}".format(pi))
print("{:>015.2f}".format(pi))
print("{:^015.2f}".format(pi))
print("{:<015.2f}".format(pi))

print("-" * 60)
print("{0:>10}\n{1:>10}\n{2:>10}".format("hello", 'world', "string"))


