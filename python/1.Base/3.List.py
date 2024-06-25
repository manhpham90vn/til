list = ["apple", "banana", "cherry"]

# len() function
print(len(list))

# access list items
print(list[0])
print(list[:2])
print(list[1:])

# check if item exists
if "apple" in list:
    print("Exists")

# change item value
list[0] = "orange"
print(list)

# insert item
list.insert(1, "kiwi")
print(list)

# append item
list.append("mango")
print(list)

# remove item
list.remove("banana")
print(list)

# delete item
del list[0]
print(list)

# clear list
list.clear()
print(list)

# loop through list
for element in ["apple", "banana", "cherry"]:
    print(element)

# loop through list using index
for i in range(len(["apple", "banana", "cherry"])):
    print(["apple", "banana", "cherry"][i])    

# loop throught list using while loop
i = 0
while i < len(["apple", "banana", "cherry"]):
    print(["apple", "banana", "cherry"][i])
    i += 1

# loop through list using list comprehension
list = [x for x in ["apple", "banana", "cherry"]]    
print(list)

# sort list
list = ["apple", "banana", "cherry"]
list.sort()
print(list)

# sort list in descending order
list.sort(reverse=True)
print(list)

# copy list
list = ["apple", "banana", "cherry"]
new_list = list.copy()
print(new_list)