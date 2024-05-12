
# C style printf

format = "Welcome %s, what a %s player"
print(f"format :{format}")

values = ("Sachin", "superb")       # tuple
print(f"values :{values}")
print("-" * 60)

# print(format, values)
print(format % values)

print("-" * 60)
print("Welcome %s, what a %s player" % ("Sachin", "superb"))

print("-" * 60)
format = "Welcome %s, your rating of %.3f, what a %s player"
print(format)
print(format % ("Sachin", 9.8, "class"))
print(format % ("Sachin", 9.893409, "class"))
print(format % ("Sachin", 9.823842034,"class"))
print(format % ("Sachin", 9, "class"))
print(format % ("class", 9, "Sachin"))

print("Welcome %s, your rating of %.3f, what a %s player" %  ("Sachin", 9.8762361, "class"))

print("-" * 60)
# unix style
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
print(tmpl.substitute(name = "Sachin", adj = "superb"))

print("-" * 60)
# format strings in python
print("Welcome {}, what a {} player for {}".format("Sachin", "superb", "India"))
print("Welcome {}, what a {} player for {}".format( "superb", "India", "Sachin"))

print("Welcome {0}, what a {1} player for {2}".format("Sachin", "superb", "India"))

print("Welcome {name}, what a {adj} player for {ctry}".format(name="Sachin", adj="superb", ctry="India"))

print("Welcome {name}, with a rating {rating}, what a {adj} player".format(name="Sachin", rating=9, adj="superb"))

print("Welcome {name}, with a rating {rating:.3f}, what a {adj} player".format(name="Sachin", rating=9.892349, adj="superb"))

print("-" * 60)

from math import pi, e
print(f"PI={pi} and Eulers constant={e}")

print("PI = {} and Eulers Constant = {}".format(pi, e))
print("PI = {pi} and Eulers Constant = {e} and magic number = {magic}".format(pi=pi, e=e, magic = 40585))

print("-" * 60)
full_name = ["Sachin", "Tendulkar"]
print(f"full name :{full_name}")
print("Mr.{name}".format(name=full_name))
print("Mr.{name[0]} {name[1]}".format(name = full_name))

print("-" * 60)
print(f"current module name :{__name__}")   #double underscore = dunder name

import math
print(__name__)
print(math.__name__)

print("the {mod.__name__} module gives the value of pi = {mod.pi} and eulers constant e = {mod.e}".format(mod=math))
