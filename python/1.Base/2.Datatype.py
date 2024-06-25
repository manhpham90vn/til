# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# creating variable

# str
x = "Hello"
print(x, type(x))

# int
x = 20
print(x, type(x))

# float
x = 20.5
print(x, type(x))

# complex
x = 1j
print(x, type(x))

# list
x = [1, 2, 3]
print(x, type(x))

# tuple
x = (1, 2, 3)
print(x, type(x))

# range
x = range(6)
print(x, type(x))

# dict
x = {"name": "John", "age": 36}
print(x, type(x))

# set
x = {"apple", "banana", "cherry"}
print(x, type(x))

# frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x, type(x))

# bool
x = True
print(x, type(x))

# bytes
x = b"Hello"
print(x, type(x))

# bytearray
x = bytearray(5)
print(x, type(x))

# memoryview
x = memoryview(bytes(5))
print(x, type(x))

# None
x = None
print(x, type(x))