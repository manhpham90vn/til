import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
print(x, type(x))
y = json.loads(x)
print(y, type(y))

object = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(object, type(object))
json_object = json.dumps(object)
print(json_object, type(json_object))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x), type(json.dumps(x)))

try:
  print(xxx)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")