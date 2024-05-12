
st = "*****Hello*****"
print(f"st :{st}")

lres = st.lstrip("*")
print(f"lres :{lres}")

rres = st.rstrip("*")
print(f"rres :{rres}")

res = st.strip("*")
print(f"res :{res}")

print("-" * 60)
st = "hello world"
print(st)
# maketrans

# the rule is length of a and b should be the same
resTbl = st.maketrans(a, b)
print(resTbl)

ures = st.translate(resTbl)
print(f"upper case :{ures}")
