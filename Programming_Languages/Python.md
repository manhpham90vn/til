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
   - [2.8 Union & Intersection Types](#28-union--intersection-types)
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
   - [6.2 Reactive Programming](#62-reactive-programming)
7. [Tầng 7: Error Handling](#tầng-7-error-handling)
   - [7.1 Xử Lý Lỗi](#71-xử-lý-lỗi)
   - [7.2 Error Types](#72-error-types)
8. [Tầng 8: Module & Organization](#tầng-8-module--organization)
   - [8.1 Import/Module](#81-importmodule)
   - [8.2 Extension Methods](#82-extension-methods)
   - [8.3 Operator Overloading](#83-operator-overloading)
   - [8.4 Circular Dependency](#84-circular-dependency)
9. [Tầng 9: I/O & Networking](#tầng-9-io--networking)
   - [9.1 HTTP & Networking](#91-http--networking)
   - [9.2 File I/O](#92-file-io)
   - [9.3 Database Access](#93-database-access)
   - [9.4 CLI I/O](#94-cli-io)
10. [Tầng 10: Data & Serialization](#tầng-10-data--serialization)
    - [10.1 JSON & Serialization](#101-json--serialization)
    - [10.2 Date & Time](#102-date--time)
    - [10.3 Regular Expression](#103-regular-expression)
    - [10.4 XML & CSV Parsing](#104-xml--csv-parsing)
    - [10.5 YAML/TOML](#105-yamltoml)
    - [10.6 Binary Serialization](#106-binary-serialization-struct)
11. [Tầng 11: Development Practices](#tầng-11-development-practices)
    - [11.1 Testing](#111-testing)
    - [11.2 Logging](#112-logging)
    - [11.3 Dependency Injection](#113-dependency-injection)
    - [11.4 Configuration](#114-configuration)
    - [11.5 Build & Package Management](#115-build--package-management)
    - [11.6 Documentation](#116-documentation)
    - [11.8 Design Patterns](#118-design-patterns)
12. [Tầng 12: Advanced Concepts](#tầng-12-advanced-concepts)
    - [12.1 Advanced Concepts](#121-advanced-concepts)
13. [Tầng 13: Memory Layout](#tầng-13-memory-layout)
    - [13.1 Object Layout](#131-object-layout)
14. [Tầng 14: Compilation Model](#tầng-14-compilation-model)
    - [14.1 Interpreter & Bytecode](#141-interpreter--bytecode)
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
    - [18.6 Math & Numeric](#186-math--numeric)
    - [18.7 Encoding](#187-encoding)
19. [Tầng 19: Ecosystem](#tầng-19-ecosystem)
    - [19.1 Web Frameworks](#191-web-frameworks)
    - [19.2 Database & ORM](#192-database--orm)
    - [19.3 Testing](#193-testing)
    - [19.4 Data Science & ML](#194-data-science--ml)
    - [19.5 Security & Cryptography](#195-security--cryptography)
    - [19.6 DevOps & Infrastructure](#196-devops--infrastructure)
20. [Tầng 20: Toolchain](#tầng-20-toolchain)
    - [20.1 Build & Package Management](#201-build--package-management)
    - [20.2 Code Quality](#202-code-quality)
    - [20.3 IDE & Debugging](#203-ide--debugging)
    - [20.4 Profiling & Performance](#204-profiling--performance)
    - [20.5 Documentation & Publishing](#205-documentation--publishing)
    - [20.6 Runtime & Environment](#206-runtime--environment)

---

## 0. Phân Loại Ngôn Ngữ

### Chạy File Python

```bash
# === Chạy trực tiếp ===
python script.py          # Chạy với python mặc định trong PATH
python3 script.py         # Chỉ định dùng Python 3 (tránh nhầm Python 2)
python3.11 script.py      # Chỉ định phiên bản cụ thể 3.11

# === Interactive mode (REPL) ===
python -i                 # Mở Python shell tương tác, gõ code trực tiếp
python -i script.py       # Chạy script rồi mở shell (giữ lại biến để debug)

# === Chạy module như script ===
python -m module_name     # Chạy module có __main__.py
python -m http.server 8080  # Ví dụ: mở web server tĩnh trên port 8080
python -m venv myenv      # Tạo virtual environment
python -m pytest          # Chạy pytest thông qua module
python -m pip install requests  # Cài package qua module pip

# === Một số flag hữu ích ===
python -c "print('Hello')"    # Chạy 1 dòng code trực tiếp từ terminal
python -O script.py           # Optimized mode: bỏ assert, __debug__ = False
python -B script.py           # Không tạo file .pyc (bytecode cache)
python -u script.py           # Unbuffered output (hữu ích khi pipe/redirect)
python -W all script.py       # Hiện tất cả warnings

# === Shebang line (Linux/Mac) ===
# Thêm dòng đầu file .py để chạy trực tiếp: ./script.py
#!/usr/bin/env python3        # Tìm python3 trong PATH (khuyến khích)
#!/usr/bin/python3            # Đường dẫn tuyệt đối (ít linh hoạt hơn)

# === Kiểm tra phiên bản ===
python --version              # Output: Python 3.11.x
python -c "import sys; print(sys.version_info)"
# Output: sys.version_info(major=3, minor=11, micro=0, releaselevel='final', serial=0)
```

### Đặc điểm Python

```text
┌──────────────────┬──────────────────────────────────────────────────────┐
│ Đặc điểm         │ Mô tả                                               │
├──────────────────┼──────────────────────────────────────────────────────┤
│ Typing           │ Dynamic + Strong typing                             │
│                  │ - Dynamic: không cần khai báo kiểu, kiểu xác định   │
│                  │   tại runtime. x = 10 → x là int, x = "hi" → x là str│
│                  │ - Strong: không tự ép kiểu ngầm.                    │
│                  │   "10" + 5 → TypeError (khác JS sẽ ra "105")        │
├──────────────────┼──────────────────────────────────────────────────────┤
│ Paradigm         │ Multi-paradigm:                                     │
│                  │ - OOP: class, inheritance, polymorphism              │
│                  │ - Functional: lambda, map, filter, reduce           │
│                  │ - Procedural: top-down scripting                    │
│                  │ - Metaprogramming: decorators, metaclasses          │
├──────────────────┼──────────────────────────────────────────────────────┤
│ Execution        │ Interpreted + Bytecode compilation:                 │
│                  │ - Source (.py) → Bytecode (.pyc) → CPython VM       │
│                  │ - Có JIT với PyPy (nhanh hơn CPython 2-10x)         │
│                  │ - Python 3.13: Free-threaded mode (thử nghiệm)      │
├──────────────────┼──────────────────────────────────────────────────────┤
│ Memory           │ Automatic (Garbage Collection):                     │
│                  │ - Reference counting + Cycle detector               │
│                  │ - Mọi thứ là object, sống trên heap                 │
├──────────────────┼──────────────────────────────────────────────────────┤
│ Concurrency      │ GIL (Global Interpreter Lock):                      │
│                  │ - 1 thread chạy Python bytecode tại 1 thời điểm     │
│                  │ - Tốt cho I/O-bound (asyncio, threading)            │
│                  │ - Dùng multiprocessing cho CPU-bound                │
├──────────────────┼──────────────────────────────────────────────────────┤
│ Use Cases        │ - Data Science: NumPy, Pandas, Matplotlib           │
│                  │ - ML/AI: TensorFlow, PyTorch, scikit-learn          │
│                  │ - Web: Django, Flask, FastAPI                       │
│                  │ - Automation/Scripting: DevOps, CLI tools            │
│                  │ - Desktop: Tkinter, PyQt, Kivy                      │
└──────────────────┴──────────────────────────────────────────────────────┘
```

```python
# === Ví dụ minh họa Dynamic + Strong Typing ===

# Dynamic: biến có thể đổi kiểu tự do
x = 10           # x là int
x = "hello"      # x giờ là str - không lỗi (dynamic)
x = [1, 2, 3]    # x giờ là list - vẫn ok

# Strong: Python KHÔNG tự ép kiểu ngầm
# "10" + 5        # ❌ TypeError: can only concatenate str to str
"10" + str(5)     # ✅ "105" - phải ép kiểu tường minh
int("10") + 5     # ✅ 15 - ép string thành int trước

# So sánh với JavaScript (weak typing):
# JS: "10" + 5 → "105"     (tự ép 5 thành "5")
# JS: "10" - 5 → 5         (tự ép "10" thành 10)
# Python: KHÔNG cho phép - phải tường minh
```

---

## 1. Tầng 1: Syntax & Semantics

### 1.1. Khai Báo Biến (Variable Declaration)

#### Mutable - Biến thường

```python
# === Khai báo biến cơ bản (dynamic typing) ===
# Python không cần từ khóa let/var/const, gán trực tiếp
x = 10                    # int - số nguyên
name = "Python"           # str - chuỗi ký tự
is_active = True          # bool - giá trị boolean
prices = [1.5, 2.0, 3.5]  # list - danh sách (mutable)
coords = (10, 20)         # tuple - bộ giá trị (immutable)
tags = {"python", "code"} # set - tập hợp không trùng lặp
user = {"name": "John"}   # dict - từ điển key-value

# === Type annotation (Python 3.5+) ===
# Chỉ là gợi ý cho IDE/type checker, KHÔNG enforce tại runtime
x: int = 10               # Gợi ý x là int
name: str = "Python"       # Gợi ý name là str
is_active: bool = True     # Gợi ý is_active là bool
prices: list[float] = [1.5, 2.0]  # Python 3.9+ syntax

# ⚠️ Lưu ý: annotation KHÔNG ngăn gán sai kiểu tại runtime
x: int = 10
x = "hello"  # KHÔNG lỗi runtime! Chỉ mypy/IDE cảnh báo
print(x)     # Output: hello
print(type(x))  # Output: <class 'str'>

# === Multiple assignment (gán nhiều biến cùng lúc) ===
a, b, c = 1, 2, 3         # a=1, b=2, c=3 (tuple unpacking ngầm)
x = y = z = 0             # Cả 3 biến cùng trỏ đến object 0
print(a, b, c)             # Output: 1 2 3
print(x, y, z)             # Output: 0 0 0

# ⚠️ Edge case: multiple assignment với mutable object
a = b = []      # a và b cùng trỏ đến 1 list!
a.append(1)     # Thay đổi list
print(b)        # Output: [1] ← b cũng bị ảnh hưởng!
# Giải pháp: tạo list riêng
a, b = [], []   # 2 list khác nhau
a.append(1)
print(b)        # Output: [] ← b không bị ảnh hưởng

# === Augmented assignment (gán kết hợp) ===
count = 0
count += 1    # count = count + 1 → 1
count -= 1    # count = count - 1 → 0
count *= 5    # count = count * 5 → 0
count //= 2   # count = count // 2 (chia lấy phần nguyên)
count **= 3   # count = count ** 3 (lũy thừa)
```

#### Immutable - Hằng số

```python
# === Python KHÔNG có const/final keyword ===
# Quy ước: viết HOA toàn bộ để đánh dấu constant
MAX_SIZE = 100              # Hằng số cấu hình
PI = 3.14159                # Hằng số toán học
BASE_URL = "https://api.example.com"  # URL không đổi
DEFAULT_TIMEOUT = 30        # Timeout mặc định (giây)

# ⚠️ Lưu ý: đây chỉ là QUY ƯỚC, Python vẫn cho phép gán lại
MAX_SIZE = 200  # KHÔNG lỗi! Nhưng vi phạm convention

# === Dùng tuple cho immutable data ===
COORDS = (10, 20)           # Tuple - không thể thay đổi phần tử
# COORDS[0] = 5            # ❌ TypeError: 'tuple' does not support item assignment

RGB_RED = (255, 0, 0)       # Màu đỏ - không nên thay đổi
ALLOWED_METHODS = ("GET", "POST", "PUT", "DELETE")

# === Dùng frozenset cho tập hợp immutable ===
VALID_STATUS = frozenset({"active", "inactive", "pending"})
# VALID_STATUS.add("banned")  # ❌ AttributeError: 'frozenset' has no 'add'

# === Real-world: dùng Enum cho hằng số có cấu trúc (xem section 2.2) ===
# === Real-world: dùng Final từ typing (Python 3.8+) ===
from typing import Final
MAX_RETRIES: Final = 3      # Type checker sẽ cảnh báo nếu gán lại
# MAX_RETRIES = 5           # ❌ mypy error (nhưng runtime vẫn ok)
```

#### Type Inference

```python
# === Python tự suy luận kiểu dựa trên giá trị gán ===
x = 10              # int - suy luận từ literal số nguyên
y = 3.14            # float - suy luận từ literal số thực
z = "hello"         # str - suy luận từ literal chuỗi
w = True            # bool - suy luận từ literal boolean
n = None            # NoneType - giá trị null

# === Kiểm tra kiểu tại runtime ===
print(type(x))             # Output: <class 'int'>
print(type(y))             # Output: <class 'float'>
print(type(z))             # Output: <class 'str'>

# isinstance() - kiểm tra có phải kiểu đó không (bao gồm kế thừa)
print(isinstance(x, int))       # Output: True
print(isinstance(x, (int, float)))  # Output: True (kiểm tra nhiều kiểu)
print(isinstance(True, int))    # Output: True ← bool kế thừa từ int!

# ⚠️ type() vs isinstance():
# type() chỉ kiểm tra kiểu chính xác, không xét kế thừa
# isinstance() xét cả kế thừa (khuyến khích dùng hơn)
class Animal: pass
class Dog(Animal): pass
dog = Dog()
print(type(dog) == Animal)       # Output: False (Dog ≠ Animal)
print(isinstance(dog, Animal))   # Output: True  (Dog kế thừa Animal)

# === Chuyển đổi kiểu tường minh (type casting) ===
int("42")       # str → int: 42
float("3.14")   # str → float: 3.14
str(42)         # int → str: "42"
bool(0)         # int → bool: False
bool(1)         # int → bool: True
list("abc")     # str → list: ['a', 'b', 'c']
tuple([1,2,3])  # list → tuple: (1, 2, 3)
set([1,1,2])    # list → set: {1, 2}

# ⚠️ Edge case: chuyển đổi thất bại
# int("abc")    # ❌ ValueError: invalid literal for int()
# int("3.14")   # ❌ ValueError: phải dùng float() trước
int(float("3.14"))  # ✅ 3 (float → int cắt phần thập phân)
```

#### Global Variable

```python
# === Biến toàn cục (global variable) ===
# Khai báo ngoài mọi function → có thể đọc từ bất kỳ đâu
global_var = "I am global"

def access_global():
    # ĐỌC biến global → không cần từ khóa 'global'
    print(global_var)  # Output: I am global

def modify_global():
    # GHI biến global → BẮT BUỘC dùng từ khóa 'global'
    global global_var           # Khai báo sẽ dùng biến global
    global_var = "Modified"     # Thay đổi giá trị biến global

def without_global_keyword():
    # Không dùng 'global' → Python tạo biến LOCAL mới
    global_var = "Local only"   # Đây là biến local, không ảnh hưởng global
    print(global_var)           # Output: Local only

# Thứ tự gọi:
access_global()               # Output: I am global
modify_global()               # Thay đổi global_var thành "Modified"
access_global()               # Output: Modified
without_global_keyword()      # Output: Local only (biến local)
access_global()               # Output: Modified (global không bị thay đổi)

# ⚠️ Lưu ý: hạn chế dùng global variable
# - Khó debug, khó test, khó theo dõi ai thay đổi
# - Thay thế bằng: class attribute, function parameter, module-level constant
```

#### Static Variable (Class-level)

```python
# === Biến class (class variable / static variable) ===
# Chia sẻ giữa TẤT CẢ instances của class
class Counter:
    count = 0  # Biến class - thuộc về class, không thuộc instance

    def __init__(self):
        Counter.count += 1  # Truy cập qua TÊN CLASS, không qua self

    def __del__(self):
        Counter.count -= 1  # Giảm khi object bị xóa

print(Counter.count)  # Output: 0 (chưa tạo instance nào)

c1 = Counter()
print(Counter.count)  # Output: 1

c2 = Counter()
print(Counter.count)  # Output: 2

c3 = Counter()
print(Counter.count)  # Output: 3

del c3
print(Counter.count)  # Output: 2 (c3 bị xóa)

# ⚠️ Edge case: gán qua instance tạo biến instance MỚI, không thay đổi class variable
class Config:
    debug = False  # Class variable

cfg1 = Config()
cfg2 = Config()
cfg1.debug = True        # Tạo biến INSTANCE cho cfg1, KHÔNG thay đổi class variable!
print(cfg1.debug)        # Output: True  (instance variable)
print(cfg2.debug)        # Output: False (vẫn đọc class variable)
print(Config.debug)      # Output: False (class variable không đổi)

# Để thay đổi class variable → dùng tên class
Config.debug = True
print(cfg2.debug)        # Output: True (giờ mới thay đổi cho tất cả)
```

#### Scope & Shadowing

```python
# === Python có LEGB rule ===
# L - Local:     biến trong hàm hiện tại
# E - Enclosing: biến trong hàm bao ngoài (closure)
# G - Global:    biến cấp module (file)
# B - Built-in:  biến/hàm có sẵn (print, len, type...)

x = "global"        # (G) Global scope

def outer():
    x = "enclosing"  # (E) Enclosing scope - shadow biến global x

    def inner():
        x = "local"  # (L) Local scope - shadow biến enclosing x
        print(x)     # Output: local (tìm L trước → thấy)

    inner()
    print(x)  # Output: enclosing (L của inner không ảnh hưởng)

outer()
print(x)      # Output: global (E và L không ảnh hưởng)

# === nonlocal - thay đổi biến enclosing ===
def counter():
    count = 0              # Biến enclosing

    def increment():
        nonlocal count     # Khai báo dùng biến từ enclosing scope
        count += 1         # Thay đổi biến enclosing
        return count

    return increment

c = counter()
print(c())  # Output: 1
print(c())  # Output: 2
print(c())  # Output: 3

# ⚠️ Không có nonlocal → UnboundLocalError
def bad_counter():
    count = 0
    def increment():
        # count += 1       # ❌ UnboundLocalError: 'count' referenced before assignment
        # Python thấy count ở vế trái → coi là local → chưa gán → lỗi
        pass
    return increment

# === Built-in scope (B) ===
# print, len, type, int, str... là built-in
# ⚠️ Có thể shadow built-in (KHÔNG nên làm)
# list = [1, 2, 3]  # Shadow built-in list()!
# list("abc")        # ❌ TypeError: 'list' object is not callable
# Giải pháp: đặt tên khác
my_list = [1, 2, 3]  # ✅ Không shadow built-in

# === Real-world: dùng closure làm factory function ===
def make_logger(prefix):
    """Tạo hàm log với prefix cố định"""
    def log(message):
        print(f"[{prefix}] {message}")
    return log

info = make_logger("INFO")
error = make_logger("ERROR")
info("Server started")    # Output: [INFO] Server started
error("Connection lost")  # Output: [ERROR] Connection lost
```

---

### 1.2. Khai Báo Hàm (Function Declaration)

#### Function cơ bản

```python
# === Function không có return (trả về None ngầm) ===
def greet():
    print("Hello!")          # Chỉ in ra, không trả về gì

result = greet()             # Output: Hello!
print(result)                # Output: None (function không return → trả về None)

# === Function có return ===
def add(a, b):
    return a + b             # Trả về tổng a + b

print(add(3, 5))             # Output: 8
print(add("Hello", " World"))  # Output: Hello World (+ cũng nối string)

# === Function với type hints (Python 3.5+) ===
# Type hints giúp IDE hiểu code, KHÔNG enforce tại runtime
def greet(name: str) -> str:
    """Trả về lời chào với tên được truyền vào."""
    return f"Hello, {name}!"

print(greet("Python"))       # Output: Hello, Python!
print(greet(42))             # Output: Hello, 42! (runtime vẫn chạy, mypy sẽ cảnh báo)

# === Docstring (Google style) ===
def calculate_area(width: float, height: float) -> float:
    """Tính diện tích hình chữ nhật.

    Args:
        width: Chiều rộng hình chữ nhật (phải > 0).
        height: Chiều cao hình chữ nhật (phải > 0).

    Returns:
        Diện tích hình chữ nhật (width × height).

    Raises:
        ValueError: Khi width hoặc height <= 0.

    Example:
        >>> calculate_area(5, 3)
        15.0
        >>> calculate_area(0, 5)
        ValueError: Dimensions must be positive
    """
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    return width * height

print(calculate_area(5, 3))  # Output: 15

# === Multiple return values (trả về tuple ngầm) ===
def divide(a, b):
    """Trả về thương và phần dư."""
    quotient = a // b        # Phần nguyên
    remainder = a % b        # Phần dư
    return quotient, remainder  # Trả về tuple (quotient, remainder)

q, r = divide(17, 5)        # Tuple unpacking
print(f"17 ÷ 5 = {q} dư {r}")  # Output: 17 ÷ 5 = 3 dư 2

# === Early return pattern ===
def find_user(user_id: int) -> dict | None:
    """Tìm user theo ID, trả về None nếu không tìm thấy."""
    if user_id <= 0:
        return None          # Early return - thoát sớm nếu ID không hợp lệ
    # ... logic tìm kiếm ...
    return {"id": user_id, "name": "John"}
```

#### Parameters

```python
# === Default parameters (tham số mặc định) ===
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("John"))              # Output: Hello, John!
print(greet("John", "Hi"))        # Output: Hi, John!
print(greet("John", greeting="Xin chào"))  # Output: Xin chào, John!

# ⚠️ TRAP: Mutable default argument
# KHÔNG BAO GIỜ dùng list/dict/set làm giá trị mặc định!
def bad_append(item, lst=[]):     # ❌ list mặc định được tạo 1 lần duy nhất
    lst.append(item)
    return lst

print(bad_append(1))              # Output: [1]
print(bad_append(2))              # Output: [1, 2] ← KHÔNG phải [2]! lst bị chia sẻ!
print(bad_append(3))              # Output: [1, 2, 3] ← Tích lũy!

# ✅ Giải pháp: dùng None làm sentinel
def good_append(item, lst=None):
    if lst is None:               # Kiểm tra None
        lst = []                  # Tạo list MỚI mỗi lần gọi
    lst.append(item)
    return lst

print(good_append(1))             # Output: [1]
print(good_append(2))             # Output: [2] ← Đúng!

# === Positional và Keyword arguments ===
def create_user(name, email, age):
    return {"name": name, "email": email, "age": age}

# Gọi theo vị trí (positional)
user1 = create_user("John", "john@example.com", 25)

# Gọi theo tên (keyword) - thứ tự tùy ý
user2 = create_user(age=25, name="John", email="john@example.com")

# Mix (positional phải đứng trước keyword)
user3 = create_user("John", age=25, email="john@example.com")
# create_user(name="John", "john@example.com", 25)  # ❌ SyntaxError

# === Keyword-only arguments (Python 3.0+) ===
# Tham số sau * BẮT BUỘC phải truyền bằng tên
def connect(host, port, *, timeout=30, retries=3):
    print(f"Connecting to {host}:{port} (timeout={timeout}s, retries={retries})")

connect("localhost", 8080)                     # Output: Connecting to localhost:8080 (timeout=30s, retries=3)
connect("localhost", 8080, timeout=60)         # Output: Connecting to localhost:8080 (timeout=60s, retries=3)
# connect("localhost", 8080, 60)              # ❌ TypeError: takes 2 positional arguments

# === Positional-only arguments (Python 3.8+) ===
# Tham số trước / BẮT BUỘC phải truyền theo vị trí
def power(base, exp, /):
    return base ** exp

print(power(2, 10))        # Output: 1024
# power(base=2, exp=10)    # ❌ TypeError: positional-only argument

# === *args và **kwargs ===
def func(*args, **kwargs):
    print(f"args = {args}")      # args là tuple chứa positional arguments
    print(f"kwargs = {kwargs}")  # kwargs là dict chứa keyword arguments

func(1, 2, 3, name="John", age=25)
# Output: args = (1, 2, 3)
# Output: kwargs = {'name': 'John', 'age': 25}

# Real-world: wrapper function
def log_call(func):
    """Decorator ghi log khi gọi function."""
    def wrapper(*args, **kwargs):   # Nhận mọi loại argument
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)  # Forward tất cả cho function gốc
    return wrapper
```

#### Variadic Parameters

```python
# === *args - nhận số lượng positional arguments không giới hạn ===
def sum_all(*numbers):
    """Tính tổng tất cả các số truyền vào."""
    print(f"Received: {numbers}")  # numbers là tuple
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))     # Output: Received: (1, 2, 3, 4, 5) → 15
print(sum_all())                    # Output: Received: () → 0 (tuple rỗng → sum = 0)
print(sum_all(10))                  # Output: Received: (10,) → 10

# === **kwargs - nhận số lượng keyword arguments không giới hạn ===
def print_info(**info):
    """In thông tin từ keyword arguments."""
    for key, value in info.items():
        print(f"  {key}: {value}")

print_info(name="John", age=25, city="HCM")
# Output:
#   name: John
#   age: 25
#   city: HCM

# === Kết hợp tất cả loại parameters ===
def complex_func(required, *args, default="value", **kwargs):
    """
    required: bắt buộc
    *args:    positional arguments thừa
    default:  keyword argument có giá trị mặc định
    **kwargs: keyword arguments thừa
    """
    print(f"required={required}")
    print(f"args={args}")
    print(f"default={default}")
    print(f"kwargs={kwargs}")

complex_func("hello", 1, 2, default="custom", extra="data")
# Output:
#   required=hello
#   args=(1, 2)
#   default=custom
#   kwargs={'extra': 'data'}

# === Unpacking arguments khi gọi function ===
def greet(name, age, city):
    print(f"{name}, {age} tuổi, sống ở {city}")

# Unpack list/tuple với *
args = ["John", 25, "HCM"]
greet(*args)                  # Output: John, 25 tuổi, sống ở HCM

# Unpack dict với **
kwargs = {"name": "John", "age": 25, "city": "HCM"}
greet(**kwargs)               # Output: John, 25 tuổi, sống ở HCM
```

#### Lambda/Arrow Function

```python
# === Lambda (anonymous function - hàm ẩn danh) ===
# Cú pháp: lambda tham_số: biểu_thức
# Chỉ chứa 1 biểu thức duy nhất, tự return kết quả
square = lambda x: x ** 2           # Bình phương
add = lambda a, b: a + b            # Cộng 2 số
identity = lambda x: x              # Trả về chính nó
always_true = lambda: True          # Không có tham số

print(square(5))                     # Output: 25
print(add(3, 4))                     # Output: 7

# === Dùng lambda với higher-order functions ===
numbers = [1, 2, 3, 4, 5]

# map() - áp dụng function cho mỗi phần tử
squared = list(map(lambda x: x ** 2, numbers))
print(squared)                       # Output: [1, 4, 9, 16, 25]

# filter() - lọc phần tử thỏa điều kiện
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)                         # Output: [2, 4]

# sorted() - sắp xếp với custom key
words = ["banana", "apple", "cherry", "date"]
sorted_by_len = sorted(words, key=lambda w: len(w))
print(sorted_by_len)                 # Output: ['date', 'apple', 'banana', 'cherry']

# === Lambda với conditional (ternary) ===
max_val = lambda a, b: a if a > b else b
print(max_val(10, 20))               # Output: 20

classify = lambda x: "even" if x % 2 == 0 else "odd"
print(classify(7))                   # Output: odd

# ⚠️ Khi nào KHÔNG nên dùng lambda:
# - Logic phức tạp → dùng def
# - Cần nhiều dòng code → dùng def
# - Cần docstring → dùng def
# - Gán lambda cho biến → dùng def (PEP 8)

# ❌ Không nên
double = lambda x: x * 2

# ✅ Nên
def double(x):
    return x * 2
```

#### Closure

```python
# === Closure - function "nhớ" biến từ scope bên ngoài ===
# Khi inner function tham chiếu biến của outer function,
# biến đó được "capture" và tồn tại sau khi outer function kết thúc

def outer(x):
    # x là biến enclosing - sẽ được capture bởi inner
    def inner(y):
        return x + y      # Closure: inner "nhớ" giá trị x
    return inner          # Trả về function inner (chưa gọi)

# Tạo các closure khác nhau
add_10 = outer(10)        # x = 10 được capture
add_100 = outer(100)      # x = 100 được capture

print(add_10(5))          # Output: 15 (10 + 5)
print(add_10(20))         # Output: 30 (10 + 20)
print(add_100(5))         # Output: 105 (100 + 5)

# === Real-world: closure làm counter ===
def make_counter(start=0):
    count = start
    def counter():
        nonlocal count    # Cần nonlocal để thay đổi biến enclosing
        count += 1
        return count
    return counter

counter = make_counter()
print(counter())          # Output: 1
print(counter())          # Output: 2

# === Real-world: closure làm rate limiter đơn giản ===
import time
def make_rate_limiter(min_interval=1.0):
    """Tạo function giới hạn tần suất gọi."""
    last_call = [0]       # Dùng list để tránh nonlocal (trick cũ)
    def limiter():
        elapsed = time.time() - last_call[0]
        if elapsed < min_interval:
            print(f"Rate limited! Wait {min_interval - elapsed:.1f}s")
            return False
        last_call[0] = time.time()
        return True
    return limiter

# ⚠️ Edge case: closure và loop
# Closure capture BIẾN, không capture GIÁ TRỊ tại thời điểm tạo
funcs = []
for i in range(3):
    funcs.append(lambda: i)  # Tất cả lambda cùng tham chiếu biến i

print([f() for f in funcs])   # Output: [2, 2, 2] ← KHÔNG phải [0, 1, 2]!
# Vì khi gọi, i = 2 (giá trị cuối cùng sau vòng lặp)

# ✅ Giải pháp: dùng default argument để capture giá trị
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)  # i=i capture giá trị tại thời điểm tạo

print([f() for f in funcs])   # Output: [0, 1, 2] ← Đúng!
```

#### Higher-Order Function

```python
# === Higher-Order Function (HOF) ===
# Function nhận function khác làm tham số HOẶC trả về function

# --- Nhận function làm tham số ---
def apply_twice(func, x):
    """Áp dụng function 2 lần liên tiếp."""
    return func(func(x))     # func(func(x))

def add_five(x):
    return x + 5

result = apply_twice(add_five, 10)  # add_five(add_five(10)) = add_five(15) = 20
print(result)                        # Output: 20

# --- Trả về function ---
def multiplier(factor):
    """Factory: tạo function nhân với factor."""
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)               # Tạo function nhân 2
triple = multiplier(3)               # Tạo function nhân 3

print(double(5))                     # Output: 10
print(triple(5))                     # Output: 15

# === Real-world: retry logic ===
import time

def with_retry(func, max_retries=3, delay=1):
    """Wrap function với retry logic."""
    def wrapper(*args, **kwargs):
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(delay)
        raise Exception(f"All {max_retries} attempts failed")
    return wrapper

# === Built-in HOFs phổ biến ===
numbers = [1, 2, 3, 4, 5]

# map - biến đổi mỗi phần tử
print(list(map(str, numbers)))        # Output: ['1', '2', '3', '4', '5']

# filter - lọc phần tử
print(list(filter(lambda x: x > 3, numbers)))  # Output: [4, 5]

# sorted - sắp xếp với key function
users = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
sorted_users = sorted(users, key=lambda u: u["age"])
print(sorted_users[0]["name"])        # Output: Alice

# min/max với key
print(min(users, key=lambda u: u["age"])["name"])  # Output: Alice
print(max(users, key=lambda u: u["age"])["name"])  # Output: Bob
```

#### Method trong Class

```python
# === 3 loại method trong class ===

class Calculator:
    precision = 2  # Class variable

    def __init__(self, name="Basic"):
        self.name = name                     # Instance variable

    # --- Instance method ---
    # Tham số đầu tiên là self (instance hiện tại)
    def multiply(self, a, b):
        result = round(a * b, self.precision)  # Truy cập instance qua self
        print(f"[{self.name}] {a} × {b} = {result}")
        return result

    # --- Class method ---
    # Tham số đầu tiên là cls (class hiện tại)
    # Dùng cho factory method, thao tác class variable
    @classmethod
    def set_precision(cls, precision):
        cls.precision = precision             # Thay đổi class variable

    @classmethod
    def create_scientific(cls):
        """Factory method tạo calculator khoa học."""
        calc = cls("Scientific")              # cls() = Calculator()
        calc.precision = 10
        return calc

    # --- Static method ---
    # KHÔNG nhận self hay cls, không truy cập instance/class
    # Chỉ là function tiện ích đặt trong class cho gọn
    @staticmethod
    def add(a, b):
        return a + b

# Sử dụng:
calc = Calculator("MyCalc")
calc.multiply(3, 4)                          # Output: [MyCalc] 3 × 4 = 12

Calculator.set_precision(4)                  # Thay đổi precision cho TẤT CẢ instance
print(Calculator.add(10, 20))                # Output: 30 (không cần instance)

sci = Calculator.create_scientific()         # Factory method
sci.multiply(1, 3)                           # Output: [Scientific] 1 × 3 = 3
```

#### Constructor & Destructor

```python
# === __init__ (Constructor) và __del__ (Destructor) ===

class Resource:
    def __init__(self, name: str):
        """Constructor - khởi tạo object.
        Gọi tự động khi tạo instance bằng Resource("...")
        """
        self.name = name                     # Gán thuộc tính cho instance
        self.is_open = True                  # Trạng thái mặc định
        print(f"✅ Creating resource: {name}")

    def __del__(self):
        """Destructor - dọn dẹp tài nguyên.
        Gọi tự động khi object bị garbage collected.
        ⚠️ Không đảm bảo thời điểm gọi chính xác!
        """
        print(f"🗑️ Deleting resource: {self.name}")

    def __repr__(self):
        """Biểu diễn chính thức (dùng trong debug, repr())."""
        return f"Resource(name={self.name!r}, is_open={self.is_open})"

    def __str__(self):
        """Biểu diễn thân thiện (dùng trong print(), str())."""
        status = "open" if self.is_open else "closed"
        return f"Resource '{self.name}' ({status})"

# Sử dụng:
r = Resource("DB Connection")               # Output: ✅ Creating resource: DB Connection
print(r)                                     # Output: Resource 'DB Connection' (open)
print(repr(r))                               # Output: Resource(name='DB Connection', is_open=True)

del r                                        # Output: 🗑️ Deleting resource: DB Connection

# ⚠️ Lưu ý: __del__ KHÔNG tin cậy cho cleanup
# Dùng context manager (with statement) thay thế:
class ManagedResource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")          # ĐẢM BẢO chạy dù có exception
        return False

with ManagedResource() as r:
    print("Using resource")
# Output:
#   Acquiring resource
#   Using resource
#   Releasing resource
```

#### Function Overloading

```python
# === Python KHÔNG hỗ trợ function overloading trực tiếp ===
# (Không thể có 2 function cùng tên khác tham số như Java/C++)
# Có 3 giải pháp thay thế:

# --- Giải pháp 1: Default arguments ---
def greet(name: str, greeting: str = "Hello", exclaim: bool = True) -> str:
    result = f"{greeting}, {name}"
    return result + "!" if exclaim else result

print(greet("John"))                         # Output: Hello, John!
print(greet("John", "Hi"))                   # Output: Hi, John!
print(greet("John", "Hey", False))           # Output: Hey, John

# --- Giải pháp 2: functools.singledispatch ---
# Dispatch dựa trên kiểu của tham số ĐẦU TIÊN
import functools

@functools.singledispatch
def process(arg):
    """Default handler cho kiểu không được register."""
    print(f"Default: {arg} (type: {type(arg).__name__})")

@process.register(int)
def _(arg):
    """Handler cho int - tính bình phương."""
    print(f"Integer: {arg} → squared = {arg ** 2}")

@process.register(str)
def _(arg):
    """Handler cho str - in uppercase."""
    print(f"String: '{arg}' → upper = '{arg.upper()}'")

@process.register(list)
def _(arg):
    """Handler cho list - in số phần tử."""
    print(f"List: {arg} → length = {len(arg)}")

process(42)           # Output: Integer: 42 → squared = 1764
process("hello")      # Output: String: 'hello' → upper = 'HELLO'
process([1, 2, 3])    # Output: List: [1, 2, 3] → length = 3
process(3.14)         # Output: Default: 3.14 (type: float)

# --- Giải pháp 3: typing.overload (chỉ cho type checking) ---
from typing import overload

@overload
def greet(name: str) -> str: ...
@overload
def greet(name: str, age: int) -> str: ...

def greet(name, age=None):
    """Implementation thực tế - phải handle tất cả overloads."""
    if age is not None:
        return f"Hello {name}, you are {age} years old"
    return f"Hello {name}"

print(greet("John"))         # Output: Hello John
print(greet("John", 30))     # Output: Hello John, you are 30 years old
```

---

### 1.3. Vòng Lặp (Loops)

#### For Loop

```python
# === range() - tạo dãy số ===
# range(stop)         → 0 đến stop-1
# range(start, stop)  → start đến stop-1
# range(start, stop, step) → start, start+step, start+2*step, ...

for i in range(5):              # Từ 0 đến 4 (5 phần tử)
    print(i, end=" ")           # Output: 0 1 2 3 4

for i in range(1, 6):           # Từ 1 đến 5
    print(i, end=" ")           # Output: 1 2 3 4 5

for i in range(0, 10, 2):       # Từ 0 đến 8, bước 2
    print(i, end=" ")           # Output: 0 2 4 6 8

for i in range(5, 0, -1):       # Đếm ngược: 5 → 1
    print(i, end=" ")           # Output: 5 4 3 2 1

# === For với iterable (list, tuple, str, dict...) ===
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:            # Duyệt trực tiếp từng phần tử
    print(fruit)
# Output: apple / banana / cherry (mỗi dòng 1 từ)

# Duyệt string từng ký tự
for ch in "Python":
    print(ch, end="")           # Output: Python

# Duyệt dict (mặc định duyệt key)
user = {"name": "John", "age": 30}
for key in user:
    print(f"{key} = {user[key]}")
# Output: name = John / age = 30

# === enumerate() - duyệt với index ===
for i, fruit in enumerate(fruits):          # Bắt đầu từ index 0
    print(f"{i}: {fruit}")
# Output: 0: apple / 1: banana / 2: cherry

for i, fruit in enumerate(fruits, start=1):  # Bắt đầu từ index 1
    print(f"{i}. {fruit}")
# Output: 1. apple / 2. banana / 3. cherry

# === zip() - duyệt nhiều iterable song song ===
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["HCM", "HN", "DN"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} ({age}) - {city}")
# Output: Alice (25) - HCM / Bob (30) - HN / Charlie (35) - DN

# ⚠️ zip() dừng ở iterable NGẮN nhất
for a, b in zip([1, 2, 3], [10, 20]):
    print(a, b)
# Output: 1 10 / 2 20 (phần tử 3 bị bỏ!)

# Dùng itertools.zip_longest() để padding
from itertools import zip_longest
for a, b in zip_longest([1, 2, 3], [10, 20], fillvalue=0):
    print(a, b)
# Output: 1 10 / 2 20 / 3 0

# === Real-world: duyệt file line by line (memory-efficient) ===
# with open("data.txt") as f:
#     for line_num, line in enumerate(f, 1):
#         print(f"Line {line_num}: {line.strip()}")
```

#### While Loop

```python
# === While cơ bản ===
count = 0
while count < 5:               # Lặp khi điều kiện còn True
    print(count, end=" ")       # Output: 0 1 2 3 4
    count += 1                  # ⚠️ PHẢI cập nhật biến, nếu không → infinite loop

# === Infinite loop + break (pattern phổ biến) ===
while True:                     # Vòng lặp vô hạn
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break                   # Thoát vòng lặp
    print(f"You entered: {user_input}")

# === While với else (chạy khi KHÔNG break) ===
count = 0
while count < 3:
    print(count, end=" ")       # Output: 0 1 2
    count += 1
else:
    print("Done!")              # Output: Done! (chạy vì không có break)

# === Walrus operator := trong while (Python 3.8+) ===
# Gán và kiểm tra cùng lúc
import random
while (n := random.randint(1, 10)) != 7:    # Gán n rồi kiểm tra
    print(f"Got {n}, not 7...")
print(f"Found 7!")

# === Real-world: retry pattern ===
max_retries = 3
attempt = 0
while attempt < max_retries:
    try:
        # result = connect_to_server()
        print(f"Attempt {attempt + 1}: success!")
        break                   # Thành công → thoát
    except Exception:
        attempt += 1
        print(f"Attempt {attempt} failed, retrying...")
else:
    # else chạy khi while kết thúc bình thường (không break)
    print("All retries exhausted!")
```

#### For-each/List Comprehension

```python
# === List comprehension - cú pháp ngắn gọn tạo list ===
# Cú pháp: [biểu_thức for biến in iterable if điều_kiện]

# Bình phương các số từ 0-9
squares = [x**2 for x in range(10)]
print(squares)                   # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Lọc số chẵn
evens = [x for x in range(20) if x % 2 == 0]
print(evens)                     # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Với biểu thức ternary
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)                    # Output: ['even', 'odd', 'even', 'odd', 'even']

# Nested comprehension (flatten 2D → 1D)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)                      # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# === Dictionary comprehension ===
square_dict = {x: x**2 for x in range(5)}
print(square_dict)               # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Đảo key-value
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)                  # Output: {1: 'a', 2: 'b', 3: 'c'}

# === Set comprehension ===
unique_chars = {char.lower() for char in "Hello World"}
print(unique_chars)              # Output: {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}

# === Generator expression (lazy - không tạo list trong memory) ===
# Dùng () thay vì []
total = sum(x**2 for x in range(1_000_000))  # Không tạo list 1 triệu phần tử!
print(total)                     # Output: 333332833333500000

# ⚠️ So sánh memory:
import sys
list_comp = [x**2 for x in range(1000)]
gen_expr = (x**2 for x in range(1000))
print(sys.getsizeof(list_comp))  # Output: ~8856 bytes (chứa tất cả)
print(sys.getsizeof(gen_expr))   # Output: ~200 bytes (chỉ chứa logic)

# === Real-world: xử lý dữ liệu ===
users = [
    {"name": "John", "age": 30, "active": True},
    {"name": "Jane", "age": 25, "active": False},
    {"name": "Bob", "age": 35, "active": True},
]

# Lấy tên users active
active_names = [u["name"] for u in users if u["active"]]
print(active_names)              # Output: ['John', 'Bob']

# Tạo lookup dict
name_to_age = {u["name"]: u["age"] for u in users}
print(name_to_age)               # Output: {'John': 30, 'Jane': 25, 'Bob': 35}
```

#### Iterator

```python
# === Iterator Protocol ===
# Object có __iter__() và __next__() là iterator
# __iter__() trả về self
# __next__() trả về phần tử tiếp theo, raise StopIteration khi hết

# --- Dùng iter() và next() ---
numbers = [1, 2, 3]
it = iter(numbers)               # Tạo iterator từ list
print(next(it))                  # Output: 1 (phần tử đầu tiên)
print(next(it))                  # Output: 2
print(next(it))                  # Output: 3
# print(next(it))                # ❌ StopIteration (đã hết phần tử)

# Dùng default value để tránh StopIteration
it = iter(numbers)
print(next(it, "hết"))           # Output: 1
print(next(it, "hết"))           # Output: 2
print(next(it, "hết"))           # Output: 3
print(next(it, "hết"))           # Output: hết (không raise lỗi)

# === Custom iterator ===
class Countdown:
    """Iterator đếm ngược từ n về 0."""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self              # Iterator trả về chính nó

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Dừng khi hết
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num, end=" ")          # Output: 5 4 3 2 1 0

# ⚠️ Iterator chỉ dùng 1 lần!
nums = [1, 2, 3]
it = iter(nums)
print(list(it))                  # Output: [1, 2, 3]
print(list(it))                  # Output: [] ← ĐÃ HẾT! Iterator exhausted

# Iterable (list, tuple) thì dùng được nhiều lần vì tạo iterator MỚI mỗi khi iter()
print(list(iter(nums)))          # Output: [1, 2, 3] (tạo iterator mới)

# === Real-world: đọc file lớn line-by-line (iterator pattern) ===
# File object là iterator, đọc từng dòng - không load hết vào memory
# with open("big_file.txt") as f:  # f là iterator
#     for line in f:                # Đọc từng dòng
#         process(line)
```

#### Generator/Yield

```python
# === Generator function - tạo iterator bằng yield ===
# yield "tạm dừng" function và trả về giá trị
# Lần gọi next() tiếp theo, function chạy tiếp từ yield

def count_up(n):
    """Generator: đếm từ 0 đến n-1."""
    i = 0
    while i < n:
        yield i                  # Trả về i và tạm dừng
        i += 1                   # Tiếp tục khi next() được gọi
    # Hết vòng lặp → tự động raise StopIteration

# Dùng trong for loop
for num in count_up(5):
    print(num, end=" ")          # Output: 0 1 2 3 4

# Generator trả về iterator
gen = count_up(3)
print(type(gen))                 # Output: <class 'generator'>
print(next(gen))                 # Output: 0
print(next(gen))                 # Output: 1
print(next(gen))                 # Output: 2

# === Generator expression (one-liner) ===
squares = (x**2 for x in range(10))  # Lazy - chưa tính gì
print(list(squares))             # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# === Generator với send() - gửi giá trị VÀO generator ===
def accumulator():
    """Generator nhận giá trị qua send() và tích lũy tổng."""
    total = 0
    while True:
        value = yield total      # yield trả về total, nhận value từ send()
        if value is None:
            break                # send(None) hoặc next() → dừng
        total += value

gen = accumulator()
next(gen)                        # Output: 0 (khởi tạo - BẮT BUỘC gọi next() đầu tiên)
print(gen.send(10))              # Output: 10 (total = 0 + 10)
print(gen.send(20))              # Output: 30 (total = 10 + 20)
print(gen.send(5))               # Output: 35 (total = 30 + 5)

# === yield from - delegate to sub-generator (Python 3.3+) ===
def flatten(nested):
    """Flatten nested list bất kỳ độ sâu."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # Delegate cho sub-generator
        else:
            yield item

data = [1, [2, 3], [4, [5, 6]], 7]
print(list(flatten(data)))       # Output: [1, 2, 3, 4, 5, 6, 7]

# === Real-world: đọc file chunks (xử lý file lớn) ===
def read_chunks(file_path, chunk_size=1024):
    """Đọc file theo từng chunk, tránh load hết vào memory."""
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break            # Hết file
            yield chunk          # Trả về từng chunk

# Real-world: pipeline xử lý data
def pipeline(data):
    """Pipeline: filter → transform → aggregate."""
    # Mỗi bước là generator → lazy evaluation
    positives = (x for x in data if x > 0)      # Bước 1: lọc
    squared = (x**2 for x in positives)          # Bước 2: bình phương
    return sum(squared)                           # Bước 3: tổng

print(pipeline([-2, -1, 0, 1, 2, 3]))  # Output: 14 (1² + 2² + 3²)

# ⚠️ Generator vs List comprehension:
# Generator: ít memory, lazy, dùng 1 lần
# List comp: nhiều memory, eager, dùng nhiều lần
```

#### Loop Control

```python
# === break - thoát vòng lặp ngay lập tức ===
for i in range(10):
    if i == 5:
        break                    # Thoát khi i = 5
    print(i, end=" ")            # Output: 0 1 2 3 4

# === continue - bỏ qua lần lặp hiện tại, chuyển sang lần tiếp ===
for i in range(6):
    if i == 2 or i == 4:
        continue                 # Bỏ qua 2 và 4
    print(i, end=" ")            # Output: 0 1 3 5

# === else trong vòng lặp ===
# else block chạy khi vòng lặp kết thúc BÌNH THƯỜNG (không break)

# Ví dụ 1: else CHẠY (không có break)
for i in range(3):
    print(i, end=" ")            # Output: 0 1 2
else:
    print("→ Completed!")        # Output: → Completed! (chạy vì không break)

# Ví dụ 2: else KHÔNG CHẠY (có break)
for i in range(10):
    if i == 3:
        break
    print(i, end=" ")            # Output: 0 1 2
else:
    print("→ Completed!")        # KHÔNG chạy vì bị break

# === Real-world: for...else tìm kiếm ===
primes = [2, 3, 5, 7, 11, 13]

# Kiểm tra số nguyên tố có trong list không
target = 8
for prime in primes:
    if prime == target:
        print(f"Found {target}!")
        break
else:
    # Chạy khi duyệt hết list mà không tìm thấy (không break)
    print(f"{target} not found in primes")
# Output: 8 not found in primes

# === pass - placeholder, không làm gì ===
for i in range(5):
    pass                         # TODO: implement later
    # Dùng khi cần block rỗng nhưng Python yêu cầu có lệnh

# ⚠️ Lưu ý: không có goto/label trong Python
# → Thoát nested loop dùng flag hoặc function + return
def find_in_matrix(matrix, target):
    """Tìm target trong matrix 2D, trả về vị trí."""
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == target:
                return (i, j)    # return thay cho goto
    return None

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(find_in_matrix(matrix, 5))  # Output: (1, 1)
print(find_in_matrix(matrix, 10)) # Output: None
```

---

### 1.4. Điều Kiện (Conditionals)

#### If-Else

```python
# === If-else cơ bản ===
age = 18
if age >= 18:                    # Kiểm tra điều kiện
    print("Adult")               # Output: Adult
else:
    print("Minor")

# === Elif - nhiều nhánh điều kiện ===
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:                # Kiểm tra tiếp nếu if sai
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:                            # Mặc định nếu tất cả sai
    grade = "F"
print(f"Score {score} → Grade {grade}")  # Output: Score 85 → Grade B

# === Toán tử so sánh ===
x = 10
print(x == 10)      # Output: True  (bằng)
print(x != 5)       # Output: True  (khác)
print(x > 5)        # Output: True  (lớn hơn)
print(x >= 10)      # Output: True  (lớn hơn hoặc bằng)
print(1 < x < 20)   # Output: True  (chained comparison - Python đặc trưng!)

# === Toán tử logic ===
a, b = True, False
print(a and b)       # Output: False (AND - cả 2 True mới True)
print(a or b)        # Output: True  (OR - 1 trong 2 True là True)
print(not a)         # Output: False (NOT - đảo giá trị)

# === Short-circuit evaluation ===
# and: nếu vế trái False → trả về vế trái, KHÔNG eval vế phải
# or:  nếu vế trái True → trả về vế trái, KHÔNG eval vế phải
name = ""
result = name or "Anonymous"     # name falsy → trả về "Anonymous"
print(result)                    # Output: Anonymous

user = {"name": "John"}
email = user.get("email") or "no-email@example.com"
print(email)                     # Output: no-email@example.com

# === Truthy / Falsy values ===
# Falsy: None, False, 0, 0.0, 0j, "", [], (), {}, set(), frozenset()
# Truthy: mọi giá trị khác
if []:                           # list rỗng → Falsy
    print("truthy")
else:
    print("falsy")               # Output: falsy

if [0]:                          # list có phần tử (dù là 0) → Truthy
    print("truthy")              # Output: truthy

# === is vs == ===
# is: so sánh IDENTITY (cùng object trong memory)
# ==: so sánh VALUE (giá trị bằng nhau)
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)        # Output: True  (cùng giá trị)
print(a is b)        # Output: False (khác object)

# Luôn dùng 'is' với None
x = None
if x is None:        # ✅ Đúng cách
    print("x is None")
# if x == None:      # ❌ Không nên (có thể bị override __eq__)

# ⚠️ Edge case: Python cache small integers (-5 đến 256)
a = 256
b = 256
print(a is b)        # Output: True  (cached!)
a = 257
b = 257
print(a is b)        # Output: False (không cached)
```

#### Match Expression (Python 3.10+)

```python
# === Structural Pattern Matching (switch-case nâng cao) ===

# --- Basic value matching ---
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 301:
            return "Moved Permanently"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:                  # _ là wildcard - match tất cả
            return f"Unknown status: {status}"

print(http_status(200))          # Output: OK
print(http_status(404))          # Output: Not Found
print(http_status(418))          # Output: Unknown status: 418

# --- Pattern matching với tuple/list ---
def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):            # x capture giá trị tại vị trí 0
            return f"On X-axis at x={x}"
        case (0, y):
            return f"On Y-axis at y={y}"
        case (x, y):
            return f"Point at ({x}, {y})"

print(describe_point((0, 0)))    # Output: Origin
print(describe_point((5, 0)))    # Output: On X-axis at x=5
print(describe_point((3, 4)))    # Output: Point at (3, 4)

# --- Pattern với guard clause (điều kiện thêm) ---
def classify_number(n):
    match n:
        case n if n < 0:         # Guard: n < 0
            return "negative"
        case 0:
            return "zero"
        case n if n % 2 == 0:    # Guard: n chẵn
            return "positive even"
        case _:
            return "positive odd"

print(classify_number(-5))       # Output: negative
print(classify_number(0))        # Output: zero
print(classify_number(4))        # Output: positive even
print(classify_number(7))        # Output: positive odd

# --- Pattern matching với class (Python 3.10+) ---
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Circle:
    center: Point
    radius: float

def describe_shape(shape):
    match shape:
        case Circle(center=Point(x=0, y=0), radius=r):
            return f"Circle at origin with radius {r}"
        case Circle(center=Point(x=x, y=y), radius=r):
            return f"Circle at ({x}, {y}) with radius {r}"
        case Point(x=x, y=y):
            return f"Point at ({x}, {y})"

print(describe_shape(Circle(Point(0, 0), 5)))  # Output: Circle at origin with radius 5
print(describe_shape(Point(3, 4)))              # Output: Point at (3, 4)

# --- Pattern matching với dict ---
def process_command(command):
    match command:
        case {"action": "move", "direction": d, "speed": s}:
            return f"Moving {d} at speed {s}"
        case {"action": "stop"}:
            return "Stopping"
        case {"action": action}:
            return f"Unknown action: {action}"

print(process_command({"action": "move", "direction": "north", "speed": 5}))
# Output: Moving north at speed 5

# --- OR pattern với | ---
def classify_http(code):
    match code:
        case 200 | 201 | 204:   # Match bất kỳ giá trị nào
            return "Success"
        case 301 | 302:
            return "Redirect"
        case 400 | 401 | 403 | 404:
            return "Client Error"
        case _:
            return "Other"

print(classify_http(201))        # Output: Success
print(classify_http(404))        # Output: Client Error
```

#### Ternary Operator

```python
# === Cú pháp: value_if_true if condition else value_if_false ===
# Tương đương: condition ? true_val : false_val trong C/Java

age = 20
status = "adult" if age >= 18 else "minor"
print(status)                    # Output: adult

# === Dùng trong biểu thức ===
x = 10
result = x * 2 if x > 5 else x + 10
print(result)                    # Output: 20

# Trong f-string
print(f"You are {'old' if age > 30 else 'young'}")
# Output: You are young

# Trong list comprehension
numbers = [1, -2, 3, -4, 5]
abs_vals = [x if x >= 0 else -x for x in numbers]
print(abs_vals)                  # Output: [1, 2, 3, 4, 5]

# === Nested ternary (⚠️ khó đọc - nên tránh) ===
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade)                     # Output: B

# ✅ Nên dùng if-elif thay vì nested ternary khi > 2 nhánh

# === Walrus operator := (Python 3.8+) ===
# Gán giá trị cho biến trong expression
import re
text = "Hello, my email is john@example.com"
if (match := re.search(r'\b\w+@\w+\.\w+\b', text)):
    print(f"Found email: {match.group()}")  # Output: Found email: john@example.com

# Trong while loop
# while (line := input("Enter text (empty to quit): ")):
#     print(f"You said: {line}")

# Trong list comprehension
results = [y for x in range(10) if (y := x ** 2) > 20]
print(results)                   # Output: [25, 36, 49, 64, 81]
```

---

### 1.5. Destructuring & Spread (Phân rã & Toán tử mở rộng)

#### Tuple/List Unpacking

```python
# === Basic unpacking - số biến phải BẰNG số phần tử ===
a, b, c = [1, 2, 3]             # Unpack list
print(a, b, c)                   # Output: 1 2 3

x, y = (10, 20)                  # Unpack tuple
print(x, y)                      # Output: 10 20

first, second = "AB"             # Unpack string
print(first, second)             # Output: A B

# ⚠️ Số biến phải khớp
# a, b = [1, 2, 3]              # ❌ ValueError: too many values to unpack
# a, b, c = [1, 2]              # ❌ ValueError: not enough values to unpack

# === Swap (hoán đổi giá trị) - không cần biến tạm ===
a, b = 1, 2
a, b = b, a                     # Python tạo tuple tạm (b, a) rồi unpack
print(a, b)                      # Output: 2 1

# Swap 3 biến
a, b, c = 1, 2, 3
a, b, c = c, a, b               # Xoay vòng
print(a, b, c)                   # Output: 3 1 2

# === Starred assignment * (rest operator) ===
first, *rest = [1, 2, 3, 4, 5]
print(first)                     # Output: 1
print(rest)                      # Output: [2, 3, 4, 5] (luôn là list)

first, *middle, last = [1, 2, 3, 4, 5]
print(first)                     # Output: 1
print(middle)                    # Output: [2, 3, 4]
print(last)                      # Output: 5

*init, last = [1, 2, 3, 4, 5]
print(init)                      # Output: [1, 2, 3, 4]
print(last)                      # Output: 5

# ⚠️ Chỉ được 1 starred expression
# *a, *b = [1, 2, 3]            # ❌ SyntaxError: multiple starred expressions

# Star với ít phần tử
first, *rest = [1]
print(first)                     # Output: 1
print(rest)                      # Output: [] (list rỗng - không lỗi!)

# === Ignore values với _ ===
_, b, _ = (1, 2, 3)             # Chỉ lấy b, bỏ phần tử 1 và 3
print(b)                         # Output: 2

# Ignore nhiều phần tử
first, *_, last = [1, 2, 3, 4, 5]  # Chỉ lấy first và last
print(first, last)               # Output: 1 5

# === Real-world: unpack hàm trả về nhiều giá trị ===
def get_user_info():
    return "John", 30, "john@example.com"

name, age, email = get_user_info()
print(f"{name} ({age}) - {email}")  # Output: John (30) - john@example.com

# Chỉ lấy tên, bỏ phần còn lại
name, *_ = get_user_info()
print(name)                      # Output: John
```

#### Dict Unpacking (Spread)

```python
# === Dict merge với ** (spread operator) ===
defaults = {"color": "red", "size": "medium", "theme": "dark"}
custom = {"size": "large", "weight": 10}

# Key trùng → giá trị CUỐI CÙNG thắng
merged = {**defaults, **custom}
print(merged)
# Output: {'color': 'red', 'size': 'large', 'theme': 'dark', 'weight': 10}
# 'size' bị override bởi custom

# Python 3.9+: dùng toán tử |
merged = defaults | custom       # Tạo dict mới
print(merged)
# Output: {'color': 'red', 'size': 'large', 'theme': 'dark', 'weight': 10}

# In-place merge với |=
config = {"debug": False}
config |= {"debug": True, "verbose": True}
print(config)                    # Output: {'debug': True, 'verbose': True}

# === Function argument unpacking ===
def greet(name, age):
    print(f"{name} is {age} years old")

data = {"name": "John", "age": 30}
greet(**data)                    # Output: John is 30 years old
# Tương đương: greet(name="John", age=30)

# ⚠️ Key trong dict phải khớp tên tham số
# greet(**{"name": "John", "score": 90})  # ❌ TypeError: unexpected keyword argument

# === List/Tuple spread với * ===
nums = [1, 2, 3]
more = [0, *nums, 4]            # Spread list vào list mới
print(more)                      # Output: [0, 1, 2, 3, 4]

# Kết hợp nhiều list
a = [1, 2]
b = [3, 4]
c = [5, 6]
combined = [*a, *b, *c]
print(combined)                  # Output: [1, 2, 3, 4, 5, 6]

# Spread vào function call
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))                # Output: 6
# Tương đương: add(1, 2, 3)

# === Real-world: merge config với defaults ===
DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8080,
    "debug": False,
    "log_level": "INFO",
}

def create_server(**user_config):
    # Merge defaults với user config (user config override)
    config = {**DEFAULT_CONFIG, **user_config}
    print(f"Server at {config['host']}:{config['port']} (debug={config['debug']})")

create_server(port=3000, debug=True)
# Output: Server at localhost:3000 (debug=True)
```

#### Nested Unpacking

```python
# === Nested tuple unpacking ===
(a, b), (c, d) = (1, 2), (3, 4)
print(a, b, c, d)               # Output: 1 2 3 4

# Sâu hơn
((a, b), c) = ((1, 2), 3)
print(a, b, c)                   # Output: 1 2 3

# === Unpacking trong for loop ===
pairs = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
for name, age in pairs:
    print(f"{name}: {age} tuổi")
# Output:
#   Alice: 25 tuổi
#   Bob: 30 tuổi
#   Charlie: 35 tuổi

# Nested trong for loop
data = [("Alice", (90, 85)), ("Bob", (80, 95))]
for name, (math, english) in data:
    print(f"{name}: Math={math}, English={english}")
# Output:
#   Alice: Math=90, English=85
#   Bob: Math=80, English=95

# === Dict items unpacking ===
user = {"name": "John", "age": 30, "city": "HCM"}
for key, value in user.items():  # .items() trả về list of tuples
    print(f"{key}: {value}")
# Output: name: John / age: 30 / city: HCM

# === Real-world: unpacking API response ===
api_response = {
    "status": 200,
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "scores": [90, 85, 92]},
            {"id": 2, "name": "Bob", "scores": [80, 95, 88]},
        ]
    }
}

# Trích xuất data
for user in api_response["data"]["users"]:
    name = user["name"]
    avg_score = sum(user["scores"]) / len(user["scores"])
    print(f"{name}: avg = {avg_score:.1f}")
# Output:
#   Alice: avg = 89.0
#   Bob: avg = 87.7

# === enumerate + unpacking combo ===
items = ["apple", "banana", "cherry"]
for i, (item) in enumerate(items, 1):
    print(f"{i}. {item}")
# Output: 1. apple / 2. banana / 3. cherry
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

#### Byte & ByteArray

```python
# bytes (immutable)
b = b"Hello"
b = bytes([72, 101, 108, 108, 111])
b[0]  # 72

# bytearray (mutable)
ba = bytearray(b"Hello")
ba[0] = 74  # Thay đổi được
ba.append(33)

# Chuyển đổi
text = b.decode('utf-8')       # bytes -> str
data = "Hello".encode('utf-8')  # str -> bytes

# Byte operations
len(b)           # 5
b.hex()          # '48656c6c6f'
bytes.fromhex('48656c6c6f')  # b'Hello'
```

#### Character (Python không có kiểu char riêng)

```python
# Python dùng str với length 1 cho character
ch = 'A'
len(ch)       # 1
ord('A')      # 65 (Unicode code point)
chr(65)       # 'A'

# Unicode
ord('你')     # 20320
chr(20320)    # '你'
'A'.isalpha()  # True
'1'.isdigit()  # True
```

---

### 2.2. Enum (Python 3.4+)

```python
from enum import Enum, auto, IntEnum, StrEnum, Flag

# === Basic Enum - nhóm các hằng số có liên quan ===
class Color(Enum):
    RED = 1              # Mỗi member có name và value
    GREEN = 2
    BLUE = 3

# Truy cập:
print(Color.RED)         # Output: Color.RED (repr)
print(Color.RED.name)    # Output: RED (tên string)
print(Color.RED.value)   # Output: 1 (giá trị)

# Tạo từ value hoặc name:
print(Color(1))          # Output: Color.RED (từ value)
print(Color["RED"])      # Output: Color.RED (từ name)

# === auto() - tự động gán giá trị tăng dần ===
class Status(Enum):
    PENDING = auto()     # 1
    APPROVED = auto()    # 2
    REJECTED = auto()    # 3
    CANCELLED = auto()   # 4

print(Status.PENDING.value)   # Output: 1
print(Status.CANCELLED.value) # Output: 4

# === Enum với methods ===
class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

    def emoji(self) -> str:
        """Trả về emoji tương ứng."""
        emojis = {1: "🟢", 2: "🟡", 3: "🟠", 4: "🔴"}
        return emojis[self.value]

    def is_urgent(self) -> bool:
        return self.value >= 3

print(Priority.HIGH.emoji())      # Output: 🟠
print(Priority.HIGH.is_urgent())  # Output: True
print(Priority.LOW.is_urgent())   # Output: False

# === IntEnum - so sánh được với int ===
class HTTPStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500

print(HTTPStatus.OK == 200)       # Output: True (IntEnum so sánh với int)
print(HTTPStatus.OK > 100)        # Output: True

# === StrEnum (Python 3.11+) - so sánh được với str ===
class Direction(StrEnum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

print(Direction.NORTH == "north")  # Output: True

# === Flag - kết hợp nhiều giá trị bằng bitwise OR ===
class Permission(Flag):
    READ = auto()        # 1
    WRITE = auto()       # 2
    EXECUTE = auto()     # 4

admin = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(admin)                           # Output: Permission.READ|WRITE|EXECUTE
print(Permission.READ in admin)        # Output: True
print(Permission.WRITE in admin)       # Output: True

# === Iteration - duyệt tất cả members ===
for color in Color:
    print(f"{color.name} = {color.value}")
# Output: RED = 1 / GREEN = 2 / BLUE = 3

# List tất cả members:
print(list(Color))       # Output: [Color.RED, Color.GREEN, Color.BLUE]

# === So sánh ===
print(Color.RED is Color.RED)    # Output: True  (luôn là singleton)
print(Color.RED == Color.RED)    # Output: True
print(Color.RED == Color.GREEN)  # Output: False
# print(Color.RED == 1)          # Output: False (Enum ≠ int, trừ IntEnum)

# ⚠️ Enum members là SINGLETON - không thể tạo thêm
# Color.YELLOW = 4              # ❌ AttributeError

# === Real-world: dùng Enum trong match/if ===
def process_status(status: Status) -> str:
    match status:
        case Status.PENDING:
            return "Đang chờ xử lý"
        case Status.APPROVED:
            return "Đã duyệt"
        case Status.REJECTED:
            return "Bị từ chối"
        case _:
            return "Không xác định"

print(process_status(Status.APPROVED))  # Output: Đã duyệt
```

---

### 2.3. Nullable Types

```python
# === Python không có null type riêng ===
# None là singleton duy nhất của NoneType
# Dùng Optional hoặc | None để đánh dấu giá trị có thể null

from typing import Optional, Union

# === Optional[X] = X | None ===
# Cú pháp cũ (Python 3.5+)
def find_user(user_id: int) -> Optional[str]:
    """Tìm user, trả về None nếu không tìm thấy."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)    # get() trả về None nếu key không tồn tại

print(find_user(1))              # Output: Alice
print(find_user(99))             # Output: None

# Cú pháp mới (Python 3.10+) - dùng toán tử |
def find_user_v2(user_id: int) -> str | None:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# === Kiểm tra None trước khi dùng ===
name = find_user(1)
if name is not None:             # ✅ Luôn dùng 'is not None'
    print(name.upper())          # Output: ALICE (an toàn)

# ⚠️ Sai lầm phổ biến:
# if name:                       # ❌ Sai! "" (string rỗng) cũng falsy
#     print(name.upper())        # Bỏ qua cả trường hợp name = ""

# === Union type - nhiều kiểu có thể ===
def process(value: Union[str, int, None]) -> str:
    """Xử lý giá trị có thể là str, int hoặc None."""
    if value is None:
        return "No value"
    return str(value)

# Python 3.10+:
def process_v2(value: str | int | None) -> str:
    if value is None:
        return "No value"
    return str(value)

print(process("hello"))          # Output: hello
print(process(42))               # Output: 42
print(process(None))             # Output: No value

# === Real-world: API response có thể null ===
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str | None = None     # Email có thể null
    phone: str | None = None     # Phone có thể null

user = User("John")
print(user.email)                # Output: None
print(user.email or "N/A")      # Output: N/A
```

---

### 2.4. Null Safety

```python
# === Python KHÔNG có null safety built-in (khác Kotlin/Swift) ===
# Phải tự kiểm tra None. Dưới đây là các pattern phổ biến:

# --- Pattern 1: Elvis-like với 'or' ---
name = None
result = name or "Unknown"       # None là falsy → trả về "Unknown"
print(result)                    # Output: Unknown

# ⚠️ Cẩn thận: 'or' coi "" và 0 là falsy
count = 0
result = count or 10             # 0 là falsy → trả về 10 (KHÔNG MONG MUỐN!)
print(result)                    # Output: 10

# ✅ Giải pháp: dùng 'if is None'
result = count if count is not None else 10
print(result)                    # Output: 0 (đúng!)

# --- Pattern 2: Safe nested access với dict.get() ---
user = {
    "name": "John",
    "address": {"city": "NYC", "zip": "10001"},
    "contacts": None
}

# Chuỗi .get() an toàn - không bao giờ raise KeyError
city = user.get("address", {}).get("city", "Unknown")
print(city)                      # Output: NYC

# Khi key không tồn tại
country = user.get("address", {}).get("country", "N/A")
print(country)                   # Output: N/A

# ⚠️ Vẫn có thể lỗi nếu value là None thay vì dict
# contacts = user.get("contacts", {}).get("email")  # ❌ AttributeError: NoneType has no 'get'

# ✅ Giải pháp an toàn hơn:
contacts = user.get("contacts")
email = contacts.get("email") if isinstance(contacts, dict) else None

# --- Pattern 3: getattr() cho object attributes ---
class Person:
    def __init__(self, name):
        self.name = name
        # Không có .email attribute

person = Person("John")
email = getattr(person, "email", "no-email")  # Default nếu attribute không tồn tại
print(email)                     # Output: no-email

# --- Pattern 4: Walrus operator := (Python 3.8+) ---
import re

text = "Contact: john@example.com"
if (match := re.search(r'[\w.-]+@[\w.-]+', text)) is not None:
    print(f"Found: {match.group()}")  # Output: Found: john@example.com
else:
    print("No email found")

# --- Pattern 5: try/except cho access chains ---
data = {"a": {"b": {"c": 42}}}
try:
    value = data["a"]["b"]["c"]
    print(value)                 # Output: 42
except (KeyError, TypeError):
    value = None

# === Real-world: safe JSON parsing ===
import json

def safe_get(data: dict, *keys, default=None):
    """Truy cập nested dict an toàn."""
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return default
    return data if data is not None else default

config = {"database": {"host": "localhost", "port": 5432}}
print(safe_get(config, "database", "host"))        # Output: localhost
print(safe_get(config, "database", "password", default="secret"))  # Output: secret
print(safe_get(config, "cache", "host", default="redis://localhost"))  # Output: redis://localhost
```

---

### 2.5. Generics

```python
# === Generics - code hoạt động với NHIỀU kiểu dữ liệu ===
# Giúp type checker hiểu kiểu trả về dựa trên kiểu đầu vào

from typing import TypeVar, Generic, List

# --- TypeVar: biến kiểu ---
T = TypeVar('T')                 # T có thể là BẤT KỲ kiểu nào

# --- Generic class ---
class Box(Generic[T]):
    """Hộp chứa 1 giá trị với kiểu xác định."""
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value

    def __repr__(self) -> str:
        return f"Box({self.value!r})"

# Usage - type checker sẽ suy luận kiểu
int_box = Box(42)                # Box[int]
str_box = Box("hello")          # Box[str]
print(int_box.get())             # Output: 42
print(str_box.get())             # Output: hello

# --- Generic function ---
def first(items: list[T]) -> T:
    """Trả về phần tử đầu tiên (giữ nguyên kiểu)."""
    if not items:
        raise ValueError("List is empty")
    return items[0]

print(first([1, 2, 3]))         # Output: 1 (type checker biết là int)
print(first(["a", "b"]))        # Output: a (type checker biết là str)

# --- Generic với multiple TypeVars ---
K = TypeVar('K')
V = TypeVar('V')

def get_or_default(d: dict[K, V], key: K, default: V) -> V:
    """Lấy value từ dict, trả về default nếu key không tồn tại."""
    return d.get(key, default)

result = get_or_default({"a": 1, "b": 2}, "c", 0)
print(result)                    # Output: 0

# --- TypeVar với constraints (giới hạn kiểu) ---
# bound: kiểu phải là subclass của bound
from typing import TypeVar

Numeric = TypeVar('Numeric', bound=float)  # int hoặc float (int kế thừa float concept)

def add_numbers(a: Numeric, b: Numeric) -> Numeric:
    return a + b

# TypeVar restrict: chỉ cho phép một số kiểu cụ thể
StrOrInt = TypeVar('StrOrInt', str, int)  # Chỉ str hoặc int

def double(x: StrOrInt) -> StrOrInt:
    return x + x                 # str + str hoặc int + int

print(double(5))                 # Output: 10
print(double("ab"))              # Output: abab

# === Python 3.12+: Simpler syntax với type statement ===
# type Point = tuple[float, float]       # Type alias
# def first[T](items: list[T]) -> T:     # Generic function (inline TypeVar)
#     return items[0]

# === Real-world: Generic repository pattern ===
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Repository(Generic[T]):
    """Generic repository - base class cho CRUD operations."""
    def __init__(self):
        self._items: dict[int, T] = {}
        self._next_id = 1

    def add(self, item: T) -> int:
        item_id = self._next_id
        self._items[item_id] = item
        self._next_id += 1
        return item_id

    def get(self, id: int) -> Optional[T]:
        return self._items.get(id)

    def all(self) -> list[T]:
        return list(self._items.values())

# Sử dụng:
user_repo = Repository[str]()   # Repository cho str
user_repo.add("Alice")
user_repo.add("Bob")
print(user_repo.all())          # Output: ['Alice', 'Bob']
print(user_repo.get(1))         # Output: Alice
print(user_repo.get(99))        # Output: None
```

#### Covariance/Contravariance

```python
from typing import TypeVar, Generic, Sequence

# === Covariance (out) - dùng cho OUTPUT (read-only) ===
# Nếu Dog kế thừa Animal:
#   Producer[Dog] có thể dùng nơi cần Producer[Animal]
# Tức là subtype TRONG → subtype NGOÀI

T_co = TypeVar('T_co', covariant=True)

class Producer(Generic[T_co]):
    """Chỉ PRODUCE (trả về) T, không nhận T."""
    def __init__(self, item: T_co):
        self._item = item
    def get(self) -> T_co:
        return self._item

# === Contravariance (in) - dùng cho INPUT (write-only) ===
# Nếu Dog kế thừa Animal:
#   Consumer[Animal] có thể dùng nơi cần Consumer[Dog]
# Tức là supertype TRONG → subtype NGOÀI (ngược với covariant!)

T_contra = TypeVar('T_contra', contravariant=True)

class Consumer(Generic[T_contra]):
    """Chỉ CONSUME (nhận vào) T, không trả về T."""
    def accept(self, item: T_contra) -> None:
        print(f"Processing: {item}")

# === Ví dụ thực tế ===
class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

# Sequence là covariant (read-only collection)
def process_animals(animals: Sequence[Animal]) -> None:
    for a in animals:
        print(a.speak())

dogs: list[Dog] = [Dog(), Dog()]
process_animals(dogs)            # ✅ OK vì Sequence là covariant
# Output: Woof! / Woof!

# ⚠️ list là INVARIANT (không covariant)
# def bad_func(animals: list[Animal]) -> None:
#     animals.append(Cat())       # Nếu được, sẽ thêm Cat vào list Dog!
# bad_func(dogs)                  # ❌ mypy error: list là invariant

# Quy tắc nhớ:
# Covariant (out/read):     T xuất hiện ở return → dùng Sequence, Iterable
# Contravariant (in/write): T xuất hiện ở param → hiếm gặp
# Invariant (in+out):       T xuất hiện ở cả 2 → dùng list, dict
```

---

### 2.6. Collection Operations

#### Map/Transform

```python
numbers = [1, 2, 3, 4, 5]

# === map() - áp dụng function lên mỗi phần tử ===
squared = list(map(lambda x: x ** 2, numbers))
print(squared)                   # Output: [1, 4, 9, 16, 25]

# map() trả về iterator (lazy) → cần list() để xem
doubled = map(lambda x: x * 2, numbers)
print(type(doubled))             # Output: <class 'map'> (iterator, chưa tính)
print(list(doubled))             # Output: [2, 4, 6, 8, 10]

# === List comprehension (Pythonic hơn map) ===
squared = [x ** 2 for x in numbers]
print(squared)                   # Output: [1, 4, 9, 16, 25]

# map() với function có sẵn
names = ["alice", "bob", "charlie"]
upper_names = list(map(str.upper, names))
print(upper_names)               # Output: ['ALICE', 'BOB', 'CHARLIE']

# map() với nhiều iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)                      # Output: [11, 22, 33]

# enumerate transform - thêm index
indexed = [(i, v) for i, v in enumerate(numbers, start=1)]
print(indexed)                   # Output: [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
```

#### Filter

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# === filter() - giữ phần tử thỏa điều kiện ===
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)                     # Output: [2, 4, 6, 8, 10]

# filter() cũng trả về iterator (lazy)
# Dùng None để loại bỏ falsy values
mixed = [0, 1, "", "hello", None, False, True, [], [1]]
truthy = list(filter(None, mixed))
print(truthy)                    # Output: [1, 'hello', True, [1]]

# === List comprehension (Pythonic hơn filter) ===
evens = [x for x in numbers if x % 2 == 0]
print(evens)                     # Output: [2, 4, 6, 8, 10]

# Kết hợp filter + map
result = [x ** 2 for x in numbers if x % 2 == 0]
print(result)                    # Output: [4, 16, 36, 64, 100]
# Tương đương: list(map(lambda x: x**2, filter(lambda x: x%2==0, numbers)))
```

#### Reduce/Fold

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# === reduce() - gộp tất cả phần tử thành 1 giá trị ===
# reduce(func, iterable, initial)
# Hoạt động: acc = initial; for x in iterable: acc = func(acc, x)
total = reduce(lambda acc, x: acc + x, numbers, 0)
print(total)                     # Output: 15 (0+1+2+3+4+5)

product = reduce(lambda acc, x: acc * x, numbers, 1)
print(product)                   # Output: 120 (1*1*2*3*4*5)

# Tìm max (không dùng max())
largest = reduce(lambda a, b: a if a > b else b, numbers)
print(largest)                   # Output: 5

# === Built-in thay thế reduce (Pythonic hơn) ===
print(sum(numbers))              # Output: 15 (thay reduce +)
print(max(numbers))              # Output: 5
print(min(numbers))              # Output: 1

# math.prod() (Python 3.8+) - thay reduce *
import math
print(math.prod(numbers))        # Output: 120

# Real-world: flatten nested dicts
configs = [{"a": 1}, {"b": 2}, {"c": 3}]
merged = reduce(lambda acc, d: {**acc, **d}, configs, {})
print(merged)                    # Output: {'a': 1, 'b': 2, 'c': 3}
```

#### FlatMap

```python
# === Flatten nested lists ===
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [x for sublist in nested for x in sublist]
print(flattened)                 # Output: [1, 2, 3, 4, 5, 6]
# Đọc: "for sublist in nested → for x in sublist → thêm x"

# Tương đương dùng itertools.chain
from itertools import chain
flattened = list(chain.from_iterable(nested))
print(flattened)                 # Output: [1, 2, 3, 4, 5, 6]

# === Map + Flatten (FlatMap) ===
words = ["hello", "world"]
chars = [ch for word in words for ch in word]
print(chars)                     # Output: ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

# Real-world: lấy tất cả tags từ list bài viết
posts = [
    {"title": "Post 1", "tags": ["python", "coding"]},
    {"title": "Post 2", "tags": ["python", "web"]},
    {"title": "Post 3", "tags": ["coding", "tips"]},
]
all_tags = [tag for post in posts for tag in post["tags"]]
print(all_tags)                  # Output: ['python', 'coding', 'python', 'web', 'coding', 'tips']
unique_tags = list(set(all_tags))
print(sorted(unique_tags))       # Output: ['coding', 'python', 'tips', 'web']
```

#### Sort

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# === sorted() - trả về list MỚI (không thay đổi gốc) ===
sorted_nums = sorted(numbers)
print(sorted_nums)               # Output: [1, 1, 2, 3, 4, 5, 6, 9]
print(numbers)                   # Output: [3, 1, 4, 1, 5, 9, 2, 6] (không đổi!)

sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)               # Output: [9, 6, 5, 4, 3, 2, 1, 1]

# === list.sort() - sắp xếp IN-PLACE (thay đổi list gốc) ===
numbers.sort()
print(numbers)                   # Output: [1, 1, 2, 3, 4, 5, 6, 9] (đã thay đổi!)

# === Sort với key function ===
words = ["banana", "apple", "cherry", "date"]
print(sorted(words))             # Output: ['apple', 'banana', 'cherry', 'date'] (alphabetical)
print(sorted(words, key=len))    # Output: ['date', 'apple', 'banana', 'cherry'] (theo độ dài)

# Sort objects / dict
users = [
    {"name": "Charlie", "age": 35},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
]
by_age = sorted(users, key=lambda u: u["age"])
print([u["name"] for u in by_age])  # Output: ['Alice', 'Bob', 'Charlie']

# Sort với nhiều tiêu chí (ưu tiên: age tăng, name giảm)
from operator import itemgetter
students = [("Alice", 85), ("Bob", 90), ("Charlie", 85)]
result = sorted(students, key=lambda s: (-s[1], s[0]))
print(result)                    # Output: [('Bob', 90), ('Alice', 85), ('Charlie', 85)]

# === Stable sort ===
# Python dùng Timsort - STABLE (phần tử bằng nhau giữ thứ tự gốc)
```

#### Find/First/Last

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# === Find first match ===
# next() + generator expression → O(n) nhưng dừng sớm khi tìm thấy
result = next((x for x in numbers if x > 5), None)
print(result)                    # Output: 6 (phần tử đầu tiên > 5)

result = next((x for x in numbers if x > 100), None)
print(result)                    # Output: None (không tìm thấy → default)

# next() không có default → StopIteration nếu không tìm thấy
# next(x for x in numbers if x > 100)  # ❌ StopIteration

# === Find index ===
print(numbers.index(3))          # Output: 2 (index đầu tiên của giá trị 3)
# numbers.index(99)              # ❌ ValueError: 99 is not in list

# Safe find index
idx = next((i for i, x in enumerate(numbers) if x > 5), -1)
print(idx)                       # Output: 5 (index của 6)

# === First / Last ===
print(numbers[0])                # Output: 1 (phần tử đầu)
print(numbers[-1])               # Output: 8 (phần tử cuối)

# First/Last N phần tử
print(numbers[:3])               # Output: [1, 2, 3] (3 phần tử đầu)
print(numbers[-3:])              # Output: [6, 7, 8] (3 phần tử cuối)

# === in - kiểm tra tồn tại ===
print(3 in numbers)              # Output: True  (O(n) cho list)
print(99 in numbers)             # Output: False

# ⚠️ Dùng set cho lookup nhanh O(1)
number_set = set(numbers)
print(3 in number_set)           # Output: True  (O(1))
```

#### Any/All/None

```python
numbers = [1, 2, 3, 4, 5]

# === any() - True nếu CÓ ÍT NHẤT 1 phần tử True ===
print(any(n > 3 for n in numbers))   # Output: True (4, 5 > 3)
print(any(n > 10 for n in numbers))  # Output: False (không có)
print(any([]))                       # Output: False (list rỗng)

# === all() - True nếu TẤT CẢ phần tử đều True ===
print(all(n > 0 for n in numbers))   # Output: True (tất cả > 0)
print(all(n > 3 for n in numbers))   # Output: False (1, 2, 3 ≤ 3)
print(all([]))                       # Output: True (⚠️ vacuous truth!)

# === Short-circuit: any/all dừng sớm ===
# any() dừng ngay khi tìm thấy True
# all() dừng ngay khi tìm thấy False
# → Hiệu quả cho list lớn

# === Kiểm tra None ===
data = [1, "hello", None, 3.14]
has_none = any(x is None for x in data)
print(has_none)                  # Output: True

all_valid = all(x is not None for x in data)
print(all_valid)                 # Output: False

# === Real-world: validate form data ===
form = {"name": "John", "email": "john@email.com", "age": "30"}
required_fields = ["name", "email", "age"]
all_filled = all(form.get(f) for f in required_fields)
print(all_filled)                # Output: True
```

#### GroupBy

```python
from itertools import groupby

# === itertools.groupby() - nhóm phần tử liên tiếp có cùng key ===
# ⚠️ DATA PHẢI ĐƯỢC SORT THEO KEY TRƯỚC KHI groupby!
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("a", 5)]

# Sai nếu không sort trước (phần tử "a" cuối không gộp!)
data.sort(key=lambda x: x[0])   # Sort theo key trước
for key, group in groupby(data, key=lambda x: x[0]):
    items = list(group)          # group là iterator - chỉ dùng 1 lần!
    print(f"{key}: {items}")
# Output:
#   a: [('a', 1), ('a', 2), ('a', 5)]
#   b: [('b', 3), ('b', 4)]

# === defaultdict - cách Pythonic hơn (không cần sort) ===
from collections import defaultdict

data = [("a", 1), ("b", 3), ("a", 2), ("b", 4), ("a", 5)]
grouped = defaultdict(list)
for key, value in data:
    grouped[key].append(value)
print(dict(grouped))             # Output: {'a': [1, 2, 5], 'b': [3, 4]}

# Real-world: nhóm users theo department
employees = [
    {"name": "Alice", "dept": "Engineering"},
    {"name": "Bob", "dept": "Marketing"},
    {"name": "Charlie", "dept": "Engineering"},
    {"name": "Diana", "dept": "Marketing"},
]
by_dept = defaultdict(list)
for emp in employees:
    by_dept[emp["dept"]].append(emp["name"])
print(dict(by_dept))
# Output: {'Engineering': ['Alice', 'Charlie'], 'Marketing': ['Bob', 'Diana']}
```

#### Chunk

```python
from itertools import islice

# === Chia list thành các nhóm nhỏ (chunks) ===
def chunk(lst, size):
    """Chia iterable thành chunks có kích thước size."""
    it = iter(lst)
    while batch := list(islice(it, size)):  # Walrus operator
        yield batch

numbers = [1, 2, 3, 4, 5, 6, 7]
result = list(chunk(numbers, 3))
print(result)                    # Output: [[1, 2, 3], [4, 5, 6], [7]]

# Python 3.12+: itertools.batched()
# from itertools import batched
# list(batched(numbers, 3))      # [((1, 2, 3), (4, 5, 6), (7,)]

# Cách khác dùng range
def chunk_v2(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

print(chunk_v2(numbers, 3))      # Output: [[1, 2, 3], [4, 5, 6], [7]]

# Real-world: batch processing
def process_in_batches(items, batch_size=100):
    for batch in chunk(items, batch_size):
        print(f"  Processing batch of {len(batch)} items")
        # db.bulk_insert(batch)

process_in_batches(list(range(250)), 100)
# Output: Processing batch of 100 items (x2) → Processing batch of 50 items
```

#### Take/Skip

```python
from itertools import islice, dropwhile, takewhile

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# === Take (lấy n phần tử đầu) ===
print(list(islice(numbers, 5)))  # Output: [1, 2, 3, 4, 5]
print(numbers[:5])               # Output: [1, 2, 3, 4, 5] (cách đơn giản hơn)

# === Skip (bỏ n phần tử đầu) ===
print(list(islice(numbers, 3, None)))  # Output: [4, 5, 6, 7, 8, 9, 10]
print(numbers[3:])               # Output: [4, 5, 6, 7, 8, 9, 10] (cách đơn giản hơn)

# === takewhile - lấy LIÊN TỤC khi điều kiện đúng ===
# Dừng ngay khi gặp phần tử KHÔNG thỏa
result = list(takewhile(lambda x: x < 5, numbers))
print(result)                    # Output: [1, 2, 3, 4]

# === dropwhile - bỏ LIÊN TỤC khi điều kiện đúng ===
# Bắt đầu lấy khi gặp phần tử KHÔNG thỏa
result = list(dropwhile(lambda x: x < 5, numbers))
print(result)                    # Output: [5, 6, 7, 8, 9, 10]

# === Slice nâng cao ===
print(numbers[2:7])              # Output: [3, 4, 5, 6, 7] (index 2 đến 6)
print(numbers[::2])              # Output: [1, 3, 5, 7, 9] (every 2nd, step=2)
print(numbers[1::2])             # Output: [2, 4, 6, 8, 10] (mỗi 2 từ index 1)
print(numbers[::-1])             # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (đảo ngược)

# ⚠️ islice() hoạt động với BẤT KỲ iterator (file, generator)
# Slice [:] chỉ hoạt động với sequence (list, tuple, str)
```

#### Zip

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

# === zip() - ghép cặp từ nhiều iterables ===
combined = list(zip(names, ages))
print(combined)                  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Zip 3+ iterables
profiles = list(zip(names, ages, cities))
print(profiles)
# Output: [('Alice', 25, 'NYC'), ('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]

# ⚠️ zip() dừng ở iterable NGẮN NHẤT
short = [1, 2]
long = [10, 20, 30, 40]
print(list(zip(short, long)))    # Output: [(1, 10), (2, 20)] (bỏ 30, 40)

# zip_longest() - pad với fillvalue
from itertools import zip_longest
print(list(zip_longest(short, long, fillvalue=0)))
# Output: [(1, 10), (2, 20), (0, 30), (0, 40)]

# === Unzip - tách zip ===
pairs = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
names_out, ages_out = zip(*pairs)  # * unpacks list of tuples
print(names_out)                 # Output: ('Alice', 'Bob', 'Charlie')
print(ages_out)                  # Output: (25, 30, 35)

# === enumerate = zip(range(n), iterable) ===
for i, name in enumerate(names, start=1):  # start=1: bắt đầu từ 1
    print(f"{i}. {name}")
# Output: 1. Alice / 2. Bob / 3. Charlie

# === Real-world: tạo dict từ 2 lists ===
keys = ["name", "age", "city"]
values = ["John", 30, "NYC"]
user_dict = dict(zip(keys, values))
print(user_dict)                 # Output: {'name': 'John', 'age': 30, 'city': 'NYC'}
```

---

### 2.7. String Operations

#### Concatenation

```python
# === Nối chuỗi ===

# + operator (tạo string mới mỗi lần → chậm trong vòng lặp)
greeting = "Hello " + "World"
print(greeting)                  # Output: Hello World

# join() - hiệu quả nhất cho nối nhiều strings
parts = ["Hello", "World", "Python"]
print(" ".join(parts))           # Output: Hello World Python
print("-".join(parts))           # Output: Hello-World-Python
print("".join(parts))            # Output: HelloWorldPython

# f-string (Python 3.6+) - rõ ràng nhất
name = "Python"
version = 3.12
print(f"Hello {name} {version}") # Output: Hello Python 3.12

# ⚠️ KHÔNG nên nối string bằng + trong vòng lặp
# result = ""
# for i in range(10000):
#     result += str(i)           # ❌ Chậm - tạo string mới mỗi lần
# ✅ Dùng: "".join(str(i) for i in range(10000))
```

#### Interpolation

```python
name = "Python"
version = 3.12
pi = 3.14159265

# === f-string (Python 3.6+) - KHUYẾN KHÍCH ===
print(f"{name} {version}")       # Output: Python 3.12

# f-string formatting
print(f"{pi:.2f}")               # Output: 3.14 (2 decimal places)
print(f"{1234567:,}")            # Output: 1,234,567 (thousands separator)
print(f"{0.85:.1%}")             # Output: 85.0% (percentage)
print(f"{42:08d}")               # Output: 00000042 (zero-padded 8 chars)
print(f"{42:#x}")                # Output: 0x2a (hex)
print(f"{42:#b}")                # Output: 0b101010 (binary)
print(f"{'hello':>15}")          # Output: '          hello' (right-aligned 15 chars)
print(f"{'hello':^15}")          # Output: '     hello     ' (center-aligned)
print(f"{'hello':<15}")          # Output: 'hello          ' (left-aligned)

# f-string expressions
items = [1, 2, 3]
print(f"Count: {len(items)}")    # Output: Count: 3
print(f"{'even' if 4 % 2 == 0 else 'odd'}")  # Output: even

# Python 3.12+: f-string có thể chứa multiline expressions
# f"result = {
#     some_long_function_call()
# }"

# === str.format() - cú pháp cũ hơn ===
print("Hello {}".format(name))   # Output: Hello Python
print("Hello {0} {1}".format(name, version))  # Output: Hello Python 3.12
print("Hello {name}".format(name="World"))    # Output: Hello World

# === % formatting - cũ nhất (tránh dùng) ===
print("Hello %s, version %.1f" % (name, version))  # Output: Hello Python, version 3.1
```

#### Template String

```python
from string import Template

# === Template - an toàn cho user input (tránh injection) ===
template = Template("Hello $name! You have $count messages.")
result = template.substitute(name="John", count=5)
print(result)                    # Output: Hello John! You have 5 messages.

# safe_substitute() - không lỗi khi thiếu biến
result = template.safe_substitute(name="John")
print(result)                    # Output: Hello John! You have $count messages.
# (giữ nguyên $count thay vì raise KeyError)

# ⚠️ Khi nào dùng Template:
# ✅ Khi string đến từ user input (tránh injection)
# ✅ Khi template nằm trong config file
# ❌ Cho code thường → dùng f-string
```

#### Split & Join

```python
text = "hello world python"

# === split() - tách string thành list ===
print(text.split())              # Output: ['hello', 'world', 'python'] (tách theo whitespace)
print(text.split('o'))           # Output: ['hell', ' w', 'rld pyth', 'n']

# split(maxsplit) - giới hạn số lần tách
print("a.b.c.d".split(".", 2))   # Output: ['a', 'b', 'c.d'] (chỉ tách 2 lần)

# rsplit() - tách từ phải sang
print("a.b.c.d".rsplit(".", 1))  # Output: ['a.b.c', 'd']

# splitlines() - tách theo dòng
multi = "line1\nline2\nline3"
print(multi.splitlines())        # Output: ['line1', 'line2', 'line3']

# partition() - tách thành 3 phần (trước, sep, sau)
print("user@domain.com".partition("@"))
# Output: ('user', '@', 'domain.com')

# === join() - nối list thành string ===
words = ["hello", "world"]
print("-".join(words))           # Output: hello-world
print(", ".join(words))          # Output: hello, world

# ⚠️ join() chỉ hoạt động với list of STRINGS
# "-".join([1, 2, 3])           # ❌ TypeError
print("-".join(map(str, [1, 2, 3])))  # Output: 1-2-3
```

#### Replace

```python
text = "Hello World World"

# === str.replace(old, new, count) ===
print(text.replace("World", "Python"))      # Output: Hello Python Python (thay TẤT CẢ)
print(text.replace("World", "Python", 1))   # Output: Hello Python World (chỉ thay 1 lần)

# === Regex replace ===
import re
result = re.sub(r'\d+', '#', "test 123 abc 456")
print(result)                    # Output: test # abc #

# Replace với function
def double_number(match):
    return str(int(match.group()) * 2)

result = re.sub(r'\d+', double_number, "price: 100, tax: 10")
print(result)                    # Output: price: 200, tax: 20

# translate() - thay thế nhiều ký tự cùng lúc
table = str.maketrans("aeiou", "12345")
print("hello world".translate(table))  # Output: h2ll4 w4rld
```

#### Regex

```python
import re

text = "My email is john@example.com and phone is 0123-456-789"

# === search() - tìm match ĐẦU TIÊN ===
match = re.search(r'[\w.-]+@[\w.-]+', text)
if match:
    print(match.group())         # Output: john@example.com
    print(match.start(), match.end())  # Output: 12 28 (vị trí)

# === findall() - tìm TẤT CẢ matches ===
numbers = re.findall(r'\d+', text)
print(numbers)                   # Output: ['0123', '456', '789']

# === Named groups (?P<name>) ===
pattern = r'(?P<user>[\w.-]+)@(?P<domain>[\w.-]+)'
match = re.search(pattern, text)
if match:
    print(match.group('user'))   # Output: john
    print(match.group('domain')) # Output: example.com
    print(match.groupdict())     # Output: {'user': 'john', 'domain': 'example.com'}

# === match() vs search() ===
# match(): kiểm tra TỪ ĐẦU string
# search(): tìm BẤT KỲ ĐÂU trong string
print(re.match(r'\d+', "abc 123"))   # Output: None (không match từ đầu)
print(re.search(r'\d+', "abc 123"))  # Output: <Match '123'>

# === Compile pattern (tối ưu khi dùng nhiều lần) ===
EMAIL_PATTERN = re.compile(r'[\w.-]+@[\w.-]+\.\w+')
emails = EMAIL_PATTERN.findall("contact john@a.com or jane@b.org")
print(emails)                    # Output: ['john@a.com', 'jane@b.org']

# === split() với regex ===
result = re.split(r'[,;\s]+', "apple, banana; cherry  date")
print(result)                    # Output: ['apple', 'banana', 'cherry', 'date']

# === Common patterns ===
# Email:    r'[\w.-]+@[\w.-]+\.\w+'
# Phone:    r'\d{3,4}[-.]?\d{3,4}[-.]?\d{3,4}'
# URL:      r'https?://[\w./%-]+'
# IP:       r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
```

#### Substring

```python
text = "Hello World"

# === Slicing ===
print(text[0:5])                 # Output: Hello
print(text[:5])                  # Output: Hello (bỏ start = 0)
print(text[6:])                  # Output: World (bỏ end = cuối)
print(text[-5:])                 # Output: World (5 ký tự cuối)
print(text[::2])                 # Output: HloWrd (mỗi 2 ký tự)

# === Tìm kiếm ===
print(text.index("World"))      # Output: 6 (index đầu tiên)
print(text.find("World"))       # Output: 6 (index đầu tiên)
print(text.find("xyz"))         # Output: -1 (không tìm thấy)
# text.index("xyz")              # ❌ ValueError

print(text.count("l"))          # Output: 3 (đếm số lần xuất hiện)

# === Kiểm tra ===
print(text.startswith("Hello"))  # Output: True
print(text.endswith("World"))    # Output: True
print("hello123".isalnum())      # Output: True (chỉ chữ + số)
print("hello".isalpha())         # Output: True (chỉ chữ)
print("123".isdigit())           # Output: True (chỉ số)
print("  ".isspace())            # Output: True (chỉ whitespace)

# === Case methods ===
print("hello".upper())          # Output: HELLO
print("HELLO".lower())          # Output: hello
print("hello world".title())    # Output: Hello World
print("hello world".capitalize())  # Output: Hello world
print("Hello".swapcase())       # Output: hELLO

# === Trim whitespace ===
text = "  hello  "
print(text.strip())              # Output: hello (trim cả 2 đầu)
print(text.lstrip())             # Output: 'hello  ' (trim trái)
print(text.rstrip())             # Output: '  hello' (trim phải)
print("...hello...".strip("."))  # Output: hello (trim ký tự cụ thể)
```

#### Multi-line String

```python
# === Triple quotes - string nhiều dòng ===
multi = """This is
a multi-line
string"""
print(multi)
# Output:
#   This is
#   a multi-line
#   string

# Dùng \ để tránh newline đầu tiên
multi = """\
Line 1
Line 2"""
print(multi)                     # Output: Line 1\nLine 2 (không có dòng trống đầu)

# === textwrap.dedent() - bỏ indentation thừa ===
import textwrap
def help_text():
    return textwrap.dedent("""\
        Usage: command [options]
        Options:
            -h  Show help
            -v  Verbose mode""")
print(help_text())
# Output: (không có indentation thừa)

# === Raw string r"..." - không xử lý escape sequences ===
raw = r"No escape: \n \t \\"
print(raw)                       # Output: No escape: \n \t \\ (in nguyên văn)

path = r"C:\Users\name\file.txt"
print(path)                      # Output: C:\Users\name\file.txt
# Không có r: "C:\Users\name\file.txt" → \n thành newline, \t thành tab

# === Byte string b"..." ===
data = b"Hello"
print(type(data))                # Output: <class 'bytes'>
print(data.decode("utf-8"))      # Output: Hello (bytes → str)
print("Hello".encode("utf-8"))   # Output: b'Hello' (str → bytes)
```

#### String Builder

```python
import io

# === Cách 1: list + join (HIỆU QUẢ NHẤT cho Python) ===
parts = []
for i in range(5):
    parts.append(f"item_{i}")
result = ", ".join(parts)
print(result)                    # Output: item_0, item_1, item_2, item_3, item_4

# === Cách 2: io.StringIO (cho streaming/write liên tục) ===
buffer = io.StringIO()
for i in range(5):
    buffer.write(f"line {i}\n")
result = buffer.getvalue()
buffer.close()
print(result)
# Output: line 0\nline 1\nline 2\nline 3\nline 4\n

# === Cách 3: generator + join (memory-efficient) ===
result = "\n".join(f"item {i}" for i in range(5))
print(result)                    # Output: item 0\nitem 1\n...item 4

# === Real-world: build HTML ===
def build_html(items):
    html = ["<ul>"]
    for item in items:
        html.append(f"  <li>{item}</li>")
    html.append("</ul>")
    return "\n".join(html)

print(build_html(["Apple", "Banana", "Cherry"]))
# Output:
#   <ul>
#     <li>Apple</li>
#     <li>Banana</li>
#     <li>Cherry</li>
#   </ul>

# ⚠️ So sánh hiệu suất:
# join():     O(n) - tạo string 1 lần
# += trong loop: O(n²) - tạo string mới mỗi lần
```

---

### 2.8. Union & Intersection Types

```python
from typing import Union, Optional

# === Union type (Python 3.5+) - giá trị có thể là NHIỀU kiểu ===
def process(value: Union[str, int]) -> str:
    """Nhận str hoặc int, trả về str."""
    return str(value)

print(process("hello"))          # Output: hello
print(process(42))               # Output: 42

# === Python 3.10+: dùng toán tử | (ngắn gọn hơn) ===
def process_v2(value: str | int) -> str:
    return str(value)

# === Optional = Union[X, None] ===
def greet(name: Optional[str] = None) -> str:
    return f"Hello, {name or 'World'}!"

print(greet("John"))             # Output: Hello, John!
print(greet())                   # Output: Hello, World!

# Python 3.10+:
def greet_v2(name: str | None = None) -> str:
    return f"Hello, {name or 'World'}!"

# === Type narrowing - thu hẹp kiểu bằng isinstance ===
def handle(value: str | int | list) -> str:
    if isinstance(value, str):
        return value.upper()     # Type checker biết đây là str
    elif isinstance(value, int):
        return str(value * 2)    # Type checker biết đây là int
    else:
        return str(len(value))   # Type checker biết đây là list

print(handle("hello"))           # Output: HELLO
print(handle(21))                # Output: 42
print(handle([1, 2, 3]))         # Output: 3

# === TypeGuard (Python 3.10+) - custom type narrowing ===
from typing import TypeGuard

def is_str_list(val: list) -> TypeGuard[list[str]]:
    """Kiểm tra list chỉ chứa strings."""
    return all(isinstance(x, str) for x in val)

def process_names(data: list) -> None:
    if is_str_list(data):
        # Type checker biết data là list[str] trong block này
        for name in data:
            print(name.upper())  # ✅ Gọi .upper() an toàn

process_names(["alice", "bob"])  # Output: ALICE / BOB

# === Type alias - đặt tên cho kiểu phức tạp ===
# Cú pháp cũ
UserId = int
UserName = str
UserInfo = dict[str, str | int]
JSON = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None

# Python 3.12+: type statement
# type UserId = int
# type JSON = dict[str, JSON] | list[JSON] | str | int | float | bool | None

# === NewType - tạo kiểu RIÊNG BIỆT (type-safe) ===
from typing import NewType

UserId = NewType('UserId', int)
OrderId = NewType('OrderId', int)

def get_user(user_id: UserId) -> dict:
    return {"id": user_id, "name": "John"}

uid = UserId(42)
oid = OrderId(100)
get_user(uid)                    # ✅ OK
# get_user(oid)                  # ❌ mypy error: OrderId ≠ UserId
# get_user(42)                   # ❌ mypy error: int ≠ UserId

# ⚠️ NewType chỉ kiểm tra tại type-check time
# Runtime: UserId(42) == 42 là True (vẫn là int)

# === Literal type - giới hạn giá trị cụ thể ===
from typing import Literal

def set_direction(direction: Literal["north", "south", "east", "west"]) -> None:
    print(f"Moving {direction}")

set_direction("north")           # ✅ OK
# set_direction("up")            # ❌ mypy error: "up" not in Literal
```

---

## 3. Tầng 3: OOP & Type Relationships

### 3.1. Class/Object

#### Class Definition

```python
# === Class cơ bản ===
class User:
    # Class attribute - chia sẻ giữa TẤT CẢ instances
    species = "Human"
    _count = 0                   # Đếm số instances

    def __init__(self, name: str, age: int):
        """Constructor - gọi khi tạo instance mới."""
        self.name = name         # Public attribute
        self._age = age          # Protected (convention: internal use)
        self.__email = None      # "Private" (name mangling → _User__email)
        User._count += 1         # Tăng counter

    # Instance method - nhận self
    def greet(self) -> str:
        return f"Hello, I'm {self.name}, {self._age} years old"

    # === Magic/Dunder methods ===
    def __str__(self) -> str:
        """Gọi bởi str(), print() - dành cho user."""
        return f"User({self.name})"

    def __repr__(self) -> str:
        """Gọi bởi repr(), debugger - dành cho developer."""
        return f"User(name={self.name!r}, age={self._age!r})"

    def __eq__(self, other) -> bool:
        """So sánh bằng ==."""
        if not isinstance(other, User):
            return NotImplemented     # ⚠️ Trả NotImplemented, KHÔNG phải False
        return self.name == other.name and self._age == other._age

    def __hash__(self) -> int:
        """Cần thiết nếu override __eq__ và muốn dùng trong set/dict."""
        return hash((self.name, self._age))

    def __len__(self) -> int:
        """Gọi bởi len()."""
        return len(self.name)

    @classmethod
    def get_count(cls) -> int:
        """Class method - truy cập class attributes."""
        return cls._count

    @staticmethod
    def validate_age(age: int) -> bool:
        """Static method - không cần self hay cls."""
        return 0 <= age <= 150

# Sử dụng:
user1 = User("John", 30)
user2 = User("Jane", 25)
print(user1.greet())             # Output: Hello, I'm John, 30 years old
print(user1)                     # Output: User(John) (gọi __str__)
print(repr(user1))               # Output: User(name='John', age=30) (gọi __repr__)
print(user1 == User("John", 30)) # Output: True (gọi __eq__)
print(len(user1))                # Output: 4 (gọi __len__)
print(User.get_count())          # Output: 2 (class method)
print(User.validate_age(200))    # Output: False (static method)
print(User.species)              # Output: Human (class attribute)
```

#### Data Class (Python 3.7+)

```python
from dataclasses import dataclass, field

# === @dataclass tự động tạo __init__, __repr__, __eq__ ===
@dataclass
class User:
    name: str                    # Required field
    age: int                     # Required field
    email: str = "unknown@example.com"  # Default value
    tags: list = field(default_factory=list)  # ⚠️ Mutable default PHẢI dùng field()

    def __post_init__(self):
        """Chạy SAU __init__ - dùng cho validation/transform."""
        self.email = self.email.lower()
        if self.age < 0:
            raise ValueError(f"Age must be >= 0, got {self.age}")

user = User("John", 30)
print(user)                      # Output: User(name='John', age=30, email='unknown@example.com', tags=[])
print(user == User("John", 30))  # Output: True (tự so sánh tất cả fields)

# === Frozen dataclass = immutable ===
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(3.0, 4.0)
print(p)                         # Output: Point(x=3.0, y=4.0)
# p.x = 10                      # ❌ FrozenInstanceError (immutable!)

# frozen=True → tự tạo __hash__ → dùng được trong set/dict
point_set = {Point(0, 0), Point(1, 1), Point(0, 0)}
print(len(point_set))            # Output: 2 (Point(0,0) bị deduplicate)

# === Dataclass với slots (Python 3.10+) - tiết kiệm memory ===
@dataclass(slots=True)
class LightUser:
    name: str
    age: int
# Dùng __slots__ thay vì __dict__ → nhanh hơn, nhẹ hơn

# === field() options ===
@dataclass
class Config:
    name: str
    debug: bool = False
    _internal: str = field(default="", repr=False)     # Ẩn khỏi repr
    created_at: float = field(default_factory=lambda: __import__('time').time())
```

#### Singleton

```python
# === Singleton Pattern - chỉ có DUY NHẤT 1 instance ===

# --- Cách 1: __new__ (classic) ---
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        self.value = value

s1 = Singleton("first")
s2 = Singleton("second")
print(s1 is s2)                  # Output: True (cùng 1 object!)
print(s1.value)                  # Output: second (⚠️ __init__ chạy lại!)

# --- Cách 2: Module-level singleton (Pythonic nhất) ---
# config.py
class _Config:
    def __init__(self):
        self.debug = False
        self.db_url = "sqlite:///app.db"

config = _Config()               # Tạo 1 lần khi import module
# Ở module khác: from config import config

# --- Cách 3: functools.lru_cache ---
from functools import lru_cache

@lru_cache(maxsize=1)
def get_database():
    print("Creating database connection...")
    return {"connection": "active"}

db1 = get_database()             # Output: Creating database connection...
db2 = get_database()             # (không in gì - cached!)
print(db1 is db2)                # Output: True
```

#### Factory Method

```python
# === Factory Method - tạo object qua @classmethod ===
import json

class User:
    def __init__(self, name: str, age: int, email: str = ""):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"User({self.name!r}, {self.age}, {self.email!r})"

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Tạo User từ dictionary."""
        return cls(
            name=data["name"],
            age=data.get("age", 0),
            email=data.get("email", ""),
        )

    @classmethod
    def from_json(cls, json_str: str) -> "User":
        """Tạo User từ JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)

    @classmethod
    def from_csv_line(cls, line: str) -> "User":
        """Tạo User từ CSV line."""
        parts = line.strip().split(",")
        return cls(name=parts[0], age=int(parts[1]), email=parts[2])

# Sử dụng:
u1 = User("John", 30)
u2 = User.from_dict({"name": "Jane", "age": 25, "email": "jane@a.com"})
u3 = User.from_json('{"name": "Bob", "age": 35}')
u4 = User.from_csv_line("Alice,28,alice@b.com")

print(u2)                        # Output: User('Jane', 25, 'jane@a.com')
print(u3)                        # Output: User('Bob', 35, '')
print(u4)                        # Output: User('Alice', 28, 'alice@b.com')
```

#### Builder Pattern

```python
# === Builder - xây dựng object phức tạp từng bước ===
class QueryBuilder:
    """SQL Query builder pattern."""
    def __init__(self, table: str):
        self._table = table
        self._columns = ["*"]
        self._conditions = []
        self._order_by = None
        self._limit = None

    def select(self, *columns: str) -> "QueryBuilder":
        self._columns = list(columns)
        return self                  # Return self cho method chaining

    def where(self, condition: str) -> "QueryBuilder":
        self._conditions.append(condition)
        return self

    def order_by(self, column: str, desc: bool = False) -> "QueryBuilder":
        self._order_by = f"{column} {'DESC' if desc else 'ASC'}"
        return self

    def limit(self, n: int) -> "QueryBuilder":
        self._limit = n
        return self

    def build(self) -> str:
        query = f"SELECT {', '.join(self._columns)} FROM {self._table}"
        if self._conditions:
            query += f" WHERE {' AND '.join(self._conditions)}"
        if self._order_by:
            query += f" ORDER BY {self._order_by}"
        if self._limit:
            query += f" LIMIT {self._limit}"
        return query

# Method chaining
query = (QueryBuilder("users")
    .select("name", "email")
    .where("age > 18")
    .where("active = true")
    .order_by("name")
    .limit(10)
    .build())
print(query)
# Output: SELECT name, email FROM users WHERE age > 18 AND active = true ORDER BY name ASC LIMIT 10
```

#### Inner/Nested Class

```python
# === Nested class - class bên trong class ===
class Outer:
    class Inner:
        def greet(self):
            return "Hello from Inner"

    def create_inner(self):
        return self.Inner()

inner = Outer.Inner()
print(inner.greet())             # Output: Hello from Inner

# === Real-world: LinkedList với Node bên trong ===
class LinkedList:
    class Node:
        """Node nội bộ - chi tiết implementation."""
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node

        def __repr__(self):
            return f"Node({self.value})"

    def __init__(self):
        self.head = None
        self._size = 0

    def add(self, value):
        """Thêm phần tử vào đầu."""
        self.head = self.Node(value, self.head)
        self._size += 1

    def __len__(self):
        return self._size

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

ll = LinkedList()
ll.add(3); ll.add(2); ll.add(1)
print(list(ll))                  # Output: [1, 2, 3]
print(len(ll))                   # Output: 3
```

---

### 3.2. Kế Thừa & Đa Hình (Inheritance & Polymorphism)

#### Inheritance

```python
# === Kế thừa cơ bản ===
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."

# Kế thừa từ Animal
class Dog(Animal):
    def speak(self) -> str:            # Override method
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:            # Override method
        return "Meow!"

# Sử dụng:
dog = Dog("Buddy")
print(dog.name)                  # Output: Buddy (kế thừa từ Animal)
print(dog.speak())               # Output: Woof!

# type checking:
print(isinstance(dog, Dog))      # Output: True
print(isinstance(dog, Animal))   # Output: True
print(issubclass(Dog, Animal))   # Output: True
```

#### Super

```python
# === super() - gọi method/constructor của class cha ===
class Animal:
    def __init__(self, name: str):
        self.name = name

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        # ⚠️ BẮT BUỘC gọi super().__init__ nếu override __init__
        # Nếu không, self.name sẽ không được gán!
        super().__init__(name)
        self.breed = breed

    def speak(self) -> str:
        # Gọi method của class cha
        parent_speech = super().speak() if hasattr(super(), 'speak') else "..."
        return f"{parent_speech} Woof! I am a {self.breed}"

dog = Dog("Max", "Husky")
print(dog.name)                  # Output: Max (nhờ super().__init__)
print(dog.breed)                 # Output: Husky
print(dog.speak())               # Output: ... Woof! I am a Husky
```

#### Abstract Class

```python
# === Abstract Base Class (ABC) - class không thể khởi tạo ===
from abc import ABC, abstractmethod

class Animal(ABC):               # Kế thừa ABC
    def __init__(self, name: str):
        self.name = name

    @abstractmethod              # BẮT BUỘC subclass phải implement
    def speak(self) -> str:
        pass

    def describe(self) -> str:   # Concrete method (đã có code)
        return f"{self.name} says {self.speak()}"

class Dog(Animal):
    # Phải implement speak(), nếu không sẽ lỗi
    def speak(self) -> str:
        return "Woof!"

# test_animal = Animal("Test")   # ❌ TypeError: Can't instantiate abstract class
dog = Dog("Buddy")               # ✅ OK
print(dog.describe())            # Output: Buddy says Woof!
```

#### Polymorphism

```python
# === Đa hình (Polymorphism) - cùng 1 hàm xử lý nhiều kiểu dữ liệu ===

# Dù là Dog hay Cat, miễn là kế thừa Animal (và có implement speak)
def make_speak(animal: Animal) -> str:
    return animal.speak()

animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(make_speak(animal))    # Tự động gọi đúng method
# Output:
#   Woof!
#   Meow!

# ⚠️ Python là ngôn ngữ Duck Typing:
# Thật ra không cần kế thừa Animal, chỉ cần class có method speak()
# là make_speak sẽ chạy được (nếu không khai báo type hint chặt chẽ)
class Robot:
    def speak(self): return "Beep boop"
# mypy sẽ báo lỗi, nhưng runtime Python vẫn chạy OK!
```

#### Multiple Inheritance

```python
# === Đa kế thừa (Multiple Inheritance) - kế thừa nhiều class cùng lúc ===
class Flyable:
    def fly(self) -> str:
        return "Flying!"

class Swimmable:
    def swim(self) -> str:
        return "Swimming!"

# Duck kế thừa cả 2
class Duck(Flyable, Swimmable):
    def quack(self) -> str:
        return "Quack!"

duck = Duck()
print(duck.fly())                # Output: Flying!
print(duck.swim())               # Output: Swimming!
print(duck.quack())              # Output: Quack!

# ⚠️ Hạn chế dùng Multiple Inheritance nếu cấu trúc phức tạp
# Nên ưu tiên Composition hoặc Mixins (trait).
```

#### Diamond Problem (MRO)

```python
# === Vấn đề kim cương & MRO (Method Resolution Order) ===
# Cấu trúc: A <- B, A <- C, D(B, C)
class A:
    def method(self) -> str:
        return "A"

class B(A):
    def method(self) -> str:
        return "B"

class C(A):
    def method(self) -> str:
        return "C"

class D(B, C):
    pass                         # D không override, sẽ dùng method cha

d = D()
# Câu hỏi: D.method() sẽ gọi B.method() hay C.method() hay A.method()?
print(d.method())                # Output: B

# Python giải quyết bằng MRO (C3 Linearization algorithm)
# Thứ tự tìm kiếm method của ng từ con → cha, từ trái → phải
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
#          <class '__main__.A'>, <class 'object'>)
```

#### Composition (thành phần hơn kế thừa)

```python
# === Composition over Inheritance ===
# Kế thừa (IS-A): Dog "là một" Animal
# Composition (HAS-A): Car "có một" Engine
# → Composition linh hoạt hơn, dễ test và thay đổi hơn.

class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def roll(self):
        return "Wheels rolling"

class Car:
    def __init__(self):
        # KHÔNG kế thừa, mà "chứa" các đối tượng bên trong
        self.engine = Engine()
        self.wheels = Wheels()

    def drive(self) -> str:
        # Gọi (delegate) cho từng thành phần xử lý
        return f"{self.engine.start()}, {self.wheels.roll()}"

car = Car()
print(car.drive())               # Output: Engine started, Wheels rolling

# Nếu muốn thay Engine khác (V8, Electric), chỉ cần truyền vào lúc khởi tạo
# (xem thêm pattern Dependency Injection ở phần 11)
```

#### Sealed/Final Class

```python
# === Hạn chế kế thừa / ghi đè (từ Python 3.8+) ===
from typing import final

@final
class Singleton:
    """Class này KHÔNG THỂ bị kế thừa."""
    pass

# Lỗi khi check bằng mypy:
# class MySingleton(Singleton):  # ❌ mypy error: Cannot inherit from final class
#     pass

class Base:
    def normal_method(self):
        pass

    @final
    def critical_method(self):
        """Method này KHÔNG THỂ bị override ở subclass."""
        return "Do not override me"

# ⚠️ LƯU Ý QUAN TRỌNG:
# @final chỉ có tác dụng khi dùng các tool kiểm tra kiểu tĩnh (mypy, pyright).
# Tại runtime (khi code chạy), Python KHÔNG NGĂN CẢN bạn kế thừa hay override.
```

#### Delegation

```python
# === Delegation - "ủy quyền" xử lý cho object khác ===

# 1. Ủy quyền tự động (thông qua __getattr__)
class Printer:
    def print_document(self, doc: str) -> str:
        return f"Printing: {doc}"

    def get_ink_level(self) -> int:
        return 85

class OfficeMachine:
    def __init__(self):
        self._printer = Printer()  # Thành phần nội bộ

    def __getattr__(self, name: str):
        # Nếu gọi method mà OfficeMachine không có,
        # tự động đẩy qua cho _printer thử xử lý!
        return getattr(self._printer, name)

machine = OfficeMachine()
# OfficeMachine KHÔNG DẠY print_document, nhưng tự động đẩy qua Printer!
print(machine.print_document("Report"))  # Output: Printing: Report
print(machine.get_ink_level())           # Output: 85

# 2. Ủy quyền minh bạch (Explicit Delegation) - An toàn hơn
class Stack:
    """Stack bọc ngoài một List, chỉ cho phép push/pop (không cho index)."""
    def __init__(self):
        self._list = []

    def push(self, item):
        self._list.append(item)    # Delegate to list.append

    def pop(self):
        return self._list.pop()    # Delegate to list.pop

    def __len__(self):
        return len(self._list)     # Delegate to len(list)
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
# === Python KHÔNG có private/protected/public keyword ===
# Dùng naming convention (quy ước đặt tên):

class Example:
    public_var = "I am public"        # Public - ai cũng truy cập được
    _protected_var = "I am protected"  # Protected - QUY ƯỚC nội bộ (vẫn truy cập được)
    __private_var = "I am private"    # "Private" - Name mangling

    def public_method(self):
        """Public method - API bên ngoài dùng."""
        return "Public"

    def _protected_method(self):
        """Protected - dùng nội bộ, subclass có thể dùng."""
        return "Protected"

    def __private_method(self):
        """'Private' - bị name mangling, khó truy cập từ bên ngoài."""
        return "Private"

obj = Example()

# --- Public: truy cập bình thường ---
print(obj.public_var)              # Output: I am public
print(obj.public_method())         # Output: Public

# --- Protected (_): QUY ƯỚC, vẫn truy cập được ---
print(obj._protected_var)         # Output: I am protected ← ⚠️ Convention: không nên dùng ngoài class
print(obj._protected_method())    # Output: Protected

# --- "Private" (__): Name Mangling ---
# Python đổi tên __attr thành _ClassName__attr
# print(obj.__private_var)         # ❌ AttributeError: no attribute '__private_var'
print(obj._Example__private_var)   # Output: I am private ← ⚠️ Vẫn truy cập được!
print(obj._Example__private_method())  # Output: Private

# === Name Mangling giải thích ===
# __var  →  _ClassName__var  (đổi tên, không phải private thật)
# Mục đích: tránh xung đột tên khi kế thừa, KHÔNG phải bảo mật
class Parent:
    __secret = "parent"

class Child(Parent):
    __secret = "child"             # Không override Parent.__secret!

c = Child()
print(c._Parent__secret)           # Output: parent
print(c._Child__secret)            # Output: child

# === Property - controlled access (getter/setter) ===
class User:
    def __init__(self, name: str, age: int):
        self._name = name          # _name: protected
        self._age = age            # Sẽ validate qua setter

    @property
    def name(self) -> str:
        """Getter - gọi khi truy cập user.name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Setter - gọi khi gán user.name = ...."""
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if not 0 <= value <= 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value

    @property
    def display(self) -> str:
        """Read-only property (không có setter)."""
        return f"{self._name} (age: {self._age})"

user = User("John", 30)
print(user.name)                   # Output: John (gọi getter)
print(user.display)                # Output: John (age: 30) (read-only property)

user.name = "Jane"                 # Gọi setter
print(user.name)                   # Output: Jane

# user.name = ""                   # ❌ ValueError: Name must be a non-empty string
# user.age = 200                   # ❌ ValueError: Age must be between 0 and 150
# user.display = "test"            # ❌ AttributeError: can't set (no setter)

# ⚠️ Quy tắc Pythonic:
# 1. Bắt đầu với public attribute
# 2. Chỉ dùng property khi CẦN validation/computation
# 3. Dùng _ cho "internal use", __ hiếm khi cần (chỉ khi tránh name clash)
# 4. "We're all consenting adults here" - tin tưởng lập trình viên
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

#### Lazy Property

```python
# functools.cached_property (Python 3.8+)
from functools import cached_property

class DataLoader:
    @cached_property
    def data(self):
        print("Loading data...")  # Chỉ chạy 1 lần
        return [1, 2, 3, 4, 5]

loader = DataLoader()
loader.data  # "Loading data..." -> [1, 2, 3, 4, 5]
loader.data  # [1, 2, 3, 4, 5] (không load lại)

# Manual lazy property
class Config:
    def __init__(self):
        self._settings = None

    @property
    def settings(self):
        if self._settings is None:
            self._settings = self._load_settings()
        return self._settings

    def _load_settings(self):
        return {"debug": True}
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

#### Lock/Mutex

```python
import threading
import asyncio

# Threading Lock
lock = threading.Lock()
counter = 0

def safe_increment():
    global counter
    with lock:  # Acquire và release tự động
        counter += 1

# RLock - Reentrant Lock (có thể acquire nhiều lần từ cùng thread)
rlock = threading.RLock()

# Async Lock
async def async_safe():
    lock = asyncio.Lock()
    async with lock:
        # Critical section
        pass

# Read-Write Lock (dùng RLock pattern)
import threading

class ReadWriteLock:
    def __init__(self):
        self._read_lock = threading.Lock()
        self._write_lock = threading.Lock()
        self._readers = 0

    def acquire_read(self):
        with self._read_lock:
            self._readers += 1
            if self._readers == 1:
                self._write_lock.acquire()

    def release_read(self):
        with self._read_lock:
            self._readers -= 1
            if self._readers == 0:
                self._write_lock.release()
```

#### Atomic & GIL

```python
# Python có GIL (Global Interpreter Lock)
# - Chỉ 1 thread chạy Python bytecode tại 1 thời điểm
# - Thích hợp I/O-bound, không tốt cho CPU-bound
# - Dùng multiprocessing cho CPU-bound

import threading

# Một số operations đã atomic nhờ GIL
# Nhưng không nên dựa vào, luôn dùng Lock

# threading.Event - flag thread-safe
event = threading.Event()
event.set()     # Set flag
event.clear()   # Clear flag
event.wait()    # Wait until set
event.is_set()  # Check flag
```

#### Future/Promise

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Future
import asyncio

# concurrent.futures.Future
with ThreadPoolExecutor(max_workers=3) as executor:
    future = executor.submit(pow, 2, 10)  # Submit task
    result = future.result()               # Block until done -> 1024
    future.done()                          # True

    # Multiple futures
    futures = [executor.submit(pow, 2, n) for n in range(5)]
    from concurrent.futures import as_completed
    for f in as_completed(futures):
        print(f.result())

# asyncio Future/Task
async def main():
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    future.set_result(42)
    result = await future  # 42
```

#### Channel (asyncio.Queue)

```python
import asyncio

async def producer(queue: asyncio.Queue):
    for i in range(5):
        await queue.put(i)
        print(f"Produced: {i}")
    await queue.put(None)  # Sentinel

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=10)
    await asyncio.gather(
        producer(queue),
        consumer(queue)
    )

asyncio.run(main())

# multiprocessing Queue
from multiprocessing import Queue, Process

def mp_producer(q):
    q.put("hello")

q = Queue()
p = Process(target=mp_producer, args=(q,))
p.start()
print(q.get())  # "hello"
p.join()
```

#### Race Condition & Deadlock

```python
import threading

# Race condition ví dụ - KHÔNG AN TOÀN
counter = 0

def unsafe_increment():
    global counter
    for _ in range(100000):
        counter += 1  # Race condition!

# Giải pháp: dùng Lock
lock = threading.Lock()

def safe_increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

# Deadlock prevention
# - Luôn acquire locks theo thứ tự nhất quán
# - Dùng timeout
lock1 = threading.Lock()
lock2 = threading.Lock()

def safe_order():
    with lock1:        # Luôn lock1 trước
        with lock2:    # Rồi lock2 sau
            pass

# Dùng timeout
if lock1.acquire(timeout=5):
    try:
        if lock2.acquire(timeout=5):
            try:
                pass  # Critical section
            finally:
                lock2.release()
    finally:
        lock1.release()
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

### 6.2. Reactive Programming

```python
# === Observer Pattern (built-in Python - không cần thư viện) ===
# Reactive programming = data streams + event-driven programming

from typing import Callable, Any

class EventEmitter:
    """Simple event emitter / observable pattern."""
    def __init__(self):
        self._listeners: dict[str, list[Callable]] = {}

    def on(self, event: str, callback: Callable) -> None:
        """Đăng ký listener cho event."""
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)
        print(f"  📡 Registered listener for '{event}'")

    def emit(self, event: str, *args: Any) -> None:
        """Phát event tới tất cả listeners."""
        for callback in self._listeners.get(event, []):
            callback(*args)

    def off(self, event: str, callback: Callable) -> None:
        """Hủy đăng ký listener."""
        if event in self._listeners:
            self._listeners[event].remove(callback)

# Sử dụng:
emitter = EventEmitter()

# Đăng ký listeners
emitter.on("user_created", lambda user: print(f"  ✅ Welcome {user['name']}!"))
emitter.on("user_created", lambda user: print(f"  📧 Sending email to {user['email']}"))
emitter.on("error", lambda msg: print(f"  ❌ Error: {msg}"))

# Phát event → tất cả listeners được gọi
emitter.emit("user_created", {"name": "John", "email": "john@example.com"})
# Output:
#   ✅ Welcome John!
#   📧 Sending email to john@example.com

emitter.emit("error", "Connection timeout")
# Output: ❌ Error: Connection timeout

# === Reactive stream với async generator (Python built-in) ===
import asyncio

async def number_stream(n: int):
    """Async generator - tạo stream số từ 0 đến n-1."""
    for i in range(n):
        await asyncio.sleep(0.1)       # Giả lập delay
        yield i

async def transform_stream(source):
    """Transform: nhân đôi mỗi giá trị."""
    async for value in source:
        yield value * 2

async def filter_stream(source, predicate):
    """Filter: chỉ giữ giá trị thỏa điều kiện."""
    async for value in source:
        if predicate(value):
            yield value

async def main():
    # Pipeline: số → nhân 2 → lọc > 4
    source = number_stream(6)                          # 0, 1, 2, 3, 4, 5
    doubled = transform_stream(source)                 # 0, 2, 4, 6, 8, 10
    filtered = filter_stream(doubled, lambda x: x > 4) # 6, 8, 10

    async for value in filtered:
        print(f"  Received: {value}")

# asyncio.run(main())
# Output:
#   Received: 6
#   Received: 8
#   Received: 10

# === RxPY - Reactive Extensions for Python (thư viện) ===
# pip install reactivex
import reactivex as rx
from reactivex import operators as ops

# Tạo Observable (stream dữ liệu)
source = rx.of(1, 2, 3, 4, 5)       # Stream từ list giá trị

# Pipe operators (giống Unix pipe)
source.pipe(
    ops.map(lambda x: x * 2),        # Nhân đôi: 2, 4, 6, 8, 10
    ops.filter(lambda x: x > 4),     # Lọc > 4: 6, 8, 10
    ops.reduce(lambda acc, x: acc + x)  # Tổng: 24
).subscribe(
    on_next=lambda x: print(f"  Result: {x}"),      # Nhận giá trị
    on_error=lambda e: print(f"  Error: {e}"),       # Xử lý lỗi
    on_completed=lambda: print("  ✅ Stream completed")  # Hoàn thành
)
# Output:
#   Result: 24
#   ✅ Stream completed

# Subject (Hot Observable - có thể push value vào)
from reactivex.subject import Subject

subject = Subject()
subject.subscribe(lambda x: print(f"  Observer 1: {x}"))
subject.subscribe(lambda x: print(f"  Observer 2: {x}"))
subject.on_next("Hello")          # Cả 2 observer đều nhận
# Output:
#   Observer 1: Hello
#   Observer 2: Hello

subject.on_next("World")
# Output:
#   Observer 1: World
#   Observer 2: World

# ⚠️ Khi nào dùng Reactive:
# ✅ Real-time data (WebSocket, sensor data, UI events)
# ✅ Complex event processing (combine, merge, debounce)
# ✅ Xử lý streams (log processing, message queues)
# ❌ Simple CRUD - overkill, dùng async/await đơn giản hơn
```

---

## 7. Tầng 7: Error Handling

### 7.1. Xử Lý Lỗi (Error Handling)

#### Try-Except

```python
# === try-except cơ bản ===
try:
    result = 10 / 0              # Chia cho 0 → ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")         # Output: Error: division by zero
    print(f"Type: {type(e).__name__}")  # Output: Type: ZeroDivisionError

# === Bắt nhiều loại exception ===
try:
    x = int("abc")               # ValueError: invalid literal for int()
    y = 10 / 0                   # Không bao giờ chạy tới (đã lỗi ở dòng trên)
except ValueError as e:
    print(f"Value error: {e}")   # Output: Value error: invalid literal for int() with base 10: 'abc'
except ZeroDivisionError as e:
    print(f"Division error: {e}")

# === Bắt nhiều exception cùng handler ===
try:
    data = [1, 2, 3]
    print(data[10])              # IndexError
except (IndexError, KeyError, TypeError) as e:
    print(f"Access error: {type(e).__name__}: {e}")
    # Output: Access error: IndexError: list index out of range

# === Catch all (Exception) - nên có logging ===
try:
    x = int("abc")
except Exception as e:           # Bắt MỌI exception (trừ SystemExit, KeyboardInterrupt)
    print(f"Unexpected: {type(e).__name__}: {e}")
    # Output: Unexpected: ValueError: invalid literal for int() with base 10: 'abc'

# ⚠️ KHÔNG BAO GIỜ dùng bare except (không có Exception)
# try: ...
# except:         # ❌ Bắt cả SystemExit, KeyboardInterrupt!
#     pass

# === try-except-else-finally ===
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ Cannot divide by zero")
        return None
    else:
        # Chạy khi KHÔNG CÓ exception (thay vì đặt trong try)
        print(f"✅ {a} / {b} = {result}")
        return result
    finally:
        # LUÔN chạy, dù có exception hay không, dù có return hay không
        print("🔄 Cleanup done")

print(safe_divide(10, 3))
# Output:
#   ✅ 10 / 3 = 3.3333333333333335
#   🔄 Cleanup done
#   3.3333333333333335

print(safe_divide(10, 0))
# Output:
#   ❌ Cannot divide by zero
#   🔄 Cleanup done
#   None
```

#### Raise Exception

```python
# === raise - ném exception ===
def validate_age(age: int) -> int:
    """Validate tuổi - raise ValueError nếu không hợp lệ."""
    if not isinstance(age, int):
        raise TypeError(f"Expected int, got {type(age).__name__}")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError(f"Age {age} is unrealistic (max: 150)")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Invalid: {e}")       # Output: Invalid: Age cannot be negative

# === Exception chaining (from) ===
def process_data(raw):
    try:
        return int(raw)
    except ValueError as original:
        # raise ... from ... → liên kết exception gốc
        raise RuntimeError(f"Failed to process: {raw!r}") from original

try:
    process_data("abc")
except RuntimeError as e:
    print(f"Error: {e}")         # Output: Error: Failed to process: 'abc'
    print(f"Caused by: {e.__cause__}")  # Output: Caused by: invalid literal...

# === Re-raise exception ===
def log_and_reraise():
    try:
        1 / 0
    except ZeroDivisionError:
        print("Logging error...")
        raise                    # Re-raise exception hiện tại (giữ traceback gốc)
```

#### Custom Exception

```python
# === Custom exception với thông tin bổ sung ===
class ValidationError(Exception):
    """Exception cho lỗi validation."""
    def __init__(self, field: str, message: str, value=None):
        self.field = field
        self.value = value
        self.message = message
        super().__init__(f"{field}: {message}")

    def to_dict(self) -> dict:
        """Chuyển thành dict (hữu ích cho API response)."""
        return {
            "field": self.field,
            "message": self.message,
            "value": self.value,
        }

# Sử dụng:
try:
    email = "invalid-email"
    if "@" not in email:
        raise ValidationError("email", "Must contain @", value=email)
except ValidationError as e:
    print(f"Validation failed: {e}")    # Output: Validation failed: email: Must contain @
    print(f"Details: {e.to_dict()}")
    # Output: Details: {'field': 'email', 'message': 'Must contain @', 'value': 'invalid-email'}
```

#### Finally Block

```python
# === finally LUÔN chạy - dù có exception, return, hay break ===
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")      # Output: File not found
finally:
    print("Cleanup!")            # Output: Cleanup! (luôn chạy)
    # file.close()               # Đóng file nếu đã mở

# === with statement thay thế try-finally (khuyến khích) ===
# with đảm bảo __exit__() luôn được gọi
try:
    with open("data.txt", "r") as file:
        content = file.read()    # File tự đóng khi thoát with
except FileNotFoundError:
    print("File not found")

# ⚠️ finally chạy TRƯỚC return
def test():
    try:
        return "from try"
    finally:
        print("finally runs!")   # Chạy TRƯỚC khi return

result = test()
# Output: finally runs!
print(result)                    # Output: from try
```

#### Exception Propagation

```python
# === Exception tự động lan truyền lên call stack ===
def level3():
    raise ValueError("Error in level3")

def level2():
    level3()                     # Exception propagates lên

def level1():
    try:
        level2()                 # Bắt exception từ level3
    except ValueError as e:
        print(f"Caught at level1: {e}")
        # Output: Caught at level1: Error in level3
        raise                    # Re-raise để caller xử lý tiếp

# === Exception Groups (Python 3.11+) ===
# Xử lý NHIỀU exception xảy ra đồng thời (concurrent errors)
# try:
#     async with asyncio.TaskGroup() as tg:
#         tg.create_task(task1())
#         tg.create_task(task2())
# except* ValueError as eg:      # except* cho ExceptionGroup
#     for e in eg.exceptions:
#         print(f"ValueError: {e}")
# except* TypeError as eg:
#     for e in eg.exceptions:
#         print(f"TypeError: {e}")
```

#### Assertion

```python
# === assert - kiểm tra điều kiện debug ===
# Cú pháp: assert condition, "error message"
# ⚠️ BỊ DISABLE khi chạy python -O (optimized mode)

items = [1, 2, 3]
assert len(items) > 0, "List must not be empty"
# Không lỗi vì len > 0

assert isinstance("hello", str), f"Expected str"
# Không lỗi vì "hello" là str

# Khi assertion fails:
# assert 1 == 2, "Math is broken"
# ❌ AssertionError: Math is broken

# === Khi nào dùng assert ===
# ✅ Debugging - kiểm tra assumptions trong code
# ✅ Internal consistency checks
# ✅ Postconditions (kết quả function đúng)
# ❌ KHÔNG dùng cho input validation (vì bị disable với -O)
# ❌ KHÔNG dùng cho security checks

def divide(a, b):
    assert b != 0, "Divisor must not be zero"  # ❌ KHÔNG NÊN - dùng if + raise
    return a / b

# ✅ Đúng cách:
def safe_divide(a, b):
    if b == 0:
        raise ValueError("Divisor must not be zero")
    return a / b

# ⚠️ assert trả về None
# x = assert True  # ❌ SyntaxError (assert là statement, không phải expression)
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
# === Monkey Patching - thêm/thay đổi method runtime ===
# Python cho phép sửa class BẤT KỲ lúc nào (nguy hiểm nhưng có ích)

# --- Thêm method vào class có sẵn ---
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Định nghĩa function rồi gán vào class
def greet(self) -> str:
    return f"Hello, I'm {self.name}!"

Person.greet = greet             # Thêm method mới vào class Person

person = Person("John", 30)
print(person.greet())            # Output: Hello, I'm John!

# --- Thêm property ---
Person.display_name = property(
    lambda self: f"{self.name} (age: {self.age})"
)
print(person.display_name)       # Output: John (age: 30)

# --- Override method built-in ---
original_str = str.upper         # Lưu method gốc

# ⚠️ Không thể monkey patch built-in types trực tiếp
# str.shout = lambda self: self.upper() + "!!!"
# ❌ TypeError: cannot set attributes of built-in type

# Nhưng có thể subclass:
class MyStr(str):
    def shout(self):
        return self.upper() + "!!!"

s = MyStr("hello")
print(s.shout())                 # Output: HELLO!!!

# --- Real-world: monkey patching cho testing ---
import json

class APIClient:
    def fetch(self, url: str) -> dict:
        """Gọi API thật."""
        import urllib.request
        response = urllib.request.urlopen(url)
        return json.loads(response.read())

# Trong test: thay thế fetch() bằng fake
def fake_fetch(self, url: str) -> dict:
    return {"status": "ok", "data": []}

# Patch cho testing
APIClient.fetch = fake_fetch
client = APIClient()
print(client.fetch("https://api.example.com"))
# Output: {'status': 'ok', 'data': []}

# ⚠️ Warnings về Monkey Patching:
# ❌ Khó debug - behavior thay đổi runtime
# ❌ Khó maintain - code ở nơi khác thay đổi class
# ❌ Conflicts - 2 module cùng patch 1 class
# ✅ Dùng unittest.mock thay vì manual monkey patching
# ✅ Dùng Protocol/ABC cho extensibility có cấu trúc
```

---

### 8.3. Operator Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Arithmetic Operators
    def __add__(self, other):       # +
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):       # -
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):      # *
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):  # /
        return Vector(self.x / scalar, self.y / scalar)

    def __neg__(self):              # unary -
        return Vector(-self.x, -self.y)

    # Comparison Operators
    def __eq__(self, other):        # ==
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):        # <
        return abs(self) < abs(other)

    def __le__(self, other):        # <=
        return abs(self) <= abs(other)

    # Subscript Operator
    def __getitem__(self, index):   # []
        return (self.x, self.y)[index]

    def __setitem__(self, index, value):  # [] =
        if index == 0: self.x = value
        elif index == 1: self.y = value

    # Logical/Container
    def __len__(self):              # len()
        return 2

    def __bool__(self):             # bool()
        return self.x != 0 or self.y != 0

    def __abs__(self):              # abs()
        return (self.x**2 + self.y**2) ** 0.5

    def __contains__(self, value):  # in
        return value in (self.x, self.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Usage
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2       # Vector(4, 6)
v4 = v1 * 3        # Vector(3, 6)
v1 == v2            # False
v1[0]               # 1
len(v1)             # 2
```

### 8.4. Circular Dependency

```python
# Circular import problem
# module_a.py
# from module_b import func_b  # Error!

# Giải pháp 1: Import trong function
def my_func():
    from module_b import func_b
    func_b()

# Giải pháp 2: Import module thay vì import function
import module_b
module_b.func_b()

# Giải pháp 3: Tách interface ra module riêng
# interfaces.py -> module_a.py imports from interfaces
#               -> module_b.py imports from interfaces

# Giải pháp 4: TYPE_CHECKING (chỉ import cho type hints)
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from module_b import ClassB  # Chỉ import khi type checking

def process(obj: 'ClassB') -> None:  # String annotation
    pass
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

#### WebSocket

```python
# pip install websockets
import asyncio
import websockets

# Server
async def handler(websocket):
    async for message in websocket:
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # Run forever

# Client
async def client():
    async with websockets.connect("ws://localhost:8765") as ws:
        await ws.send("Hello")
        response = await ws.recv()
        print(response)  # "Echo: Hello"
```

#### SSE (Server-Sent Events)

```python
# Server (FastAPI)
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def event_generator():
    for i in range(10):
        yield f"data: Event {i}\n\n"
        await asyncio.sleep(1)

@app.get("/events")
async def sse():
    return StreamingResponse(event_generator(), media_type="text/event-stream")

# Client
import requests

response = requests.get("http://localhost:8000/events", stream=True)
for line in response.iter_lines():
    print(line.decode())
```

#### Middleware

```python
# Flask middleware
from flask import Flask, request

app = Flask(__name__)

@app.before_request
def before_request():
    print(f"Before: {request.method} {request.path}")

@app.after_request
def after_request(response):
    print(f"After: {response.status_code}")
    return response

# FastAPI middleware
from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

#### Stream & Buffer

```python
import io

# BytesIO - binary buffer
buf = io.BytesIO()
buf.write(b"Hello World")
buf.seek(0)
data = buf.read()  # b"Hello World"

# StringIO - text buffer
buf = io.StringIO()
buf.write("Hello\n")
buf.write("World\n")
buf.seek(0)
content = buf.getvalue()  # "Hello\nWorld\n"

# BufferedReader/Writer
with open("file.bin", "rb") as f:
    reader = io.BufferedReader(f)
    chunk = reader.read(1024)  # Read 1KB chunks
```

#### Async File I/O

```python
# pip install aiofiles
import aiofiles
import asyncio

async def read_file():
    async with aiofiles.open("data.txt", mode="r") as f:
        content = await f.read()
    return content

async def write_file():
    async with aiofiles.open("output.txt", mode="w") as f:
        await f.write("Hello async world!")

asyncio.run(read_file())
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

### 9.5. Async File I/O (aiofiles)

Xem section [Async File I/O](#async-file-io) ở trên.

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

### 10.5. YAML/TOML

```python
# YAML - pip install pyyaml
import yaml

# Read YAML
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Write YAML
with open('output.yaml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)

# Parse string
yaml_str = """
name: John
age: 30
skills:
  - Python
  - Django
"""
data = yaml.safe_load(yaml_str)

# TOML (Python 3.11+ built-in)
import tomllib  # Python 3.11+

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)

# Older Python: pip install tomli
import tomli
with open('config.toml', 'rb') as f:
    config = tomli.load(f)

# Write TOML: pip install tomli-w
import tomli_w
with open('output.toml', 'wb') as f:
    tomli_w.dump(config, f)
```

### 10.6. Binary Serialization (struct)

```python
import struct

# Pack (Python -> bytes)
packed = struct.pack('iif', 1, 2, 3.14)
# i = int (4 bytes), f = float (4 bytes)

# Unpack (bytes -> Python)
a, b, c = struct.unpack('iif', packed)
# a=1, b=2, c=3.14

# MessagePack - pip install msgpack
import msgpack

data = {"name": "John", "age": 30}
packed = msgpack.packb(data)
unpacked = msgpack.unpackb(packed)  # {'name': 'John', 'age': 30}

# Protobuf - pip install protobuf
# Requires .proto file compilation
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
# === Dependency Injection (DI) - tách rời dependency khỏi class ===
# Thay vì class TỰ TẠO dependency, ta TRUYỀN dependency vào từ bên ngoài
# → Dễ test, dễ thay đổi, loose coupling

# --- Pattern 1: Constructor Injection (phổ biến nhất) ---
from abc import ABC, abstractmethod

# Định nghĩa interface (Abstract Base Class)
class Repository(ABC):
    @abstractmethod
    def find(self, id: int) -> dict | None:
        """Tìm entity theo ID."""
        ...

    @abstractmethod
    def save(self, data: dict) -> None:
        """Lưu entity."""
        ...

# Implementation thật - kết nối database
class PostgresRepository(Repository):
    def __init__(self, connection_string: str):
        self.conn_str = connection_string

    def find(self, id: int) -> dict | None:
        # Giả lập query database
        print(f"[Postgres] SELECT * FROM users WHERE id = {id}")
        return {"id": id, "name": "John"}

    def save(self, data: dict) -> None:
        print(f"[Postgres] INSERT INTO users VALUES ({data})")

# Implementation giả - cho testing
class InMemoryRepository(Repository):
    def __init__(self):
        self._store: dict[int, dict] = {}

    def find(self, id: int) -> dict | None:
        return self._store.get(id)

    def save(self, data: dict) -> None:
        self._store[data["id"]] = data

# Service nhận Repository qua constructor (DI!)
class UserService:
    def __init__(self, repository: Repository):
        self.repo = repository   # KHÔNG tự tạo Repository, nhận từ bên ngoài

    def get_user(self, id: int) -> dict | None:
        return self.repo.find(id)

    def create_user(self, name: str) -> dict:
        user = {"id": 1, "name": name}
        self.repo.save(user)
        return user

# Production:
prod_repo = PostgresRepository("postgresql://localhost/mydb")
prod_service = UserService(prod_repo)
print(prod_service.get_user(1))
# Output: [Postgres] SELECT * FROM users WHERE id = 1
# Output: {'id': 1, 'name': 'John'}

# Testing (thay đổi dependency dễ dàng!):
test_repo = InMemoryRepository()
test_service = UserService(test_repo)
test_service.create_user("Alice")
print(test_service.get_user(1))  # Output: {'id': 1, 'name': 'Alice'}

# --- Pattern 2: Factory / Provider ---
from typing import Callable

class NotificationService:
    def __init__(self, sender_factory: Callable[[str], None]):
        self.send = sender_factory

    def notify(self, message: str):
        self.send(message)

# Inject khác nhau tùy môi trường
def email_sender(msg: str): print(f"📧 Email: {msg}")
def sms_sender(msg: str): print(f"📱 SMS: {msg}")
def console_sender(msg: str): print(f"🖥️ Console: {msg}")

# Production
service = NotificationService(email_sender)
service.notify("Order confirmed")  # Output: 📧 Email: Order confirmed

# Development
dev_service = NotificationService(console_sender)
dev_service.notify("Order confirmed")  # Output: 🖥️ Console: Order confirmed

# --- Pattern 3: Simple DI Container ---
class Container:
    """DI Container đơn giản - registry cho dependencies."""
    def __init__(self):
        self._factories: dict[type, Callable] = {}

    def register(self, interface: type, factory: Callable):
        """Đăng ký factory cho interface."""
        self._factories[interface] = factory

    def resolve(self, interface: type):
        """Tạo instance cho interface."""
        factory = self._factories.get(interface)
        if factory is None:
            raise ValueError(f"No factory registered for {interface}")
        return factory()

# Sử dụng
container = Container()
container.register(Repository, lambda: InMemoryRepository())
container.register(UserService, lambda: UserService(container.resolve(Repository)))

user_service = container.resolve(UserService)
user_service.create_user("Bob")
print(user_service.get_user(1))  # Output: {'id': 1, 'name': 'Bob'}

# ⚠️ Cho DI phức tạp hơn, dùng thư viện:
# - dependency-injector (phổ biến nhất)
# - inject
# - python-inject
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
# === Reflection - kiểm tra và thao tác object tại runtime ===

class MyClass:
    class_attr = "value"

    def __init__(self):
        self.instance_attr = 42

    def method(self):
        return "hello"

obj = MyClass()

# --- type() và isinstance() ---
print(type(obj))                 # Output: <class '__main__.MyClass'>
print(type(obj).__name__)        # Output: MyClass
print(isinstance(obj, MyClass))  # Output: True

# --- Class metadata ---
print(MyClass.__name__)          # Output: MyClass (tên class)
print(MyClass.__module__)        # Output: __main__ (module chứa class)
print(MyClass.__bases__)         # Output: (<class 'object'>,) (class cha)
print(MyClass.__mro__)           # Method Resolution Order
# Output: (<class 'MyClass'>, <class 'object'>)

# --- __dict__ - namespace dict ---
print(MyClass.__dict__.keys())   # Class attributes + methods
# Output: dict_keys(['__module__', 'class_attr', '__init__', 'method', ...])
print(obj.__dict__)              # Instance attributes chỉ
# Output: {'instance_attr': 42}

# --- dir() vs vars() ---
# dir(): TẤT CẢ attributes (kể cả kế thừa và dunder)
# vars(): chỉ __dict__ của object (instance attributes)
print(len(dir(obj)))             # Output: ~30+ (bao gồm __dunder__)
print(vars(obj))                 # Output: {'instance_attr': 42}

# --- hasattr, getattr, setattr, delattr ---
print(hasattr(obj, "instance_attr"))   # Output: True (kiểm tra attribute tồn tại)
print(hasattr(obj, "missing"))         # Output: False

print(getattr(obj, "instance_attr"))   # Output: 42 (lấy giá trị)
print(getattr(obj, "missing", "N/A"))  # Output: N/A (default nếu không tồn tại)

setattr(obj, "new_attr", "dynamic!")   # Thêm attribute runtime
print(obj.new_attr)                    # Output: dynamic!

delattr(obj, "new_attr")              # Xóa attribute
# print(obj.new_attr)                 # ❌ AttributeError

# === Real-world: dynamic dispatch ===
def call_method(obj, method_name: str, *args):
    """Gọi method bằng tên (string) - hữu ích cho plugin systems."""
    method = getattr(obj, method_name, None)
    if method and callable(method):
        return method(*args)
    raise AttributeError(f"{type(obj).__name__} has no method '{method_name}'")

result = call_method(obj, "method")
print(result)                    # Output: hello
```

#### Introspection

```python
import inspect

# === inspect module - phân tích code tại runtime ===

def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting message."""
    return f"{greeting}, {name}!"

# --- Function signature ---
sig = inspect.signature(greet)
print(sig)                       # Output: (name: str, greeting: str = 'Hello') -> str

for param_name, param in sig.parameters.items():
    default = param.default if param.default != inspect.Parameter.empty else "required"
    annotation = param.annotation.__name__ if param.annotation != inspect.Parameter.empty else "any"
    print(f"  {param_name}: {annotation} = {default}")
# Output:
#   name: str = required
#   greeting: str = Hello

# --- Source code ---
source = inspect.getsource(greet)
print(source)                    # In ra source code của function

# --- File location ---
print(inspect.getfile(inspect))  # Output: /path/to/inspect.py

# --- Kiểm tra loại object ---
print(inspect.isclass(MyClass))   # Output: True
print(inspect.isfunction(greet))  # Output: True
print(inspect.ismethod(obj.method))  # Output: True
print(callable(greet))            # Output: True (kiểm tra có gọi được không)

# --- Lấy members của class ---
for name, method in inspect.getmembers(MyClass, predicate=inspect.isfunction):
    print(f"  {name}: {inspect.signature(method)}")
# Output: __init__: (self) / method: (self)

# === Real-world: auto-register plugins ===
def get_public_methods(cls):
    """Lấy danh sách public methods của class."""
    return [
        name for name, _ in inspect.getmembers(cls, predicate=inspect.isfunction)
        if not name.startswith('_')
    ]

print(get_public_methods(MyClass))  # Output: ['method']
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

#### FFI (Foreign Function Interface)

```python
# ctypes - gọi C functions từ Python
import ctypes

# Load shared library
lib = ctypes.CDLL('./mylib.so')  # Linux
# lib = ctypes.CDLL('./mylib.dll')  # Windows

# Call C function
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int
result = lib.add(3, 4)  # 7

# cffi - pip install cffi
from cffi import FFI
ffi = FFI()
ffi.cdef("int add(int, int);")
lib = ffi.dlopen('./mylib.so')
result = lib.add(3, 4)  # 7

# C extension module (setup.py)
# Dùng Cython, pybind11, hoặc Python C API
```

#### Lazy Evaluation

```python
# Python generators là lazy evaluation
def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Không tạo tất cả giá trị cùng lúc
for x in lazy_range(1_000_000):
    if x > 10:
        break

# itertools - lazy operations
from itertools import islice, count

# Lấy 5 số chẵn đầu tiên từ dãy vô hạn
evens = (x for x in count(0) if x % 2 == 0)
first_5_evens = list(islice(evens, 5))  # [0, 2, 4, 6, 8]

# map/filter trả về iterator lazy
numbers = range(1_000_000)
squared = map(lambda x: x**2, numbers)  # Lazy!
filtered = filter(lambda x: x > 100, squared)  # Still lazy!
first_10 = list(islice(filtered, 10))  # Chỉ tính 10 giá trị
```

#### DSL (Domain-Specific Language)

```python
# Python cho phép tạo DSL đơn giản với:
# - Operator overloading
# - Decorators
# - Context managers
# - Metaclasses

# Ví dụ: Query DSL
class Query:
    def __init__(self, table):
        self._table = table
        self._conditions = []

    def where(self, condition):
        self._conditions.append(condition)
        return self  # Fluent interface

    def select(self, *fields):
        self._fields = fields
        return self

    def build(self):
        sql = f"SELECT {', '.join(self._fields)} FROM {self._table}"
        if self._conditions:
            sql += " WHERE " + " AND ".join(self._conditions)
        return sql

# Usage
query = (Query("users")
    .select("name", "email")
    .where("age > 18")
    .where("active = true")
    .build())
# "SELECT name, email FROM users WHERE age > 18 AND active = true"
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
# === "If it walks like a duck and quacks like a duck, it's a duck" ===
# Python không kiểm tra KIỂU của object, mà kiểm tra HÀNH VI (method/attribute)
# → Không cần implement interface/inherit class, chỉ cần có method đúng tên

class Duck:
    def speak(self):
        return "Quack!"

    def walk(self):
        return "Waddle waddle"

class Dog:
    def speak(self):
        return "Woof!"

    def walk(self):
        return "Tap tap tap"

class Cat:
    def speak(self):
        return "Meow!"

    def walk(self):
        return "Soft padding"

# Hàm này KHÔNG quan tâm kiểu - chỉ cần có .speak()
def make_speak(animal):
    """Bất kỳ object nào có method speak() đều dùng được."""
    return animal.speak()

# Cả 3 class đều hoạt động - không cần kế thừa chung!
print(make_speak(Duck()))  # Output: Quack!
print(make_speak(Dog()))   # Output: Woof!
print(make_speak(Cat()))   # Output: Meow!

# ⚠️ Lỗi nếu object không có method cần thiết
class Rock:
    pass

# make_speak(Rock())  # ❌ AttributeError: 'Rock' object has no attribute 'speak'

# === Protocol (Python 3.8+) - "Interface" cho duck typing ===
# Protocol cho phép type checker kiểm tra duck typing mà không cần kế thừa
from typing import Protocol, runtime_checkable

@runtime_checkable                   # Cho phép kiểm tra isinstance()
class Speakable(Protocol):
    def speak(self) -> str: ...      # Chỉ khai báo signature, không implement

class Parrot:
    def speak(self) -> str:
        return "Polly wants a cracker!"

# Type checker đảm bảo Parrot có .speak() → thỏa mãn Speakable
def greet(obj: Speakable) -> str:
    return f"Animal says: {obj.speak()}"

print(greet(Parrot()))                 # Output: Animal says: Polly wants a cracker!
print(isinstance(Parrot(), Speakable)) # Output: True (nhờ @runtime_checkable)
print(isinstance(Rock(), Speakable))   # Output: False

# === Real-world: file-like objects ===
# Nhiều object hoạt động như file: StringIO, BytesIO, socket, HTTP response...
from io import StringIO

def read_data(source):
    """Đọc data từ bất kỳ object nào có .read() method."""
    return source.read()

# Hoạt động với file thật
# with open("data.txt") as f:
#     print(read_data(f))

# Hoạt động với StringIO (fake file)
fake_file = StringIO("Hello from StringIO!")
print(read_data(fake_file))        # Output: Hello from StringIO!

# === Ưu điểm Duck Typing ===
# ✅ Linh hoạt - không cần kế thừa/interface
# ✅ Dễ test - tạo mock object đơn giản
# ✅ Dễ mở rộng - thêm class mới không cần sửa code cũ
#
# ⚠️ Nhược điểm:
# ❌ Lỗi runtime thay vì compile-time
# ❌ Khó biết object cần method gì → dùng Protocol để document
```

---

### 17.2. Context Managers

```python
# === Context Manager = quản lý tài nguyên với with statement ===
# Đảm bảo tài nguyên được giải phóng dù có exception hay không

# --- Pattern cơ bản: __enter__ và __exit__ ---
class FileManager:
    """Context manager đọc file an toàn."""
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Gọi khi vào with block - mở tài nguyên."""
        self.file = open(self.filename, self.mode)
        print(f"📂 Opened {self.filename}")
        return self.file         # Giá trị gán cho biến sau 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Gọi khi thoát with block - LUÔN chạy, kể cả có exception.

        Args:
            exc_type: Loại exception (None nếu không có)
            exc_val:  Giá trị exception
            exc_tb:   Traceback
        Returns:
            True để suppress exception, False để re-raise
        """
        if self.file:
            self.file.close()
        print(f"📁 Closed {self.filename}")
        return False             # False = không nuốt exception

# Sử dụng:
# with FileManager("test.txt", "w") as f:
#     f.write("Hello!")
# Output: 📂 Opened test.txt → 📁 Closed test.txt

# --- contextlib.contextmanager - tạo CM bằng generator (đơn giản hơn) ---
from contextlib import contextmanager
import time

@contextmanager
def timer(label=""):
    """Đo thời gian thực thi code block."""
    start = time.time()
    print(f"⏱️ [{label}] Starting...")
    try:
        yield                    # Code trong with block chạy ở đây
    finally:
        elapsed = time.time() - start
        print(f"⏱️ [{label}] Done in {elapsed:.3f}s")

with timer("Processing"):
    total = sum(range(1_000_000))
# Output: ⏱️ [Processing] Starting...
# Output: ⏱️ [Processing] Done in 0.025s

# --- contextlib.contextmanager trả về giá trị ---
@contextmanager
def database_connection(db_url):
    """Tạo và tự động đóng database connection."""
    print(f"🔌 Connecting to {db_url}")
    conn = {"url": db_url, "connected": True}  # Giả lập connection
    try:
        yield conn                # Trả connection cho with block
    except Exception as e:
        print(f"❌ Error: {e}")
        # conn.rollback()        # Rollback nếu lỗi
    finally:
        conn["connected"] = False
        print(f"🔌 Disconnected from {db_url}")

with database_connection("postgresql://localhost/mydb") as conn:
    print(f"Using connection: {conn}")
# Output:
#   🔌 Connecting to postgresql://localhost/mydb
#   Using connection: {'url': 'postgresql://localhost/mydb', 'connected': True}
#   🔌 Disconnected from postgresql://localhost/mydb

# --- Built-in context managers ---
# File I/O
with open("output.txt", "w") as f:
    f.write("Hello")             # File tự động đóng khi thoát with

# Threading lock
import threading
lock = threading.Lock()
with lock:                       # Tự acquire/release lock
    pass  # critical section

# Suppress exceptions
from contextlib import suppress
with suppress(FileNotFoundError):
    # open("nonexistent.txt")    # Không raise lỗi, chỉ bỏ qua
    pass

# --- Multiple context managers (Python 3.10+ with parentheses) ---
# with (
#     open("input.txt") as fin,
#     open("output.txt", "w") as fout,
# ):
#     fout.write(fin.read())

# === Real-world: temporary directory ===
import tempfile
import os

with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Temp dir: {tmpdir}")     # Tự tạo thư mục tạm
    filepath = os.path.join(tmpdir, "test.txt")
    with open(filepath, "w") as f:
        f.write("temporary data")
# Khi thoát with → thư mục tạm bị XÓA hoàn toàn

# ⚠️ Lưu ý:
# - Luôn dùng with cho file I/O, DB connections, locks
# - __exit__ LUÔN chạy → đảm bảo cleanup
# - Return True trong __exit__ để suppress exception (dùng cẩn thận!)
```

---

## 18. Tầng 18: Standard Library

### 18.1. Collections

```python
# === List - dynamic array (mutable, ordered) ===
lst = [1, 2, 3]
lst.append(4)                    # Thêm cuối: [1, 2, 3, 4]
lst.insert(0, 0)                 # Chèn tại index 0: [0, 1, 2, 3, 4]
lst.pop()                        # Xóa + trả về phần tử cuối: 4, list = [0, 1, 2, 3]
lst.pop(0)                       # Xóa + trả về tại index 0: 0, list = [1, 2, 3]
lst.remove(2)                    # Xóa phần tử đầu tiên có giá trị 2: [1, 3]
lst.extend([4, 5])               # Nối thêm iterable: [1, 3, 4, 5]
lst.sort()                       # Sắp xếp in-place: [1, 3, 4, 5]
lst.reverse()                    # Đảo ngược in-place: [5, 4, 3, 1]
print(lst.index(3))              # Output: 2 (index đầu tiên của giá trị 3)
print(lst.count(3))              # Output: 1 (đếm số lần xuất hiện)

# === Deque - efficient append/pop from both ends (O(1)) ===
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)                 # Thêm đầu: deque([0, 1, 2, 3])
dq.append(4)                     # Thêm cuối: deque([0, 1, 2, 3, 4])
print(dq.popleft())              # Output: 0 (xóa đầu - O(1), list là O(n)!)
print(dq.pop())                  # Output: 4 (xóa cuối)
print(dq)                        # Output: deque([1, 2, 3])

# Deque rotation
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)                     # Xoay phải 2 vị trí
print(dq)                        # Output: deque([4, 5, 1, 2, 3])
dq.rotate(-1)                    # Xoay trái 1 vị trí
print(dq)                        # Output: deque([5, 1, 2, 3, 4])

# Deque maxlen - circular buffer
buffer = deque(maxlen=3)         # Max 3 phần tử
buffer.append(1)                 # deque([1])
buffer.append(2)                 # deque([1, 2])
buffer.append(3)                 # deque([1, 2, 3])
buffer.append(4)                 # deque([2, 3, 4]) ← 1 bị loại bỏ!
print(buffer)                    # Output: deque([2, 3, 4], maxlen=3)

# === Dict operations ===
d = {"a": 1, "b": 2, "c": 3}
print(d.get("a"))                # Output: 1
print(d.get("z", 0))            # Output: 0 (default nếu key không tồn tại)
print(d.keys())                  # Output: dict_keys(['a', 'b', 'c'])
print(d.values())                # Output: dict_values([1, 2, 3])
print(d.items())                 # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

d.setdefault("d", 4)            # Thêm key 'd' với value 4 nếu chưa tồn tại
d.update({"e": 5, "a": 10})     # Merge + override: a=10, e=5
print(d["a"])                    # Output: 10

# === defaultdict - dict tự tạo default value ===
from collections import defaultdict

# Nhóm items theo key
words = ["apple", "banana", "avocado", "blueberry", "cherry"]
by_letter = defaultdict(list)    # Default = list rỗng
for word in words:
    by_letter[word[0]].append(word)  # Tự tạo list nếu key chưa tồn tại
print(dict(by_letter))
# Output: {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

# Đếm với defaultdict(int)
counter = defaultdict(int)       # Default = 0
for char in "hello world":
    counter[char] += 1           # Tự bắt đầu từ 0
print(dict(counter))
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# === Counter - đếm phần tử ===
from collections import Counter

cnt = Counter(["a", "b", "a", "c", "a", "b"])
print(cnt)                       # Output: Counter({'a': 3, 'b': 2, 'c': 1})
print(cnt["a"])                  # Output: 3
print(cnt["z"])                  # Output: 0 (không lỗi, trả về 0)
print(cnt.most_common(2))        # Output: [('a', 3), ('b', 2)]

# Counter arithmetic
cnt1 = Counter("aabbc")
cnt2 = Counter("abcdd")
print(cnt1 + cnt2)               # Output: Counter({'a': 3, 'b': 3, 'c': 2, 'd': 2})
print(cnt1 - cnt2)               # Output: Counter({'a': 1, 'b': 1}) (chỉ giữ positive)

# === Set operations ===
s = {1, 2, 3}
s.add(4)                         # Thêm: {1, 2, 3, 4}
s.discard(5)                     # Xóa (không lỗi nếu không tồn tại)
# s.remove(5)                    # ❌ KeyError nếu không tồn tại

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)                     # Output: {1, 2, 3, 4, 5, 6} (union)
print(a & b)                     # Output: {3, 4} (intersection)
print(a - b)                     # Output: {1, 2} (difference)
print(a ^ b)                     # Output: {1, 2, 5, 6} (symmetric difference)
print(a.issubset({1, 2, 3, 4, 5}))  # Output: True

# === frozenset - immutable set (dùng làm dict key) ===
fs = frozenset([1, 2, 3])
# fs.add(4)                      # ❌ AttributeError
d = {fs: "value"}               # ✅ frozenset có thể làm dict key (hashable)

# === Named tuple - tuple có tên field ===
from collections import namedtuple

# Tạo class Point với fields x, y
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x)                      # Output: 1 (truy cập bằng tên)
print(p.y)                      # Output: 2
print(p[0])                     # Output: 1 (truy cập bằng index)
print(p)                        # Output: Point(x=1, y=2)

# Named tuple là immutable
# p.x = 10                      # ❌ AttributeError: can't set attribute
p2 = p._replace(x=10)           # Tạo bản sao với field mới
print(p2)                       # Output: Point(x=10, y=2)

# ⚠️ Với Python 3.6+, khuyến khích dùng typing.NamedTuple:
from typing import NamedTuple

class Color(NamedTuple):
    r: int
    g: int
    b: int
    a: float = 1.0               # Default value

red = Color(255, 0, 0)
print(red)                       # Output: Color(r=255, g=0, b=0, a=1.0)
transparent_red = Color(255, 0, 0, 0.5)
print(transparent_red.a)         # Output: 0.5

# === ChainMap - gộp nhiều dict (lookup theo thứ tự) ===
from collections import ChainMap

defaults = {"color": "red", "size": "medium"}
user_prefs = {"color": "blue"}
env_vars = {"size": "large", "debug": "true"}

config = ChainMap(env_vars, user_prefs, defaults)  # Ưu tiên: env > user > default
print(config["color"])           # Output: blue (từ user_prefs)
print(config["size"])            # Output: large (từ env_vars)
print(config["debug"])           # Output: true (từ env_vars)
```

#### Heap/Priority Queue

```python
import heapq

# === Min heap - phần tử nhỏ nhất luôn ở gốc ===
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(numbers)           # Chuyển list thành heap - O(n)
print(numbers)                   # Output: [1, 1, 2, 6, 5, 9, 4, 3] (heap order)

heapq.heappush(numbers, 0)       # Push 0 vào heap - O(log n)
smallest = heapq.heappop(numbers)  # Pop phần tử nhỏ nhất - O(log n)
print(smallest)                  # Output: 0
print(heapq.heappop(numbers))    # Output: 1

# === N nhỏ nhất / lớn nhất ===
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(heapq.nsmallest(3, data))  # Output: [1, 1, 2]
print(heapq.nlargest(3, data))   # Output: [9, 6, 5]

# Với key function
users = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
youngest = heapq.nsmallest(2, users, key=lambda u: u[1])
print(youngest)                  # Output: [('Bob', 25), ('Alice', 30)]

# === Max heap (trick: dùng giá trị âm) ===
max_heap = []
for n in [3, 1, 4, 1, 5]:
    heapq.heappush(max_heap, -n)  # Đảo dấu khi push
largest = -heapq.heappop(max_heap)  # Đảo dấu khi pop
print(largest)                   # Output: 5

# === Priority Queue pattern ===
tasks = []
heapq.heappush(tasks, (1, "🔴 Critical: Fix crash"))
heapq.heappush(tasks, (3, "🟢 Low: Update docs"))
heapq.heappush(tasks, (2, "🟡 Medium: Add feature"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"  Priority {priority}: {task}")
# Output:
#   Priority 1: 🔴 Critical: Fix crash
#   Priority 2: 🟡 Medium: Add feature
#   Priority 3: 🟢 Low: Update docs

# === queue.PriorityQueue (thread-safe) ===
from queue import PriorityQueue

pq = PriorityQueue()
pq.put((1, "high"))
pq.put((3, "low"))
pq.put((2, "medium"))
print(pq.get())                  # Output: (1, 'high') - highest priority (smallest number)
print(pq.qsize())                # Output: 2

# ⚠️ PriorityQueue chậm hơn heapq nhưng thread-safe
# Dùng heapq cho single-thread, PriorityQueue cho multi-thread
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

### 19.4. Data Science & ML

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

### 19.5. Security & Cryptography

```python
# hashlib - hàm băm
import hashlib

hash_sha256 = hashlib.sha256(b"Hello").hexdigest()
hash_md5 = hashlib.md5(b"Hello").hexdigest()

# Password hashing - bcrypt
# pip install bcrypt
import bcrypt

password = b"my_password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
bcrypt.checkpw(password, hashed)  # True

# secrets - sinh số ngẫu nhiên an toàn
import secrets

token = secrets.token_hex(32)       # Token hex
token_url = secrets.token_urlsafe(32)  # Token URL-safe

# JWT - pip install PyJWT
import jwt

token = jwt.encode({"user_id": 123}, "secret", algorithm="HS256")
data = jwt.decode(token, "secret", algorithms=["HS256"])

# cryptography - pip install cryptography
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
encrypted = f.encrypt(b"Hello World")
decrypted = f.decrypt(encrypted)  # b"Hello World"
```

### 19.6. DevOps & Infrastructure

```python
# Docker
# Dockerfile cho Python
"""
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
"""

# Docker SDK - pip install docker
import docker
client = docker.from_env()
client.containers.list()

# Fabric - SSH automation
# pip install fabric
from fabric import Connection

conn = Connection('user@host')
result = conn.run('ls -la')
```

---

## 20. Tầng 20: Toolchain

### 20.1. Build & Package Management

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
requires-python = ">= 3.8"
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

### 20.2. Code Quality

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

### 20.3. IDE & Debugging

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

### 20.4. Profiling & Performance

```python
# cProfile - built-in profiler
import cProfile

def my_function():
    return sum(range(1000000))

cProfile.run('my_function()')

# Profile to file
cProfile.run('my_function()', 'output.prof')

# Visualize with snakeviz
# pip install snakeviz
# snakeviz output.prof

# timeit - benchmark
import timeit

timeit.timeit('sum(range(1000))', number=10000)

# line_profiler - pip install line_profiler
# @profile
# def my_function():
#     ...
# kernprof -l -v script.py

# memory_profiler - pip install memory_profiler
from memory_profiler import profile

@profile
def memory_heavy():
    return [i for i in range(1000000)]

# tracemalloc (built-in)
import tracemalloc

tracemalloc.start()
# ... code ...
snapshot = tracemalloc.take_snapshot()
top = snapshot.statistics('lineno')
for stat in top[:5]:
    print(stat)
```

### 20.5. Documentation & Publishing

```python
# Sphinx - sinh tài liệu
# pip install sphinx
# sphinx-quickstart docs/
# sphinx-build docs/ docs/_build/

# mkdocs - pip install mkdocs
# mkdocs new myproject
# mkdocs serve
# mkdocs build

# pdoc - simple doc generation
# pip install pdoc
# pdoc mymodule --output-dir docs/

# PyPI publishing
# pip install twine build
# python -m build
# twine upload dist/*
```

### 20.6. Runtime & Environment

```bash
# pyenv - quản lý phiên bản Python
pyenv install 3.11.0
pyenv global 3.11.0
pyenv local 3.11.0

# Implementations
# CPython - default, reference implementation
# PyPy - JIT compiler, faster for some workloads
# Jython - Python on JVM
# IronPython - Python on .NET

# REPL
python -i           # Interactive mode
ipython              # Enhanced REPL (pip install ipython)
jupyter notebook     # Jupyter (pip install jupyter)
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
