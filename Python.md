# Python Syntax Reference

## Mục Lục

0. [Phân Loại Ngôn Ngữ](#1-phân-loại-ngôn-ngữ)
1. [Tầng 1: Syntax & Semantics](#tầng-1-syntax--semantics)
   - [1.1 Khai Báo Biến](#11-khai-báo-biến)
   - [1.2 Khai Báo Hàm](#12-khai-báo-hàm)
   - [1.3 Vòng Lặp](#13-vòng-lặp)
   - [1.4 Điều Kiện](#14-điều-kiện)
   - [1.5 Destructuring & Spread](#15-destructuring--spread)
2. [Tầng 2: Type System](#tầng-2-type-system)
   - [2.1 Kiểu Dữ Liệu Cơ Bản](#21-kiểu-dữ-liệu-cơ-bản)
   - [2.2 Enum](#22-enum)
   - [2.3 Nullable Types](#23-nullable-types)
   - [2.4 Null Safety](#24-null-safety)
   - [2.5 Generics](#25-generics)
   - [2.6 Collection Operations](#26-collection-operations)
   - [2.7 String Operations](#27-string-operations)
3. [Tầng 3: OOP & Type Relationships](#tầng-3-oop--type-relationships)
   - [3.1 Class/Object](#31-classobject)
   - [3.2 Kế Thừa & Đa Hình](#32-kế-thừa--đa-hình)
   - [3.3 Interface/Trait/Protocol](#33-interfacetraitprotocol)
   - [3.4 Visibility/Access Modifiers](#34-visibilityaccess-modifiers)
4. [Tầng 4: Memory Model](#tầng-4-memory-model)
   - [4.1 Memory Management](#41-memory-management)
   - [4.2 Property & Getter/Setter](#42-property--gettersetter)
5. [Tầng 5: Concurrency Model](#tầng-5-concurrency-model)
   - [5.1 Concurrency/Async](#51-concurrencyasync)
6. [Tầng 6: Paradigm](#tầng-6-paradigm)
   - [6.1 Functional Programming](#61-functional-programming)
7. [Tầng 7: Error Handling](#tầng-7-error-handling)
   - [7.1 Xử Lý Lỗi](#71-xử-lý-lỗi)
   - [7.2 Error Types](#72-error-types)
8. [Tầng 8: Module & Organization](#tầng-8-module--organization)
   - [8.1 Import/Module](#81-importmodule)
   - [8.2 Extension Methods](#82-extension-methods)
9. [Tầng 9: I/O & Networking](#tầng-9-io--networking)
   - [9.1 HTTP & Networking](#91-http--networking)
   - [9.2 File I/O](#92-file-io)
10. [Tầng 10: Data & Serialization](#tầng-10-data--serialization)
    - [10.1 JSON & Serialization](#101-json--serialization)
    - [10.2 Date & Time](#102-date--time)
    - [10.3 Regular Expression](#103-regular-expression)
11. [Tầng 11: Development Practices](#tầng-11-development-practices)
    - [11.1 Testing](#111-testing)
    - [11.2 Logging](#112-logging)
    - [11.3 Dependency Injection](#113-dependency-injection)
    - [11.4 Configuration](#114-configuration)
    - [11.5 Build & Package Management](#115-build--package-management)
    - [11.6 Documentation](#116-documentation)
12. [Tầng 12: Advanced Concepts](#tầng-12-advanced-concepts)
    - [12.1 Advanced Concepts](#121-advanced-concepts)
13. [Tầng 13: Memory Layout](#tầng-13-memory-layout)
    - [13.1 Object Layout](#131-object-layout)
    - [13.2 Array/String Layout](#132-arraystring-layout)
14. [Tầng 14: Compilation Model](#tầng-14-compilation-model)
    - [14.1 Interpreter](#141-interpreter)
    - [14.2 Bytecode](#142-bytecode)
    - [14.3 JIT](#143-jit)
15. [Tầng 15: Linking Model](#tầng-15-linking-model)
    - [15.1 Module Loading](#151-module-loading)
16. [Tầng 16: Runtime](#tầng-16-runtime)
    - [16.1 Stack Frame](#161-stack-frame)
    - [16.2 Garbage Collector](#162-garbage-collector)
17. [Tầng 17: Language Design Patterns](#tầng-17-language-design-patterns)
    - [17.1 Duck Typing](#171-duck-typing)
    - [17.2 Context Managers](#172-context-managers)
18. [Tầng 18: Standard Library](#tầng-18-standard-library)
    - [18.1 Collections](#181-collections)
    - [18.2 Utilities](#182-utilities)
    - [18.3 I/O & System](#183-io--system)
19. [Tầng 19: Ecosystem](#tầng-19-ecosystem)
    - [19.1 Web Frameworks](#191-web-frameworks)
    - [19.2 Database & ORM](#192-database--orm)
    - [19.3 Testing](#193-testing)
    - [19.4 Data Science & ML](#194-data-science--ml)
20. [Tầng 20: Toolchain](#tầng-20-toolchain)
    - [20.1 Build & Package Management](#201-build--package-management)
    - [20.2 Code Quality](#202-code-quality)
    - [20.3 IDE & Debugging](#203-ide--debugging)

---

## 0. Phân Loại Ngôn Ngữ

### Chạy File Python

```bash
# Chạy trực tiếp
python script.py

# Chạy với phiên bản cụ thể
python3 script.py
python3.11 script.py

# Interactive mode
python -i

# Module
python -m module_name
```

### Đặc điểm Python

- **Typing**: Dynamic, Strong typing
- **Paradigm**: Multi-paradigm (Functional, OOP, Procedural)
- **Execution**: Interpreted/Bytecode với optional JIT (PyPy)
- **Use Cases**: Data Science, ML/AI, Web (Django/Flask), Automation, Scripting

---

## 1. Tầng 1: Syntax & Semantics

### 1.1. Khai Báo Biến (Variable Declaration)

#### Mutable - Biến thường

```python
# Khai báo biến (dynamic typing)
x = 10
name = "Python"
is_active = True
prices = [1.5, 2.0, 3.5]

# Type annotation (Python 3.5+)
x: int = 10
name: str = "Python"
is_active: bool = True

# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0
```

#### Immutable - Hằng số

```python
# Python không có const thực sự
# Quy ước: viết hoa để đánh dấu là constant
MAX_SIZE = 100
PI = 3.14159

# Dùng tuple cho immutable data
COORDS = (10, 20)  # Tuple
```

#### Type Inference

```python
# Python tự suy luận kiểu
x = 10          # int
y = 3.14        # float
z = "hello"     # str

# Kiểm tra kiểu
type(x)         # <class 'int'>
isinstance(x, int)  # True
```

#### Global Variable

```python
# Biến toàn cục
global_var = "I am global"

def access_global():
    print(global_var)  # Truy cập biến toàn cục

def modify_global():
    global global_var
    global_var = "Modified"
```

#### Static Variable (Class-level)

```python
class Counter:
    count = 0  # Biến class

    def __init__(self):
        Counter.count += 1

print(Counter.count)  # 0
c1 = Counter()
print(Counter.count)  # 1
```

#### Scope & Shadowing

```python
# Python có LEGB rule: Local, Enclosing, Global, Built-in
x = "global"

def outer():
    x = "enclosing"  # Shadowing global x

    def inner():
        x = "local"  # Shadowing enclosing x
        print(x)     # "local"

    inner()
    print(x)  # "enclosing"

outer()
print(x)  # "global"

# nonlocal - thay đổi biến enclosing
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
c()  # 1
c()  # 2
```

---

### 1.2. Khai Báo Hàm (Function Declaration)

#### Function cơ bản

```python
# Function không có return
def greet():
    print("Hello!")

# Function có return
def add(a, b):
    return a + b

# Function với type hints (Python 3.5+)
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Docstring
def calculate_area(width: float, height: float) -> float:
    """Calculate rectangle area.

    Args:
        width: Width of rectangle
        height: Height of rectangle

    Returns:
        Area of rectangle
    """
    return width * height
```

#### Parameters

```python
# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Named arguments
def create_user(name, email, age):
    return {"name": name, "email": email, "age": age}

user = create_user(age=25, name="John", email="john@example.com")

# *args và **kwargs
def func(*args, **kwargs):
    print(args)    # Tuple
    print(kwargs)  # Dictionary

func(1, 2, 3, name="John", age=25)
```

#### Variadic Parameters

```python
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4, 5)  # 15

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="John", age=25)
```

#### Lambda/Arrow Function

```python
# Lambda (anonymous function)
square = lambda x: x ** 2
add = lambda a, b: a + b

# Dùng với các hàm higher-order
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Lambda với conditional
max_val = lambda a, b: a if a > b else b
```

#### Closure

```python
def outer(x):
    def inner(y):
        return x + y  # Closure: capture biến từ outer
    return inner

closure = outer(10)
closure(5)  # 15
```

#### Higher-Order Function

```python
# Function nhận function khác làm tham số
def apply_twice(func, x):
    return func(func(x))

def add_five(x):
    return x + 5

result = apply_twice(add_five, 10)  # 20

# Function trả về function
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
double(5)  # 10
```

#### Method trong Class

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def create(cls, value):
        return cls(value)

    def multiply(self, a, b):
        return a * b
```

#### Constructor & Destructor

```python
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"Creating {name}")

    def __del__(self):
        print(f"Deleting {self.name}")

    def __repr__(self):
        return f"Resource({self.name})"
```

---

### 1.3. Vòng Lặp (Loops)

#### For Loop

```python
# For với range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# For với list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# For với index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

#### While Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1

# While với break/continue
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")
```

#### For-each/List Comprehension

```python
# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Dictionary comprehension
square_dict = {x: x**2 for x in range(5)}

# Set comprehension
unique_chars = {char.lower() for char in "Hello World"}

# Generator expression
sum(x**2 for x in range(10))  # Lazy evaluation
```

#### Iterator

```python
# Dùng iter() và next()
numbers = [1, 2, 3]
it = iter(numbers)
next(it)  # 1
next(it)  # 2
next(it)  # 3
# next(it)  # StopIteration

# Custom iterator
class RangeIterator:
    def __init__(self, max_val):
        self.current = 0
        self.max = max_val

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for i in RangeIterator(5):
    print(i)  # 0, 1, 2, 3, 4
```

#### Generator/Yield

```python
# Generator function - lazy evaluation
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1

for num in count_up(5):
    print(num)  # 0, 1, 2, 3, 4

# Generator với send()
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)        # 0 (khởi tạo)
gen.send(10)     # 10
gen.send(20)     # 30

# yield from - delegate to sub-generator
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

list(flatten([1, [2, 3], [4, [5, 6]]]))  # [1, 2, 3, 4, 5, 6]

# Generator expression
squares = (x**2 for x in range(10))  # Lazy
list(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### Loop Control

```python
# Break - thoát vòng lặp
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# Continue - bỏ qua lần lặp hiện tại
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4

# Else trong vòng lặp (chạy khi không có break)
for i in range(5):
    print(i)
else:
    print("Loop completed!")  # Chạy vì không có break
```

---

### 1.4. Điều Kiện (Conditionals)

#### If-Else

```python
# If-else cơ bản
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Elif
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# One-liner
status = "Adult" if age >= 18 else "Minor"
```

#### Match Expression (Python 3.10+)

```python
# Pattern matching (switch-case)
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"

# Với pattern
def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"On X-axis at {x}"
        case (0, y):
            return f"On Y-axis at {y}"
        case (x, y):
            return f"Point at ({x}, {y})"
```

#### Ternary Operator

```python
# Cú pháp: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"

# Nested ternary
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
```

---

### 1.5. Destructuring & Spread (Phân rã & Toán tử mở rộng)

#### Tuple/List Unpacking

```python
# Basic unpacking
a, b, c = [1, 2, 3]
x, y = (10, 20)

# Swap
a, b = b, a

# Starred assignment (rest operator)
first, *rest = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

# Ignore values
_, b, _ = (1, 2, 3)  # Chỉ lấy b = 2
```

#### Dict Unpacking (Spread)

```python
# Dict unpacking với **
defaults = {"color": "red", "size": "medium"}
custom = {"size": "large", "weight": 10}

merged = {**defaults, **custom}
# {'color': 'red', 'size': 'large', 'weight': 10}

# Function argument unpacking
def greet(name, age):
    print(f"{name} is {age}")

data = {"name": "John", "age": 30}
greet(**data)  # "John is 30"

# List unpacking với *
nums = [1, 2, 3]
more = [0, *nums, 4]  # [0, 1, 2, 3, 4]
```

#### Nested Unpacking

```python
# Nested tuple unpacking
(a, b), (c, d) = (1, 2), (3, 4)

# In for loop
pairs = [("Alice", 25), ("Bob", 30)]
for name, age in pairs:
    print(f"{name}: {age}")

# Dict items unpacking
user = {"name": "John", "age": 30}
for key, value in user.items():
    print(f"{key}: {value}")
```

---

## 2. Tầng 2: Type System

### 2.1. Kiểu Dữ Liệu Cơ Bản (Primitive Types)

#### Integer

```python
# Integer (unlimited precision trong Python 3)
x = 10
negative = -5
hex_val = 0xFF      # 255
binary_val = 0b1010  # 10
octal_val = 0o777    # 511

# Operations
5 + 3    # 8 (addition)
5 - 3    # 2 (subtraction)
5 * 3    # 15 (multiplication)
5 / 3    # 1.666... (division)
5 // 3   # 1 (floor division)
5 % 3    # 2 (modulus)
5 ** 3   # 125 (exponentiation)
abs(-5)   # 5
divmod(5, 3)  # (1, 2)
```

#### Float

```python
# Float (double precision)
x = 3.14
y = -2.5
scientific = 1.5e10  # 15000000000.0

# Operations
3.14 + 1.0   # 4.14
3.14 * 2     # 6.28
3.14 / 2     # 1.57

# Special values
float('inf')    # Infinity
float('-inf')   # -Infinity
float('nan')    # Not a Number
import math
math.isnan(float('nan'))  # True
math.isinf(float('inf'))  # True
```

#### Boolean

```python
# Boolean
is_active = True
is_deleted = False

# Operations
True and False   # False
True or False    # True
not True         # False

# Truthy/Falsy values
# Falsy: None, False, 0, 0.0, '', [], {}, set()
# Truthy: mọi giá trị khác
bool(0)     # False
bool(1)     # True
bool([])    # False
bool([1])   # True
```

#### String

```python
# String
s1 = 'Hello'
s2 = "World"
s3 = '''Multi
line
string'''
s4 = """Multi
line
string"""

# String methods
s = "Hello World"
s.upper()        # "HELLO WORLD"
s.lower()        # "hello world"
s.capitalize()   # "Hello world"
s.strip()        # Remove whitespace
s.split()        # ['Hello', 'World']
s.replace('World', 'Python')  # "Hello Python"
s.find('World')  # 6
s.startswith('Hello')  # True
s.endswith('World')    # True

# f-string (Python 3.6+)
name = "Python"
version = 3.11
f"Welcome to {name} {version}"  # "Welcome to Python 3.11"
```

#### List

```python
# List (mutable sequence)
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Methods
numbers.append(6)      # Thêm vào cuối
numbers.insert(0, 0)   # Chèn tại vị trí
numbers.remove(1)      # Xóa theo giá trị
popped = numbers.pop() # Xóa và trả về phần tử cuối
numbers.sort()         # Sắp xếp
numbers.reverse()      # Đảo ngược

# Slicing
lst = [0, 1, 2, 3, 4]
lst[1:3]    # [1, 2]
lst[:3]     # [0, 1, 2]
lst[3:]     # [3, 4]
lst[::2]    # [0, 2, 4] (step 2)
lst[::-1]   # [4, 3, 2, 1, 0] (reverse)
```

#### Tuple

```python
# Tuple (immutable sequence)
point = (10, 20)
coords = (1, 2, 3)
single = (1,)  # Cần dấu phẩy

# Unpacking
x, y = point  # x=10, y=20
a, b, c = coords

# Named tuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
p.x  # 10
p.y  # 20
```

#### Set

```python
# Set (unordered, no duplicates)
s = {1, 2, 3, 3, 3}  # {1, 2, 3}

# Methods
s.add(4)          # Thêm
s.remove(1)       # Xóa (lỗi nếu không tồn tại)
s.discard(1)      # Xóa (không lỗi)
s.pop()           # Xóa và trả về phần tử bất kỳ

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}
a | b     # Union: {1, 2, 3, 4}
a & b     # Intersection: {2, 3}
a - b     # Difference: {1}
a ^ b     # Symmetric difference: {1, 4}
```

#### Dictionary

```python
# Dictionary (key-value)
user = {
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}

# Methods
user["name"]          # "John"
user.get("name")      # "John"
user.get("phone", "N/A")  # "N/A" (default)
user["phone"] = "123" # Thêm/cập nhật
user.pop("age")       # Xóa và trả về
user.keys()           # dict_keys(['name', 'email', 'phone'])
user.values()         # dict_values(['John', 'john@example.com', '123'])
user.items()          # dict_items([('name', 'John'), ...])

# Dictionary comprehension
square_dict = {x: x**2 for x in range(5)}
```

#### None

```python
# None (null value)
value = None

# Check None
if value is None:
    print("No value")

# is vs ==
value is None    # Recommended
value == None    # Works but not recommended
```

#### Callable

```python
# Callable (function, class, method)
def callable_func():
    pass

class CallableClass:
    def __call__(self):
        return "Called!"

# Kiểm tra callable
callable(callable_func)  # True
callable(callable_class())  # True nếu có __call__
```

---

### 2.2. Enum (Python 3.4+)

```python
from enum import Enum, auto

# Basic Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

Color.RED           # Color.RED
Color.RED.name      # "RED"
Color.RED.value     # 1

# Enum with auto
class Status(Enum):
    PENDING = auto()
    APPROVED = auto()
    REJECTED = auto()

# Enum with methods
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    def description(self):
        return f"Color {self.name}"

# Iteration
for color in Color:
    print(color)  # Color.RED, Color.GREEN, Color.BLUE

# Comparison
Color.RED is Color.RED   # True
Color.RED == Color.RED  # True
Color.RED == Color.GREEN  # False
```

---

### 2.3. Nullable Types

```python
# Python không có null type riêng
# Dùng Optional từ typing hoặc Union

from typing import Optional, Union

# Optional[str] = str | None (Python 3.10+)
def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, World!"
    return f"Hello, {name}!"

# Union type
def process(value: Union[str, int]) -> str:
    return str(value)
```

---

### 2.4. Null Safety

```python
# Python không có built-in null safety
# Dùng conditional và short-circuit

# Elvis operator (ternary)
name = None
result = name if name else "Unknown"

# Safe access với get
user = {"name": "John", "address": {"city": "NYC"}}
city = user.get("address", {}).get("city", "Unknown")

# Dùng getattr
city = getattr(user.get("address"), "city", "Unknown")

# Walrus operator (Python 3.8+)
if (name := get_name()) is not None:
    print(f"Hello, {name}")
```

---

### 2.5. Generics

```python
# Generics với typing module
from typing import TypeVar, Generic, List, Dict

T = TypeVar('T')

class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value

# Usage
int_container = Container(42)      # Container[int]
str_container = Container("hello")  # Container[str]

# Generic functions
from typing import TypeVar
T = TypeVar('T')

def first(lst: List[T]) -> T:
    return lst[0]

# Generic constraints
from typing import TypeVar

T = TypeVar('T', bound=int)  # Must be subclass of int

# TypeVar với Union
from typing import Union
T = Union[str, int]  # str | int (Python 3.10+)
```

---

### 2.6. Collection Operations

#### Map/Transform

```python
numbers = [1, 2, 3, 4, 5]

# map()
squared = list(map(lambda x: x ** 2, numbers))

# List comprehension (preferred)
squared = [x ** 2 for x in numbers]

# enumerate transform
indexed = [(i, v) for i, v in enumerate(numbers)]
```

#### Filter

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))

# List comprehension (preferred)
evens = [x for x in numbers if x % 2 == 0]
```

#### Reduce/Fold

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# reduce()
total = reduce(lambda acc, x: acc + x, numbers, 0)  # 15
product = reduce(lambda acc, x: acc * x, numbers, 1)  # 120

# sum() - thường dùng hơn
total = sum(numbers)  # 15
```

#### FlatMap

```python
# flatten nested lists
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [x for sublist in nested for x in sublist]
# [1, 2, 3, 4, 5, 6]

# map + flatten
words = ["hello", "world"]
chars = [ch for word in words for ch in word]
# ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
```

#### Sort

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sorted() - trả về list mới
sorted_nums = sorted(numbers)           # Tăng dần
sorted_nums_desc = sorted(numbers, reverse=True)

# list.sort() - sắp xếp in-place
numbers.sort()

# Sort với key
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)  # ['apple', 'banana', 'cherry']

# Sort dict
users = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
sorted_users = sorted(users, key=lambda x: x["age"])
```

#### Find/First/Last

```python
numbers = [1, 2, 3, 4, 5]

# Find first match
result = next((x for x in numbers if x > 3), None)  # 4

# Index
index = numbers.index(3)  # 2 (ValueError if not found)
index = next((i for i, x in enumerate(numbers) if x > 3), None)

# Last
numbers[-1]  # 5
```

#### Any/All/None

```python
numbers = [1, 2, 3, 4, 5]

any(n > 3 for n in numbers)  # True (có ít nhất 1)
all(n > 0 for n in numbers)  # True (tất cả đều > 0)
all(n > 10 for n in numbers)  # False

# None check
all(x is not None for x in numbers)
any(x is None for x in numbers)
```

#### GroupBy

```python
from itertools import groupby

data = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]

# Group by key
data.sort(key=lambda x: x[0])
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# Với dict
from collections import defaultdict
grouped = defaultdict(list)
for key, value in data:
    grouped[key].append(value)
```

#### Chunk

```python
from itertools import islice

def chunk(lst, size):
    it = iter(lst)
    while chunk := list(islice(it, size)):
        yield chunk

# Usage
numbers = [1, 2, 3, 4, 5, 6, 7]
list(chunk(numbers, 3))  # [[1,2,3], [4,5,6], [7]]
```

#### Zip

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Zip
combined = list(zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Unzip
names2, ages2 = zip(*combined)

# Enumerate (index + value)
for i, name in enumerate(names):
    print(f"{i}: {name}")
```

---

### 2.7. String Operations

#### Concatenation

```python
# Dùng +
"Hello " + "World"  # "Hello World"

# Dùng join
parts = ["Hello", "World"]
" ".join(parts)  # "Hello World"

# f-string (Python 3.6+)
name = "Python"
f"Hello {name}"  # "Hello Python"
```

#### Interpolation

```python
# f-string
name = "Python"
version = 3.11
f"{name} {version}"  # "Python 3.11"

# Format
"Hello {}".format(name)  # "Hello Python"
"Hello {0} {1}".format(name, version)
"Hello {name} {version}".format(name="Python", version=3.11)

# % formatting (cũ)
"Hello %s" % name  # "Hello Python"
```

#### Template String

```python
from string import Template

template = Template("Hello $name!")
template.substitute(name="Python")  # "Hello Python!"

# With safe substitution
template.safe_substitute(name="Python", missing="$undefined")
```

#### Split & Join

```python
text = "hello world python"

# Split
text.split()           # ['hello', 'world', 'python']
text.split('o')        # ['hell', ' w', 'rld pyth', '']

# Join
words = ['hello', 'world']
"-".join(words)        # "hello-world"
```

#### Replace

```python
text = "Hello World World"

text.replace("World", "Python")      # "Hello Python Python"
text.replace("World", "Python", 1)  # "Hello Python World"

# Regex replace
import re
re.sub(r'\d+', '#', "test 123 abc 456")  # "test # abc #"
```

#### Regex

```python
import re

text = "My email is john@example.com"

# Match
match = re.search(r'[\w.-]+@[\w.-]+', text)
if match:
    print(match.group())  # "john@example.com"

# Find all
emails = re.findall(r'[\w.-]+@[\w.-]+', text)

# Pattern với named groups
pattern = r'(?P<user>[\w.-]+)@(?P<domain>[\w.-]+)'
match = re.search(pattern, text)
match.group('user')    # 'john'
match.group('domain') # 'example.com'

# Split
re.split(r'\s+', text)  # ['My', 'email', 'is', 'john@example.com']
```

#### Substring

```python
text = "Hello World"

# Slicing
text[0:5]    # "Hello"
text[:5]     # "Hello"
text[6:]     # "World"
text[-5:]    # "World"

# methods
text.index("World")  # 6
text.find("World")  # 6 (-1 if not found)
text.startswith("Hello")  # True
text.endswith("World")    # True
```

---

### 2.8. Union & Intersection Types

```python
from typing import Union, Optional

# Union type (Python 3.5+)
def process(value: Union[str, int]) -> str:
    return str(value)

# Python 3.10+ syntax
def process(value: str | int) -> str:
    return str(value)

# Optional = Union[X, None]
def greet(name: Optional[str] = None) -> str:
    return f"Hello, {name or 'World'}!"

# Type narrowing / Type guard
def handle(value: str | int):
    if isinstance(value, str):
        print(value.upper())  # Type narrowed to str
    else:
        print(value + 1)      # Type narrowed to int

# TypeGuard (Python 3.10+)
from typing import TypeGuard

def is_str_list(val: list) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

# Type alias
UserId = int
UserName = str
UserInfo = dict[str, str | int]

# NewType for distinct types
from typing import NewType
UserId = NewType('UserId', int)
user_id = UserId(42)  # Type-safe wrapper
```

---

## 3. Tầng 3: OOP & Type Relationships

### 3.1. Class/Object

#### Class Definition

```python
class User:
    # Class attribute
    species = "Human"

    # Instance attribute
    def __init__(self, name: str, age: int):
        self.name = name    # Public
        self._age = age     # Protected (convention)
        self.__email = None # Private (name mangling)

    # Instance method
    def greet(self) -> str:
        return f"Hello, I'm {self.name}"

    # Magic methods
    def __str__(self):
        return f"User({self.name})"

    def __repr__(self):
        return f"User(name={self.name!r}, age={self._age!r})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.name == other.name and self._age == other._age

# Create instance
user = User("John", 30)
user.greet()  # "Hello, I'm John"
```

#### Data Class (Python 3.7+)

```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    email: str = "unknown@example.com"  # Default value
    tags: list = field(default_factory=list)  # Mutable default

    def __post_init__(self):
        self.email = self.email.lower()

# Usage
user = User("John", 30)
user.name  # "John"

# Immutable dataclass
@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

#### Singleton

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Alternative: module singleton
# singleton.py
class _Singleton:
    def foo(self):
        pass

singleton = _Singleton()
# Import singleton elsewhere
```

#### Factory Method

```python
class User:
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"])

    @classmethod
    def from_json(cls, json_str: str):
        import json
        data = json.loads(json_str)
        return cls.from_dict(data)

user = User.from_dict({"name": "John"})
```

#### Builder Pattern

```python
class User:
    def __init__(self):
        self.name = None
        self.email = None
        self.age = None

    def __str__(self):
        return f"User({self.name}, {self.email}, {self.age})"

class UserBuilder:
    def __init__(self):
        self._user = User()

    def name(self, name: str):
        self._user.name = name
        return self

    def email(self, email: str):
        self._user.email = email
        return self

    def age(self, age: int):
        self._user.age = age
        return self

    def build(self):
        return self._user

# Usage
user = (UserBuilder()
    .name("John")
    .email("john@example.com")
    .age(30)
    .build())
```

#### Inner/Nested Class

```python
# Nested class (static-like)
class Outer:
    class Inner:
        def greet(self):
            return "Hello from Inner"

    def create_inner(self):
        return self.Inner()

inner = Outer.Inner()
inner.greet()  # "Hello from Inner"

# Inner class với tham chiếu outer
class LinkedList:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node

    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = self.Node(value, self.head)
```

---

### 3.2. Kế Thừa & Đa Hình (Inheritance & Polymorphism)

#### Inheritance

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

# Create instances
dog = Dog("Buddy")
dog.speak()  # "Woof!"
```

#### Super

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)  # Gọi parent constructor
        self.breed = breed

    def speak(self) -> str:
        return f"{super().speak()} Woof!"  # Gọi parent method
```

#### Abstract Class

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def speak(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} says {self.speak()}"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

# animal = Animal("Test")  # TypeError: Can't instantiate abstract class
dog = Dog("Buddy")  # OK
```

#### Polymorphism

```python
def make_speak(animal: Animal) -> str:
    return animal.speak()

animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())  # Polymorphism
```

#### Multiple Inheritance

```python
class Flyable:
    def fly(self):
        return "Flying!"

class Swimmable:
    def swim(self):
        return "Swimming!"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"

duck = Duck()
duck.fly()    # "Flying!"
duck.swim()  # "Swimming!"

# Method Resolution Order (MRO)
Duck.__mro__
```

#### Diamond Problem (MRO)

```python
# Python giải quyết diamond problem bằng C3 Linearization (MRO)
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
d.method()  # "B" (theo MRO: D -> B -> C -> A)
print(D.__mro__)  # (D, B, C, A, object)
```

---

### 3.3. Interface/Trait/Protocol

#### Mixin

```python
# Mixin - tái sử dụng code không cần kế thừa chính
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        import json
        return cls(**json.loads(json_str))

class LogMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

# Sử dụng mixin
class User(JsonMixin, LogMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("John", 30)
user.to_json()       # '{"name": "John", "age": 30}'
user.log("Created")  # "[User] Created"
```

#### Protocol (Python 3.8+)

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

class Square:
    def draw(self) -> None:
        print("Drawing square")

# Type checking
def render(shape: Drawable) -> None:
    shape.draw()

render(Circle())  # Works!
render(Square()) # Works!

# Protocol với inheritance
class Renderable(Protocol):
    def render(self) -> str:
        ...

class HTMLRenderer:
    def render(self) -> str:
        return "<div>...</div>"

class JSONRenderer:
    def render(self) -> str:
        return '{"html": "..."}'
```

#### Abstract Base Class as Interface

```python
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, key: str, value: Any) -> None:
        pass

    @abstractmethod
    def load(self, key: str) -> Any:
        pass

class MemoryStorage(Storage):
    def __init__(self):
        self._data = {}

    def save(self, key: str, value: Any) -> None:
        self._data[key] = value

    def load(self, key: str) -> Any:
        return self._data.get(key)
```

---

### 3.4. Visibility/Access Modifiers

```python
class Example:
    public_var = "I am public"       # Public
    _protected_var = "I am protected" # Protected (convention)
    __private_var = "I am private"   # Private (name mangling)

    def public_method(self):
        return "Public"

    def _protected_method(self):
        return "Protected"

    def __private_method(self):
        return "Private"

obj = Example()
obj.public_var          # OK
obj._protected_var     # OK (nhưng convention là không dùng)
obj._Example__private_var  # Access private (không nên)

# Property cho controlled access
class Person:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value:
            self.__name = value
```

---

## 4. Tầng 4: Memory Model

### 4.1. Memory Management

#### Garbage Collection

```python
import gc

# Reference counting (automatic)
a = object()  # refcount = 1
b = a        # refcount = 2
del a        # refcount = 1
del b        # refcount = 0 -> garbage collected

# Manual GC
gc.collect()  # Force garbage collection

# Disable GC
gc.disable()
# ... code ...
gc.enable()

# Track objects
gc.get_objects()
gc.get_referrers(obj)
gc.get_referents(obj)
```

#### Weak Reference

```python
import weakref

class MyClass:
    def __init__(self, name):
        self.name = name

obj = MyClass("test")
ref = weakref.ref(obj)

ref()           # Returns the object
ref() is obj    # True

del obj
ref()           # Returns None (object was garbage collected)

# Weakref callbacks
def callback(ref):
    print("Object was garbage collected")

obj = MyClass("test")
ref = weakref.ref(obj, callback)
del obj  # Prints "Object was garbage collected"
```

#### Memory Info

```python
import sys

# Object size
x = [1, 2, 3]
sys.getsizeof(x)  # Size in bytes

# More accurate with pympler
# pip install pympler
from pympler import asizeof
asizeof.asizeof(x)  # More accurate size
```

#### Stack vs Heap

```python
# Python: Mọi object đều trên heap
# Biến là reference (trên stack) trỏ đến object (trên heap)

# Value type behavior (immutable)
a = 10
b = a     # b là copy của giá trị (vì int là immutable)
b = 20
print(a)  # 10 (không bị ảnh hưởng)

# Reference type behavior (mutable) 
a = [1, 2, 3]
b = a     # b trỏ cùng object
b.append(4)
print(a)  # [1, 2, 3, 4] (bị ảnh hưởng!)

# Copy để tránh shared reference
import copy
a = [1, 2, [3, 4]]
b = a.copy()           # Shallow copy
c = copy.deepcopy(a)   # Deep copy
```

#### Memory Safety

```python
# Python đảm bảo memory safety tự động:
# - Không có buffer overflow (bounds checking)
# - Không có dangling pointer (GC quản lý)
# - Không có use-after-free

# Memory leak có thể xảy ra với circular reference
class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a  # Circular reference!

# GC cycle detector sẽ xử lý
import gc
gc.collect()  # Force cleanup circular references

# Dùng weakref để tránh circular reference
import weakref

class Cache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get(self, key):
        return self._cache.get(key)

    def set(self, key, value):
        self._cache[key] = value
```

---

### 4.2. Property & Getter/Setter

```python
class Temperature:
    def __init__(self):
        self._celsius = 0

    # Getter
    @property
    def celsius(self):
        return self._celsius

    # Setter
    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    # Read-only (chỉ có getter)
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    # Computed property
    @property
    def kelvin(self):
        return self._celsius + 273.15

temp = Temperature()
temp.celsius = 25
print(temp.fahrenheit)  # 77.0
```

---

## 5. Tầng 5: Concurrency Model

### 5.1. Concurrency/Async

#### Threading

```python
import threading
import time

def worker(name, delay):
    print(f"{name} started")
    time.sleep(delay)
    print(f"{name} finished")

# Tạo thread
t1 = threading.Thread(target=worker, args=("Thread-1", 2))
t2 = threading.Thread(target=worker, args=("Thread-2", 1))

t1.start()
t2.start()

t1.join()  # Đợi thread kết thúc
t2.join()

# Thread với class
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"Running {self.name}")

# Thread pool
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(worker, "Task-1", 1)
    executor.map(lambda x: worker(x, 1), ["A", "B", "C"])
```

#### Multiprocessing

```python
import multiprocessing
from multiprocessing import Process, Pool

def worker(x):
    return x * x

# Process
if __name__ == '__main__':
    p = Process(target=worker, args=(5,))
    p.start()
    p.join()

# Pool
with Pool(4) as pool:
    result = pool.map(worker, [1, 2, 3, 4])
    # [1, 4, 9, 16]

# Shared memory
from multiprocessing import Value, Array
counter = Value('i', 0)
shared_array = Array('i', 10)
```

#### Async/Await (Python 3.5+)

```python
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate I/O
    return {"data": "result"}

async def main():
    # Single task
    result = await fetch_data()
    print(result)

    # Multiple tasks
    tasks = [fetch_data() for _ in range(3)]
    results = await asyncio.gather(*tasks)

    # With timeout
    try:
        async with asyncio.timeout(3):
            await fetch_data()
    except asyncio.TimeoutError:
        print("Timed out!")

asyncio.run(main())
```

#### Async HTTP Request

```python
import aiohttp
import asyncio

async def fetch_urls(urls):
    async with aiohttp.ClientSession() as session:
        async def fetch(url):
            async with session.get(url) as response:
                return await response.text()

        tasks = [fetch(url) for url in urls]
        return await asyncio.gather(*tasks)

# Usage
urls = ["https://example.com", "https://python.org"]
results = asyncio.run(fetch_urls(urls))
```

#### Event Loop

```python
import asyncio

# Event loop là core của asyncio
loop = asyncio.get_event_loop()

# asyncio.run() tạo và quản lý event loop tự động
async def main():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(main())  # Tạo loop, chạy, đóng
```

#### Semaphore & Barrier

```python
import asyncio
import threading

# Async Semaphore - giới hạn số task đồng thời
async def limited_task(sem, name):
    async with sem:
        print(f"{name} running")
        await asyncio.sleep(1)

async def main():
    sem = asyncio.Semaphore(3)  # Tối đa 3 task cùng lúc
    tasks = [limited_task(sem, f"Task-{i}") for i in range(10)]
    await asyncio.gather(*tasks)

# Threading Barrier
barrier = threading.Barrier(3)  # Chờ 3 threads

def worker(name):
    print(f"{name} waiting")
    barrier.wait()  # Chờ các thread khác
    print(f"{name} proceeding")
```

#### Structured Concurrency (Python 3.11+)

```python
import asyncio

async def main():
    # TaskGroup - structured concurrency
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data("url1"))
        task2 = tg.create_task(fetch_data("url2"))
    # Tất cả tasks hoàn thành hoặc tất cả bị cancel nếu 1 task lỗi

    print(task1.result(), task2.result())
```

---

## 6. Tầng 6: Paradigm

### 6.1. Functional Programming

#### Pure Function

```python
# Pure function - không có side effects
def add(a, b):
    return a + b

# Impure function - có side effects
counter = 0
def impure_add(a, b):
    global counter
    counter += 1
    return a + b
```

#### Immutability

```python
# Dùng tuple thay vì list cho immutable data
point = (10, 20)
# point[0] = 5  # TypeError!

# Frozenset
frozen_set = frozenset([1, 2, 3])

# dataclass với frozen=True
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

#### First-Class Function

```python
# Function là first-class citizens
def apply(func, x):
    return func(x)

def double(x):
    return x * 2

apply(double, 5)  # 10
apply(lambda x: x ** 2, 5)  # 25
```

#### Function Composition

```python
from functools import reduce

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

# Usage
f = compose(lambda x: x + 1, lambda x: x * 2)
f(3)  # (3 * 2) + 1 = 7
```

#### Currying

```python
def curry(func):
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *args2: curried(*(args + args2))
    return curried

@curry
def add(a, b, c):
    return a + b + c

add(1)(2)(3)   # 6
add(1, 2)(3)   # 6
add(1)(2, 3)  # 6
```

#### Partial Application

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

square(5)  # 25
cube(5)    # 125
```

---

## 7. Tầng 7: Error Handling

### 7.1. Xử Lý Lỗi (Error Handling)

#### Try-Except

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
    print(f"Type: {type(e).__name__}")

# Multiple exceptions
try:
    x = int("abc")
    y = 10 / 0
except ValueError as e:
    print(f"Value error: {e}")
except ZeroDivisionError as e:
    print(f"Division error: {e}")

# Catch all
try:
    x = int("abc")
except Exception as e:
    print(f"Error: {e}")
```

#### Raise Exception

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is unrealistic")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(e)  # "Age cannot be negative"
```

#### Custom Exception

```python
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        super().__init__(message)

    def __str__(self):
        return f"{self.field}: {self.message}"

# Usage
raise ValidationError("email", "Invalid email format")
```

#### Finally Block

```python
try:
    file = open("data.txt", "r")
    content = file.read()
finally:
    file.close()  # Always executed

# Try-with-resources (Python 3.7+)
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closed
```

#### Exception Propagation

```python
def level3():
    raise ValueError("Error in level3")

def level2():
    level3()  # Exception propagates up

def level1():
    try:
        level2()
    except ValueError as e:
        print(f"Caught: {e}")
        raise  # Re-raise exception
```

#### Assertion

```python
# assert - kiểm tra điều kiện (bị disable khi python -O)
assert len(items) > 0, "List must not be empty"
assert isinstance(name, str), f"Expected str, got {type(name)}"

# Dùng cho debugging, không dùng cho validation
def divide(a, b):
    assert b != 0, "Divisor must not be zero"
    return a / b
```

---

### 7.2. Error Types

#### Built-in Exceptions

```python
# Common exceptions
SyntaxError    # Syntax error
IndentationError
TypeError      # Wrong type operation
ValueError     # Right type, wrong value
NameError      # Undefined name
IndexError     # Index out of range
KeyError       # Key not found
AttributeError # Attribute not found
FileNotFoundError
IOError
RuntimeError
NotImplementedError
KeyboardInterrupt  # Ctrl+C
```

#### Custom Error Hierarchy

```python
class AppError(Exception):
    """Base exception for application"""
    pass

class ValidationError(AppError):
    """Validation error"""
    pass

class DatabaseError(AppError):
    """Database error"""
    pass

class ConnectionError(DatabaseError):
    """Connection error"""
    pass
```

#### Error Wrapping (Exception Chaining)

```python
# Exception chaining với from
try:
    result = int("abc")
except ValueError as e:
    raise RuntimeError("Failed to parse input") from e
# RuntimeError: Failed to parse input
# Caused by: ValueError: invalid literal...

# Stack trace với traceback
import traceback

try:
    1 / 0
except ZeroDivisionError:
    traceback.print_exc()  # In full stack trace
    tb_str = traceback.format_exc()  # Lấy string
```

---

## 8. Tầng 8: Module & Organization

### 8.1. Import/Module

#### Import

```python
# Import module
import math
math.sqrt(16)  # 4.0

# Import với alias
import numpy as np
import pandas as pd

# Import specific
from math import sqrt, pi
from collections import defaultdict as dd

# Import all (không nên)
from math import *  # Bad practice
```

#### Module

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}"

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

# __name__ check
if __name__ == "__main__":
    # Code chạy khi file được chạy trực tiếp
    print(greet("World"))
```

#### Namespace

```python
# Package structure
# mypackage/
#     __init__.py
#     module1.py
#     submodule/
#         __init__.py
#         module2.py

# Import
from mypackage import module1
from mypackage.submodule import module2

# __init__.py
# Export specific items
from .module1 import greet
__all__ = ['greet']
```

#### Autoloading

```python
# importlib for dynamic imports
import importlib

module = importlib.import_module("numpy")
np = importlib.import_module("numpy")

# import_module with reload
import importlib
import numpy
importlib.reload(numpy)  # Reload module
```

---

### 8.2. Extension Methods

#### Monkey Patching

```python
# Thêm method vào class có sẵn
class Extensions:
    pass

Extensions.greet = lambda self: f"Hello, {self.name}"

# Sử dụng
class Person:
    def __init__(self, name):
        self.name = name

person = Person("John")
person.greet()  # "Hello, John"
```

---

## 9. Tầng 9: I/O & Networking

### 9.1. HTTP & Networking

#### Built-in urllib

```python
import urllib.request
import urllib.parse

# GET request
response = urllib.request.urlopen("https://example.com")
print(response.read().decode())

# POST request
data = urllib.parse.urlencode({"name": "John", "age": 30})
data = data.encode()
response = urllib.request.urlopen("https://example.com", data=data)

# With headers
req = urllib.request.Request(
    "https://api.example.com",
    method="GET",
    headers={"Authorization": "Bearer token"}
)
response = urllib.request.urlopen(req)
```

#### Requests Library (phổ biến)

```python
import requests

# GET
response = requests.get("https://api.example.com/users")
response.json()  # Parse JSON
response.status_code  # 200
response.headers  # Headers dict

# POST
response = requests.post(
    "https://api.example.com/users",
    json={"name": "John", "email": "john@example.com"}
)

# With headers
headers = {"Authorization": "Bearer token"}
response = requests.get("https://api.example.com", headers=headers)

# Error handling
response.raise_for_status()

# Session
session = requests.Session()
session.headers.update({"Authorization": "Bearer token"})
response = session.get("https://api.example.com")
```

#### aiohttp (Async)

```python
import aiohttp
import asyncio

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.example.com") as response:
            return await response.json()

result = asyncio.run(fetch())
```

---

### 9.2. File I/O

#### Read File

```python
# Read all
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Read line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line, end="")

# Read as list
with open("file.txt", "r") as f:
    lines = f.readlines()

# Read with encoding
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

#### Write File

```python
# Write
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello World")

# Append
with open("log.txt", "a") as f:
    f.write("New log entry\n")

# Multiple lines
lines = ["Line 1\n", "Line 2\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

#### Path (Python 3.4+)

```python
from pathlib import Path

p = Path("file.txt")

# Check existence
p.exists()
p.is_file()
p.is_dir()

# Read/Write
content = p.read_text()
p.write_text("Hello")

# Glob
for file in Path(".").glob("*.py"):
    print(file)

# Resolve path
p.resolve()
```

#### JSON

```python
import json

# Read JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Write JSON
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)

# Parse string
json_str = '{"name": "John", "age": 30}'
data = json.loads(json_str)

# Pretty print
json.dumps(data, indent=2, sort_keys=True)
```

---

### 9.3. Database Access

```python
import sqlite3

# Connection
conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    )
''')

# Prepared statement (parameterized query)
cursor.execute(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    ("John", "john@example.com")
)

# Transaction
try:
    conn.execute("BEGIN")
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Jane", "jane@example.com"))
    conn.commit()
except Exception:
    conn.rollback()
    raise
finally:
    conn.close()

# Connection pool (với SQLAlchemy)
from sqlalchemy import create_engine
engine = create_engine('sqlite:///app.db', pool_size=5, max_overflow=10)
```

### 9.4. CLI I/O

```python
import sys

# Stdin/Stdout
name = input("Enter your name: ")  # Đọc từ stdin
print(f"Hello, {name}", file=sys.stdout)  # Ghi ra stdout
print("Error!", file=sys.stderr)  # Ghi ra stderr

# argparse - Command line parsing
import argparse

parser = argparse.ArgumentParser(description="My CLI tool")
parser.add_argument("-n", "--name", required=True, help="Your name")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("--count", type=int, default=1)
args = parser.parse_args()
print(f"Hello, {args.name}")

# click (thư viện bên thứ 3)
# pip install click
import click

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option('--count', default=1, help='Number of greetings.')
def hello(name, count):
    for _ in range(count):
        click.echo(f"Hello, {name}!")

# ANSI Colors
print("\033[31mRed text\033[0m")
print("\033[32mGreen text\033[0m")
print("\033[1;34mBold blue\033[0m")

# Rich library for fancy terminal output
# pip install rich
from rich.console import Console
console = Console()
console.print("[bold red]Error![/bold red] Something went wrong")
```

---

## 10. Tầng 10: Data & Serialization

### 10.1. JSON & Serialization

#### JSON

```python
import json

# Serialize
data = {"name": "John", "age": 30, "active": True}
json_str = json.dumps(data)
json_str = json.dumps(data, indent=2)

# Deserialize
data = json.loads(json_str)

# Custom encoder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

json.dumps(data, cls=CustomEncoder)
```

#### Pickle

```python
import pickle

# Serialize (Python only, not secure)
data = {"name": "John", "func": lambda x: x * 2}
pickled = pickle.dumps(data)

# Deserialize
unpickled = pickle.loads(pickled)

# File
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    data = pickle.load(f)
```

---

### 10.2. Date & Time

#### datetime

```python
from datetime import datetime, date, time, timedelta

# Current datetime
now = datetime.now()
today = date.today()

# Create datetime
dt = datetime(2024, 1, 15, 10, 30, 0)
d = date(2024, 1, 15)
t = time(10, 30, 0)

# Format
dt.strftime("%Y-%m-%d %H:%M:%S")  # "2024-01-15 10:30:00"
datetime.strptime("2024-01-15", "%Y-%m-%d")

# Arithmetic
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)

# Compare
dt1 = datetime(2024, 1, 1)
dt2 = datetime(2024, 1, 15)
(dt2 - dt1).days  # 14

# Unix timestamp
timestamp = dt.timestamp()
datetime.fromtimestamp(timestamp)
```

#### timezone

```python
from datetime import datetime, timezone
import pytz  # pip install pytz

# UTC
utc = timezone.utc
dt_utc = datetime.now(utc)

# Timezone
tz = pytz.timezone("America/New_York")
dt_ny = datetime.now(tz)

# Convert timezone
dt_utc = dt_ny.astimezone(timezone.utc)
```

#### Timestamp & Calendar

```python
import time
from datetime import datetime
import calendar

# Unix timestamp
timestamp = time.time()  # 1710000000.123
dt = datetime.fromtimestamp(timestamp)
dt.timestamp()  # Ngược lại

# Calendar
cal = calendar.month(2024, 1)  # Xem lịch tháng 1/2024
calendar.isleap(2024)  # True (năm nhuận)
calendar.monthrange(2024, 2)  # (3, 29) - (weekday đầu tháng, số ngày)
```

---

### 10.3. Regular Expression

```python
import re

# Match
text = "My email is john@example.com"
match = re.search(r'[\w.-]+@[\w.-]+', text)
if match:
    print(match.group())  # "john@example.com"
    print(match.span())   # (12, 29)

# Find all
emails = re.findall(r'[\w.-]+@[\w.-]+', text)

# Groups
pattern = r'(?P<user>[\w.-]+)@(?P<domain>[\w.-]+)'
match = re.search(pattern, text)
match.group('user')    # "john"
match.group('domain') # "example.com"

# Replace
re.sub(r'\d+', '#', "test 123")  # "test #"

# Split
re.split(r'\s+', "hello world test")  # ["hello", "world", "test"]

# Compile for reuse
email_pattern = re.compile(r'[\w.-]+@[\w.-]+')
email_pattern.findall(text)
```

### 10.4. XML & CSV Parsing

```python
# XML Parsing
import xml.etree.ElementTree as ET

xml_str = '''<users>
    <user id="1"><name>John</name></user>
    <user id="2"><name>Jane</name></user>
</users>'''

root = ET.fromstring(xml_str)
for user in root.findall('user'):
    uid = user.get('id')
    name = user.find('name').text
    print(f"{uid}: {name}")

# CSV Parsing
import csv

# Read CSV
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])

# Write CSV
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerow({'name': 'John', 'age': 30})
```

---

## 11. Tầng 11: Development Practices

### 11.1. Testing

#### unittest

```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def setUp(self):
        self.data = {"key": "value"}

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
```

#### pytest

```python
# test_math.py

def test_add():
    assert 1 + 1 == 2

def test_list():
    numbers = [1, 2, 3]
    assert len(numbers) == 3
    assert numbers[0] == 1

def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# Fixtures
import pytest

@pytest.fixture
def user():
    return {"name": "John", "age": 30}

def test_user(user):
    assert user["name"] == "John"

# Parametrize
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert input * 2 == expected
```

#### Mocking

```python
from unittest.mock import Mock, patch, MagicMock

# Mock function
mock = Mock(return_value=42)
mock()  # 42

# Mock object
class API:
    def fetch(self):
        return "real data"

api = Mock(spec=API)
api.fetch.return_value = "mocked data"
api.fetch()  # "mocked data"

# Patch
@patch('module.function')
def test_with_patch(mock_func):
    mock_func.return_value = 42
    # ...

# Spy
with patch('module.function', wraps=module.function) as spy:
    module.function()
    spy.assert_called_once()
```

---

### 11.2. Logging

```python
import logging

# Basic config
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

# Logger với handler
logger = logging.getLogger(__name__)
handler = logging.FileHandler('app.log')
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)
```

---

### 11.3. Dependency Injection

```python
# Constructor injection
class UserService:
    def __init__(self, repository):
        self.repository = repository

    def get_user(self, id):
        return self.repository.find(id)

# Usage
class UserRepository:
    def find(self, id):
        return {"id": id, "name": "John"}

service = UserService(UserRepository())

# Interface injection
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, data):
        pass

class FileStorage(Storage):
    def save(self, data):
        with open("data.txt", "w") as f:
            f.write(data)

class UserService:
    def __init__(self, storage: Storage):
        self.storage = storage
```

---

### 11.4. Configuration

#### Environment Variables

```python
import os

# Read
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")

# Set
os.environ["DEBUG"] = "true"

# .env file với python-dotenv
# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()  # Load .env file
```

#### Config File

```python
# config.py
class Config:
    DEBUG = False
    DATABASE_URL = "postgresql://localhost/mydb"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DATABASE_URL = os.getenv("DATABASE_URL")

# config.json
import json
with open("config.json") as f:
    config = json.load(f)
```

---

### 11.5. Build & Package Management

#### pip

```bash
# Install
pip install package
pip install package==1.0.0
pip install "package>=1.0.0"

# Requirements file
pip install -r requirements.txt

# Virtual environment
python -m venv venv
source v  # Linux/Menv/bin/activateac
venv\Scripts\activate     # Windows

# Freeze
pip freeze > requirements.txt
```

#### pyproject.toml / setup.py

```toml
# pyproject.toml (PEP 517/518)
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "1.0.0"
description = "My package"
requires-python = ">=3.8"
dependencies = [
    "requests>=2.28",
]

[project.optional-dependencies]
dev = ["pytest", "black"]

[tool.black]
line-length = 88
```

---

### 11.6. Documentation

#### Docstring

```python
"""Module docstring."""

class MyClass:
    """Class docstring.

    Attributes:
        name: Description of name attribute

    Example:
        >>> obj = MyClass("test")
        >>> obj.name
        'test'
    """

    def method(self, param: str) -> str:
        """Method docstring.

        Args:
            param: Description of param

        Returns:
            Description of return value

        Raises:
            ValueError: When param is invalid
        """
        return param
```

#### Comments

```python
# Single line comment

# Multi-line comment
# can span
# multiple lines
```

---

### 11.8. Design Patterns

```python
# Observer Pattern
class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args):
        for callback in self._listeners.get(event, []):
            callback(*args)

emitter = EventEmitter()
emitter.on("user_created", lambda name: print(f"Welcome {name}!"))
emitter.emit("user_created", "John")  # "Welcome John!"

# Strategy Pattern
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        return sorted(data)  # simplified

class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data)  # simplified

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)

# Repository Pattern
class UserRepository:
    def __init__(self):
        self._users = {}

    def save(self, user):
        self._users[user['id']] = user

    def find_by_id(self, id):
        return self._users.get(id)

    def find_all(self):
        return list(self._users.values())

# Decorator Pattern (Python built-in!)
import functools

def cache(func):
    memo = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## 12. Tầng 12: Advanced Concepts

### 12.1. Advanced Concepts

#### Reflection

```python
# Get object type
type(obj)
isinstance(obj, MyClass)

# Get class attributes
class MyClass:
    class_attr = "value"

    def __init__(self):
        self.instance_attr = 42

# Class attributes
MyClass.__name__        # "MyClass"
MyClass.__dict__        # Class namespace
MyClass.__bases__       # Parent classes

# Instance attributes
obj = MyClass()
obj.__dict__            # Instance namespace

# Get all attributes
dir(obj)                # All attributes and methods
vars(obj)               # Instance __dict__
```

#### Introspection

```python
import inspect

# Get function signature
def func(a: int, b: str = "default") -> bool:
    pass

sig = inspect.signature(func)
# <Signature (a: int, b: str = 'default') -> bool>

for param in sig.parameters:
    print(param.name, sig.parameters[param].default)

# Get source code
source = inspect.getsource(func)

# Check if callable
callable(func)

# Get module
import json
inspect.getfile(json)  # Path to module file
```

#### Decorator

```python
import functools
import time

# Basic decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

# Decorator với arguments
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_api_call():
    pass

# Class decorator
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance
```

#### Meta-programming

```python
# __new__ for customizing object creation
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# __getattr__ for dynamic attributes
class Dynamic:
    def __getattr__(self, name):
        return f"Dynamic: {name}"

obj = Dynamic()
obj.anything  # "Dynamic: anything"

# __slots__
class Optimized:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age
# Uses less memory, faster attribute access

# Descriptors
class Descriptor:
    def __get__(self, obj, objtype=None):
        return obj._value * 2

    def __set__(self, obj, value):
        obj._value = value

class MyClass:
    value = Descriptor()
```

#### Context Manager

```python
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"Elapsed: {self.end - self.start}")
        return False

# Usage
with Timer() as timer:
    time.sleep(1)

# contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Acquiring")
    yield "resource"
    print("Releasing")

with managed_resource() as r:
    print(f"Using {r}")
```

---

## 13. Tầng 13: Memory Layout

### 13.1. Object Layout

#### Python Objects

```python
# Mọi thứ trong Python là object
# Có: type pointer, reference count, và data

# Integer object (PyLongObject)
# - ob_digit[] array cho multi-precision

# List object (PyListObject)
# - ob_item: array of pointers to objects
# - allocated: allocated slots

# String object (PyUnicodeObject)
# - UTF-8 hoặc compact representation

# Kiểm tra memory layout
import sys

x = 1000
sys.getsizeof(x)  # 28 bytes (trên 64-bit)

lst = [1, 2, 3]
sys.getsizeof(lst)  # 88 bytes (chỉ container, không tính elements)

# More detailed với pympler
from pympler import asizeof
asizeof.asizeof(lst)  # Bao gồm cả elements
```

#### Memory Management

```python
# Python Memory Allocator
# Small allocations: < 256 bytes -> Pymalloc
# Large allocations: > 256 bytes -> malloc()

# GC (Garbage Collection)
# 1. Reference counting (immediate)
# 2. Cycle detector (periodic)

# Generations
import gc

gc.get_threshold()  # (700, 10, 10)
# Generation 0: 700 objects threshold
# Check every 10 allocations in gen 1
# Check every 10 allocations in gen 2

# Manual collection
gc.collect()
gc.get_objects()

# Track memory
import tracemalloc
tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()
# ... code ...
snapshot2 = tracemalloc.take_snapshot()

top_stats = snapshot2.compare_to(snapshot1, 'lineno')
for stat in top_stats[:10]:
    print(stat)
```

---

## 14. Tầng 14: Compilation Model

### 14.1. Interpreter & Bytecode

#### CPython Execution

```python
# 1. Tokenization (lexer) -> tokens
# 2. Parsing (parser) -> AST (Abstract Syntax Tree)
# 3. Compilation (compiler) -> bytecode (.pyc)
# 4. Execution (VM) -> runs bytecode

# Compile string to code object
code = compile("print('hello')", "<string>", "exec")
exec(code)

# Compile to AST
import ast
tree = ast.parse("x = 1 + 2")
ast.dump(tree)
```

#### Bytecode

```python
# View bytecode
import dis

def add(a, b):
    return a + b

dis.dis(add)

# Output:
#   ...
#   LOAD_FAST                0 (a)
#   LOAD_FAST                1 (b)
#   BINARY_ADD
#   RETURN_VALUE

# .pyc files (compiled bytecode)
# __pycache__/module.cpython-311.pyc

# force recompile
import py_compile
py_compile.compile('script.py', cfile='script.pyc')
```

#### OPcache (không có trong CPython chuẩn)

```python
# PyPy có JIT compilation
# pip install pypy
# PyPy > CPython for some workloads

# CPython 3.11+ có specialized adaptive interpreter
# Nhưng không có OPcache như PHP
```

---

## 15. Tầng 15: Linking Model

### 15.1. Module Loading

#### Import System

```python
# Import process:
# 1. Find module (sys.path)
# 2. Load module
# 3. Add to sys.modules
# 4. Execute module code

import sys
sys.path  # List of paths searched

# __pycache__ contains compiled .pyc files

# Relative imports
from . import module_name
from ..package import module
```

---

## 16. Tầng 16: Runtime

### 16.1. Stack Frame

#### Call Stack

```python
import traceback
import sys

def level3():
    # Print current stack
    for frame in traceback.extract_stack():
        print(f"{frame.filename}:{frame.lineno} in {frame.name}")

def level2():
    level3()

def level1():
    level2()

level1()

# sys._getframe()
def current_frame():
    frame = sys._getframe()
    return frame.f_code.co_name, frame.f_lineno
```

### 16.2. Garbage Collector

```python
import gc

# Reference counting (automatic)
a = []
b = a
del a
# b still references the list

# Cycle detection
gc.collect()  # Force collection

# Disable GC
gc.disable()
# ... code ...
gc.enable()

# Track uncollectable objects
gc.set_debug(gc.DEBUG_SAVEALL)
gc.collect()
print(gc.garbage)

# Generations
gc.get_threshold()  # (700, 10, 10)
gc.set_threshold(700, 10, 10)
```

---

## 17. Tầng 17: Language Design Patterns

### 17.1. Duck Typing

```python
# "If it walks like a duck and quacks like a duck, it's a duck"

class Duck:
    def speak(self):
        return "Quack!"
```

---

### 17.2. Context Managers

```
class Dog:
def speak(self):
return "Woof!"

def make_speak(obj):
return obj.speak()

# Both work!

make_speak(Duck()) # "Quack!"
make_speak(Dog()) # "Woof!"

# Protocol-based (Python 3.8+)

from typing import Protocol

class Speakable(Protocol):
def speak(self) -> str: ...

class Cat:
def speak(self) -> str:
return "Meow!"

def process(obj: Speakable) -> str:
return obj.speak()

process(Cat()) # Works!
```

## 18. Tầng 18: Standard Library

### 18.1. Collections

```python
# List - dynamic array
lst = [1, 2, 3]
lst.append(4)
lst.pop()

# Deque - efficient append/pop from both ends
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.popleft()

# Dict - hash map
d = {}
d = dict()
d = {"a": 1, "b": 2}

# defaultdict - dict với default value
from collections import defaultdict
dd = defaultdict(list)  # default là list
dd["key"].append(1)  # No error!

# OrderedDict - Python 3.7+ dict is ordered
# For older versions:
from collections import OrderedDict

# Counter - đếm elements
from collections import Counter
cnt = Counter(["a", "b", "a", "c", "a"])
cnt["a"]  # 3

# Set
s = set()
s.add(1)

# frozenset - immutable set
fs = frozenset([1, 2, 3])

# Tuple - immutable sequence
t = (1, 2, 3)

# Named tuple
from collections import namedtuple
("Point", ["Point = namedtuplex", "y"])
p = Point(1, 2)
```

### 18.2. Utilities

#### itertools

```python
import itertools

# Infinite iterators
count(10)       # 10, 11, 12, ...
cycle([1,2,3]) # 1, 2, 3, 1, 2, 3, ...
repeat(5)      # 5, 5, 5, ...

# Combinatoric
product([1,2], [3,4])   # (1,3), (1,4), (2,3), (2,4)
permutations("ABC")    # All orderings
combinations("ABC", 2) # All pairs

# Chain
chain([1,2], [3,4])    # 1, 2, 3, 4
chain.from_iterable([[1,2], [3,4]])  # 1, 2, 3, 4

# Filter/transform
filterfalse(lambda x: x%2, range(10))  # 0, 2, 4, 6, 8
islice(range(10), 0, 10, 2)           # 0, 2, 4, 6, 8
```

#### functools

```python
import functools

# lru_cache - memoization
@functools.lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# partial
from functools import partial
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
square(5)  # 25

# reduce
from functools import reduce
reduce(lambda a, b: a + b, [1, 2, 3, 4])  # 10

# singledispatch - function overloading
@functools.singledispatch
def process(arg):
    print(f"Default: {arg}")

@process.register(int)
def process_int(arg):
    print(f"Integer: {arg}")

@process.register(str)
def process_str(arg):
    print(f"String: {arg}")
```

### 18.3. I/O & System

```python
# File operations
import os
os.path.exists("file.txt")
os.path.isfile("file.txt")
os.path.isdir("folder")
os.listdir(".")
os.walk(".")

# Path (Python 3.4+)
from pathlib import Path
p = Path(".")
list(p.glob("*.py"))

# Environment
import os
os.environ.get("PATH")
os.getcwd()

# Command line
import sys
sys.argv  # [script.py, arg1, arg2]

# argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

# subprocess
import subprocess
subprocess.run(["ls", "-la"])
subprocess.run(["ls"], capture_output=True, text=True)

# Process info
import os, psutil
os.getpid()
psutil.Process().memory_info()
```

---

### 18.6. Math & Numeric

```python
import math
import decimal
import random

# Math functions
math.sqrt(16)      # 4.0
math.pow(2, 10)    # 1024.0
math.abs(-5)       # Lỗi, dùng abs(-5)
math.ceil(3.2)     # 4
math.floor(3.8)    # 3
math.pi            # 3.14159...
math.sin(math.pi/2)  # 1.0
math.log(100, 10)  # 2.0

# BigDecimal - số chính xác
from decimal import Decimal
a = Decimal('0.1') + Decimal('0.2')  # Decimal('0.3') (chính xác!)
0.1 + 0.2  # 0.30000000000000004 (float không chính xác)

# Random
random.random()           # 0.0 - 1.0
random.randint(1, 100)    # 1 - 100
random.choice([1, 2, 3])  # Chọn ngẫu nhiên
random.shuffle([1, 2, 3]) # Xáo trộn in-place
random.sample(range(100), 5)  # Chọn 5 số không trùng
```

### 18.7. Encoding

```python
import base64
import urllib.parse
import codecs

# Base64
encoded = base64.b64encode(b"Hello World")  # b'SGVsbG8gV29ybGQ='
decoded = base64.b64decode(encoded)          # b'Hello World'

# URL Encoding
urllib.parse.quote("hello world")      # "hello%20world"
urllib.parse.unquote("hello%20world")  # "hello world"
urllib.parse.urlencode({"name": "John", "age": 30})  # "name=John&age=30"

# Unicode / UTF-8
text = "你好"
encoded = text.encode('utf-8')    # b'\xe4\xbd\xa0\xe5\xa5\xbd'
decoded = encoded.decode('utf-8') # '你好'

# Hex encoding
data = b"Hello"
hex_str = data.hex()                    # '48656c6c6f'
bytes.fromhex('48656c6c6f')            # b'Hello'
```

---

## 19. Tầng 19: Ecosystem

### 19.1. Web Frameworks

#### Django

```python
# Full-featured framework
# pip install django

# django-admin startproject myproject
# django-admin startapp myapp

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.user_list),
]

# views.py
from django.http import JsonResponse

def user_list(request):
    return JsonResponse({"users": []})

# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = 'users'
```

#### Flask

```python
# Microframework
# pip install flask

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": []})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({"id": 1, **data}), 201

# With database
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
```

#### FastAPI

```python
# Modern async framework
# pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: int | None = None

@app.get("/users")
async def get_users():
    return [{"name": "John"}]

@app.post("/users")
async def create_user(user: User):
    return {"id": 1, **user.dict()}

# Run: uvicorn main:app --reload
```

---

### 19.2. Database & ORM

#### SQLAlchemy

```python
# pip install sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

# Create engine
engine = create_engine('sqlite:///app.db', echo=True)
Base.metadata.create_all(engine)

# Session
Session = sessionmaker(bind=engine)
session = Session()

# CRUD
user = User(name="John", email="john@example.com")
session.add(user)
session.commit()

users = session.query(User).all()
user = session.query(User).filter_by(name="John").first()
session.delete(user)
session.commit()
```

#### Django ORM

```python
# pip install django
# django-admin startproject myproject

# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

# Queries
User.objects.all()
User.objects.filter(name="John")
User.objects.get(id=1)
User.objects.create(name="John", email="john@example.com")

# Related
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

user.post_set.all()
```

---

### 19.3. Testing

#### pytest

```python
# pip install pytest

# test_example.py
def test_simple():
    assert 1 + 1 == 2

def test_list():
    numbers = [1, 2, 3]
    assert len(numbers) == 3

# Fixtures
import pytest

@pytest.fixture
def sample_data():
    return {"name": "test"}

def test_with_fixture(sample_data):
    assert sample_data["name"] == "test"

# Mock
from unittest.mock import Mock, patch

@patch('module.Class')
def test_mock(MockClass):
    MockClass.return_value.method.return_value = "mocked"
    # ...

# Coverage
# pytest --cov=myapp --cov-report=html
```

---

## 20. Tầng 20: Toolchain

### 2.1. Build & Package Management

#### NumPy

```python
# pip install numpy

import numpy as np

# Array
arr = np.array([1, 2, 3, 4, 5])
arr.shape  # (5,)

# Operations
arr * 2        # [2, 4, 6, 8, 10]
arr + arr      # [2, 4, 6, 8, 10]
np.sum(arr)    # 15
np.mean(arr)   # 3.0

# 2D array
matrix = np.array([[1, 2], [3, 4]])
matrix.shape  # (2, 2)
np.dot(matrix, matrix)  # Matrix multiplication

# Slicing
arr[1:3]       # [2, 3]
matrix[0, :]   # First row
```

#### Pandas

```python
# pip install pandas

import pandas as pd

# DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'score': [85, 90, 95]
})

# Operations
df.head()
df.describe()
df['age'].mean()
df[df['age'] > 30]

# I/O
df.to_csv('data.csv')
df = pd.read_csv('data.csv')

# Group by
df.groupby('age').mean()

# Merge
pd.merge(df1, df2, on='id')
```

#### scikit-learn

```python
# pip install scikit-learn

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Prepare data
X, y = [[1], [2], [3], [4], [5]], [2, 4, 6, 8, 10]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
error = mean_squared_error(y_test, predictions)
```

---

## 20. Tầng 20: Toolchain

### 20.2. Build & Package Management

#### pip & venv

```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install
pip install package
pip install -r requirements.txt

# Create package
pip install -e .
```

#### Poetry

```bash
# pip install poetry
poetry new mypackage
poetry add requests
poetry install
poetry build
```

#### pyproject.toml

```toml
[project]
name = "mypackage"
version = "1.0.0"
description = "My package"
requires-python = ">=3.8"
dependencies = []

[project.optional-dependencies]
dev = ["pytest", "black"]

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"

[tool.black]
line-length = 88

[tool.isort]
profile = "black"
```

---

### 20.3. Code Quality

#### Black (Formatter)

```bash
# pip install black
black src/           # Format code
black --check src/   # Check only
black --diff src/    # Show diff
```

#### flake8 (Linter)

```bash
# pip install flake8
flake8 src/          # Check
flake8 --max-line-length=88 src/
```

#### mypy (Type Checker)

```bash
# pip install mypy
mypy src/           # Type check
mypy --strict src/  # Strict mode
```

#### pre-commit

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
```

---

### 20.4. IDE & Debugging

#### VS Code

```json
// .vscode/settings.json
{
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.testing.pytestEnabled": true,
  "python.analysis.typeCheckingMode": "basic"
}
```

#### Debugging

```python
# Print debugging
print("Debug:", variable)

# assert
assert condition, "Debug message"

# pdb - Python debugger
import pdb
pdb.set_trace()

# ipdb - Enhanced debugger
# pip install ipdb
import ipdb; ipdb.set_trace()

# breakpoint() (Python 3.7+)
breakpoint()

# VS Code / PyCharm debugging
# Set breakpoints in IDE
```

---

## Tổng Kết

Python là ngôn ngữ:

- **Dynamic typing** với optional type annotations (Python 3.5+)
- **Strong typing** với duck typing
- **Multi-paradigm**: Functional, OOP, Procedural
- **Rich ecosystem**: Data Science (NumPy, Pandas), Web (Django, Flask), ML (TensorFlow, PyTorch)
- **Modern features**: Type hints (3.5+), Pattern matching (3.10+), Structural pattern matching (3.10+)

### Python Version History

| Version     | Release Date | Key Features                                           |
| ----------- | ------------ | ------------------------------------------------------ |
| Python 3.0  | 2009-12-03   | Print function, kwargs                                 |
| Python 3.5  | 2015-09-13   | Type hints, async/await                                |
| Python 3.7  | 2018-06-27   | dataclasses, breakpoint()                              |
| Python 3.8  | 2019-10-14   | Assignment expressions, positional-only params         |
| Python 3.9  | 2020-10-05   | Pattern matching (preview), built-in types as generics |
| Python 3.10 | 2021-10-04   | Structural pattern matching, match expression          |
| Python 3.11 | 2022-10-03   | Better error messages, faster execution                |
| Python 3.12 | 2023-10-02   | Better performance, improved typing                    |
| Python 3.13 | 2024-10-07   | Free-threaded CPython (experimental)                   |
