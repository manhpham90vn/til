# creating variable
x = 1
y = "Hello"

print(x)
print(y)

# casting
x = str(3)
print(x)

# get the type
print(type(x))

# assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

# unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)

# global variable
def myfunc():
    global g
    g = "fantastic"

myfunc()
print(g)