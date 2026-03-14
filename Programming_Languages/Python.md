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
# Python không cần từ khóa let/var/const - gán trực tiếp tên_biến = giá_trị
# Kiểu dữ liệu được xác định tự động tại runtime dựa trên giá trị gán

x = 10                    # Tạo biến x với giá trị 10 → Python tự nhận kiểu int
name = "Python"           # Tạo biến name với chuỗi "Python" → kiểu str (string)
is_active = True          # Tạo biến boolean với giá trị True (viết hoa đầu)
prices = [1.5, 2.0, 3.5]  # List (mảng) chứa các số thực - có thể thay đổi (mutable)
coords = (10, 20)         # Tuple - cặp giá trị cố định, KHÔNG thể thay đổi (immutable)
tags = {"python", "code"} # Set - tập hợp các phần tử DUY NHẤT, không trùng lặp
user = {"name": "John"}   # Dict (dictionary) - cặp key-value, tra cứu theo key

# === Type annotation (Python 3.5+) ===
# Cú pháp: ten_bien: kieu_du_lieu = gia_tri
# Chỉ là gợi ý cho IDE/type checker, KHÔNG enforce tại runtime
# Giúp IDE đề xuất autocomplete và phát hiện lỗi sớm

x: int = 10               # Gợi ý x thuộc kiểu int (số nguyên)
name: str = "Python"       # Gợi ý name thuộc kiểu str (chuỗi)
is_active: bool = True     # Gợi ý is_active thuộc kiểu bool (boolean)
prices: list[float] = [1.5, 2.0]  # Python 3.9+ - list chứa float (generic syntax)

# ⚠️ Lưu ý QUAN TRỌNG: annotation KHÔNG ngăn gán sai kiểu tại runtime
# Type annotation chỉ là "gợi ý" - Python hoàn toàn bỏ qua tại runtime
x: int = 10               # Khai báo x là int (gợi ý)
x = "hello"               # Gán string cho x - Python KHÔNG báo lỗi!
# Lý do: Python là dynamic typing, kiểu được xác định tại runtime
print(x)                   # Output: hello
print(type(x))             # Output: <class 'str'>  → x thực sự là string

# === Multiple assignment (gán nhiều biến cùng lúc) ===
# Tuple unpacking: Python tự động pack các giá trị thành tuple
a, b, c = 1, 2, 3         # Gán đồng thời a=1, b=2, c=3 (từ tuple ẩn)
x = y = z = 0             # Cả 3 biến cùng trỏ đến object 0 (cùng id)
print(a, b, c)             # Output: 1 2 3
print(x, y, z)             # Output: 0 0 0

# ⚠️ Edge case: multiple assignment với mutable object - NGUY HIỂM!
# Khi dùng = với mutable object (list, dict, set), TẤT CẢ biến trỏ cùng 1 object
a = b = []                # a và b cùng trỏ đến 1 list rỗng trong memory!
a.append(1)               # Thêm phần tử vào list mà a trỏ đến
print(b)                  # Output: [1]  ← b cũng bị ảnh hưởng! (cùng list)
# Giải pháp: tạo list riêng biệt cho mỗi biến
a, b = [], []              # Tạo 2 list ĐỘC LẬP trong memory
a.append(1)               # Chỉ thêm vào list a
print(b)                  # Output: []  ← b không bị ảnh hưởng

# === Augmented assignment (gán kết hợp toán tử) ===
# Cú pháp: bien_toan_tu= gia_tri  → bien = bien toan_tu gia_tri
count = 0                 # Khởi tạo count = 0
count += 1                # count = count + 1 → 1 (tăng 1 đơn vị)
count -= 1                # count = count - 1 → 0 (giảm 1 đơn vị)
count *= 5                # count = count * 5 → 0 (nhân với 5)
count //= 2               # count = count // 2 → 0 (chia lấy phần nguyên, 0//2=0)
count **= 3               # count = count ** 3 → 0 (lũy thừa, 0**3=0)

# === Real-world use case: Cấu hình ứng dụng ===
# Khai báo biến cấu hình theo quy ước UPPER_CASE
API_BASE_URL = "https://api.example.com/v1"  # URL API cố định
MAX_RETRY_ATTEMPTS = 3                         # Số lần thử lại tối đa
DEFAULT_TIMEOUT_SECONDS = 30                   # Timeout mặc định (giây)
ALLOWED_HTTP_METHODS = {"GET", "POST", "PUT", "DELETE"}  # Methods được phép

# Truy cập trong code
def call_api(endpoint):
    url = f"{API_BASE_URL}/{endpoint}"  # Nối chuỗi f-string
    print(f"Calling: {url}")            # Output: Calling: https://api.example.com/v1/endpoint
    return {"status": "success"}

# === Edge case: Tên biến không hợp lệ ===
# 123abc = 10        # ❌ SyntaxError: invalid token (không bắt đầu bằng số)
# my-var = 1        # ❌ SyntaxError: không dùng dấu gạch ngang
# class = "test"    # ❌ SyntaxError: từ khóa Python không dùng được
my_var = 1           # ✅ Dùng underscore (snake_case - convention Python)
myVar = 1            # ✅ CamelCase cũng được nhưng ít dùng trong Python
_ = 10               # ✅ Biến "vô nghĩa" thường dùng cho giá trị không dùng đến
```

#### Immutable - Hằng số

```python
# === Python KHÔNG có const/final keyword như Java/C++ ===
# Quy ước (convention) PEP 8: viết HOA toàn bộ + underscore để đánh dấu constant
# Đây là thỏa thuận giữa lập trình viên, Python không enforce

MAX_SIZE = 100              # Hằng số giới hạn kích thước (số nguyên)
PI = 3.14159                # Hằng số toán học π
BASE_URL = "https://api.example.com"  # URL gốc của API, không thay đổi
DEFAULT_TIMEOUT = 30        # Timeout mặc định tính bằng giây

# ⚠️ Lưu ý: đây chỉ là QUY ƯỚC, Python vẫn cho phép gán lại
MAX_SIZE = 200              # KHÔNG lỗi runtime! Nhưng vi phạm convention
# → Dùng linter (flake8, pylint) hoặc mypy để phát hiện vi phạm

# === Dùng tuple cho immutable data ===
# Tuple không có method .append(), .remove() → không thể thay đổi cấu trúc
COORDS = (10, 20)           # Tọa độ cố định (x, y)
# COORDS[0] = 5            # ❌ TypeError: 'tuple' object does not support item assignment

RGB_RED = (255, 0, 0)       # Màu đỏ theo RGB - không nên thay đổi
ALLOWED_METHODS = ("GET", "POST", "PUT", "DELETE")  # HTTP methods hợp lệ

# === Dùng frozenset cho tập hợp immutable ===
# frozenset giống set nhưng không thể thêm/xóa phần tử sau khi tạo
VALID_STATUS = frozenset({"active", "inactive", "pending"})
# VALID_STATUS.add("banned")  # ❌ AttributeError: 'frozenset' object has no attribute 'add'
print("active" in VALID_STATUS)   # Output: True  (vẫn có thể kiểm tra membership)
print("banned" in VALID_STATUS)   # Output: False

# === Real-world: dùng Final từ typing (Python 3.8+) ===
# Final cho phép type checker (mypy) phát hiện khi bạn vô tình gán lại
from typing import Final

MAX_RETRIES: Final = 3      # Khai báo MAX_RETRIES là hằng số cuối cùng
API_KEY: Final[str] = "sk-abc123"  # Chỉ định cả kiểu dữ liệu
# MAX_RETRIES = 5           # ❌ mypy error: Cannot assign to final name "MAX_RETRIES"
# Nhưng runtime vẫn chạy bình thường - Final chỉ là hint cho type checker

# === Real-world use case: Cấu hình database ===
DB_HOST: Final = "localhost"
DB_PORT: Final = 5432
DB_NAME: Final = "myapp"
DB_POOL_SIZE: Final = 10    # Số connection tối đa trong pool

# Dùng trong code
def get_connection_string() -> str:
    return f"postgresql://{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(get_connection_string())  # Output: postgresql://localhost:5432/myapp

# === Edge case: Hằng số trong module ===
# Thường đặt hằng số ở đầu file hoặc trong file config.py riêng
# Tránh "magic numbers" - số không có tên trong code
# ❌ Không nên:
# if len(users) > 100:  # 100 là magic number, không rõ ý nghĩa
#     ...
# ✅ Nên:
MAX_USERS_PER_PAGE = 100
# if len(users) > MAX_USERS_PER_PAGE:  # Rõ ràng hơn
#     ...
```

#### Type Inference

```python
# === Python tự suy luận kiểu dựa trên giá trị gán (type inference) ===
# Không cần khai báo kiểu - Python tự xác định tại runtime

x = 10              # Literal số nguyên → Python suy luận kiểu int
y = 3.14            # Literal số thực (có dấu chấm) → Python suy luận kiểu float
z = "hello"         # Literal chuỗi (trong nháy đơn/kép) → Python suy luận kiểu str
w = True            # Literal boolean (True/False viết hoa) → Python suy luận kiểu bool
n = None            # Literal None → Python suy luận kiểu NoneType (giá trị null)
c = 3 + 4j          # Literal số phức (j là đơn vị ảo) → Python suy luận kiểu complex

# === Kiểm tra kiểu tại runtime với type() ===
# type() trả về đối tượng kiểu (class) của biến
print(type(x))             # Output: <class 'int'>
print(type(y))             # Output: <class 'float'>
print(type(z))             # Output: <class 'str'>
print(type(w))             # Output: <class 'bool'>
print(type(n))             # Output: <class 'NoneType'>
print(type(c))             # Output: <class 'complex'>

# === isinstance() - kiểm tra kiểu có xét kế thừa ===
# isinstance(obj, type) → True nếu obj là instance của type hoặc subclass của type
print(isinstance(x, int))           # Output: True  (x là int)
print(isinstance(x, (int, float)))  # Output: True  (kiểm tra nhiều kiểu cùng lúc)
print(isinstance(True, int))        # Output: True  ← bool kế thừa từ int!
print(isinstance(True, bool))       # Output: True
print(isinstance(1.0, int))         # Output: False (float không kế thừa int)

# ⚠️ type() vs isinstance() - khi nào dùng cái nào?
# type() chỉ kiểm tra kiểu CHÍNH XÁC, không xét kế thừa → dùng khi cần phân biệt chính xác
# isinstance() xét cả kế thừa → dùng khi muốn kiểm tra "có phải loại này không"
class Animal: pass
class Dog(Animal): pass

dog = Dog()                          # Tạo instance của Dog
print(type(dog) == Animal)           # Output: False (Dog ≠ Animal, khác nhau)
print(type(dog) == Dog)              # Output: True  (Dog == Dog, chính xác)
print(isinstance(dog, Animal))       # Output: True  (Dog kế thừa Animal)
print(isinstance(dog, Dog))          # Output: True

# === Chuyển đổi kiểu tường minh (explicit type casting) ===
# Python không tự ép kiểu ngầm → phải gọi hàm chuyển đổi tường minh
print(int("42"))        # Output: 42    (str → int: parse chuỗi số)
print(float("3.14"))    # Output: 3.14  (str → float: parse chuỗi số thực)
print(str(42))          # Output: 42    (int → str: chuyển số thành chuỗi)
print(bool(0))          # Output: False (int → bool: 0 là falsy)
print(bool(1))          # Output: True  (int → bool: khác 0 là truthy)
print(bool(""))         # Output: False (str → bool: chuỗi rỗng là falsy)
print(bool("hello"))    # Output: True  (str → bool: chuỗi không rỗng là truthy)
print(list("abc"))      # Output: ['a', 'b', 'c']  (str → list: tách từng ký tự)
print(tuple([1,2,3]))   # Output: (1, 2, 3)         (list → tuple)
print(set([1,1,2,2]))   # Output: {1, 2}             (list → set: loại bỏ trùng lặp)

# ⚠️ Edge case: chuyển đổi thất bại → ValueError
# int("abc")            # ❌ ValueError: invalid literal for int() with base 10: 'abc'
# int("3.14")           # ❌ ValueError: phải dùng float() trước, không parse trực tiếp
# float("hello")        # ❌ ValueError: could not convert string to float: 'hello'
print(int(float("3.14")))  # Output: 3  ✅ str → float → int (cắt phần thập phân)
print(int(3.99))           # Output: 3  ✅ float → int (KHÔNG làm tròn, chỉ cắt)

# ⚠️ Edge case: bool là subclass của int
print(True + True)         # Output: 2  (True = 1, nên 1 + 1 = 2)
print(True * 5)            # Output: 5  (True = 1, nên 1 * 5 = 5)
print(False + 10)          # Output: 10 (False = 0, nên 0 + 10 = 10)

# === Real-world: kiểm tra kiểu trước khi xử lý ===
def process_value(value):
    """Xử lý giá trị theo kiểu dữ liệu."""
    if isinstance(value, str):
        return value.upper()          # Chuỗi → chuyển hoa
    elif isinstance(value, (int, float)):
        return value * 2              # Số → nhân đôi
    elif isinstance(value, list):
        return sorted(value)          # List → sắp xếp
    else:
        return str(value)             # Kiểu khác → chuyển thành chuỗi

print(process_value("hello"))         # Output: HELLO
print(process_value(21))              # Output: 42
print(process_value([3, 1, 2]))       # Output: [1, 2, 3]
print(process_value(None))            # Output: None
```

#### Global Variable

```python
# === Biến toàn cục (global variable) ===
# Biến khai báo ở cấp module (ngoài mọi function/class) → có thể đọc từ bất kỳ đâu
global_var = "I am global"  # Biến global - tồn tại suốt vòng đời chương trình

def access_global():
    # ĐỌC biến global → không cần từ khóa 'global'
    # Python tìm theo LEGB: Local → Enclosing → Global → Built-in
    print(global_var)       # Output: I am global (tìm thấy ở Global scope)

def modify_global():
    # GHI biến global → BẮT BUỘC khai báo 'global' trước
    # Nếu không có 'global', Python sẽ tạo biến LOCAL mới thay vì sửa global
    global global_var           # Báo Python: global_var ở đây là biến GLOBAL
    global_var = "Modified"     # Thay đổi giá trị biến global thực sự

def without_global_keyword():
    # Không dùng 'global' → Python tạo biến LOCAL mới, che khuất biến global
    global_var = "Local only"   # Biến local mới, KHÔNG ảnh hưởng global
    print(global_var)           # Output: Local only (đọc biến local)

# Thứ tự gọi để thấy sự khác biệt:
access_global()               # Output: I am global
modify_global()               # Thay đổi global_var thành "Modified"
access_global()               # Output: Modified  (global đã bị thay đổi)
without_global_keyword()      # Output: Local only (biến local trong function)
access_global()               # Output: Modified  (global vẫn là "Modified")

# ⚠️ Lưu ý: hạn chế dùng global variable vì:
# - Khó debug: không biết ai thay đổi giá trị
# - Khó test: function phụ thuộc vào state bên ngoài
# - Khó đọc: phải tìm khắp file để hiểu giá trị hiện tại
# ✅ Thay thế bằng: class attribute, function parameter, dependency injection

# === Real-world: module-level state (dùng cẩn thận) ===
_cache = {}  # Dấu _ đầu = "private" theo convention

def get_user(user_id: int) -> dict:
    """Lấy user với cache đơn giản."""
    if user_id not in _cache:           # Kiểm tra cache
        # Giả lập gọi database
        _cache[user_id] = {"id": user_id, "name": f"User {user_id}"}
    return _cache[user_id]              # Trả về từ cache

print(get_user(1))   # Output: {'id': 1, 'name': 'User 1'}  (gọi DB)
print(get_user(1))   # Output: {'id': 1, 'name': 'User 1'}  (từ cache)
print(get_user(2))   # Output: {'id': 2, 'name': 'User 2'}  (gọi DB)
```

#### Static Variable (Class-level)

```python
# === Biến class (class variable / static variable) ===
# Biến class được chia sẻ giữa TẤT CẢ instances của class
# Thay đổi ở một nơi → thấy ở mọi nơi
class Counter:
    count = 0              # Biến class - thuộc về class, KHÔNG thuộc instance

    def __init__(self):
        # Truy cập biến class qua TÊN CLASS (Counter.count), không phải self.count
        Counter.count += 1  # Tăng biến class mỗi khi tạo instance mới

    def __del__(self):
        # Giảm biến class khi object bị xóa (garbage collected)
        Counter.count -= 1

# Kiểm tra số lượng instance đã tạo
print(Counter.count)  # Output: 0 (chưa tạo instance nào)

c1 = Counter()              # Tạo instance thứ 1
print(Counter.count)  # Output: 1 (c1: count tăng lên 1)

c2 = Counter()              # Tạo instance thứ 2
print(Counter.count)  # Output: 2 (c2: count tăng lên 2)

c3 = Counter()              # Tạo instance thứ 3
print(Counter.count)  # Output: 3 (c3: count tăng lên 3)

del c3                      # Xóa instance c3 (gọi __del__)
print(Counter.count)  # Output: 2 (count giảm xuống 2)

# ⚠️ Edge case: gán qua instance tạo biến instance MỚI, không thay đổi class variable
# Đây là PITFALL phổ biến trong Python!
class Config:
    debug = False           # Class variable - thuộc về class

cfg1 = Config()             # Tạo instance 1
cfg2 = Config()             # Tạo instance 2

# Gán qua instance tạo INSTANCE VARIABLE mới, KHÔNG thay đổi class variable!
cfg1.debug = True           # Tạo biến instance 'debug' mới cho cfg1
print(cfg1.debug)          # Output: True  (đọc instance variable)
print(cfg2.debug)          # Output: False (vẫn đọc class variable!)
print(Config.debug)        # Output: False (class variable vẫn không đổi)

# Để thay đổi class variable → dùng TÊN CLASS
Config.debug = True         # Thay đổi biến class trực tiếp
print(cfg2.debug)          # Output: True  (giờ mới thay đổi)
print(Config.debug)        # Output: True

# === Real-world: đếm số lượng objects, cache chung, cấu hình chia sẻ ===
class DatabaseConnection:
    _pool_size = 0         # Class variable: số connection trong pool
    _active_connections = 0 # Class variable: số connection đang dùng
    _max_connections = 10  # Class variable: giới hạn tối đa

    def __init__(self):
        # Chỉ tạo connection nếu chưa đạt giới hạn
        if DatabaseConnection._active_connections < DatabaseConnection._max_connections:
            DatabaseConnection._active_connections += 1
            self.connected = True
        else:
            self.connected = False
            raise RuntimeError("Connection pool exhausted")

    def close(self):
        if self.connected:
            DatabaseConnection._active_connections -= 1

    @classmethod
    def status(cls):
        return f"Active: {cls._active_connections}/{cls._max_connections}"

# Test
try:
    conn1 = DatabaseConnection()
    conn2 = DatabaseConnection()
    print(DatabaseConnection.status())  # Output: Active: 2/10
    conn1.close()
    print(DatabaseConnection.status())  # Output: Active: 1/10
except Exception as e:
    print(f"Error: {e}")
```

#### Scope & Shadowing

```python
# === Python có LEGB rule - thứ tự tìm biến ===
# Khi truy cập biến, Python tìm theo thứ tự:
# 1. L - Local:     biến trong hàm hiện tại
# 2. E - Enclosing: biến trong hàm bao ngoài (closure/nested function)
# 3. G - Global:    biến cấp module (file .py)
# 4. B - Built-in:  biến/hàm có sẵn (print, len, type, str, int...)

x = "global"        # (G) Global scope - biến ở cấp module

def outer():
    x = "enclosing"  # (E) Enclosing scope - biến trong function bao ngoài

    def inner():
        x = "local"  # (L) Local scope - biến trong function hiện tại
        print(x)     # Output: local (tìm thấy ở L trước → dừng tìm)

    inner()
    print(x)         # Output: enclosing (L của inner không ảnh hưởng đến E)

outer()
print(x)             # Output: global (E và L không ảnh hưởng đến G)

# === nonlocal - thay đổi biến enclosing (trong nested function) ===
# nonlocal cho phép sửa biến ở enclosing scope (không phải global)
def counter():
    count = 0              # Biến enclosing (trong outer function)

    def increment():
        nonlocal count     # Khai báo: biến count ở đây là từ enclosing scope
        count += 1         # Thay đổi biến enclosing, không tạo biến local
        return count

    return increment       # Trả về function chưa gọi (closure)

c = counter()              # Tạo closure với count = 0
print(c())                 # Output: 1 (increment: 0 + 1 = 1)
print(c())                 # Output: 2 (increment: 1 + 1 = 2)
print(c())                 # Output: 3 (increment: 2 + 1 = 3)

# ⚠️ PITFALL: Không có nonlocal → UnboundLocalError
# Python phân tích code TRƯỚC KHI chạy, thấy count ở vế trái → coi là local
# Nhưng local chưa được gán → lỗi!
def bad_counter():
    count = 0
    def increment():
        # count += 1       # ❌ UnboundLocalError: local variable 'count' referenced before assignment
        # Giải pháp: dùng nonlocal count hoặc dùng list/dict (mutable trick)
        pass
    return increment

# === Built-in scope (B) ===
# Python có sẵn nhiều hàm và kiểu dữ liệu built-in
# print, len, type, int, str, list, dict, set, tuple, range, enumerate, zip...
# ⚠️ Có thể vô tình shadow built-in (KHÔNG nên làm!)
# list = [1, 2, 3]          # ❌ Shadow built-in list()!
# print(list)                # Output: [1, 2, 3] (không còn là hàm)
# list("abc")                # ❌ TypeError: 'list' object is not callable

# ✅ Giải pháp: đặt tên khác hoặc dùng underscore prefix
my_list = [1, 2, 3]        # ✅ Không shadow built-in
_builtin_list = list       # Lưu lại built-in nếu cần dùng

# === Real-world: dùng closure làm factory function ===
# Tạo các function với behavior khác nhau dựa trên tham số
def make_logger(prefix):
    """Factory function: tạo hàm log với prefix cố định."""
    def log(message):
        # Inner function "nhớ" prefix từ enclosing scope (closure)
        print(f"[{prefix}] {message}")
    return log                # Trả về function chưa gọi

info = make_logger("INFO")   # Tạo logger với prefix = "INFO"
error = make_logger("ERROR") # Tạo logger với prefix = "ERROR"
debug = make_logger("DEBUG") # Tạo logger với prefix = "DEBUG"

info("Server started")       # Output: [INFO] Server started
error("Connection lost")     # Output: [ERROR] Connection lost
debug("Processing request")  # Output: [DEBUG] Processing request

# === Real-world: closure với configuration ===
def create_formatter(decimal_places: int, prefix: str = "$"):
    """Tạo hàm format tiền tệ với cấu hình cố định."""
    def format(amount: float) -> str:
        return f"{prefix}{amount:.{decimal_places}f}"
    return format

format_currency = create_formatter(decimal_places=2)    # 2 chữ số thập phân
format_stock = create_formatter(decimal_places=4, prefix="") # 4 chữ số, không prefix

print(format_currency(99.9))   # Output: $99.90
print(format_currency(100))    # Output: $100.00
print(format_stock(123.456789)) # Output: 123.4568
```

---

### 1.2. Khai Báo Hàm (Function Declaration)

#### Function cơ bản

```python
# === Function không có return (trả về None ngầm) ===
# Cú pháp: def ten_ham(tham_so): → thụt lề 4 spaces
def greet():
    print("Hello!")          # In ra màn hình, không trả về giá trị

result = greet()             # Gọi function → in "Hello!" và gán kết quả vào result
# Output: Hello!
print(result)                # Output: None  (function không có return → trả về None ngầm)

# === Function có return ===
def add(a, b):
    return a + b             # Tính tổng và trả về kết quả cho caller

print(add(3, 5))             # Output: 8      (3 + 5 = 8)
print(add("Hello", " World"))  # Output: Hello World  (+ với string = nối chuỗi)

# === Function với type hints (Python 3.5+) ===
# Cú pháp: def ten(tham_so: kieu) -> kieu_tra_ve:
# Type hints giúp IDE autocomplete và phát hiện lỗi, KHÔNG enforce tại runtime
def greet(name: str) -> str:
    """Trả về lời chào với tên được truyền vào."""
    return f"Hello, {name}!"  # f-string: nhúng biến vào chuỗi

print(greet("Python"))       # Output: Hello, Python!
print(greet(42))             # Output: Hello, 42!  (runtime vẫn chạy, mypy sẽ cảnh báo)

# === Docstring (Google style) ===
# Docstring là chuỗi đầu tiên trong function, dùng để mô tả function
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
        raise ValueError("Dimensions must be positive")  # Ném exception nếu input không hợp lệ
    return width * height                                  # Trả về diện tích

print(calculate_area(5, 3))   # Output: 15.0
print(calculate_area(2.5, 4)) # Output: 10.0
# calculate_area(-1, 5)       # ❌ ValueError: Dimensions must be positive

# === Multiple return values (trả về tuple ngầm) ===
# Python không có cú pháp return nhiều giá trị riêng biệt
# Thực chất là trả về 1 tuple, sau đó unpack
def divide(a, b):
    """Trả về thương và phần dư."""
    quotient = a // b           # Phép chia lấy phần nguyên (floor division)
    remainder = a % b           # Phép chia lấy phần dư (modulo)
    return quotient, remainder  # Trả về tuple (quotient, remainder) ngầm

q, r = divide(17, 5)           # Tuple unpacking: q=3, r=2
print(f"17 ÷ 5 = {q} dư {r}") # Output: 17 ÷ 5 = 3 dư 2

result = divide(17, 5)         # Không unpack → nhận tuple
print(result)                  # Output: (3, 2)
print(result[0])               # Output: 3  (phần nguyên)
print(result[1])               # Output: 2  (phần dư)

# === Early return pattern (guard clause) ===
# Thoát sớm khi điều kiện không thỏa → tránh lồng if sâu
def find_user(user_id: int) -> dict | None:
    """Tìm user theo ID, trả về None nếu không tìm thấy."""
    if user_id <= 0:
        return None              # Guard: thoát sớm nếu ID không hợp lệ
    if user_id > 1000:
        return None              # Guard: thoát sớm nếu ID vượt giới hạn
    # Logic chính chỉ chạy khi input hợp lệ
    return {"id": user_id, "name": f"User {user_id}"}

print(find_user(0))             # Output: None  (ID không hợp lệ)
print(find_user(-5))            # Output: None  (ID âm)
print(find_user(42))            # Output: {'id': 42, 'name': 'User 42'}

# === Real-world: function xử lý dữ liệu ===
def parse_price(price_str: str) -> float | None:
    """Parse chuỗi giá tiền thành float.
    Xử lý các định dạng: "$99.99", "99.99", "99,99"
    """
    if not price_str:
        return None                          # Chuỗi rỗng → None
    cleaned = price_str.strip()             # Xóa khoảng trắng đầu/cuối
    cleaned = cleaned.replace("$", "")      # Xóa ký hiệu tiền tệ
    cleaned = cleaned.replace(",", ".")     # Thay dấu phẩy bằng dấu chấm
    try:
        return float(cleaned)               # Chuyển thành float
    except ValueError:
        return None                          # Không parse được → None

print(parse_price("$99.99"))   # Output: 99.99
print(parse_price("99,99"))    # Output: 99.99
print(parse_price("  $50  "))  # Output: 50.0
print(parse_price("abc"))      # Output: None
print(parse_price(""))         # Output: None
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
# Python cho phép gọi function theo 2 cách: theo vị trí hoặc theo tên
def create_user(name, email, age):
    """Tạo user dict từ thông tin."""
    return {"name": name, "email": email, "age": age}

# Gọi theo vị trí (positional arguments)
# Thứ tự argument phải khớp với thứ tự parameter trong function definition
user1 = create_user("John", "john@example.com", 25)
print(user1)  # Output: {'name': 'John', 'email': 'john@example.com', 'age': 25}

# Gọi theo tên (keyword arguments)
# Dùng ten_tham_so=gia_tri → thứ tự không quan trọng
user2 = create_user(age=25, name="John", email="john@example.com")
print(user2)  # Output: {'name': 'John', 'email': 'john@example.com', 'age': 25}

# Mix cả hai (positional phải đứng trước keyword)
user3 = create_user("John", age=25, email="john@example.com")
print(user3)  # Output: {'name': 'John', 'email': 'john@example.com', 'age': 25}
# create_user(name="John", "john@example.com", 25)  # ❌ SyntaxError: positional argument follows keyword argument

# === Keyword-only arguments (Python 3.0+) ===
# Tham số sau * hoặc *args BẮT BUỘC phải truyền bằng tên (keyword)
# Dấu * ngăn việc truyền positional vào các tham số sau nó
def connect(host, port, *, timeout=30, retries=3):
    """Kết nối đến server với các tham số tùy chọn."""
    print(f"Connecting to {host}:{port} (timeout={timeout}s, retries={retries})")

connect("localhost", 8080)                        # Truyền đủ 2 required params
# Output: Connecting to localhost:8080 (timeout=30s, retries=3)
connect("localhost", 8080, timeout=60)            # Ghi đè timeout bằng keyword
# Output: Connecting to localhost:8080 (timeout=60s, retries=3)
# connect("localhost", 8080, 60)                 # ❌ TypeError: positional argument not allowed

# === Positional-only arguments (Python 3.8+) ===
# Tham số trước / BẮT BUỘC phải truyền theo vị trí, KHÔNG được dùng keyword
# / ngăn việc truyền keyword vào các tham số trước nó
def power(base, exp, /):
    """Tính lũy thừa: base^exp."""
    return base ** exp

print(power(2, 10))             # Output: 1024 (truyền theo vị trí)
# power(base=2, exp=10)        # ❌ TypeError: positional-only argument

# === *args và **kwargs - Variadic parameters ===
# *args: thu thập TẤT CẢ positional arguments thành tuple
# **kwargs: thu thập TẤT CẢ keyword arguments thành dict
def func(*args, **kwargs):
    print(f"args = {args}")       # Tuple: (1, 2, 3)
    print(f"kwargs = {kwargs}")   # Dict: {'name': 'John', 'age': 25}

func(1, 2, 3, name="John", age=25)
# Output: args = (1, 2, 3)
# Output: kwargs = {'name': 'John', 'age': 25}

# === Real-world: wrapper/decorator function ===
import time

def log_call(func):
    """Decorator: ghi log thời gian thực thi và tham số."""
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"📞 Calling {func.__name__}(args={args}, kwargs={kwargs})")
        result = func(*args, **kwargs)  # Gọi function gốc, forward tất cả args/kwargs
        elapsed = time.time() - start
        print(f"✅ {func.__name__} returned {result} in {elapsed:.4f}s")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
# Output:
# 📞 Calling add(args=(5, 3), kwargs={})
# ✅ add returned 8 in 0.0000s
# 8

# === Real-world: API endpoint handler ===
def handle_request(method, path, *args, **kwargs):
    """Xử lý HTTP request với các tham số tùy ý."""
    print(f"{method} {path}")
    if args:
        print(f"  Positional args: {args}")
    if kwargs:
        print(f"  Query params: {kwargs}")
    return {"status": "ok"}

handle_request("GET", "/users", 1, 2, page=1, limit=10)
# Output:
# GET /users
#   Positional args: (1, 2)
#   Query params: {'page': 1, 'limit': 10}
```

#### Variadic Parameters

```python
# === *args - nhận số lượng positional arguments không giới hạn ===
# *args thu thập tất cả positional arguments thừa vào 1 TUPLE
# Tên "args" là convention, có thể đặt tên khác (*numbers, *items...)
def sum_all(*numbers):
    """Tính tổng tất cả các số truyền vào."""
    print(f"Received: {numbers}")  # numbers là tuple, không phải list
    return sum(numbers)            # sum() tính tổng các phần tử trong iterable

print(sum_all(1, 2, 3, 4, 5))     # Output: Received: (1, 2, 3, 4, 5)
                                   # Output: 15
print(sum_all())                   # Output: Received: ()
                                   # Output: 0  (tuple rỗng → sum = 0)
print(sum_all(10))                 # Output: Received: (10,)
                                   # Output: 10

# === **kwargs - nhận số lượng keyword arguments không giới hạn ===
# **kwargs thu thập tất cả keyword arguments thừa vào 1 DICT
# Tên "kwargs" là convention, có thể đặt tên khác (**options, **params...)
def print_info(**info):
    """In thông tin từ keyword arguments."""
    for key, value in info.items():  # Duyệt qua dict
        print(f"  {key}: {value}")

print_info(name="John", age=25, city="HCM")
# Output:
#   name: John
#   age: 25
#   city: HCM

# === Kết hợp tất cả loại parameters ===
# Thứ tự BẮT BUỘC: positional → *args → keyword-only → **kwargs
def complex_func(required, *args, default="value", **kwargs):
    """
    required: tham số bắt buộc (positional)
    *args:    positional arguments thừa → tuple
    default:  keyword-only argument có giá trị mặc định
    **kwargs: keyword arguments thừa → dict
    """
    print(f"required={required}")  # Tham số bắt buộc
    print(f"args={args}")          # Tuple các positional thừa
    print(f"default={default}")    # Keyword-only với default
    print(f"kwargs={kwargs}")      # Dict các keyword thừa

complex_func("hello", 1, 2, default="custom", extra="data")
# Output:
#   required=hello
#   args=(1, 2)
#   default=custom
#   kwargs={'extra': 'data'}

# === Unpacking arguments khi gọi function ===
# Dùng * để unpack list/tuple thành positional arguments
# Dùng ** để unpack dict thành keyword arguments
def greet(name, age, city):
    print(f"{name}, {age} tuổi, sống ở {city}")

# Unpack list/tuple với *
args = ["John", 25, "HCM"]
greet(*args)                  # Output: John, 25 tuổi, sống ở HCM
# Tương đương: greet("John", 25, "HCM")

# Unpack dict với **
kwargs = {"name": "John", "age": 25, "city": "HCM"}
greet(**kwargs)               # Output: John, 25 tuổi, sống ở HCM
# Tương đương: greet(name="John", age=25, city="HCM")

# === Real-world: merge dicts với ** (Python 3.5+) ===
defaults = {"timeout": 30, "retries": 3, "debug": False}
overrides = {"timeout": 60, "debug": True}
config = {**defaults, **overrides}  # Merge: overrides ghi đè defaults
print(config)  # Output: {'timeout': 60, 'retries': 3, 'debug': True}

# === Real-world: forward arguments đến function khác ===
def create_connection(host, port, **options):
    """Tạo connection với các tùy chọn."""
    print(f"Connecting to {host}:{port}")
    print(f"Options: {options}")

def create_ssl_connection(host, port, **options):
    """Tạo SSL connection - thêm ssl=True rồi forward."""
    options["ssl"] = True          # Thêm option ssl
    options["ssl_verify"] = True   # Thêm option ssl_verify
    create_connection(host, port, **options)  # Forward tất cả options

create_ssl_connection("api.example.com", 443, timeout=30)
# Output:
# Connecting to api.example.com:443
# Options: {'timeout': 30, 'ssl': True, 'ssl_verify': True}

# ⚠️ Edge case: *args và **kwargs phải ở đúng vị trí
# def bad(a, *args, b, **kwargs, c):  # ❌ SyntaxError: **kwargs phải cuối cùng
# def bad(*args, *more):              # ❌ SyntaxError: chỉ 1 *args
# def bad(**kw1, **kw2):             # ❌ SyntaxError: chỉ 1 **kwargs
```

#### Lambda/Arrow Function

```python
# === Lambda (anonymous function - hàm ẩn danh) ===
# Lambda là function không có tên, dùng cho các tác vụ đơn giản
# Cú pháp: lambda tham_số: biểu_thức
# Chỉ chứa 1 biểu thức duy nhất, tự return kết quả (không cần từ khóa return)
square = lambda x: x ** 2           # Nhận x, trả về x bình phương
add = lambda a, b: a + b            # Nhận a, b, trả về a + b
identity = lambda x: x              # Nhận x, trả về chính x
always_true = lambda: True          # Không tham số, luôn trả về True

print(square(5))                     # Output: 25  (5 ** 2)
print(add(3, 4))                     # Output: 7   (3 + 4)
print(identity(42))                  # Output: 42
print(always_true())                 # Output: True

# === Dùng lambda với higher-order functions ===
# map(), filter(), sorted() nhận function làm tham số → dùng lambda tiện
numbers = [1, 2, 3, 4, 5]

# map(function, iterable) - áp dụng function cho MỖI phần tử, trả về map object
squared = list(map(lambda x: x ** 2, numbers))
print(squared)                       # Output: [1, 4, 9, 16, 25]

# filter(function, iterable) - lọc phần tử THỎA ĐIỀU KIỆN (function trả về True)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)                         # Output: [2, 4]

# sorted(iterable, key=function) - sắp xếp theo giá trị trả về của key function
words = ["banana", "apple", "cherry", "date"]
sorted_by_len = sorted(words, key=lambda w: len(w))
print(sorted_by_len)                 # Output: ['date', 'apple', 'banana', 'cherry']
# Giải thích: len("date")=4, len("apple")=5, len("banana")=6, len("cherry")=6

# === Lambda với conditional (ternary expression) ===
# Cú pháp: gia_tri_true if condition else gia_tri_false
max_val = lambda a, b: a if a > b else b
print(max_val(10, 20))               # Output: 20  (10 > 20? Không → trả b)

classify = lambda x: "even" if x % 2 == 0 else "odd"
print(classify(7))                   # Output: odd
print(classify(8))                   # Output: even

# === Real-world: lambda với các hàm phổ biến ===
# max(), min() với key
names = ["Alice", "Bob", "Charlie", "David"]
print(max(names, key=lambda n: len(n)))  # Output: Charlie (dài nhất)
print(min(names, key=lambda n: len(n)))  # Output: Bob (ngắn nhất)

# reduce() từ functools - giảm list thành 1 giá trị
from functools import reduce
product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
print(product)                       # Output: 120  (1*2*3*4*5)

# === ⚠️ Khi nào KHÔNG nên dùng lambda ===
# - Logic phức tạp → dùng def (lambda chỉ 1 dòng)
# - Cần nhiều dòng code → dùng def
# - Cần docstring → dùng def (lambda không có tên, khó debug)
# - Gán lambda cho biến → dùng def (PEP 8 khuyên nên dùng def)

# ❌ Không nên: gán lambda cho biến (PEP 8 violation)
double = lambda x: x * 2

# ✅ Nên: dùng def thay thế
def double(x):
    return x * 2

# === Real-world: dùng lambda đúng cách ===
# 1. Sort một list các dict theo key
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_users = sorted(users, key=lambda u: u["age"])
print([u["name"] for u in sorted_users])  # Output: ['Bob', 'Alice', 'Charlie']

# 2. Filter dicts
adults = list(filter(lambda u: u["age"] >= 18, users))
print([u["name"] for u in adults])        # Output: ['Alice', 'Bob', 'Charlie']

# 3. Map để transform dicts
names_upper = list(map(lambda u: u["name"].upper(), users))
print(names_upper)                        # Output: ['ALICE', 'BOB', 'CHARLIE']
```

#### Closure

```python
# === Closure - function "nhớ" biến từ scope bên ngoài ===
# Closure xảy ra khi inner function tham chiếu biến của outer function
# Biến đó được "capture" vào closure và tồn tại sau khi outer function kết thúc
# Closure = function + môi trường (environment) chứa các biến được capture

def outer(x):
    # x là biến enclosing - sẽ được capture bởi inner function
    def inner(y):
        return x + y      # inner "nhớ" x từ outer scope (closure)
    return inner          # Trả về function inner (chưa gọi, chỉ trả về object)

# Tạo các closure khác nhau với x khác nhau
add_10 = outer(10)        # Tạo closure với x = 10 được capture
add_100 = outer(100)      # Tạo closure với x = 100 được capture

print(add_10(5))          # Output: 15  (x=10, y=5 → 10 + 5)
print(add_10(20))         # Output: 30  (x=10, y=20 → 10 + 20)
print(add_100(5))         # Output: 105 (x=100, y=5 → 100 + 5)

# Kiểm tra closure variables
print(add_10.__closure__)           # Output: (<cell at 0x...>,)
print(add_10.__closure__[0].cell_contents)  # Output: 10 (giá trị x được capture)

# === Real-world: closure làm counter với state ===
def make_counter(start=0, step=1):
    """Factory tạo counter với start và step tùy chỉnh."""
    count = start          # Biến enclosing - state của counter

    def counter():
        nonlocal count     # Cần nonlocal để thay đổi biến enclosing
        count += step      # Tăng theo step
        return count

    return counter         # Trả về closure

counter = make_counter()           # start=0, step=1
print(counter())          # Output: 1
print(counter())          # Output: 2
print(counter())          # Output: 3

counter_by_5 = make_counter(start=0, step=5)  # Đếm theo 5
print(counter_by_5())     # Output: 5
print(counter_by_5())     # Output: 10

# === Real-world: closure làm rate limiter đơn giản ===
import time

def make_rate_limiter(min_interval=1.0):
    """Tạo function giới hạn tần suất gọi."""
    last_call = [0]        # Dùng list để tránh nonlocal (trick cũ, nay dùng nonlocal)

    def limiter():
        elapsed = time.time() - last_call[0]  # Thời gian từ lần gọi trước
        if elapsed < min_interval:
            print(f"Rate limited! Wait {min_interval - elapsed:.1f}s")
            return False
        last_call[0] = time.time()  # Cập nhật thời gian gọi cuối
        return True

    return limiter

# === ⚠️ PITFALL: closure và loop - lỗi phổ biến nhất ===
# Closure capture BIẾN (tham chiếu), không capture GIÁ TRỊ tại thời điểm tạo
funcs = []
for i in range(3):
    funcs.append(lambda: i)  # Tất cả lambda cùng tham chiếu biến i (cùng object)

print([f() for f in funcs])   # Output: [2, 2, 2]  ← KHÔNG phải [0, 1, 2]!
# Lý do: khi gọi f(), i đã là 2 (giá trị cuối sau vòng lặp)
# Tất cả lambda đều trỏ đến CÙNG biến i, không phải copy của i

# ✅ Giải pháp 1: dùng default argument để capture giá trị tại thời điểm tạo
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)  # i=i: tạo local variable i với giá trị hiện tại

print([f() for f in funcs])   # Output: [0, 1, 2]  ← Đúng!

# ✅ Giải pháp 2: dùng functools.partial
from functools import partial

def get_value(i):
    return i

funcs = [partial(get_value, i) for i in range(3)]
print([f() for f in funcs])   # Output: [0, 1, 2]  ← Đúng!

# === Real-world: closure làm memoization đơn giản ===
def make_memoized(func):
    """Tạo phiên bản memoized của function."""
    cache = {}             # Dict lưu kết quả đã tính

    def memoized(*args):
        if args not in cache:
            cache[args] = func(*args)  # Tính và lưu vào cache
        return cache[args]             # Trả về từ cache

    return memoized

@make_memoized
def fibonacci(n):
    """Tính số Fibonacci thứ n."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Output: 55
print(fibonacci(30))  # Output: 832040  (nhanh nhờ cache)
```

#### Higher-Order Function

```python
# === Higher-Order Function (HOF) ===
# HOF = function nhận function khác làm tham số HOẶC trả về function
# Python treat functions as first-class objects → có thể gán, truyền, trả về

# --- Type 1: Nhận function làm tham số ---
def apply_twice(func, x):
    """Áp dụng function 2 lần liên tiếp."""
    return func(func(x))     # Gọi func 2 lần: func(func(x))

def add_five(x):
    return x + 5

result = apply_twice(add_five, 10)  # add_five(add_five(10)) = add_five(15) = 20
print(result)                        # Output: 20

# --- Type 2: Trả về function ---
def multiplier(factor):
    """Factory: tạo function nhân với factor cố định."""
    def multiply(x):
        return x * factor      # inner function "nhớ" factor (closure)
    return multiply            # Trả về function, chưa gọi

double = multiplier(2)               # Tạo function nhân với 2
triple = multiplier(3)               # Tạo function nhân với 3

print(double(5))                     # Output: 10  (5 * 2)
print(triple(5))                     # Output: 15  (5 * 3)

# === Real-world: retry logic với HOF ===
import time

def with_retry(func, max_retries=3, delay=1):
    """Wrap function với retry logic - HOF nhận function, trả về function."""
    def wrapper(*args, **kwargs):
        for attempt in range(max_retries):      # Thử max_retries lần
            try:
                return func(*args, **kwargs)    # Thử gọi function
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:   # Nếu còn lần thử
                    time.sleep(delay)            # Đợi delay giây
        raise Exception(f"All {max_retries} attempts failed")  # Thử hết rồi → lỗi
    return wrapper

def unstable_api_call():
    """API call có thể thất bại ngẫu nhiên."""
    import random
    if random.random() < 0.5:  # 50% chance thất bại
        raise ConnectionError("Random failure!")
    return "Success!"

safe_call = with_retry(unstable_api_call, max_retries=3, delay=0.1)
# Test: chạy nhiều lần để xem retry hoạt động

# === Built-in HOFs phổ biến trong Python ===
numbers = [1, 2, 3, 4, 5]

# map(function, iterable) - biến đổi mỗi phần tử
print(list(map(str, numbers)))        # Output: ['1', '2', '3', '4', '5']

# filter(function, iterable) - lọc phần tử thỏa điều kiện
print(list(filter(lambda x: x > 3, numbers)))  # Output: [4, 5]

# sorted(iterable, key=function) - sắp xếp theo key
users = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
sorted_users = sorted(users, key=lambda u: u["age"])  # Sắp xếp theo age
print(sorted_users[0]["name"])        # Output: Alice (age=25 nhỏ nhất)

# min(iterable, key=function) / max(iterable, key=function)
print(min(users, key=lambda u: u["age"])["name"])  # Output: Alice
print(max(users, key=lambda u: u["age"])["name"])  # Output: Bob

# === Real-world: Debounce function ===
import time

def debounce(wait):
    """Tạo debounced function - chỉ gọi sau khi đợi wait giây không có request mới."""
    timer = [None]  # Dùng list để mutable

    def debounced(func):
        def wrapper(*args, **kwargs):
            def call_it():
                timer[0] = None
                return func(*args, **kwargs)

            if timer[0]:
                timer[0].cancel()  # Hủy timer cũ
            timer[0] = threading.Timer(wait, call_it)
            timer[0].start()

        return wrapper
    return debounced

# Test debounce với threading
import threading
@debounce(0.5)
def save_to_db(data):
    print(f"Saving {data} to database...")

# Khi gọi nhiều lần liên tiếp, chỉ lần cuối mới thực sự gọi function
```

#### Method trong Class

```python
# === 3 loại method trong class ===
# 1. Instance method: nhận self → truy cập instance attributes
# 2. Class method: nhận cls → truy cập class attributes, dùng làm factory
# 3. Static method: không nhận self/cls → utility function đặt trong class

class Calculator:
    precision = 2              # Class variable: số chữ số thập phân mặc định

    def __init__(self, name="Basic"):
        self.name = name       # Instance variable: tên riêng của mỗi calculator

    # --- Instance method ---
    # Tham số đầu tiên LUÔN là self (tham chiếu đến instance hiện tại)
    # Có thể truy cập cả instance variable (self.name) và class variable (self.precision)
    def multiply(self, a, b):
        result = round(a * b, self.precision)  # Làm tròn theo precision của instance
        print(f"[{self.name}] {a} × {b} = {result}")
        return result

    # --- Class method ---
    # Decorator @classmethod → Python tự động truyền class (cls) làm tham số đầu
    # Dùng cho: factory method, thao tác class variable, alternative constructors
    @classmethod
    def set_precision(cls, precision):
        cls.precision = precision  # Thay đổi class variable → ảnh hưởng TẤT CẢ instances

    @classmethod
    def create_scientific(cls):
        """Factory method: tạo calculator khoa học với precision cao."""
        calc = cls("Scientific")   # cls() = Calculator() → tạo instance mới
        calc.precision = 10        # Ghi đè precision cho instance này
        return calc

    # --- Static method ---
    # Decorator @staticmethod → không nhận self hay cls
    # Không truy cập được instance hay class attributes
    # Chỉ là utility function đặt trong class cho gọn về mặt tổ chức
    @staticmethod
    def add(a, b):
        return a + b               # Không cần self hay cls

# Sử dụng:
calc = Calculator("MyCalc")        # Tạo instance với name="MyCalc"
calc.multiply(3, 4)                # Output: [MyCalc] 3 × 4 = 12

Calculator.set_precision(4)        # Thay đổi precision cho TẤT CẢ instances
print(Calculator.add(10, 20))      # Output: 30  (gọi static method qua class)
print(calc.add(10, 20))            # Output: 30  (cũng có thể gọi qua instance)

sci = Calculator.create_scientific()  # Gọi factory method
sci.multiply(1, 3)                    # Output: [Scientific] 1 × 3 = 3.0000000000

# ⚠️ Phân biệt khi nào dùng loại nào:
# - Instance method: khi cần truy cập/thay đổi state của instance (self.xxx)
# - Class method: khi cần factory method, thay đổi class variable, alternative constructor
# - Static method: khi logic không phụ thuộc vào instance hay class

# === Real-world: class với đầy đủ 3 loại method ===
class Temperature:
    """Lớp đại diện nhiệt độ với các phương thức chuyển đổi."""
    _unit = "Celsius"  # Class variable: đơn vị mặc định

    def __init__(self, value: float):
        self.value = value  # Instance variable: giá trị nhiệt độ

    # Instance method: chuyển đổi dựa trên giá trị của instance
    def to_fahrenheit(self) -> float:
        return self.value * 9/5 + 32  # Công thức C → F

    def to_kelvin(self) -> float:
        return self.value + 273.15    # Công thức C → K

    # Class method: factory method tạo từ Fahrenheit
    @classmethod
    def from_fahrenheit(cls, f: float) -> "Temperature":
        celsius = (f - 32) * 5/9     # Công thức F → C
        return cls(celsius)           # Tạo instance mới

    # Static method: kiểm tra nhiệt độ hợp lệ (không cần instance/class)
    @staticmethod
    def is_valid(value: float) -> bool:
        return value >= -273.15       # Nhiệt độ tuyệt đối tối thiểu

# Test
t = Temperature(100)                  # 100°C
print(t.to_fahrenheit())              # Output: 212.0  (100°C = 212°F)
print(t.to_kelvin())                  # Output: 373.15 (100°C = 373.15K)

t2 = Temperature.from_fahrenheit(32) # Tạo từ 32°F = 0°C
print(t2.value)                       # Output: 0.0

print(Temperature.is_valid(-300))     # Output: False  (dưới 0K)
print(Temperature.is_valid(25))       # Output: True
```

#### Constructor & Destructor

```python
# === __init__ (Constructor) ===
# __init__ được gọi TỰ ĐỘNG khi tạo instance mới với ClassName(...)
# Dùng để khởi tạo instance attributes

class Resource:
    def __init__(self, name: str):
        """Constructor - khởi tạo object.
        Gọi tự động khi tạo instance bằng Resource("...")
        """
        self.name = name                     # Tạo/gán instance attribute
        self.is_open = True                  # Khởi tạo trạng thái mặc định
        print(f"✅ Creating resource: {name}")

    def __repr__(self):
        """Biểu diễn chính thức (dùng trong debug, repr(), list())."""
        # !r dùng repr() để hiển thị chuỗi có quotes
        return f"Resource(name={self.name!r}, is_open={self.is_open})"

    def __str__(self):
        """Biểu diễn thân thiện (dùng trong print(), str())."""
        status = "open" if self.is_open else "closed"
        return f"Resource '{self.name}' ({status})"

# Sử dụng:
r = Resource("DB Connection")          # Output: ✅ Creating resource: DB Connection
print(r)                              # Output: Resource 'DB Connection' (open) → __str__()
print(repr(r))                        # Output: Resource(name='DB Connection', is_open=True) → __repr__()

# === __del__ (Destructor) - HIẾM KHI DÙNG ===
# __del__ được gọi khi object bị garbage collected (không còn tham chiếu)
# ⚠️ CẢNH BÁO: Không đảm bảo thời điểm gọi, không tin cậy cho cleanup
class Demo:
    def __del__(self):
        print(f"🗑️ Object is being deleted!")

d = Demo()  # Tạo object
del d       # Xóa tham chiếu → có thể gọi __del__ ngay hoặc không

# ⚠️ __del__ KHÔNG tin cậy - dùng context manager thay thế:
# Context manager đảm bảo cleanup luôn chạy dù có exception hay không

class ManagedResource:
    def __enter__(self):
        """Được gọi khi bắt đầu với: with ... as ... """
        print("Acquiring resource")  # Setup: mở file, kết nối DB, lock...
        return self                  # Đối tượng được gán cho biến sau 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Được gọi khi kết thúc block (dù bình thường hay có exception)."""
        print("Releasing resource")  # Teardown: đóng file, đóng DB, unlock...
        return False                 # False = không swallow exception

with ManagedResource() as r:
    print("Using resource")
    # Output:
    #   Acquiring resource
    #   Using resource
    #   Releasing resource
# Khi ra khỏi block, __exit__ LUÔN ĐƯỢC GỌI

# === Real-world: context manager với file ===
# Python có sẵn file objects là context managers
with open("test.txt", "w") as f:
    f.write("Hello, World!")  # Viết vào file
    # Khi ra khỏi block, file TỰ ĐỘNG ĐƯỢC ĐÓNG

# === Real-world: context manager với database ===
# class DatabaseConnection:
#     def __enter__(self):
#         self.conn = connect_to_db()
#         return self.conn
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.conn.close()
#         return False
#
# with DatabaseConnection() as conn:
#     conn.execute("INSERT INTO users VALUES (1, 'John')")
#     # Database connection được đóng tự động
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
# === range() - tạo dãy số (không tạo list, chỉ là lazy iterator) ===
# range(stop)         → 0 đến stop-1
# range(start, stop)  → start đến stop-1
# range(start, stop, step) → start, start+step, start+2*step, ...

# range(5) = [0, 1, 2, 3, 4] - 5 phần tử, bắt đầu từ 0
for i in range(5):
    print(i, end=" ")           # Output: 0 1 2 3 4

print()  # Xuống dòng

# range(1, 6) = [1, 2, 3, 4, 5] - bắt đầu từ 1, kết thúc ở 5 (6-1)
for i in range(1, 6):
    print(i, end=" ")           # Output: 1 2 3 4 5

print()

# range(0, 10, 2) = [0, 2, 4, 6, 8] - bước nhảy 2
for i in range(0, 10, 2):
    print(i, end=" ")           # Output: 0 2 4 6 8

print()

# range(5, 0, -1) = [5, 4, 3, 2, 1] - đếm ngược
for i in range(5, 0, -1):
    print(i, end=" ")           # Output: 5 4 3 2 1

print()

# === For với iterable (list, tuple, str, dict...) ===
# Python for loop duyệt trực tiếp từng phần tử, không cần index
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:            # Duyệt trực tiếp từng phần tử
    print(fruit)
# Output:
# apple
# banana
# cherry

# Duyệt string từng ký tự
for ch in "Python":
    print(ch, end="")           # Output: Python
print()

# Duyệt dict (mặc định duyệt key, không phải value)
user = {"name": "John", "age": 30}
for key in user:               # Iterating over dict = iterating over keys
    print(f"{key} = {user[key]}")
# Output:
# name = John
# age = 30

# Duyệt values trực tiếp
for value in user.values():
    print(value, end=" ")      # Output: John 30

print()

# Duyện key-value pairs
for key, value in user.items():
    print(f"{key}:{value}", end=" ")  # Output: name:John age:30

print()

# === enumerate() - duyệt với index ===
# Trả về tuple (index, value) cho mỗi phần tử
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):          # Bắt đầu từ index 0
    print(f"{i}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

for i, fruit in enumerate(fruits, start=1):  # start=1: bắt đầu đếm từ 1
    print(f"{i}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. cherry

# === zip() - duyệt nhiều iterable song song ===
# Zip ghép các phần tử cùng index từ nhiều iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["HCM", "HN", "DN"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} ({age}) - {city}")
# Output:
# Alice (25) - HCM
# Bob (30) - HN
# Charlie (35) - DN

# ⚠️ PITFALL: zip() dừng ở iterable NGẮN nhất
for a, b in zip([1, 2, 3], [10, 20]):
    print(a, b)
# Output:
# 1 10
# 2 20
# (phần tử thứ 3 bị bỏ vì list thứ 2 chỉ có 2 phần tử)

# ✅ Dùng itertools.zip_longest() để padding cho iterable ngắn
from itertools import zip_longest
for a, b in zip_longest([1, 2, 3], [10, 20], fillvalue=0):
    print(a, b)
# Output:
# 1 10
# 2 20
# 3 0  (fillvalue=0 cho phần tử thiếu)

# === Real-world: xử lý dữ liệu với enumerate và zip ===
sales = [100, 200, 150, 300]
products = ["A", "B", "C", "D"]

# Tính tổng doanh thu
total = sum(sales)
print(f"Total: {total}")  # Output: Total: 750

# In báo cáo doanh thu theo sản phẩm
print("=== Sales Report ===")
for i, (product, sale) in enumerate(zip(products, sales), 1):
    print(f"{i}. {product}: ${sale}")

# Output:
# === Sales Report ===
# 1. A: $100
# 2. B: $200
# 3. C: $150
# 4. D: $300
```

#### While Loop

```python
# === While cơ bản ===
# While lặp khi điều kiện là True
count = 0
while count < 5:               # Lặp trong khi count < 5
    print(count, end=" ")       # In rồi tăng count
    count += 1                  # Cập nhật biến để tránh infinite loop!
# Output: 0 1 2 3 4

# ⚠️ CẢNH BÁO: Infinite loop - vòng lặp vô tận
# while True:
#     print("This runs forever!")  # Chỉ thoát bằng Ctrl+C hoặc break

# === Infinite loop + break (pattern phổ biến) ===
# Dùng while True khi không biết trước số lần lặp
# while True:                     # Vòng lặp vô hạn
#     user_input = input("Enter 'quit' to exit: ")
#     if user_input == 'quit':
#         break                   # Thoát vòng lặp ngay lập tức
#     print(f"You entered: {user_input}")

# === While với else (chạy khi KHÔNG break) ===
# Python đặc biệt: while có else block!
count = 0
while count < 3:
    print(count, end=" ")       # 0 1 2
    count += 1
else:
    print("Done!")              # Output: Done! (chạy vì không có break)
# Output: 0 1 2 Done!

# So sánh với break:
count = 0
while count < 3:
    print(count, end=" ")
    if count == 1:
        break                  # Thoát sớm khi count = 1
    count += 1
else:
    print("Done!")              # KHÔNG chạy vì có break
# Output: 0 1

# === Walrus operator := trong while (Python 3.8+) ===
# Gán và kiểm tra cùng lúc - tránh phải viết 2 dòng
import random
while (n := random.randint(1, 10)) != 7:    # Gán n rồi kiểm tra
    print(f"Got {n}, not 7...")
print(f"Found 7!")

# === Real-world: retry pattern với while-else ===
max_retries = 3
attempt = 0

while attempt < max_retries:
    try:
        result = "success"  # Giả lập gọi API
        print(f"Attempt {attempt + 1}: {result}!")
        break                   # Thành công → thoát
    except Exception as e:
        attempt += 1
        print(f"Attempt {attempt} failed: {e}")
else:
    # else chạy khi while kết thúc bình thường (điều kiện = False)
    # Nghĩa là đã thử hết max_retries mà không break
    print("All retries exhausted!")

# === Real-world: đọc input cho đến khi hợp lệ ===
def get_positive_number():
    """Yêu cầu user nhập số dương."""
    while True:
        user_input = input("Enter a positive number: ")
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Invalid input. Try again.")

# number = get_positive_number()
# print(f"You entered: {number}")

# === Real-world: game loop ===
# def game_loop():
#     """Game loop đơn giản."""
#     player_hp = 100
#     while player_hp > 0:
#         action = input("Choose action (attack/run): ")
#         if action == "attack":
#             damage = random.randint(10, 30)
#             player_hp -= damage
#             print(f"You took {damage} damage! HP: {player_hp}")
#         elif action == "run":
#             print("You ran away!")
#             break
#         else:
#             print("Invalid action!")
#     else:
#         print("Game Over!")  # Chạy khi player_hp <= 0
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
# === Integer (số nguyên) - unlimited precision trong Python 3 ===
# Python 3 không giới hạn kích thước int (khác C/Java có int32/int64)
x = 10                  # Số nguyên dương
negative = -5           # Số nguyên âm
big = 10 ** 100         # Số rất lớn (googol) - Python xử lý được!

# Các hệ cơ số khác nhau
hex_val = 0xFF          # Hexadecimal (0x prefix) → 255
binary_val = 0b1010     # Binary (0b prefix) → 10
octal_val = 0o777       # Octal (0o prefix) → 511

print(hex_val)          # Output: 255
print(binary_val)       # Output: 10
print(octal_val)        # Output: 511

# Dấu _ để dễ đọc số lớn (Python 3.6+)
million = 1_000_000     # Dễ đọc hơn 1000000
print(million)          # Output: 1000000

# === Các phép toán số học ===
print(5 + 3)            # Output: 8   (cộng)
print(5 - 3)            # Output: 2   (trừ)
print(5 * 3)            # Output: 15  (nhân)
print(5 / 3)            # Output: 1.6666666666666667  (chia - luôn trả về float!)
print(5 // 3)           # Output: 1   (chia lấy phần nguyên - floor division)
print(5 % 3)            # Output: 2   (chia lấy phần dư - modulo)
print(5 ** 3)           # Output: 125 (lũy thừa)
print(abs(-5))          # Output: 5   (giá trị tuyệt đối)
print(divmod(5, 3))     # Output: (1, 2)  (trả về tuple (thương, dư))

# ⚠️ Edge case: phép chia / luôn trả về float
print(type(10 / 2))     # Output: <class 'float'>  (10/2 = 5.0, không phải 5!)
print(type(10 // 2))    # Output: <class 'int'>    (10//2 = 5)

# ⚠️ Edge case: floor division với số âm
print(-7 // 2)          # Output: -4  (floor về phía âm vô cực, không phải -3!)
print(-7 % 2)           # Output: 1   (luôn cùng dấu với divisor)

# === Real-world: kiểm tra số chẵn/lẻ, chia hết ===
def is_even(n: int) -> bool:
    return n % 2 == 0   # Số chẵn khi chia 2 dư 0

def is_divisible(n: int, divisor: int) -> bool:
    return n % divisor == 0

print(is_even(10))      # Output: True
print(is_even(7))       # Output: False
print(is_divisible(15, 3))  # Output: True  (15 chia hết cho 3)
```

#### Float

```python
# === Float (số thực) - double precision (64-bit IEEE 754) ===
x = 3.14                # Số thực thông thường
y = -2.5                # Số thực âm
scientific = 1.5e10     # Ký hiệu khoa học: 1.5 × 10^10 = 15000000000.0
small = 1.5e-10         # 1.5 × 10^-10 = 0.00000000015

print(scientific)       # Output: 15000000000.0
print(small)            # Output: 1.5e-10

# === Phép toán ===
print(3.14 + 1.0)       # Output: 4.140000000000001  (floating point imprecision!)
print(3.14 * 2)         # Output: 6.28
print(3.14 / 2)         # Output: 1.57

# ⚠️ PITFALL: Floating point imprecision
print(0.1 + 0.2)        # Output: 0.30000000000000004  (KHÔNG phải 0.3!)
print(0.1 + 0.2 == 0.3) # Output: False  ← Đây là lỗi phổ biến!

# ✅ Giải pháp: dùng round() hoặc math.isclose()
import math
print(round(0.1 + 0.2, 10))           # Output: 0.3
print(math.isclose(0.1 + 0.2, 0.3))  # Output: True  (so sánh với tolerance)

# Hoặc dùng Decimal cho tính toán tài chính
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # Output: 0.3  (chính xác!)

# === Special values ===
print(float('inf'))     # Output: inf   (dương vô cực)
print(float('-inf'))    # Output: -inf  (âm vô cực)
print(float('nan'))     # Output: nan   (Not a Number)

import math
print(math.isnan(float('nan')))   # Output: True
print(math.isinf(float('inf')))   # Output: True
print(math.isfinite(3.14))        # Output: True

# ⚠️ Edge case: NaN không bằng chính nó!
nan = float('nan')
print(nan == nan)       # Output: False  (NaN ≠ NaN theo IEEE 754)
print(math.isnan(nan))  # Output: True   (dùng isnan() để kiểm tra)

# ⚠️ Edge case: Infinity arithmetic
print(float('inf') + 1)    # Output: inf
print(float('inf') - float('inf'))  # Output: nan  (vô cực - vô cực = không xác định)

# === Real-world: làm tròn số ===
price = 99.999
print(round(price, 2))  # Output: 100.0  (làm tròn 2 chữ số thập phân)
print(round(price, 0))  # Output: 100.0  (làm tròn về số nguyên, vẫn là float)
print(int(price))       # Output: 99     (cắt phần thập phân, không làm tròn)
```

#### Boolean

```python
# === Boolean - kiểu dữ liệu logic ===
# bool là subclass của int: True = 1, False = 0
is_active = True        # Giá trị True (viết hoa chữ đầu)
is_deleted = False      # Giá trị False (viết hoa chữ đầu)

# === Phép toán logic ===
print(True and False)   # Output: False (AND: cả 2 phải True)
print(True or False)    # Output: True  (OR: ít nhất 1 True)
print(not True)         # Output: False (NOT: đảo ngược)
print(not False)        # Output: True

# === Truthy/Falsy values ===
# Falsy (coi như False): None, False, 0, 0.0, 0j, "", [], (), {}, set(), frozenset()
# Truthy (coi như True): mọi giá trị khác
print(bool(0))          # Output: False (số 0)
print(bool(1))          # Output: True  (số khác 0)
print(bool(-1))         # Output: True  (số âm cũng truthy)
print(bool([]))         # Output: False (list rỗng)
print(bool([1]))        # Output: True  (list có phần tử)
print(bool(""))         # Output: False (chuỗi rỗng)
print(bool("0"))        # Output: True  (chuỗi "0" là truthy! Khác số 0)
print(bool(None))       # Output: False (None là falsy)

# ⚠️ Edge case: bool là subclass của int
print(True + True)      # Output: 2   (True = 1, 1 + 1 = 2)
print(True * 5)         # Output: 5   (True = 1, 1 * 5 = 5)
print(False + 10)       # Output: 10  (False = 0, 0 + 10 = 10)
print(sum([True, False, True, True]))  # Output: 3 (đếm số True)

# ⚠️ Edge case: "0" là truthy nhưng 0 là falsy
print(bool("0"))        # Output: True  (chuỗi "0" không rỗng → truthy)
print(bool(0))          # Output: False (số 0 → falsy)

# === Short-circuit evaluation ===
# and: nếu vế trái False → trả về vế trái (không eval vế phải)
# or:  nếu vế trái True → trả về vế trái (không eval vế phải)
print(False and 1/0)    # Output: False (không eval 1/0 → không lỗi!)
print(True or 1/0)      # Output: True  (không eval 1/0 → không lỗi!)

# === Real-world: dùng truthy/falsy để viết code ngắn gọn ===
name = ""
display_name = name or "Anonymous"  # Nếu name falsy → dùng "Anonymous"
print(display_name)     # Output: Anonymous

items = []
if not items:           # Kiểm tra list rỗng
    print("No items")   # Output: No items

# Đếm số phần tử thỏa điều kiện
numbers = [1, 2, 3, 4, 5, 6]
even_count = sum(1 for n in numbers if n % 2 == 0)
print(even_count)       # Output: 3  (2, 4, 6)
```

#### String

```python
# === String (chuỗi) - immutable sequence of characters ===
# Python strings là immutable - không thể thay đổi sau khi tạo
s1 = 'Hello'             # Single quotes
s2 = "World"             # Double quotes (giống nhau)
s3 = '''Multi             # Triple quotes cho chuỗi nhiều dòng
line
string'''
s4 = """Multi            # Triple double quotes cũng được
line
string"""

# === String methods ===
s = "Hello World"

# Chuyển đổi case
print(s.upper())           # Output: HELLO WORLD (viết hoa tất cả)
print(s.lower())           # Output: hello world (viết thường tất cả)
print(s.capitalize())      # Output: Hello world (viết hoa chữ đầu)
print(s.title())           # Output: Hello World (viết hoa chữ đầu mỗi từ)
print(s.swapcase())        # Output: hELLO wORLD (đảo ngược case)

# Tìm kiếm và thay thế
print(s.find('World'))     # Output: 6 (vị trí bắt đầu của 'World', -1 nếu không tìm thấy)
print(s.find('Python'))    # Output: -1 (không tìm thấy)
print(s.index('World'))    # Output: 6 (giống find nhưng ValueError nếu không tìm thấy)
print(s.replace('World', 'Python'))  # Output: Hello Python (thay thế chuỗi)
print(s.replace('o', '0'))          # Output: Hell0 W0rld (thay thế tất cả)

# Kiểm tra đầu/cuối
print(s.startswith('Hello'))  # Output: True (kiểm tra bắt đầu)
print(s.endswith('World'))    # Output: True (kiểm tra kết thúc)
print(s.startswith('hello'))  # Output: False (case-sensitive!)

# Cắt và tách
print(s.split())             # Output: ['Hello', 'World'] (tách theo khoảng trắng)
print("a,b,c".split(','))   # Output: ['a', 'b', 'c'] (tách theo dấu phẩy)
print("  hello  ".strip())  # Output: hello (xóa khoảng trắng đầu/cuối)
print("hello".ljust(10))    # Output: 'hello     ' (căn trái, thêm space)
print("hello".rjust(10))    # Output: '     hello' (căn phải)
print("hello".center(10))   # Output: '  hello   ' (căn giữa)

# Định dạng
name = "Python"
version = 3.11
print(f"Welcome to {name} {version}")  # Output: Welcome to Python 3.11 (f-string)
print(f"{name:*>10}")                   # Output: ****Python (fill với *)
print(f"{version:.2f}")                 # Output: 3.11 (format số thập phân)

# === Edge cases và lưu ý quan trọng ===
# ⚠️ String là immutable - không thể thay đổi
s = "hello"
# s[0] = 'H'        # ❌ TypeError: 'str' object does not support item assignment
s = s.upper()       # ✅ Phải gán biến mới
print(s)             # Output: HELLO

# ⚠️ Index out of range
try:
    print(s[100])    # ❌ IndexError: string index out of range
except IndexError as e:
    print(f"Error: {e}")  # Output: Error: string index out of range

# ⚠️ Falsy string
print(bool(""))      # Output: False (chuỗi rỗng là falsy)
print(bool(" "))     # Output: True (khoảng trắng là truthy!)

# === Real-world use cases ===
# 1. Validation
email = "user@example.com"
is_valid = "@" in email and "." in email.split("@")[-1]
print(f"Email valid: {is_valid}")  # Output: Email valid: True

# 2. Parse data
log = "2024-01-15 ERROR: Connection failed"
date, level, msg = log.split(" ", 2)  # Split tối đa 2 lần
print(f"Date: {date}, Level: {level}")  # Output: Date: 2024-01-15, Level: ERROR

# 3. Sanitize input
user_input = "  <script>alert('xss')</script>  "
cleaned = user_input.strip().replace("<", "&lt;").replace(">", "&gt;")
print(cleaned)  # Output: &lt;script&gt;alert('xss')&lt;/script&gt;

# 4. Build URL query string
params = {"name": "John", "age": "30", "city": "NYC"}
query = "&".join(f"{k}={v}" for k, v in params.items())
print(query)  # Output: name=John&age=30&city=NYC
```

#### List

```python

# === List (danh sách) - mutable sequence ===
# List có thể thay đổi sau khi tạo - thêm, xóa, sửa
numbers = [1, 2, 3, 4, 5]       # Tạo list
mixed = [1, "hello", 3.14, True]  # List chứa nhiều kiểu (dynamic typing)

# === List Methods ===
numbers = [1, 2, 3, 4, 5]

# Thêm phần tử
numbers.append(6)                  # Thêm vào cuối → [1, 2, 3, 4, 5, 6]
print(numbers)                     # Output: [1, 2, 3, 4, 5, 6]

numbers.insert(0, 0)               # Chèn tại index 0 → [0, 1, 2, 3, 4, 5, 6]
print(numbers)                     # Output: [0, 1, 2, 3, 4, 5, 6]

# Xóa phần tử
numbers.remove(0)                  # Xóa theo giá trị (xóa đầu tiên tìm thấy)
print(numbers)                     # Output: [1, 2, 3, 4, 5, 6]

popped = numbers.pop()            # Xóa và trả về phần tử CUỐI
print(popped)                     # Output: 6
print(numbers)                    # Output: [1, 2, 3, 4, 5]

numbers.clear()                   # Xóa tất cả phần tử
print(numbers)                    # Output: []

# Sắp xếp và đảo ngược
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()                    # Sắp xếp tăng dần (in-place)
print(numbers)                    # Output: [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)        # Sắp xếp giảm dần
print(numbers)                    # Output: [9, 6, 5, 4, 3, 2, 1, 1]

numbers.reverse()                 # Đảo ngược (in-place)
print(numbers)                    # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# === Slicing - trích xuất phần tử ===
lst = [0, 1, 2, 3, 4]
print(lst[1:3])     # Output: [1, 2]      (index 1 đến 2, không bao gồm 3)
print(lst[:3])      # Output: [0, 1, 2]    (từ đầu đến index 2)
print(lst[3:])      # Output: [3, 4]       (từ index 3 đến cuối)
print(lst[::2])     # Output: [0, 2, 4]    (bước nhảy 2)
print(lst[::-1])    # Output: [4, 3, 2, 1, 0]  (đảo ngược)

# ⚠️ Edge case: index âm
print(lst[-1])      # Output: 4   (phần tử cuối cùng)
print(lst[-2])      # Output: 3   (phần tử thứ 2 từ cuối)

# === Real-world: List operations ===
# Lọc phần tử
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)                     # Output: [2, 4, 6, 8, 10]

# Tìm max/min
print(max(numbers))              # Output: 10
print(min(numbers))              # Output: 1

# Kiểm tra membership
print(5 in numbers)             # Output: True

# List comprehension với if-else
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]
print(labels)                    # Output: ['even', 'odd', 'even', 'odd', 'even']
```

#### Tuple

```python
# === Tuple - immutable sequence ===
# Tuple không thể thay đổi sau khi tạo (immutable)
# Dùng cho: tọa độ, trả về nhiều giá trị, dictionary keys
point = (10, 20)                 # Tọa độ 2D
coords = (1, 2, 3)               # Tuple 3 phần tử

# ⚠️ Tuple với 1 phần tử cần dấu phẩy!
single = (1,)                     # Tuple 1 phần tử (cần ,)
not_tuple = (1)                   # Đây là int, KHÔNG phải tuple!
print(type(single))               # Output: <class 'tuple'>
print(type(not_tuple))            # Output: <class 'int'>

# === Unpacking ===
x, y = point                     # Unpack tuple vào 2 biến
print(f"x={x}, y={y}")          # Output: x=10, y=20
a, b, c = coords                 # Unpack tuple 3 phần tử
print(a, b, c)                   # Output: 1 2 3

# === Named tuple (dùng khi cần truy cập theo tên) ===
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])  # Định nghĩa named tuple
p = Point(10, 20)                         # Tạo instance
print(p.x)                # Output: 10  (truy cập như attribute)
print(p.y)                # Output: 20
print(p[0])               # Output: 10  (cũng có thể truy cập như tuple)
print(p[1])               # Output: 20

# Named tuple với default values (Python 3.7+)
from collections import namedtuple
Point3D = namedtuple('Point3D', ['x', 'y', 'z'], defaults=(0, 0))
p2 = Point3D(10, 20)  # z sẽ là 0
print(p2)               # Output: Point3D(x=10, y=20, z=0)

# === Real-world use cases ===
# 1. Trả về nhiều giá trị từ function
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

min_val, max_val, avg = get_stats([1, 2, 3, 4, 5])
print(f"Min: {min_val}, Max: {max_val}, Avg: {avg}")
# Output: Min: 1, Max: 5, Avg: 3.0

# 2. Swap không cần biến tạm
a, b = 1, 2
a, b = b, a
print(f"a={a}, b={b}")  # Output: a=2, b=1

# 3. Dùng làm dictionary key (vì hashable/immutable)
locations = {
    (10, 20): "Office",
    (30, 40): "Home"
}
print(locations[(10, 20)])  # Output: Office
```

#### Set

```python
# === Set - tập hợp không có phần tử trùng lặp, không có thứ tự ===
# Dùng cho: loại bỏ trùng lặp, kiểm tra membership nhanh O(1), phép toán tập hợp
s = {1, 2, 3, 3, 3}             # Tạo set - tự động loại bỏ trùng lặp
print(s)                          # Output: {1, 2, 3}  (thứ tự không đảm bảo)

# ⚠️ Set rỗng phải dùng set(), không phải {}
empty_set = set()                 # ✅ Set rỗng
empty_dict = {}                   # ❌ Đây là dict rỗng, không phải set!
print(type(empty_set))            # Output: <class 'set'>
print(type(empty_dict))           # Output: <class 'dict'>

# === Set Methods ===
s = {1, 2, 3}
s.add(4)                          # Thêm phần tử
print(s)                          # Output: {1, 2, 3, 4}

s.remove(1)                       # Xóa phần tử (KeyError nếu không tồn tại)
print(s)                          # Output: {2, 3, 4}

s.discard(100)                    # Xóa phần tử (KHÔNG lỗi nếu không tồn tại)
print(s)                          # Output: {2, 3, 4}  (không thay đổi)

popped = s.pop()                  # Xóa và trả về phần tử BẤT KỲ (không đoán được)
print(popped)                     # Output: 2 (hoặc 3 hoặc 4 - không đảm bảo)

# === Set Operations (phép toán tập hợp) ===
a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)                      # Output: {1, 2, 3, 4}  (Union - hợp)
print(a & b)                      # Output: {2, 3}         (Intersection - giao)
print(a - b)                      # Output: {1}            (Difference - hiệu: a trừ b)
print(b - a)                      # Output: {4}            (Difference: b trừ a)
print(a ^ b)                      # Output: {1, 4}         (Symmetric difference - phần không chung)

# Kiểm tra quan hệ
print(a.issubset({1, 2, 3, 4}))  # Output: True  (a ⊆ {1,2,3,4})
print(a.issuperset({1, 2}))      # Output: True  (a ⊇ {1,2})
print(a.isdisjoint({5, 6}))      # Output: True  (không có phần tử chung)

# === Real-world use cases ===
# 1. Loại bỏ trùng lặp
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com"]
unique_emails = list(set(emails))
print(unique_emails)              # Output: ['a@x.com', 'b@x.com', 'c@x.com'] (thứ tự có thể khác)

# 2. Kiểm tra membership nhanh O(1) - nhanh hơn list O(n)
VALID_ROLES = {"admin", "user", "moderator"}
user_role = "admin"
if user_role in VALID_ROLES:
    print(f"Role {user_role} is valid")  # Output: Role admin is valid

# 3. Tìm phần tử chung/khác nhau
users_a = {"Alice", "Bob", "Charlie"}
users_b = {"Bob", "Charlie", "David"}
common = users_a & users_b
print(f"Common users: {common}")  # Output: Common users: {'Bob', 'Charlie'}
only_in_a = users_a - users_b
print(f"Only in A: {only_in_a}")  # Output: Only in A: {'Alice'}
```

#### Dictionary

```python
# === Dictionary (dict) - cặp key-value, hash table ===

# Dùng để tra cứu nhanh theo key, tương tự HashMap/Map trong các ngôn ngữ khác

user = {
"name": "John",
"age": 30,
"email": "john@example.com"
}

# === Truy cập ===

print(user["name"]) # Output: John (truy cập trực tiếp - lỗi nếu không có key)
print(user.get("name")) # Output: John (truy cập an toàn)
print(user.get("phone", "N/A")) # Output: N/A (default nếu key không tồn tại)
print(user.get("phone")) # Output: None (không có default → None)

# === Thêm/Sửa/Xóa ===

user["phone"] = "123-456" # Thêm hoặc cập nhật key
print(user["phone"]) # Output: 123-456

user["age"] = 31 # Cập nhật giá trị
print(user["age"]) # Output: 31

popped = user.pop("age") # Xóa và trả về giá trị
print(popped) # Output: 31
print("age" in user) # Output: False (đã bị xóa)

# === Duyệt Dictionary ===

print(user.keys()) # Output: dict_keys(['name', 'email', 'phone'])
print(user.values()) # Output: dict_values(['John', 'john@example.com', '123-456'])
print(user.items()) # Output: dict_items([('name', 'John'), ...])

# Duyệt key-value

for key, value in user.items():
    print(f"{key}: {value}")

# Output:

# name: John

# email: john@example.com

# phone: 123-456

# === Dictionary Comprehension ===

square_dict = {x: x**2 for x in range(5)}
print(square_dict) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# === Real-world use cases ===

# 1. Count occurrences

text = "hello world hello python world"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count) # Output: {'hello': 2, 'world': 2, 'python': 1}

# 2. Lookup table

ROLES = {
    "admin": {"permissions": ["read", "write", "delete"]},
    "user": {"permissions": ["read"]},
    "guest": {"permissions": []}
}
print(ROLES["admin"]["permissions"]) # Output: ['read', 'write', 'delete']

# 3. Merge dicts (Python 3.9+)

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2 # Python 3.9+: merge operator
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4} (b bị ghi đè)
```

#### None

```python
# === None - giá trị null của Python ===
# None là singleton - chỉ có 1 object None trong toàn bộ chương trình
# Dùng để biểu diễn "không có giá trị", "chưa khởi tạo", "không tìm thấy"
value = None                      # Gán None

# === Kiểm tra None ===
# ✅ Luôn dùng 'is' hoặc 'is not' để kiểm tra None
if value is None:
    print("No value")             # Output: No value

if value is not None:
    print("Has value")
else:
    print("Still None")           # Output: Still None

# ❌ Không nên dùng == với None (có thể bị override bởi __eq__)
# value == None  # Works nhưng không phải best practice

# === None trong function ===
def find_user(user_id: int):
    """Trả về None nếu không tìm thấy."""
    if user_id == 1:
        return {"id": 1, "name": "John"}
    return None                   # Explicit return None

user = find_user(1)
print(user)                       # Output: {'id': 1, 'name': 'John'}

user = find_user(999)
print(user)                       # Output: None

# Kiểm tra trước khi dùng
if user is not None:
    print(user["name"])
else:
    print("User not found")       # Output: User not found

# === None vs 0 vs "" vs [] ===
# Tất cả đều falsy nhưng có ý nghĩa khác nhau
print(None is None)               # Output: True
print(0 is None)                  # Output: False (0 ≠ None)
print("" is None)                 # Output: False ("" ≠ None)
print([] is None)                 # Output: False ([] ≠ None)

# ⚠️ Edge case: None trong list
items = [1, None, 3, None, 5]
non_none = [x for x in items if x is not None]
print(non_none)                   # Output: [1, 3, 5]

# === Real-world: Optional pattern ===
from typing import Optional

def get_config(key: str) -> Optional[str]:
    """Lấy config, trả về None nếu không tồn tại."""
    config = {"host": "localhost", "port": "5432"}
    return config.get(key)        # dict.get() trả về None nếu không có key

host = get_config("host")
print(host)                       # Output: localhost

db_name = get_config("db_name")
print(db_name)                    # Output: None

# Dùng walrus operator để kiểm tra và gán cùng lúc
if (host := get_config("host")) is not None:
    print(f"Connecting to {host}")  # Output: Connecting to localhost
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

# === Threading - chạy nhiều threads trong cùng process ===
# ⚠️ Python có GIL (Global Interpreter Lock) → threads không chạy song song CPU-bound tasks
# Tốt cho I/O-bound tasks (network, file, database)

def worker(name, delay):
    """Worker function chạy trong thread riêng."""
    print(f"{name} started")      # Thread bắt đầu
    time.sleep(delay)             # Simulate I/O operation
    print(f"{name} finished")     # Thread hoàn thành

# Tạo thread với target function và arguments
t1 = threading.Thread(target=worker, args=("Thread-1", 2))  # Chạy sau 2 giây
t2 = threading.Thread(target=worker, args=("Thread-2", 1))  # Chạy sau 1 giây

t1.start()                       # Bắt đầu thread (non-blocking)
t2.start()                       # Bắt đầu thread (non-blocking)

# ⚠️ join() chặn cho đến khi thread hoàn thành
t1.join()                        # Đợi t1 hoàn thành
t2.join()                        # Đợi t2 hoàn thành

print("All threads done!")       # Output sau khi cả 2 thread hoàn thành

# === Thread với class ===
class MyThread(threading.Thread):
    """Custom thread class."""
    def __init__(self, name):
        super().__init__()        # Gọi constructor của threading.Thread
        self.name = name

    def run(self):
        """Method này tự động chạy khi thread.start() được gọi."""
        print(f"Running {self.name}")

# Sử dụng
thread = MyThread("CustomThread")
thread.start()
thread.join()

# === Thread Pool - tái sử dụng threads ===
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    # submit() - gửi task cho executor, trả về Future
    future1 = executor.submit(worker, "Task-1", 1)
    future2 = executor.submit(worker, "Task-2", 1)

    # map() - gửi nhiều tasks với các arguments khác nhau
    results = executor.map(lambda x: worker(x, 1), ["A", "B", "C"])

# === Real-world: Download nhiều files đồng thời ===
import urllib.request

def download(url):
    """Download một URL."""
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.read()
    except Exception as e:
        return f"Error: {e}"

urls = [
    "https://python.org",
    "https://github.com",
    "https://stackoverflow.com"
]

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(download, urls))
    # Download tất cả URLs song song

# === ⚠️ Thread Safety - Race Condition ===
# Khi nhiều threads cùng truy cập shared data → race condition
counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # ⚠️ KHÔNG atomic - race condition!

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Expected: 500000, Actual: {counter}")  # Output: < 500000 (mất updates!)

# ✅ Giải pháp: dùng Lock
counter = 0
lock = threading.Lock()

def increment_safe():
    global counter
    for _ in range(100000):
        with lock:                    # Lock trước khi đọc/ghi
            counter += 1

threads = [threading.Thread(target=increment_safe) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Expected: 500000, Actual: {counter}")  # Output: 500000 (đúng!)
```

#### Multiprocessing

```python
import multiprocessing
from multiprocessing import Process, Pool

# === Multiprocessing - chạy nhiều processes riêng biệt ===
# Mỗi process có Python interpreter riêng → KHÔNG bị GIL
# Tốt cho CPU-bound tasks (tính toán nặng, xử lý ảnh, ML)
# ⚠️ Overhead cao hơn threading (tạo process tốn thời gian hơn)

def worker(x):
    """CPU-bound task: tính bình phương."""
    return x * x

# === Process đơn lẻ ===
# ⚠️ PHẢI có if __name__ == '__main__' trên Windows/macOS
if __name__ == '__main__':
    p = Process(target=worker, args=(5,))  # Tạo process mới
    p.start()                               # Bắt đầu process
    p.join()                                # Đợi process hoàn thành
    print("Process done")

# === Pool - quản lý nhiều processes ===
# Pool tạo sẵn N processes, tái sử dụng cho nhiều tasks
if __name__ == '__main__':
    with Pool(4) as pool:                   # 4 worker processes
        result = pool.map(worker, [1, 2, 3, 4])  # Phân phối tasks
        print(result)                       # Output: [1, 4, 9, 16]

    # Pool.starmap() cho functions nhiều arguments
    def add(a, b):
        return a + b

    with Pool(4) as pool:
        results = pool.starmap(add, [(1, 2), (3, 4), (5, 6)])
        print(results)                      # Output: [3, 7, 11]

# === Shared memory - chia sẻ dữ liệu giữa processes ===
from multiprocessing import Value, Array

# Value: chia sẻ 1 giá trị đơn
counter = Value('i', 0)                     # 'i' = integer, initial = 0

# Array: chia sẻ mảng
shared_array = Array('i', 10)              # 10 integers

# === Real-world: xử lý ảnh song song ===
from concurrent.futures import ProcessPoolExecutor

def process_image(image_path):
    """Xử lý 1 ảnh (CPU-bound)."""
    # Giả lập xử lý ảnh nặng
    import time
    time.sleep(0.1)
    return f"Processed: {image_path}"

if __name__ == '__main__':
    image_paths = [f"image_{i}.jpg" for i in range(10)]

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_image, image_paths))
        print(f"Processed {len(results)} images")

# === Threading vs Multiprocessing ===
# Threading:
#   ✅ Nhẹ, ít overhead
#   ✅ Chia sẻ memory dễ dàng
#   ❌ GIL giới hạn CPU-bound tasks
#   → Dùng cho: I/O-bound (network, file, DB)
#
# Multiprocessing:
#   ✅ Không bị GIL, thực sự song song
#   ❌ Overhead cao (tạo process, copy memory)
#   ❌ Khó chia sẻ data
#   → Dùng cho: CPU-bound (tính toán, xử lý ảnh, ML)
```

#### Async/Await (Python 3.5+)

```python
import asyncio

# === Async/Await - Cooperative multitasking ===
# Coroutine: function với async def, có thể bị tạm dừng tại await
# Event loop: quản lý và chạy các coroutines
# Tốt cho I/O-bound tasks với nhiều concurrent operations

async def fetch_data(name: str, delay: float):
    """Coroutine giả lập fetch data từ API."""
    print(f"[{name}] Fetching data...")    # Bắt đầu fetch
    await asyncio.sleep(delay)             # Tạm dừng, nhường CPU cho coroutine khác
    print(f"[{name}] Done!")               # Hoàn thành
    return {"name": name, "data": "result"}

async def main():
    # === Single task ===
    result = await fetch_data("Task-1", 1)  # Đợi coroutine hoàn thành
    print(result)                           # Output: {'name': 'Task-1', 'data': 'result'}

    # === Multiple tasks song song với gather() ===
    # gather() chạy tất cả coroutines ĐỒNG THỜI, đợi tất cả hoàn thành
    results = await asyncio.gather(
        fetch_data("A", 1),
        fetch_data("B", 2),
        fetch_data("C", 0.5),
    )
    # Tổng thời gian ≈ 2s (max), không phải 3.5s (sum)
    print(f"Got {len(results)} results")    # Output: Got 3 results

    # === Timeout ===
    try:
        async with asyncio.timeout(1.5):    # Python 3.11+
            await fetch_data("Slow", 3)     # Sẽ timeout sau 1.5s
    except asyncio.TimeoutError:
        print("Timed out!")                 # Output: Timed out!

    # === asyncio.wait_for() cho Python < 3.11 ===
    try:
        result = await asyncio.wait_for(fetch_data("Slow", 3), timeout=1.5)
    except asyncio.TimeoutError:
        print("Timed out!")

# Chạy event loop
asyncio.run(main())

# === Real-world: Async web scraper ===
import asyncio

async def scrape_page(url: str) -> dict:
    """Scrape một trang web."""
    print(f"Scraping {url}...")
    await asyncio.sleep(0.5)               # Simulate network request
    return {"url": url, "status": 200, "content": "..."}

async def scrape_all(urls: list[str]) -> list[dict]:
    """Scrape nhiều trang song song."""
    tasks = [scrape_page(url) for url in urls]
    return await asyncio.gather(*tasks)    # Chạy tất cả song song

async def main_scraper():
    urls = [f"https://example.com/page/{i}" for i in range(10)]
    results = await scrape_all(urls)
    print(f"Scraped {len(results)} pages")  # Output: Scraped 10 pages

asyncio.run(main_scraper())

# === ⚠️ Edge cases ===
# 1. Không thể await trong non-async function
# def sync_func():
#     await asyncio.sleep(1)  # ❌ SyntaxError

# 2. asyncio.run() không thể gọi trong event loop đang chạy
# asyncio.run(main())  # ❌ RuntimeError nếu đang trong event loop (Jupyter)
# Dùng: await main()  # ✅ Trong Jupyter

# 3. CPU-bound tasks vẫn block event loop
async def cpu_heavy():
    result = sum(range(10_000_000))  # ❌ Block event loop!
    return result

# ✅ Giải pháp: chạy trong thread pool
async def cpu_heavy_safe():
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, lambda: sum(range(10_000_000)))
    return result
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
# === Exception Hierarchy (quan trọng nhất) ===
# BaseException
# ├── SystemExit          # sys.exit() - KHÔNG nên bắt
# ├── KeyboardInterrupt   # Ctrl+C - KHÔNG nên bắt
# ├── GeneratorExit       # Generator bị close
# └── Exception           # ← Bắt từ đây trở xuống
#     ├── ValueError
#     ├── TypeError
#     ├── KeyError
#     ├── IndexError
#     ├── AttributeError
#     ├── FileNotFoundError
#     ├── RuntimeError
#     └── ...

# === Ví dụ từng loại exception phổ biến ===

# --- SyntaxError: lỗi cú pháp (phát hiện khi parse, TRƯỚC khi chạy) ---
# eval("if True print('hello')")  # ❌ SyntaxError: invalid syntax
# Không thể bắt bằng try-except trong cùng file (vì file không parse được)

# --- IndentationError: lỗi thụt lề (subclass của SyntaxError) ---
# def foo():
# print("hello")  # ❌ IndentationError: expected an indented block

# --- TypeError: sai kiểu dữ liệu trong phép toán ---
try:
    result = "hello" + 5           # str + int → không hợp lệ
except TypeError as e:
    print(f"TypeError: {e}")
    # Output: TypeError: can only concatenate str (not "int") to str

try:
    len(42)                        # int không có len()
except TypeError as e:
    print(f"TypeError: {e}")
    # Output: TypeError: object of type 'int' has no len()

# --- ValueError: đúng kiểu nhưng sai giá trị ---
try:
    int("abc")                     # str đúng kiểu nhưng không parse được
except ValueError as e:
    print(f"ValueError: {e}")
    # Output: ValueError: invalid literal for int() with base 10: 'abc'

try:
    import math
    math.sqrt(-1)                  # Số âm không có căn bậc 2 thực
except ValueError as e:
    print(f"ValueError: {e}")
    # Output: ValueError: math domain error

# --- NameError: biến chưa được định nghĩa ---
try:
    print(undefined_variable)      # Biến chưa tồn tại
except NameError as e:
    print(f"NameError: {e}")
    # Output: NameError: name 'undefined_variable' is not defined

# --- IndexError: truy cập index ngoài phạm vi ---
try:
    lst = [1, 2, 3]
    print(lst[10])                 # Index 10 không tồn tại (chỉ có 0, 1, 2)
except IndexError as e:
    print(f"IndexError: {e}")
    # Output: IndexError: list index out of range

# --- KeyError: truy cập key không tồn tại trong dict ---
try:
    d = {"name": "John"}
    print(d["age"])                # Key "age" không tồn tại
except KeyError as e:
    print(f"KeyError: {e}")
    # Output: KeyError: 'age'

# ✅ Tránh KeyError: dùng .get()
print(d.get("age", "N/A"))        # Output: N/A (không lỗi)

# --- AttributeError: truy cập attribute không tồn tại ---
try:
    x = 42
    x.append(1)                    # int không có method .append()
except AttributeError as e:
    print(f"AttributeError: {e}")
    # Output: AttributeError: 'int' object has no attribute 'append'

# --- FileNotFoundError: file không tồn tại ---
try:
    with open("nonexistent_file.txt") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
    # Output: FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'

# --- IOError / OSError: lỗi I/O (file, network, OS) ---
# FileNotFoundError, PermissionError, IsADirectoryError đều kế thừa OSError
try:
    with open("/root/secret.txt") as f:  # Không có quyền đọc
        pass
except PermissionError as e:
    print(f"PermissionError: {e}")
    # Output: PermissionError: [Errno 13] Permission denied: '/root/secret.txt'

# --- RuntimeError: lỗi runtime chung ---
# Dùng khi không có exception cụ thể phù hợp
try:
    raise RuntimeError("Something went wrong at runtime")
except RuntimeError as e:
    print(f"RuntimeError: {e}")

# --- NotImplementedError: method chưa được implement ---
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError("Subclass must implement area()")

# --- StopIteration: iterator hết phần tử ---
it = iter([1, 2])
next(it)  # 1
next(it)  # 2
try:
    next(it)                       # Hết phần tử
except StopIteration:
    print("Iterator exhausted")    # Output: Iterator exhausted

# --- ZeroDivisionError: chia cho 0 ---
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
    # Output: ZeroDivisionError: division by zero

# --- ImportError / ModuleNotFoundError: import thất bại ---
try:
    import nonexistent_module
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")
    # Output: ModuleNotFoundError: No module named 'nonexistent_module'

# --- RecursionError: đệ quy quá sâu ---
try:
    def infinite(): return infinite()
    infinite()
except RecursionError as e:
    print(f"RecursionError: {e}")
    # Output: RecursionError: maximum recursion depth exceeded

# --- KeyboardInterrupt: Ctrl+C (KHÔNG nên bắt trong except Exception) ---
# ⚠️ KeyboardInterrupt kế thừa BaseException, KHÔNG phải Exception
# → except Exception sẽ KHÔNG bắt KeyboardInterrupt (đúng ý đồ)

# --- OverflowError: số quá lớn ---
try:
    import math
    math.exp(1000)                 # e^1000 quá lớn cho float
except OverflowError as e:
    print(f"OverflowError: {e}")
    # Output: OverflowError: math range error

# === Bảng tóm tắt: khi nào gặp exception nào ===
# ┌─────────────────────┬──────────────────────────────────────────┐
# │ Exception           │ Khi nào xảy ra                           │
# ├─────────────────────┼──────────────────────────────────────────┤
# │ TypeError           │ Sai kiểu: "a" + 1, len(42)              │
# │ ValueError          │ Sai giá trị: int("abc"), sqrt(-1)        │
# │ KeyError            │ Dict key không tồn tại: d["missing"]     │
# │ IndexError          │ List index ngoài phạm vi: lst[999]       │
# │ AttributeError      │ Attribute không tồn tại: 42.append()     │
# │ NameError           │ Biến chưa định nghĩa: print(x)          │
# │ FileNotFoundError   │ File không tồn tại: open("missing.txt")  │
# │ ZeroDivisionError   │ Chia cho 0: 10 / 0                      │
# │ ImportError         │ Import thất bại: import nonexistent      │
# │ RecursionError      │ Đệ quy quá sâu (default: 1000 levels)   │
# │ StopIteration       │ Iterator hết phần tử: next(empty_iter)   │
# │ PermissionError     │ Không có quyền truy cập file/resource    │
# └─────────────────────┴──────────────────────────────────────────┘
```

#### Custom Error Hierarchy

```python
# === Custom Error Hierarchy - tổ chức exceptions theo cấp bậc ===
# Quy tắc: tạo base exception cho app, các exception cụ thể kế thừa từ đó
# Giúp caller bắt lỗi ở mức chi tiết hoặc tổng quát tùy nhu cầu

class AppError(Exception):
    """Base exception cho toàn bộ application.
    Bắt AppError = bắt TẤT CẢ lỗi của app."""
    def __init__(self, message: str, code: str = "UNKNOWN"):
        self.code = code
        super().__init__(message)

class ValidationError(AppError):
    """Lỗi validation input từ user."""
    def __init__(self, field: str, message: str):
        self.field = field
        super().__init__(f"Validation error on '{field}': {message}", code="VALIDATION_ERROR")

class DatabaseError(AppError):
    """Lỗi liên quan đến database."""
    def __init__(self, message: str):
        super().__init__(message, code="DB_ERROR")

class ConnectionError(DatabaseError):
    """Không kết nối được database."""
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        super().__init__(f"Cannot connect to {host}:{port}")

class QueryError(DatabaseError):
    """Lỗi khi thực thi query."""
    def __init__(self, query: str, reason: str):
        self.query = query
        super().__init__(f"Query failed: {reason}")

class AuthError(AppError):
    """Lỗi authentication/authorization."""
    def __init__(self, message: str):
        super().__init__(message, code="AUTH_ERROR")

class NotFoundError(AppError):
    """Resource không tìm thấy."""
    def __init__(self, resource: str, identifier):
        self.resource = resource
        self.identifier = identifier
        super().__init__(f"{resource} with id={identifier} not found", code="NOT_FOUND")

# === Sử dụng ===
def get_user(user_id: int):
    if user_id <= 0:
        raise ValidationError("user_id", "Must be positive")
    if user_id == 999:
        raise NotFoundError("User", user_id)
    return {"id": user_id, "name": "John"}

# Bắt lỗi cụ thể
try:
    user = get_user(999)
except NotFoundError as e:
    print(f"[{e.code}] {e}")
    # Output: [NOT_FOUND] User with id=999 not found
    print(f"Resource: {e.resource}, ID: {e.identifier}")
    # Output: Resource: User, ID: 999

# Bắt lỗi tổng quát (tất cả lỗi app)
try:
    user = get_user(-1)
except AppError as e:
    print(f"[{e.code}] {e}")
    # Output: [VALIDATION_ERROR] Validation error on 'user_id': Must be positive

# === Hierarchy diagram ===
# AppError
# ├── ValidationError
# ├── DatabaseError
# │   ├── ConnectionError
# │   └── QueryError
# ├── AuthError
# └── NotFoundError
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
# === Import module - nạp module vào namespace hiện tại ===
import math                        # Import toàn bộ module math
print(math.sqrt(16))               # Output: 4.0 (truy cập qua tên module)
print(math.pi)                     # Output: 3.141592653589793

# Import với alias - đặt tên ngắn hơn
import numpy as np                 # Convention: numpy → np
import pandas as pd                # Convention: pandas → pd
# np.array([1, 2, 3])             # Dùng alias thay vì numpy.array

# Import specific names - chỉ import những gì cần
from math import sqrt, pi          # Import sqrt và pi vào namespace hiện tại
print(sqrt(25))                    # Output: 5.0 (không cần math.sqrt)
print(pi)                          # Output: 3.141592653589793

from collections import defaultdict as dd  # Import với alias

# ⚠️ Import all - KHÔNG nên dùng
# from math import *               # ❌ Ô nhiễm namespace, khó debug
# sqrt(16)                         # Không rõ sqrt từ đâu

# === Thứ tự import (PEP 8) ===
# 1. Standard library
import os
import sys
from pathlib import Path

# 2. Third-party packages
# import requests
# import numpy as np

# 3. Local modules
# from myapp import utils

# === Conditional import ===
try:
    import ujson as json            # Thử import ujson (nhanh hơn)
except ImportError:
    import json                     # Fallback về json chuẩn

# === Lazy import (chỉ import khi cần) ===
def process_image(path):
    """Import PIL chỉ khi function được gọi."""
    from PIL import Image           # Import trong function
    img = Image.open(path)
    return img

# === Real-world: kiểm tra package có sẵn không ===
def check_optional_dependency(package_name: str) -> bool:
    """Kiểm tra package có được cài không."""
    import importlib.util
    spec = importlib.util.find_spec(package_name)
    return spec is not None

print(check_optional_dependency("json"))     # Output: True (stdlib)
print(check_optional_dependency("numpy"))    # Output: True/False (tùy cài đặt)
```

#### Module

```python
# === Module - file .py chứa code Python ===
# Mỗi file .py là 1 module, có thể import từ module khác

# mymodule.py
def greet(name: str) -> str:
    """Trả về lời chào."""
    return f"Hello, {name}"

class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

# === __name__ check - phân biệt chạy trực tiếp vs import ===
# Khi chạy trực tiếp: __name__ == "__main__"
# Khi import từ module khác: __name__ == "mymodule"
if __name__ == "__main__":
    # Code này CHỈ chạy khi file được chạy trực tiếp
    # Không chạy khi file được import
    print(greet("World"))          # Output: Hello, World
    calc = Calculator()
    print(calc.add(1, 2))          # Output: 3

# === Module attributes ===
# __name__: tên module
# __file__: đường dẫn file
# __doc__: docstring của module
# __all__: danh sách public API

# === Real-world: module với __all__ ===
# utils.py
__all__ = ["public_func", "PublicClass"]  # Chỉ export những gì trong __all__

def public_func():
    """Hàm public - có trong __all__."""
    return "public"

def _private_func():
    """Hàm private - không có trong __all__, convention dùng _ prefix."""
    return "private"

class PublicClass:
    pass

class _PrivateClass:
    pass
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
# === Circular Dependency - Khi nào xảy ra? ===
# Xảy ra khi:
#   module_a.py imports module_b
#   module_b.py imports module_a
# → Python chưa load xong module này đã cần module kia

# === Ví dụ lỗi ===
# models.py
# from user_service import UserService  # ❌ Lỗi! UserService chưa được định nghĩa
# class User(models.Model):
#     name = models.CharField(max_length=100)

# user_service.py
# from models import User  # ❌ Lỗi! User model chưa được định nghĩa
# class UserService:
#     def get_users(self):
#         return User.objects.all()

# === Giải pháp 1: Import trong function (Lazy import) ===
# models.py
# class User(models.Model):
#     name = models.CharField(max_length=100)

# user_service.py - KHÔNG import ở top-level
class UserService:
    def get_users(self):
        from models import User  # Import ở trong method
        return User.objects.all()

    def create_user(self, name):
        from models import User
        return User.objects.create(name=name)

# ⚠️ Ưu điểm: tránh circular import
# ⚠️ Nhược điểm: import lặp lại mỗi lần gọi (nhưng Python cache nên OK)

# === Giải pháp 2: Import module thay vì import function ===
# Thay vì: from module_b import func_b
# Dùng: import module_b → module_b.func_b()

# user_service.py
import models  # Import cả module, không phải class

class UserService:
    def get_users(self):
        return models.User.objects.all()  # Dùng models.User

# === Giải pháp 3: Tách interface ra module riêng ===
# interfaces.py - Định nghĩa abstract classes
# from abc import ABC, abstractmethod
# class IUserService(ABC):
#     @abstractmethod
#     def get_users(self): pass

# models.py
# from interfaces import IUserService
# class User(models.Model): ...

# user_service.py
# from interfaces import IUserService
# class UserService(IUserService): ...

# === Giải pháp 4: TYPE_CHECKING (chỉ import cho type hints) ===
from __future__ import annotations  # Python 3.7+, forward references
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Chỉ import khi type checking (mypy, pyright)
    # KHÔNG import khi chạy thực tế
    from module_b import ClassB

# Không cần import ClassB, dùng string annotation
def process(obj: 'ClassB') -> 'ClassB':  # Hoặc dùng forward reference
    return obj

# Hoặc không cần annotation
def process(obj) -> object:
    return obj

# === Giải pháp 5: Refactor cấu trúc ===
# Gom các class có circular relationship vào cùng 1 module
# Hoặc dùng dependency injection

# === Giải pháp 6: Import cuối file ===
# Đôi khi circular import xảy ra do thứ tự import
# Thử di chuyển import xuống cuối file

# === Real-world example ===
# Giả sử có:
# app/
#   __init__.py
#   models.py         # Django models
#   services.py       # Business logic
#   serializers.py    # Django REST framework serializers

# serializers.py (lỗi)
# from app.models import User  # ❌ Có thể lỗi nếu models import serializers

# services.py (lỗi)
# from app.models import User
# from app.serializers import UserSerializer  # ❌ Có thể lỗi

# Cách fix:
# services.py
class UserService:
    def get_user_data(self, user_id):
        from app.models import User  # Lazy import
        from app.serializers import UserSerializer  # Lazy import
        user = User.objects.get(id=user_id)
        return UserSerializer(user).data

# === Cách phát hiện circular dependency ===
# 1. Chạy: python -c "import module_name"
# 2. ImportError: cannot import name ...
# 3. Dùng tool: pip install pydep
#    pydep -f .  # Hiển thị dependency graph
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

# === requests - HTTP library phổ biến nhất cho Python ===
# pip install requests

# === GET request ===
response = requests.get("https://api.example.com/users")
print(response.status_code)       # Output: 200 (HTTP status code)
print(response.json())            # Output: {...} (parse JSON response)
print(response.text)              # Output: '{"users": [...]}' (raw text)
print(response.headers)           # Output: {'Content-Type': 'application/json', ...}

# GET với query parameters
response = requests.get(
    "https://api.example.com/users",
    params={"page": 1, "limit": 10, "sort": "name"}
    # URL: https://api.example.com/users?page=1&limit=10&sort=name
)

# === POST request ===
response = requests.post(
    "https://api.example.com/users",
    json={"name": "John", "email": "john@example.com"}  # Tự set Content-Type: application/json
)
print(response.status_code)       # Output: 201 (Created)
print(response.json())            # Output: {'id': 1, 'name': 'John', ...}

# POST với form data
response = requests.post(
    "https://api.example.com/login",
    data={"username": "john", "password": "secret"}  # form-urlencoded
)

# === Headers ===
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9...",
    "Content-Type": "application/json",
    "Accept": "application/json"
}
response = requests.get("https://api.example.com/profile", headers=headers)

# === Error handling ===
try:
    response = requests.get("https://api.example.com/users", timeout=10)
    response.raise_for_status()   # Raise HTTPError nếu status >= 400
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")
except requests.exceptions.ConnectionError:
    print("Connection failed")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# === Session - tái sử dụng connection, headers ===
# Session tự động giữ cookies, headers, auth giữa các requests
session = requests.Session()
session.headers.update({
    "Authorization": "Bearer token",
    "User-Agent": "MyApp/1.0"
})

# Tất cả requests qua session đều có headers trên
response1 = session.get("https://api.example.com/users")
response2 = session.get("https://api.example.com/posts")

# === Real-world: API client class ===
class APIClient:
    """Wrapper cho requests với retry và error handling."""

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })

    def get(self, endpoint: str, **kwargs) -> dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, timeout=30, **kwargs)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict) -> dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data, timeout=30)
        response.raise_for_status()
        return response.json()

# Sử dụng
# client = APIClient("https://api.example.com", "my-api-key")
# users = client.get("users", params={"page": 1})
# new_user = client.post("users", {"name": "John"})
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
# === Đọc file với context manager (tự động đóng) ===
# ⚠️ LUÔN dùng with để đảm bảo file được đóng

# Đọc toàn bộ file vào memory
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# Đọc từng dòng - tốt cho file lớn (không load hết vào memory)
with open("file.txt", "r") as f:
    for line in f:            # File object là iterator
        print(line, end="")   # end="" tránh dòng trống thừa (line đã có \n)

# Đọc thành list các dòng
with open("file.txt", "r") as f:
    lines = f.readlines()    # List[str] - mỗi dòng là 1 phần tử

# Đọc N ký tự
with open("file.txt", "r") as f:
    first_100 = f.read(100)  # Đọc 100 ký tự đầu tiên

# ⚠️ Encoding: LUÔN chỉ định encoding
# Windows default: 'utf-8' hoặc 'cp1252'
# Linux/Mac default: 'utf-8'
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

#### Write File

```python
# === Ghi file ===
# 'w' - ghi đè (xóa file cũ nếu có)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello World\n")  # Viết chuỗi vào file
    f.write("Line 2\n")

# 'a' - append (thêm vào cuối file)
with open("log.txt", "a") as f:
    f.write("New log entry\n")

# 'x' - tạo mới, lỗi nếu file đã tồn tại
try:
    with open("new.txt", "x") as f:
        f.write("New file\n")
except FileExistsError:
    print("File đã tồn tại!")

# Ghi nhiều dòng
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)  # Ghi list các chuỗi

# ⚠️ File modes:
# 'r'  - đọc (mặc định)
# 'w'  - ghi đè
# 'a'  - append
# 'x'  - tạo mới
# 'r+' - đọc + ghi
# 'w+' - đọc + ghi (đè)
# 'a+' - đọc + append
# Thêm 'b' cho binary: 'rb', 'wb', 'ab'
```

#### Path (Python 3.4+)

```python
from pathlib import Path

# === pathlib - OOP cho đường dẫn (khuyến khích) ===
p = Path("file.txt")

# Kiểm tra
print(p.exists())          # Output: True/False (file có tồn tại không)
print(p.is_file())         # Output: True/False (có phải file không)
print(p.is_dir())          # Output: True/False (có phải directory không)
print(p.is_symlink())      # Output: True/False (có phải symlink không)

# Đọc/Ghi (tiện hơn open)
content = p.read_text(encoding="utf-8")  # Đọc text
p.write_text("Hello", encoding="utf-8") # Ghi text
bytes_data = p.read_bytes()              # Đọc binary

# Thông tin
print(p.name)         # Output: file.txt (tên file)
print(p.stem)        # Output: file (không có extension)
print(p.suffix)      # Output: .txt (extension)
print(p.parent)      # Output: Path(/home/user) (thư mục cha)
print(p.parts)       # Output: ('/home', 'user', 'file.txt')

# Glob - tìm files theo pattern
for file in Path(".").glob("*.py"):         # Tìm .py files
    print(file)

for file in Path(".").glob("**/*.py"):      # Recursive search
    print(file)

# Walk - duyệt cây thư mục
for item in Path(".").rglob("*"):          # Recursive glob
    if item.is_file():
        print(f"File: {item}")

# Resolve - lấy đường dẫn tuyệt đối
abs_path = p.resolve()
print(abs_path)  # Output: /home/user/project/file.txt

# Tạo directory
Path("new_dir").mkdir(exist_ok=True)           # Tạo 1 directory
Path("a/b/c").mkdir(parents=True, exist_ok=True) # Tạo cả cây

# === Real-world: đọc file lớn line-by-line ===
def process_large_file(filepath: str):
    """Đọc và xử lý file lớn mà không load hết vào memory."""
    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):  # enumerate với start=1
            line = line.strip()                  # Xóa \n và whitespace
            if not line or line.startswith("#"): # Bỏ dòng trống và comment
                continue
            # Xử lý từng dòng...
            print(f"Line {line_num}: {line}")

# === Real-world: safe file write ===
import tempfile
import shutil

def safe_write(filepath: str, content: str):
    """Ghi file an toàn - không làm mất file cũ nếu lỗi."""
    filepath = Path(filepath)
    tmp = filepath.with_suffix('.tmp')

    try:
        tmp.write_text(content, encoding='utf-8')
        tmp.replace(filepath)  # Atomic trên POSIX
    except Exception:
        tmp.unlink(missing_ok=True)  # Xóa temp file nếu lỗi
        raise
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

# === Serialize Python dict → JSON string ===
data = {"name": "John", "age": 30, "active": True}  # Python dict với các key-value
json_str = json.dumps(data)                          # Serialize thành chuỗi JSON compact
print(json_str)                                      # Output: {"name": "John", "age": 30, "active": true}

# ⚠️ Lưu ý: Boolean trong Python (True/False) → JSON (true/false) lowercase
# ⚠️ None trong Python → JSON null

# === Serialize với indent (định dạng đẹp) ===
json_str = json.dumps(data, indent=2)  # Thêm indent 2 spaces cho dễ đọc
print(json_str)                         # Output:
# {
#   "name": "John",
#   "age": 30,
#   "active": true
# }

# === Deserialize: JSON string → Python dict ===
data = json.loads(json_str)  # Parse JSON string thành Python object
print(data["name"])          # Output: John
print(type(data["active"]))  # Output: <class 'bool'> - boolean được convert về Python bool

# === Serialize ra file ===
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=2)  # Ghi trực tiếp vào file object

# === Deserialize từ file ===
# with open("data.json", "r") as f:
#     data = json.load(f)  # Đọc trực tiếp từ file object

# === Custom Encoder cho kiểu dữ liệu không có sẵn trong JSON ===
from datetime import datetime, date  # Import datetime để test

class CustomEncoder(json.JSONEncoder):
    """Custom JSONEncoder để handle các kiểu đặc biệt"""
    def default(self, obj):
        # Xử lý datetime → ISO format string
        if isinstance(obj, datetime):
            return obj.isoformat()  # "2024-01-15T10:30:00"
        # Xử lý date → ISO format string
        if isinstance(obj, date):
            return obj.isoformat()  # "2024-01-15"
        # Gọi default cho các kiểu không support
        return super().default(obj)

# Tạo data với datetime
data_with_date = {
    "event": "meeting",
    "timestamp": datetime(2024, 1, 15, 10, 30, 0),  # Python datetime object
    "created": date(2024, 1, 15)                      # Python date object
}

# Serialize với custom encoder
json_str = json.dumps(data_with_date, cls=CustomEncoder)
print(json_str)  # Output: {"event": "meeting", "timestamp": "2024-01-15T10:30:00", "created": "2024-01-15"}

# === Custom Decoder (JSON string → Python object) ===
def custom_decoder(dct):
    """Custom object_hook để convert ngược từ JSON"""
    # Parse ISO date string thành date object
    if "created" in dct and isinstance(dct["created"], str):
        dct["created"] = date.fromisoformat(dct["created"])
    return dct

data = json.loads(json_str, object_hook=custom_decoder)
print(type(data["created"]))  # Output: <class 'datetime.date'>

# === JSON với ensure_ascii ===
emoji_data = {"message": "Xin chào 👋", "emoji": "🎉"}
json_str = json.dumps(emoji_data)  # Mặc định escape Unicode
print(json_str)                     # Output: {"message": "Xin ch\u00e0o 👋", "emoji": "🎉"}

json_str = json.dumps(emoji_data, ensure_ascii=False)  # Giữ nguyên Unicode
print(json_str)  # Output: {"message": "Xin chào 👋", "emoji": "🎉"}

# === JSON với sort_keys ===
unsorted = {"z": 1, "a": 2, "m": 3}
json_str = json.dumps(unsorted)             # Không sort
print(json_str)                              # Output: {"z": 1, "a": 2, "m": 3}
json_str_sorted = json.dumps(unsorted, sort_keys=True)  # Sort theo key
print(json_str_sorted)                       # Output: {"a": 2, "m": 3, "z": 1}

# ⚠️ Edge case: JSON float precision
float_data = {"price": 123456789.123456789}
json_str = json.dumps(float_data)
print(json_str)  # Output: {"price": 123456789.12345679}
# ⚠️ Lưu ý: JavaScript JSON parse có thể mất precision với số > 2^53

# === Real-world: API Response Caching ===
import hashlib
from functools import lru_cache

def cache_json_response(func):
    """Decorator cache JSON response vào memory"""
    cache = {}
    def wrapper(*args, **kwargs):
        # Tạo cache key từ arguments
        cache_key = hashlib.md5(
            f"{args}{sorted(kwargs.items())}".encode()
        ).hexdigest()
        if cache_key not in cache:
            # Gọi API và serialize kết quả
            result = func(*args, **kwargs)
            cache[cache_key] = json.dumps(result)
        return json.loads(cache[cache_key])
    return wrapper

# @cache_json_response
# def fetch_user(user_id):
#     return {"id": user_id, "name": "John", "email": f"user{user_id}@example.com"}

# === Real-world: Configuration File ===
# JSON config file (nhưng thường dùng YAML/TOML sẽ tốt hơn cho config)
config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": True,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "features": ["auth", "api", "dashboard"]
}

# Lưu config
# with open("config.json", "w") as f:
#     json.dump(config, f, indent=2)

# Đọc config
# with open("config.json", "r") as f:
#     loaded_config = json.load(f)

# === Edge cases: JSON parsing errors ===
# Invalid JSON sẽ raise JSONDecodeError
try:
    json.loads('{"invalid": json}')
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")  # Output: Expecting property name enclosed in double quotes...

# === Real-world: Safe JSON parsing với fallback ===
def safe_json_loads(json_str, default=None):
    """Parse JSON với fallback value nếu lỗi"""
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError):
        return default if default is not None else {}

data = safe_json_loads('{"valid": true}', {"fallback": True})
print(data)  # Output: {'valid': True}

data = safe_json_loads('invalid json', {"fallback": True})
print(data)  # Output: {'fallback': True}

# === Real-world: Merge JSON configs ===
base_config = {"app": "web", "debug": False, "timeout": 30}
override_config = {"debug": True, "port": 8080}

# Merge: override ghi đè base
merged = {**base_config, **override_config}
print(merged)  # Output: {'app': 'web', 'debug': True, 'timeout': 30, 'port': 8080}
```

#### Pickle

```python
import pickle

# ⚠️ CẢNH BÁO BẢO MẬT: Không bao giờ unpickle dữ liệu từ nguồn không tin cậy!
# pickle có thể execute arbitrary code khi unpickling

# === Serialize Python object → bytes (Python only, không human-readable) ===
data = {"name": "John", "func": lambda x: x * 2}  # Bao gồm cả function/lambda!
pickled = pickle.dumps(data)                       # Serialize thành bytes
print(type(pickled))                                # Output: <class 'bytes'>
print(len(pickled))                                # Output: ~50 (tùy nội dung)

# === Deserialize: bytes → Python object ===
unpickled = pickle.loads(pickled)  # Deserialize ngược lại
print(unpickled["name"])           # Output: John

# === Serialize ra file (binary mode bắt buộc!) ===
with open("data.pkl", "wb") as f:  # "wb" = write binary
    pickle.dump(data, f)           # Ghi pickle vào file

# === Deserialize từ file (binary mode bắt buộc!) ===
with open("data.pkl", "rb") as f:  # "rb" = read binary
    data = pickle.load(f)          # Đọc pickle từ file
print(data["name"])               # Output: John

# ⚠️ Edge case: pickle protocol version
# pickle.HIGHEST_PROTOCOL = 5 (Python 3.8+), dùng cho performance tốt hơn
pickled_v5 = pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
print(f"Protocol: {pickle.HIGHEST_PROTOCOL}")  # Output: 5

# === Real-world: Cache Python objects ===
import pickle
import hashlib
from pathlib import Path

class ObjectCache:
    """Cache Python objects vào disk bằng pickle"""
    def __init__(self, cache_dir=".cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)

    def _get_cache_path(self, key):
        """Tạo cache file path từ key"""
        cache_key = hashlib.md5(key.encode()).hexdigest()
        return self.cache_dir / f"{cache_key}.pkl"

    def get(self, key):
        """Lấy object từ cache"""
        cache_path = self._get_cache_path(key)
        if cache_path.exists():
            with open(cache_path, "rb") as f:
                return pickle.load(f)
        return None

    def set(self, key, value):
        """Lưu object vào cache"""
        cache_path = self._get_cache_path(key)
        with open(cache_path, "wb") as f:
            pickle.dump(value, f)

# Sử dụng:
# cache = ObjectCache()
# cache.set("user_123", {"name": "John", "age": 30})
# user = cache.get("user_123")

# ⚠️ Edge case: Class định nghĩa sau khi unpickle
# Nếu class definition thay đổi giữa pickle và unpickle, có thể lỗi
# Giải pháp: Dùng __reduce__ hoặc __getstate__/__setstate__

# === Real-world: Deep copy với pickle ===
import copy

original = {"list": [1, 2, 3], "dict": {"nested": True}}
deep_copy = pickle.loads(pickle.dumps(original))  # Copy phức tạp hơn copy.deepcopy
shallow_copy = original.copy()                    # Chỉ copy 1 level

# Test sự khác biệt:
original["list"].append(4)
print(original["list"])      # Output: [1, 2, 3, 4]
print(deep_copy["list"])     # Output: [1, 2, 3] - không bị ảnh hưởng
print(shallow_copy["list"])  # Output: [1, 2, 3, 4] - bị ảnh hưởng (shallow)

# === Pickle vs JSON comparison ===
"""
| Feature          | JSON                    | Pickle                  |
|------------------|-------------------------|-------------------------|
| Human readable   | ✅ Yes                  | ❌ No (binary)          |
| Cross-language   | ✅ Yes (JS, Java...)   | ❌ Python only          |
| Security         | ✅ Safe                | ⚠️ Dangerous            |
| Speed            | ⚠️ Slower              | ✅ Faster               |
| All Python types | ❌ Limited             | ✅ Almost all           |
| Functions/classes| ❌ No                  | ✅ Yes (with limits)    |
"""
```

---

### 10.2. Date & Time

#### datetime

```python
from datetime import datetime, date, time, timedelta

# === Lấy thời gian hiện tại ===
now = datetime.now()    # Datetime hiện tại theo local timezone (naive - không có tz info)
today = date.today()    # Chỉ ngày hôm nay (không có giờ)
print(now)              # Output: 2024-01-15 10:30:00.123456 (tùy thời điểm chạy)
print(today)            # Output: 2024-01-15

# ⚠️ datetime.now() trả về naive datetime (không có timezone info)
# Dùng datetime.now(timezone.utc) để có timezone-aware datetime

# === Tạo datetime cụ thể ===
dt = datetime(2024, 1, 15, 10, 30, 0)  # year, month, day, hour, minute, second
d = date(2024, 1, 15)                   # Chỉ ngày
t = time(10, 30, 0)                     # Chỉ giờ
print(dt)  # Output: 2024-01-15 10:30:00
print(d)   # Output: 2024-01-15
print(t)   # Output: 10:30:00

# === Format datetime → string ===
formatted = dt.strftime("%Y-%m-%d %H:%M:%S")  # Format theo pattern
print(formatted)                               # Output: 2024-01-15 10:30:00

# Các format codes phổ biến:
# %Y = năm 4 chữ số (2024), %m = tháng (01-12), %d = ngày (01-31)
# %H = giờ 24h (00-23), %M = phút (00-59), %S = giây (00-59)
# %A = tên ngày (Monday), %B = tên tháng (January)
# %I = giờ 12h (01-12), %p = AM/PM

# === Parse string → datetime ===
parsed = datetime.strptime("2024-01-15", "%Y-%m-%d")  # Parse theo pattern
print(parsed)  # Output: 2024-01-15 00:00:00

# === ISO format (khuyến nghị cho API/JSON) ===
iso_str = dt.isoformat()                    # Serialize thành ISO 8601
print(iso_str)                              # Output: 2024-01-15T10:30:00
parsed_iso = datetime.fromisoformat(iso_str)  # Parse ISO 8601 (Python 3.7+)
print(parsed_iso)                           # Output: 2024-01-15 10:30:00

# === Arithmetic với timedelta ===
tomorrow = now + timedelta(days=1)          # Cộng 1 ngày
last_week = now - timedelta(weeks=1)        # Trừ 1 tuần
in_2_hours = now + timedelta(hours=2)       # Cộng 2 giờ
print(tomorrow.date())                      # Output: 2024-01-16 (ngày mai)

# timedelta components:
delta = timedelta(days=1, hours=2, minutes=30, seconds=15)
print(delta.total_seconds())  # Output: 95415.0 (tổng số giây)
print(delta.days)             # Output: 1 (chỉ phần ngày)

# === So sánh datetime ===
dt1 = datetime(2024, 1, 1)   # Ngày 1/1/2024
dt2 = datetime(2024, 1, 15)  # Ngày 15/1/2024
diff = dt2 - dt1              # Hiệu 2 datetime → timedelta
print(diff.days)              # Output: 14 (cách nhau 14 ngày)
print(dt1 < dt2)              # Output: True (dt1 trước dt2)
print(dt1 == dt2)             # Output: False

# ⚠️ Edge case: So sánh naive và aware datetime sẽ raise TypeError
# datetime.now() vs datetime.now(timezone.utc) → TypeError: can't compare offset-naive and offset-aware datetimes

# === Unix timestamp ===
timestamp = dt.timestamp()                  # datetime → Unix timestamp (float)
print(timestamp)                            # Output: 1705312200.0 (seconds since epoch)
dt_back = datetime.fromtimestamp(timestamp) # Unix timestamp → datetime (local tz)
print(dt_back)                              # Output: 2024-01-15 10:30:00

# ⚠️ Edge case: datetime.fromtimestamp() dùng local timezone
# Dùng datetime.utcfromtimestamp() để lấy UTC (nhưng vẫn naive!)
# Tốt nhất: datetime.fromtimestamp(ts, tz=timezone.utc) để có aware datetime

# === Real-world: Tính tuổi từ ngày sinh ===
def calculate_age(birth_date: date) -> int:
    """Tính tuổi chính xác từ ngày sinh"""
    today = date.today()
    # Kiểm tra xem đã qua sinh nhật năm nay chưa
    birthday_this_year = birth_date.replace(year=today.year)
    age = today.year - birth_date.year
    if today < birthday_this_year:
        age -= 1  # Chưa đến sinh nhật năm nay
    return age

birth = date(1990, 6, 15)
print(calculate_age(birth))  # Output: 33 hoặc 34 (tùy ngày chạy)

# === Real-world: Deadline checker ===
def is_overdue(deadline: datetime) -> bool:
    """Kiểm tra deadline đã qua chưa"""
    return datetime.now() > deadline

deadline = datetime(2024, 12, 31, 23, 59, 59)
print(is_overdue(deadline))  # Output: True/False tùy ngày chạy

# === Real-world: Format thân thiện ===
def time_ago(dt: datetime) -> str:
    """Hiển thị thời gian dạng '2 hours ago'"""
    diff = datetime.now() - dt
    seconds = diff.total_seconds()
    if seconds < 60:
        return f"{int(seconds)} seconds ago"
    elif seconds < 3600:
        return f"{int(seconds // 60)} minutes ago"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hours ago"
    else:
        return f"{int(seconds // 86400)} days ago"

past = datetime.now() - timedelta(hours=2, minutes=30)
print(time_ago(past))  # Output: 2 hours ago
```

#### timezone

```python
from datetime import datetime, timezone, timedelta
import zoneinfo  # Python 3.9+ (built-in, không cần pip)
# import pytz  # Cho Python < 3.9: pip install pytz

# === UTC timezone (built-in, không cần thư viện) ===
utc = timezone.utc                    # UTC timezone object
dt_utc = datetime.now(utc)           # Datetime hiện tại theo UTC (timezone-aware)
print(dt_utc)                         # Output: 2024-01-15 03:30:00+00:00

# === Tạo timezone với offset cố định ===
vn_tz = timezone(timedelta(hours=7))  # Vietnam UTC+7
dt_vn = datetime.now(vn_tz)          # Datetime hiện tại theo VN timezone
print(dt_vn)                          # Output: 2024-01-15 10:30:00+07:00

# === Dùng zoneinfo (Python 3.9+, khuyến nghị) ===
from zoneinfo import ZoneInfo
ny_tz = ZoneInfo("America/New_York")  # New York timezone (tự động DST)
dt_ny = datetime.now(ny_tz)          # Datetime hiện tại theo New York
print(dt_ny)                          # Output: 2024-01-14 22:30:00-05:00

# === Convert timezone ===
dt_utc = datetime.now(timezone.utc)          # Lấy UTC
dt_vn = dt_utc.astimezone(vn_tz)            # Convert sang VN
dt_ny = dt_utc.astimezone(ZoneInfo("America/New_York"))  # Convert sang NY
print(f"UTC: {dt_utc.strftime('%H:%M')}")   # Output: UTC: 03:30
print(f"VN:  {dt_vn.strftime('%H:%M')}")    # Output: VN:  10:30
print(f"NY:  {dt_ny.strftime('%H:%M')}")    # Output: NY:  22:30

# ⚠️ Edge case: Naive datetime không có timezone info
naive = datetime(2024, 1, 15, 10, 30)  # Không có timezone
aware = datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc)  # Có timezone

# Không thể so sánh naive và aware:
# naive < aware  # ❌ TypeError: can't compare offset-naive and offset-aware datetimes

# === Chuyển naive → aware (localize) ===
naive = datetime(2024, 1, 15, 10, 30)
aware = naive.replace(tzinfo=timezone.utc)  # Gán UTC timezone (không convert)
print(aware)  # Output: 2024-01-15 10:30:00+00:00

# ⚠️ replace(tzinfo=...) KHÔNG convert, chỉ gán timezone label
# Dùng astimezone() để convert sang timezone khác

# === Real-world: Lưu datetime vào database ===
# Best practice: Luôn lưu UTC, hiển thị theo local timezone
def save_event(event_time_local: datetime, user_tz: str) -> datetime:
    """Convert local time → UTC để lưu vào DB"""
    tz = ZoneInfo(user_tz)
    # Gán timezone cho local time
    local_aware = event_time_local.replace(tzinfo=tz)
    # Convert sang UTC để lưu
    utc_time = local_aware.astimezone(timezone.utc)
    return utc_time

# Người dùng ở VN nhập 10:30 AM
local_time = datetime(2024, 1, 15, 10, 30)
utc_time = save_event(local_time, "Asia/Ho_Chi_Minh")
print(utc_time)  # Output: 2024-01-15 03:30:00+00:00 (UTC)
```

#### Timestamp & Calendar

```python
import time
from datetime import datetime, timezone
import calendar

# === Unix timestamp (seconds since 1970-01-01 00:00:00 UTC) ===
timestamp = time.time()                    # Lấy Unix timestamp hiện tại (float)
print(f"{timestamp:.3f}")                  # Output: 1705312200.123 (tùy thời điểm)

dt = datetime.fromtimestamp(timestamp)     # Unix timestamp → local datetime (naive)
print(dt)                                  # Output: 2024-01-15 10:30:00.123000

# Tốt hơn: dùng timezone-aware
dt_utc = datetime.fromtimestamp(timestamp, tz=timezone.utc)  # → UTC aware datetime
print(dt_utc)  # Output: 2024-01-15 03:30:00.123000+00:00

# Ngược lại: datetime → Unix timestamp
ts = dt.timestamp()  # datetime → float timestamp
print(ts)            # Output: 1705312200.123

# === Performance timing với time.perf_counter() ===
start = time.perf_counter()  # High-resolution timer (không phải wall clock)
# ... code cần đo ...
end = time.perf_counter()
elapsed = end - start
print(f"Elapsed: {elapsed:.6f}s")  # Output: Elapsed: 0.000123s

# ⚠️ Dùng time.perf_counter() cho benchmarking, KHÔNG dùng time.time()
# time.time() có thể bị ảnh hưởng bởi NTP sync, DST changes

# === Calendar ===
cal = calendar.month(2024, 1)  # Tạo string lịch tháng 1/2024
print(cal)
# Output:
#     January 2024
# Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7
#  8  9 10 11 12 13 14
# ...

is_leap = calendar.isleap(2024)  # Kiểm tra năm nhuận
print(is_leap)                    # Output: True (2024 là năm nhuận)
print(calendar.isleap(2023))      # Output: False

# monthrange trả về (weekday của ngày 1, số ngày trong tháng)
first_weekday, num_days = calendar.monthrange(2024, 2)
print(first_weekday)  # Output: 3 (Thursday, 0=Monday)
print(num_days)       # Output: 29 (2024 là năm nhuận)

# === Real-world: Tính ngày làm việc ===
def count_business_days(start: datetime, end: datetime) -> int:
    """Đếm số ngày làm việc (không tính T7, CN) giữa 2 ngày"""
    count = 0
    current = start
    while current <= end:
        if current.weekday() < 5:  # 0-4 = Mon-Fri, 5=Sat, 6=Sun
            count += 1
        current += timedelta(days=1)
    return count

from datetime import timedelta
start = datetime(2024, 1, 1)   # Thứ 2
end = datetime(2024, 1, 14)    # Chủ nhật
print(count_business_days(start, end))  # Output: 10 (2 tuần = 10 ngày làm việc)
```

---

### 10.3. Regular Expression

```python
import re

# === Tìm kiếm pattern đầu tiên ===
text = "My email is john@example.com and jane@domain.org"
match = re.search(r'[\w.-]+@[\w.-]+', text)  # Tìm pattern đầu tiên khớp
if match:
    print(match.group())  # Output: john@example.com (toàn bộ match)
    print(match.span())   # Output: (12, 29) (vị trí bắt đầu, kết thúc)
    print(match.start())  # Output: 12 (vị trí bắt đầu)
    print(match.end())    # Output: 29 (vị trí kết thúc)

# ⚠️ Lưu ý: re.search() chỉ tìm match đầu tiên, dùng re.findall() để tìm tất cả

# === Tìm tất cả các match ===
emails = re.findall(r'[\w.-]+@[\w.-]+', text)  # Trả về list các match
print(emails)  # Output: ['john@example.com', 'jane@domain.org']

# ⚠️ Khi dùng capture groups với findall(), trả về list of tuples
text_with_groups = "john@example.com, jane@domain.org"
# Pattern có 2 groups: ([\w.-]+) và ([\w.-]+)
matches = re.findall(r'([\w.-]+)@([\w.-]+)', text_with_groups)
print(matches)  # Output: [('john', 'example.com'), ('jane', 'domain.org')]

# === Named groups ===
pattern = r'(?P<user>[\w.-]+)@(?P<domain>[\w.-]+)'  # (?P<name>pattern) đặt tên group
match = re.search(pattern, text)
if match:
    print(match.group('user'))     # Output: john (lấy theo tên group)
    print(match.group('domain'))   # Output: example.com
    print(match.group(1))          # Output: john (lấy theo index)
    print(match.group(2))          # Output: example.com
    print(match.groups())          # Output: ('john', 'example.com')

# === Thay thế (replace/substitute) ===
result = re.sub(r'\d+', '#', "test 123 and 456")  # Thay thế tất cả số bằng #
print(result)  # Output: test # and #

# Thay thế với callback function
def replace_number(match):
    num = int(match.group())
    return "odd" if num % 2 else "even"

result = re.sub(r'\d+', replace_number, "1 2 3 4 5")
print(result)  # Output: odd even odd even odd

# === Tách (split) ===
parts = re.split(r'\s+', "hello   world  test")  # Tách theo 1+ whitespace
print(parts)  # Output: ['hello', 'world', 'test']

# Split với capture group - giữ lại delimiter
parts_with_sep = re.split(r'(\s+)', "hello world")
print(parts_with_sep)  # Output: ['hello', ' ', 'world']

# === Compile pattern để tái sử dụng (tốt cho performance) ===
email_pattern = re.compile(r'[\w.-]+@[\w.-]+')  # Compile 1 lần, dùng nhiều lần
result = email_pattern.findall(text)  # Dùng pattern đã compile
print(result)  # Output: ['john@example.com', 'jane@domain.org']

# === Flags điều chỉnh behavior ===
text_multi = "Hello\nWorld"
match = re.search(r'hello', text_multi, re.IGNORECASE)  # Không phân biệt hoa thường
print(match.group() if match else None)  # Output: Hello

match = re.search(r'.+', text_multi)  # Mặc định . không khớp \n
print(match.group() if match else None)  # Output: Hello (chỉ 1 line)

match = re.search(r'.+', text_multi, re.DOTALL)  # . khớp cả \n
print(match.group() if match else None)  # Output: Hello\nWorld

# === Real-world: Validation patterns ===
def validate_email(email: str) -> bool:
    """Kiểm tra email hợp lệ"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(validate_email("user@example.com"))     # Output: True
print(validate_email("invalid@email"))        # Output: False
print(validate_email("@example.com"))         # Output: False
print(validate_email("user@.com"))            # Output: False

def validate_phone(phone: str) -> bool:
    """Kiểm tra số điện thoại VN (10 số, bắt đầu bằng 0)"""
    pattern = r'^0\d{9}$'  # 0 + 9 chữ số
    return bool(re.match(pattern, phone))

print(validate_phone("0912345678"))  # Output: True
print(validate_phone("9123456789"))  # Output: False
print(validate_phone("091234567"))   # Output: False

def validate_password(password: str) -> tuple[bool, str]:
    """Kiểm tra password: 8+ ký tự, có chữ hoa, thường, số"""
    if len(password) < 8:
        return False, "Ít nhất 8 ký tự"
    if not re.search(r'[A-Z]', password):
        return False, "Cần ít nhất 1 chữ hoa"
    if not re.search(r'[a-z]', password):
        return False, "Cần ít nhất 1 chữ thường"
    if not re.search(r'\d', password):
        return False, "Cần ít nhất 1 số"
    return True, "Hợp lệ"

print(validate_password("Pass1234"))  # Output: (True, 'Hợp lệ')
print(validate_password("password"))   # Output: (False, 'Cần ít nhất 1 chữ hoa')

# === Real-world: Data extraction ===
log = "2024-01-15 10:30:45 ERROR [Auth] Login failed for user john"
pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) \[(\w+)\] (.+)'
match = re.match(pattern, log)
if match:
    date, time, level, module, message = match.groups()
    print(f"Date: {date}, Time: {time}, Level: {level}, Module: {module}")  # Output: Date: 2024-01-15, Time: 10:30:45, Level: ERROR, Module: Auth
    print(f"Message: {message}")  # Output: Message: Login failed for user john

# === Real-world: HTML/Sanitization ===
import html

def sanitize_input(user_input: str) -> str:
    """Loại bỏ HTML tags từ user input"""
    # Cách 1: Strip tags
    clean = re.sub(r'<[^>]+>', '', user_input)
    # Cách 2: Escape HTML entities
    escaped = html.escape(user_input)
    return clean

dirty = "<script>alert('xss')</script>Hello"
print(sanitize_input(dirty))  # Output: Hello

# === Real-world: Text formatting ===
def format_phone_numbers(text: str) -> str:
    """Định dạng lại số điện thoại: 0912345678 → (091) 234-5678"""
    def format_number(match):
        num = match.group()
        return f"({num[:3]}) {num[3:6]}-{num[6:]}"
    return re.sub(r'\d{10}', format_number, text)

text = "Gọi cho tôi: 0912345678 hoặc 0987654321"
print(format_phone_numbers(text))  # Output: Gọi cho tôi: (091) 234-5678 hoặc (098) 765-4321

# === Edge cases: Greedy vs Non-greedy ===
text_html = "<div>content</div>"

# Greedy: .* khớp nhiều nhất có thể
greedy = re.search(r'<div>.*</div>', text_html)
print(greedy.group() if greedy else None)  # Output: <div>content</div>

# Non-greedy: .*? khớp ít nhất có thể
non_greedy = re.search(r'<div>.*?</div>', text_html)
print(non_greedy.group() if non_greedy else None)  # Output: <div>content</div>

# ⚠️ Với input phức tạp, dùng BeautifulSoup thay vì regex để parse HTML

# === Edge cases: Lookahead/Lookbehind ===
text_prices = "$100 USD, $50 EUR, £80 GBP"

# Positive lookahead: khớp $ + số nhưng không include "USD"
prices_usd = re.findall(r'\$\d+(?= USD)', text_prices)
print(prices_usd)  # Output: ['$100']

# Negative lookahead: khớp $ + số KHÔNG theo sau bởi USD
prices_other = re.findall(r'\$\d+(?! USD)', text_prices)
print(prices_other)  # Output: ['$50']

# Positive lookbehind: khớp số theo sau bởi $ (không include $)
amounts = re.findall(r'(?<=\$)\d+', text_prices)
print(amounts)  # Output: ['100', '50']

# === Edge cases: Backreference ===
# Khớp từ có chữ cái lặp lại: "hello", "book" (không khớp "test")
words_double = re.findall(r'\b(\w)\1\w*\b', "hello book test apple")
print(words_double)  # Output: ['l', 'o', 'p'] - chữ cái lặp

# Khớp HTML tags đóng mở khớp nhau
html_content = "<div><span>text</span></div>"
# ⚠️ Regex không thể handle nested HTML properly - dùng parser

# === Common regex patterns ===
"""
| Pattern      | Meaning                           | Example              |
|--------------|-----------------------------------|----------------------|
| \d           | Digit (0-9)                      | \d{3} = 3 digits    |
| \D           | Non-digit                        | \D+ = non-digits     |
| \w           | Word char (a-z, A-Z, 0-9, _)     | \w+ = word           |
| \W           | Non-word char                    | \W+ = symbols        |
| \s           | Whitespace                       | \s+ = whitespace     |
| \S           | Non-whitespace                   | \S+ = non-space      |
| .            | Any char (except newline)         | a.c = abc, aXc       |
| ^            | Start of string/line              | ^Hello               |
| $            | End of string/line               | world$               |
| *            | 0 or more (greedy)               | a* = '', 'a', 'aaa'  |
| +            | 1 or more (greedy)               | a+ = 'a', 'aaa'      |
| ?            | 0 or 1, or non-greedy            | colou?r = color/r    |
| {n}          | Exactly n times                  | \d{4} = 4 digits     |
| {n,}         | n or more times                  | \w{3,} = 3+ chars    |
| {n,m}        | Between n and m times             | \d{2,4} = 2-4 digits |
| []           | Character class                  | [aeiou] = vowel      |
| [^...]       | Negated class                    | [^0-9] = non-digit   |
| \|           | Alternation (or)                  | cat\|dog = cat/dog   |
| ()           | Group (capture)                  | (\d+) groups digits  |
| (?:...)      | Non-capturing group              | (?:ab)+ = abab       |
| (?P<name>...)| Named group                      | (?P<year>\d{4})      |
"""
```

### 10.4. XML & CSV Parsing

```python
# === XML Parsing với ElementTree (built-in) ===
import xml.etree.ElementTree as ET

xml_str = '''<users>
    <user id="1"><name>John</name><email>john@example.com</email></user>
    <user id="2"><name>Jane</name><email>jane@example.com</email></user>
</users>'''

root = ET.fromstring(xml_str)  # Parse XML string → Element object
print(root.tag)                 # Output: users (tên tag gốc)

# Duyệt qua các phần tử con
for user in root.findall('user'):  # Tìm tất cả <user> trực tiếp trong root
    uid = user.get('id')           # Lấy attribute 'id'
    name = user.find('name').text  # Tìm <name> và lấy text content
    email = user.find('email').text
    print(f"{uid}: {name} ({email})")
# Output:
# 1: John (john@example.com)
# 2: Jane (jane@example.com)

# === Tạo XML ===
root = ET.Element('users')                    # Tạo root element
user1 = ET.SubElement(root, 'user')           # Thêm child element
user1.set('id', '1')                          # Set attribute
name_elem = ET.SubElement(user1, 'name')      # Thêm nested element
name_elem.text = 'John'                       # Set text content

tree = ET.ElementTree(root)                   # Tạo tree từ root
ET.indent(tree, space="  ")                   # Thêm indentation (Python 3.9+)
# tree.write('output.xml', encoding='utf-8', xml_declaration=True)

# In ra string
import io
output = io.StringIO()
tree.write(output, encoding='unicode')
print(output.getvalue())
# Output: <users><user id="1"><name>John</name></user></users>

# ⚠️ Lưu ý: ElementTree không hỗ trợ XPath đầy đủ
# Dùng lxml (pip install lxml) cho XPath phức tạp và namespace

# === CSV Parsing ===
import csv
import io

# === Đọc CSV từ string (demo không cần file) ===
csv_content = """name,age,city
John,30,Hanoi
Jane,25,HCMC
Bob,35,Danang"""

reader = csv.DictReader(io.StringIO(csv_content))  # DictReader: mỗi row là dict
for row in reader:
    print(f"{row['name']}: {row['age']} tuổi, {row['city']}")
# Output:
# John: 30 tuổi, Hanoi
# Jane: 25 tuổi, HCMC
# Bob: 35 tuổi, Danang

# === Đọc CSV từ file ===
# with open('data.csv', 'r', encoding='utf-8', newline='') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)  # Đọc tất cả vào list

# ⚠️ Luôn dùng newline='' khi mở file CSV để tránh lỗi trên Windows

# === Ghi CSV ===
data = [
    {'name': 'John', 'age': 30, 'city': 'Hanoi'},
    {'name': 'Jane', 'age': 25, 'city': 'HCMC'},
]

output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=['name', 'age', 'city'])
writer.writeheader()          # Ghi header row
writer.writerows(data)        # Ghi tất cả rows
print(output.getvalue())
# Output:
# name,age,city
# John,30,Hanoi
# Jane,25,HCMC

# === CSV với delimiter khác ===
tsv_content = "name\tage\tcity\nJohn\t30\tHanoi"
reader = csv.DictReader(io.StringIO(tsv_content), delimiter='\t')  # Tab-separated
for row in reader:
    print(row)  # Output: {'name': 'John', 'age': '30', 'city': 'Hanoi'}

# ⚠️ Edge case: CSV với dấu phẩy trong giá trị
csv_with_comma = 'name,address\nJohn,"123 Main St, Apt 4"'
reader = csv.DictReader(io.StringIO(csv_with_comma))
for row in reader:
    print(row['address'])  # Output: 123 Main St, Apt 4 (csv tự handle quotes)

# === Real-world: Đọc CSV lớn theo batch ===
def read_csv_in_batches(filepath, batch_size=1000):
    """Đọc CSV lớn theo từng batch để tiết kiệm memory"""
    with open(filepath, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        batch = []
        for row in reader:
            batch.append(row)
            if len(batch) >= batch_size:
                yield batch  # Yield batch, không load toàn bộ vào memory
                batch = []
        if batch:
            yield batch  # Yield batch cuối

# for batch in read_csv_in_batches('large_file.csv'):
#     process_batch(batch)

# === Real-world: CSV → JSON conversion ===
def csv_to_json(csv_string: str) -> list[dict]:
    """Convert CSV string thành list of dicts"""
    reader = csv.DictReader(io.StringIO(csv_string))
    return [dict(row) for row in reader]

csv_data = "id,name,score\n1,Alice,95\n2,Bob,87"
json_data = csv_to_json(csv_data)
print(json_data)  # Output: [{'id': '1', 'name': 'Alice', 'score': '95'}, ...]
# ⚠️ Lưu ý: CSV không có type info, tất cả đều là string
# Cần convert thủ công: int(row['id']), float(row['score'])
```

### 10.5. YAML/TOML

```python
# === YAML - pip install pyyaml ===
import yaml

# === Parse YAML string ===
yaml_str = """
name: John
age: 30
active: true
skills:
  - Python
  - Django
  - PostgreSQL
database:
  host: localhost
  port: 5432
  name: mydb
"""

data = yaml.safe_load(yaml_str)  # safe_load: an toàn, không execute Python code
print(data['name'])              # Output: John
print(data['age'])               # Output: 30 (int, không phải string!)
print(data['active'])            # Output: True (bool)
print(data['skills'])            # Output: ['Python', 'Django', 'PostgreSQL']
print(data['database']['host'])  # Output: localhost

# ⚠️ CẢNH BÁO: Không dùng yaml.load() (không có Loader) - có thể execute code!
# ❌ yaml.load(yaml_str)  # Nguy hiểm!
# ✅ yaml.safe_load(yaml_str)  # An toàn

# === Serialize Python → YAML string ===
config = {
    "app": "MyApp",
    "version": "1.0.0",
    "debug": False,
    "features": ["auth", "api"],
    "database": {"host": "localhost", "port": 5432}
}

yaml_output = yaml.dump(config, default_flow_style=False, allow_unicode=True)
print(yaml_output)
# Output:
# app: MyApp
# database:
#   host: localhost
#   port: 5432
# debug: false
# features:
# - auth
# - api
# version: 1.0.0

# ⚠️ Lưu ý: yaml.dump() sort keys theo alphabet mặc định
yaml_output_unsorted = yaml.dump(config, default_flow_style=False, sort_keys=False)

# === Đọc/Ghi YAML file ===
# with open('config.yaml', 'r', encoding='utf-8') as f:
#     config = yaml.safe_load(f)

# with open('output.yaml', 'w', encoding='utf-8') as f:
#     yaml.dump(config, f, default_flow_style=False, allow_unicode=True)

# === YAML multi-document ===
multi_yaml = """
---
name: John
---
name: Jane
"""
docs = list(yaml.safe_load_all(multi_yaml))  # Load nhiều documents
print(len(docs))       # Output: 2
print(docs[0]['name']) # Output: John
print(docs[1]['name']) # Output: Jane

# === TOML (Python 3.11+ built-in) ===
import tomllib  # Python 3.11+ built-in (read-only)

toml_str = b"""
[app]
name = "MyApp"
version = "1.0.0"
debug = false

[database]
host = "localhost"
port = 5432

[features]
enabled = ["auth", "api"]
"""

# ⚠️ tomllib.loads() nhận bytes, không phải str
config = tomllib.loads(toml_str.decode())  # Decode bytes → str trước
print(config['app']['name'])               # Output: MyApp
print(config['database']['port'])          # Output: 5432 (int)
print(config['features']['enabled'])       # Output: ['auth', 'api']

# Đọc từ file (phải mở binary mode!)
# with open('config.toml', 'rb') as f:  # 'rb' bắt buộc!
#     config = tomllib.load(f)

# === Ghi TOML: pip install tomli-w ===
# import tomli_w
# with open('output.toml', 'wb') as f:
#     tomli_w.dump(config, f)

# === So sánh YAML vs TOML vs JSON ===
"""
| Feature          | JSON              | YAML              | TOML              |
|------------------|-------------------|-------------------|-------------------|
| Human readable   | ✅ OK             | ✅ Best           | ✅ Good           |
| Comments         | ❌ No             | ✅ Yes (#)        | ✅ Yes (#)        |
| Data types       | ✅ Basic          | ✅ Rich           | ✅ Rich           |
| Multiline string | ❌ Awkward        | ✅ Easy           | ✅ Easy           |
| Config files     | ⚠️ OK             | ✅ Popular        | ✅ Growing        |
| Security         | ✅ Safe           | ⚠️ safe_load!     | ✅ Safe           |
| Python built-in  | ✅ json           | ❌ pip pyyaml     | ✅ tomllib 3.11+  |
| Use case         | API, data         | Config, k8s       | pyproject.toml    |
"""

# === Real-world: Config loader với fallback ===
def load_config(config_path: str) -> dict:
    """Load config từ YAML/TOML/JSON tùy extension"""
    from pathlib import Path
    path = Path(config_path)

    if not path.exists():
        return {}

    with open(path, 'r', encoding='utf-8') as f:
        if path.suffix in ('.yaml', '.yml'):
            return yaml.safe_load(f) or {}
        elif path.suffix == '.json':
            import json
            return json.load(f)
        else:
            raise ValueError(f"Unsupported config format: {path.suffix}")

# config = load_config("config.yaml")
```

### 10.6. Binary Serialization (struct)

```python
import struct

# === Pack: Python values → bytes (binary format) ===
# Format string: 'i' = signed int (4 bytes), 'f' = float (4 bytes)
packed = struct.pack('iif', 1, 2, 3.14)  # Pack 2 ints + 1 float
print(type(packed))   # Output: <class 'bytes'>
print(len(packed))    # Output: 12 (4 + 4 + 4 bytes)

# === Unpack: bytes → Python values ===
a, b, c = struct.unpack('iif', packed)  # Unpack theo cùng format
print(a, b, c)  # Output: 1 2 3.140000104904175 (float precision loss!)

# ⚠️ Edge case: float precision loss khi pack/unpack
# 3.14 → float32 → 3.140000104904175 (không chính xác)
# Dùng 'd' (double, 8 bytes) thay vì 'f' (float, 4 bytes) cho precision tốt hơn
packed_d = struct.pack('iid', 1, 2, 3.14)  # 'd' = double (8 bytes)
a, b, c = struct.unpack('iid', packed_d)
print(c)  # Output: 3.14 (chính xác hơn)

# === Byte order (endianness) ===
# '>' = big-endian (network byte order), '<' = little-endian, '=' = native
packed_be = struct.pack('>i', 256)  # Big-endian
packed_le = struct.pack('<i', 256)  # Little-endian
print(packed_be.hex())  # Output: 00000100 (big-endian)
print(packed_le.hex())  # Output: 00010000 (little-endian)

# ⚠️ Quan trọng khi giao tiếp với network protocols hoặc binary file formats

# === calcsize: tính kích thước format ===
size = struct.calcsize('iif')  # Tính số bytes cần thiết
print(size)  # Output: 12

# === struct.Struct: compile format để tái sử dụng ===
fmt = struct.Struct('!HHI')  # '!' = network byte order, H = unsigned short, I = unsigned int
print(fmt.size)  # Output: 8 (2 + 2 + 4 bytes)

# Pack/unpack với Struct object
packed = fmt.pack(80, 443, 1234567890)  # port_http, port_https, timestamp
http_port, https_port, ts = fmt.unpack(packed)
print(http_port, https_port, ts)  # Output: 80 443 1234567890

# === Real-world: Đọc binary file header ===
# Ví dụ: BMP file header (14 bytes)
# struct BitmapFileHeader {
#     uint16_t bfType;      // 'BM' = 0x4D42
#     uint32_t bfSize;      // File size
#     uint16_t bfReserved1; // 0
#     uint16_t bfReserved2; // 0
#     uint32_t bfOffBits;   // Offset to pixel data
# }
BMP_HEADER_FORMAT = '<HIHHI'  # little-endian: H=uint16, I=uint32
BMP_HEADER_SIZE = struct.calcsize(BMP_HEADER_FORMAT)
print(BMP_HEADER_SIZE)  # Output: 14

# def read_bmp_header(filepath):
#     with open(filepath, 'rb') as f:
#         header_bytes = f.read(BMP_HEADER_SIZE)
#         bfType, bfSize, _, _, bfOffBits = struct.unpack(BMP_HEADER_FORMAT, header_bytes)
#         if bfType != 0x4D42:
#             raise ValueError("Not a BMP file")
#         return {"size": bfSize, "data_offset": bfOffBits}

# === MessagePack - pip install msgpack ===
# MessagePack: binary JSON, nhanh hơn và nhỏ hơn JSON
# import msgpack
# data = {"name": "John", "age": 30, "scores": [95, 87, 92]}
# packed = msgpack.packb(data, use_bin_type=True)  # Serialize
# print(len(packed))  # Nhỏ hơn JSON
# unpacked = msgpack.unpackb(packed, raw=False)  # Deserialize
# print(unpacked)  # Output: {'name': 'John', 'age': 30, 'scores': [95, 87, 92]}

# === Format codes reference ===
"""
| Code | Type              | Size  |
|------|-------------------|-------|
| b    | signed char       | 1     |
| B    | unsigned char     | 1     |
| h    | signed short      | 2     |
| H    | unsigned short    | 2     |
| i    | signed int        | 4     |
| I    | unsigned int      | 4     |
| l    | signed long       | 4     |
| L    | unsigned long     | 4     |
| q    | signed long long  | 8     |
| Q    | unsigned long long| 8     |
| f    | float             | 4     |
| d    | double            | 8     |
| s    | char[]            | n     |
| x    | pad byte          | 1     |
"""
```

---

## 11. Tầng 11: Development Practices

### 11.1. Testing

#### unittest

```python
import unittest

# === Hàm cần test ===
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# === Test class kế thừa unittest.TestCase ===
class TestMath(unittest.TestCase):
    # setUp chạy TRƯỚC mỗi test method
    def setUp(self):
        self.data = {"key": "value"}  # Khởi tạo test data
        self.numbers = [1, 2, 3, 4, 5]

    # tearDown chạy SAU mỗi test method (dù pass hay fail)
    def tearDown(self):
        pass  # Cleanup resources (close DB, delete temp files...)

    # Test method phải bắt đầu bằng 'test_'
    def test_add_positive(self):
        result = add(1, 1)
        self.assertEqual(result, 2)  # Kiểm tra bằng nhau

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)  # Số âm

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)  # Cộng với 0

    def test_divide_normal(self):
        self.assertAlmostEqual(divide(10, 3), 3.333, places=3)  # Float comparison

    def test_divide_by_zero(self):
        # Kiểm tra exception được raise
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_divide_by_zero_message(self):
        # Kiểm tra cả message của exception
        with self.assertRaises(ZeroDivisionError) as ctx:
            divide(1, 0)
        self.assertIn("Cannot divide by zero", str(ctx.exception))

    # === Các assertion methods phổ biến ===
    def test_assertions(self):
        self.assertEqual(1, 1)          # a == b
        self.assertNotEqual(1, 2)       # a != b
        self.assertTrue(True)           # bool(x) is True
        self.assertFalse(False)         # bool(x) is False
        self.assertIsNone(None)         # x is None
        self.assertIsNotNone(1)         # x is not None
        self.assertIn(1, [1, 2, 3])     # a in b
        self.assertNotIn(4, [1, 2, 3])  # a not in b
        self.assertIsInstance(1, int)   # isinstance(a, b)
        self.assertGreater(2, 1)        # a > b
        self.assertLess(1, 2)           # a < b

    # === setUpClass/tearDownClass: chạy 1 lần cho cả class ===
    @classmethod
    def setUpClass(cls):
        # Khởi tạo expensive resources (DB connection, server...)
        cls.db_connection = None  # Ví dụ: cls.db = create_test_db()

    @classmethod
    def tearDownClass(cls):
        # Cleanup expensive resources
        pass  # Ví dụ: cls.db.close()

# Chạy tests
if __name__ == '__main__':
    unittest.main(verbosity=2)  # verbosity=2 hiển thị tên từng test
```

#### pytest

```python
# test_math.py - pytest không cần class, chỉ cần function bắt đầu bằng test_
import pytest

# === Hàm cần test ===
def add(a, b):
    return a + b

def get_user(user_id):
    users = {1: {"name": "John", "age": 30}, 2: {"name": "Jane", "age": 25}}
    if user_id not in users:
        raise KeyError(f"User {user_id} not found")
    return users[user_id]

# === Test functions đơn giản ===
def test_add():
    assert add(1, 1) == 2  # pytest dùng assert thông thường

def test_add_negative():
    assert add(-1, -1) == -2

def test_list():
    numbers = [1, 2, 3]
    assert len(numbers) == 3  # Kiểm tra độ dài
    assert numbers[0] == 1    # Kiểm tra phần tử đầu

def test_exception():
    with pytest.raises(ZeroDivisionError):  # Kiểm tra exception
        1 / 0

def test_exception_message():
    with pytest.raises(KeyError, match="User 99 not found"):  # Kiểm tra message
        get_user(99)

# === Fixtures: cung cấp test data/resources ===
@pytest.fixture
def user():
    """Fixture trả về user data"""
    return {"name": "John", "age": 30, "email": "john@example.com"}

@pytest.fixture
def admin_user():
    """Fixture trả về admin user"""
    return {"name": "Admin", "age": 35, "role": "admin"}

def test_user_name(user):  # pytest tự inject fixture theo tên parameter
    assert user["name"] == "John"

def test_user_age(user):
    assert user["age"] == 30

def test_admin_role(admin_user):
    assert admin_user["role"] == "admin"

# === Fixture với scope ===
@pytest.fixture(scope="module")  # Chạy 1 lần cho cả module (tiết kiệm hơn)
def db_connection():
    """Tạo DB connection 1 lần cho cả module"""
    # conn = create_connection()
    conn = {"connected": True}  # Mock
    yield conn  # yield thay vì return để có teardown
    # Teardown: chạy sau khi tất cả tests trong module xong
    # conn.close()

# scope options: "function" (default), "class", "module", "session"

# === Parametrize: chạy test với nhiều input ===
@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),    # Test case 1
    (2, 3, 5),    # Test case 2
    (-1, 1, 0),   # Test case 3: số âm
    (0, 0, 0),    # Test case 4: zero
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected  # Chạy 4 lần với 4 bộ input

# === Marks: đánh dấu tests ===
@pytest.mark.slow  # Custom mark
def test_slow_operation():
    pass  # Chạy với: pytest -m slow

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass  # Bỏ qua test này

@pytest.mark.skipif(True, reason="Skip on CI")
def test_local_only():
    pass

# === conftest.py: shared fixtures ===
# Tạo file conftest.py trong thư mục test để share fixtures giữa các files
# conftest.py:
# @pytest.fixture(scope="session")
# def app():
#     return create_app(testing=True)
```

#### Mocking

```python
from unittest.mock import Mock, patch, MagicMock, call

# === Mock cơ bản ===
mock = Mock(return_value=42)  # Tạo mock object trả về 42
result = mock()               # Gọi mock như function
print(result)                 # Output: 42
print(mock.called)            # Output: True (đã được gọi)
print(mock.call_count)        # Output: 1 (gọi 1 lần)

# === Mock với side_effect ===
mock_error = Mock(side_effect=ValueError("Invalid input"))
try:
    mock_error()
except ValueError as e:
    print(e)  # Output: Invalid input

# side_effect với list: trả về lần lượt
mock_sequence = Mock(side_effect=[1, 2, 3])
print(mock_sequence())  # Output: 1
print(mock_sequence())  # Output: 2
print(mock_sequence())  # Output: 3

# === Mock object với spec ===
class UserService:
    def get_user(self, user_id: int) -> dict:
        return {"id": user_id, "name": "John"}

    def create_user(self, name: str) -> dict:
        return {"id": 1, "name": name}

# spec=UserService: mock chỉ có các methods của UserService
mock_service = Mock(spec=UserService)
mock_service.get_user.return_value = {"id": 1, "name": "Mocked John"}

result = mock_service.get_user(1)
print(result)  # Output: {'id': 1, 'name': 'Mocked John'}

# ⚠️ Với spec, gọi method không tồn tại sẽ raise AttributeError
# mock_service.nonexistent()  # ❌ AttributeError

# === patch: thay thế object trong module ===
# Giả sử có module: myapp.services.user_service
# Trong test, ta muốn mock requests.get

import requests  # Thư viện thực

def fetch_user_from_api(user_id: int) -> dict:
    """Hàm gọi API thực"""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

# Test với patch decorator
@patch('requests.get')  # Patch requests.get trong scope của test
def test_fetch_user(mock_get):
    # Cấu hình mock response
    mock_response = Mock()
    mock_response.json.return_value = {"id": 1, "name": "John"}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    # Gọi hàm cần test
    result = fetch_user_from_api(1)

    # Kiểm tra kết quả
    assert result == {"id": 1, "name": "John"}

    # Kiểm tra mock được gọi đúng cách
    mock_get.assert_called_once_with("https://api.example.com/users/1")

# === patch như context manager ===
def test_fetch_user_context():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"id": 1, "name": "Jane"}
        result = fetch_user_from_api(1)
        assert result["name"] == "Jane"

# === MagicMock: Mock với magic methods ===
magic = MagicMock()
magic.__len__.return_value = 5  # Mock __len__
print(len(magic))               # Output: 5

magic.__str__.return_value = "mocked string"
print(str(magic))               # Output: mocked string

# === assert_called methods ===
mock = Mock()
mock(1, 2, key="value")

mock.assert_called()                          # Đã được gọi ít nhất 1 lần
mock.assert_called_once()                     # Đã được gọi đúng 1 lần
mock.assert_called_with(1, 2, key="value")    # Gọi với args này
mock.assert_called_once_with(1, 2, key="value")  # Gọi đúng 1 lần với args này

# === Real-world: Test với database mock ===
class UserRepository:
    def __init__(self, db):
        self.db = db

    def find_by_id(self, user_id: int) -> dict | None:
        return self.db.query(f"SELECT * FROM users WHERE id = {user_id}")

def test_user_repository():
    # Mock database
    mock_db = Mock()
    mock_db.query.return_value = {"id": 1, "name": "John"}

    # Test
    repo = UserRepository(mock_db)
    user = repo.find_by_id(1)

    assert user["name"] == "John"
    mock_db.query.assert_called_once_with("SELECT * FROM users WHERE id = 1")
```

---

### 11.2. Logging

```python
import logging

# === Cấu hình cơ bản ===
logging.basicConfig(
    level=logging.DEBUG,                          # Level thấp nhất: DEBUG < INFO < WARNING < ERROR < CRITICAL
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)  # __name__ = module path, ví dụ: "myapp.views"

# Các level log:
logger.debug("Debug message")     # Output: DEBUG - Chi tiết cho debugging
logger.info("Info message")       # Output: INFO  - Xác nhận mọi thứ hoạt động tốt
logger.warning("Warning message") # Output: WARNING - Cảnh báo, có vấn đề nhưng không nghiêm trọng
logger.error("Error message")     # Output: ERROR - Lỗi nghiêm trọng, chức năng không hoạt động
logger.critical("Critical")       # Output: CRITICAL - Lỗi rất nghiêm trọng, chương trình có thể dừng

# === Format placeholders ===
# %(name)s         - Tên logger (module name)
# %(levelname)s    - DEBUG, INFO, WARNING, ERROR, CRITICAL
# %(asctime)s      - Thời gian
# %(filename)s     - Tên file
# %(lineno)d       - Số dòng
# %(funcName)s     - Tên function
# %(message)s      - Nội dung log

# === Logger với FileHandler ===
logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)  # Set level cho logger (độc lập với handlers)

# Console handler
console_handler = logging.StreamHandler()  # Log ra console
console_handler.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler('app.log', encoding='utf-8')  # Log ra file
file_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter(
    '%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("Application started")  # Log ra cả console và file

# ⚠️ Lưu ý: Set level cho cả logger VÀ handler
# Handler level quyết định messages nào được ghi
# Logger level quyết định messages nào được truyền đến handlers

# === Real-world: Logger config với dict ===
logging_config = {
    'version': 1,                    # Config version (luôn là 1)
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(funcName)s() - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': 'app.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5       # Giữ 5 file backup
        }
    },
    'loggers': {
        'myapp': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False    # Không propagate lên parent logger
        }
    },
    'root': {
        'level': 'WARNING',
        'handlers': ['console']
    }
}

# logging.config.dictConfig(logging_config)  # Apply config
# logger = logging.getLogger("myapp")

# === Real-world: Logger per module ===
# myapp/__init__.py
# logger = logging.getLogger("myapp")  # Parent logger

# myapp/database.py
# db_logger = logging.getLogger("myapp.database")  # Con của myapp
# db_logger.info("Database query executed")

# myapp/api.py
# api_logger = logging.getLogger("myapp.api")

# === Structured logging (JSON) ===
import json
import logging

class JSONFormatter(logging.Formatter):
    """Format log thành JSON cho logging system dễ parse"""
    def format(self, record):
        log_data = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_data)

# json_handler = logging.StreamHandler()
# json_handler.setFormatter(JSONFormatter())
# logger.addHandler(json_handler)

# === Best practices ===
# 1. Dùng __name__ để logger có tên module rõ ràng
# 2. Set level phù hợp: DEBUG cho dev, INFO cho production
# 3. KHÔNG log sensitive data (passwords, tokens)
# 4. Dùng structured logging cho production (JSON)
# 5. Rotate log files để tránh full disk
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

# === Đọc environment variables ===
db_host = os.getenv("DB_HOST", "localhost")  # Trả về default nếu không có
db_port = os.getenv("DB_PORT", "5432")       # Luôn trả về string!
debug = os.getenv("DEBUG", "false")

# ⚠️ os.getenv() luôn trả về string, cần convert thủ công
db_port_int = int(db_port)                   # "5432" → 5432
is_debug = debug.lower() == "true"           # "true" → True

# ⚠️ Khác với os.environ[key]: raise KeyError nếu không có
# os.environ["MISSING_KEY"]  # ❌ KeyError
# os.getenv("MISSING_KEY")   # ✅ None

# === Set environment variable ===
os.environ["DEBUG"] = "true"  # Set trong process hiện tại (không persist)

# === .env file với python-dotenv ===
# pip install python-dotenv
# .env file:
# DB_HOST=localhost
# DB_PORT=5432
# SECRET_KEY=my-secret-key
# DEBUG=true

from dotenv import load_dotenv

load_dotenv()  # Load .env file từ thư mục hiện tại
# load_dotenv(".env.production")  # Load file cụ thể

db_host = os.getenv("DB_HOST")  # Đọc sau khi load_dotenv()
print(db_host)  # Output: localhost (từ .env file)

# ⚠️ Không commit .env file vào git! Thêm vào .gitignore
# ⚠️ Dùng .env.example để document các biến cần thiết

# === Real-world: Type-safe config với pydantic ===
# pip install pydantic-settings
# from pydantic_settings import BaseSettings
# class Settings(BaseSettings):
#     db_host: str = "localhost"
#     db_port: int = 5432
#     debug: bool = False
#     secret_key: str
#
#     class Config:
#         env_file = ".env"
#
# settings = Settings()  # Tự động đọc từ env vars và .env file
# print(settings.db_port)  # int, không phải string!
```

#### Config File

```python
import os

# === Pattern: Config class với inheritance ===
class Config:
    """Base config - shared settings"""
    DEBUG = False                                    # Mặc định tắt debug
    TESTING = False                                  # Mặc định không phải test
    DATABASE_URL = "postgresql://localhost/mydb"     # Default DB
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key") # Từ env var
    LOG_LEVEL = "INFO"

class DevelopmentConfig(Config):
    """Config cho môi trường development"""
    DEBUG = True                                     # Bật debug
    DATABASE_URL = "postgresql://localhost/mydb_dev" # DB riêng cho dev
    LOG_LEVEL = "DEBUG"                              # Log nhiều hơn

class TestingConfig(Config):
    """Config cho testing"""
    TESTING = True                                   # Bật testing mode
    DATABASE_URL = "sqlite:///:memory:"              # In-memory DB cho test
    LOG_LEVEL = "WARNING"                            # Ít log hơn

class ProductionConfig(Config):
    """Config cho production"""
    DATABASE_URL = os.getenv("DATABASE_URL")         # Bắt buộc từ env var
    SECRET_KEY = os.getenv("SECRET_KEY")             # Bắt buộc từ env var
    LOG_LEVEL = "ERROR"                              # Chỉ log errors

# Mapping tên → class
config_map = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}

# Chọn config theo env var
env = os.getenv("APP_ENV", "development")
config = config_map[env]()  # Tạo instance
print(config.DEBUG)         # Output: True (nếu APP_ENV=development)

# === Real-world: Validate config khi startup ===
def validate_config(config):
    """Kiểm tra config hợp lệ trước khi start app"""
    errors = []
    if not config.SECRET_KEY:
        errors.append("SECRET_KEY is required")
    if not config.DATABASE_URL:
        errors.append("DATABASE_URL is required")
    if errors:
        raise ValueError(f"Invalid config: {', '.join(errors)}")
    return True

# validate_config(config)  # Raise ValueError nếu thiếu config
```

---

### 11.5. Build & Package Management

#### pip

```bash
# === Cài đặt packages ===
pip install package               # Cài mới nhất
pip install package==1.0.0        # Cài version cụ thể
pip install "package>=1.0.0"     # Cài version thỏa mãn điều kiện
pip install -U package           # Upgrade lên version mới nhất

# === Requirements files ===
# requirements.txt chứa danh sách packages cần cài
# Ví dụ:
# requests>=2.28.0
# flask>=2.0.0,<3.0.0
# numpy==1.24.0

pip install -r requirements.txt  # Cài tất cả từ file
pip install -r requirements-dev.txt  # Cài dev dependencies

# === Virtual Environment ===
# Tạo virtual environment để cô lập dependencies
python -m venv venv              # Tạo thư mục venv/
# Hoặc: python3 -m venv venv

# Activate (Linux/Mac):
source venv/bin/activate         # Kích hoạt virtual environment
# activate → thấy (venv) ở đầu dòng lệnh

# Activate (Windows):
venv\Scripts\activate            # Kích hoạt trên Windows

# Sau khi activate, pip sẽ cài vào venv, không ảnh hưởng global Python

# Deactivate khi xong:
deactivate                      # Thoát khỏi virtual environment

# === pip freeze ===
pip freeze                      # Liệt kê tất cả packages đã cài
pip freeze > requirements.txt   # Lưu vào file (dùng cho production)
pip freeze > requirements-dev.txt  # Cho development

# ⚠️ pip freeze không phân biệt direct deps vs transitive deps
# Dùng pip-tools để quản lý tốt hơn:
# pip install pip-tools
# pip-compile requirements.in  # Tạo requirements.txt với pinned versions

# === pipx - cài tool global mà không pollute system ===
# pipx install black   # Cài black như command line tool global
# pipx install httpie  # Cài httpie

# === poetry - alternative package manager ===
# pip install poetry
# poetry new mypackage           # Tạo project mới
# poetry add requests           # Thêm dependency
# poetry add --group dev pytest # Thêm dev dependency
# poetry install                # Cài tất cả
# poetry build                  # Build package
```

#### pyproject.toml / setup.py

```toml
# === pyproject.toml (PEP 517/518) - KHUYẾN NGHỊ ===
# Đây là cách chuẩn để định nghĩa package Python

[build-system]
requires = ["setuptools>=61.0", "wheel"]  # Build tools cần thiết
build-backend = "setuptools.build_meta"  # Backend dùng để build

[project]
name = "mypackage"                        # Tên package (unique trên PyPI)
version = "1.0.0"                        # Version (dùng semver)
description = "My awesome Python package" # Mô tả ngắn
readme = "README.md"                      # File README
license = {text = "MIT"}                  # License
authors = [
    {name = "Your Name", email = "you@example.com"}
]
requires-python = ">=3.8"                # Python version tối thiểu
classifiers = [                           # Phân loại (giúp người tìm thấy)
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

# === Dependencies ===
# Main dependencies (cài khi pip install mypackage)
dependencies = [
    "requests>=2.28.0",
    "flask>=2.0.0",
    "django>=4.0.0,<5.0.0",  # Pin version
]

# Optional dependencies (cài với: pip install mypackage[extra])
[project.optional-dependencies]
dev = ["pytest", "pytest-cov", "black", "ruff"]
test = ["pytest", "pytest-asyncio", "httpx"]
docs = ["sphinx", "myst-parser"]

# === Entry points - command line tools ===
[project.scripts]
mytool = "mypackage.cli:main"  # Tạo command: mytool

# === Package metadata ===
keywords = ["python", "utility", "tool"]
homepage = "https://github.com/username/mypackage"
repository = "https://github.com/username/mypackage"

# === Tool configurations ===
[tool.setuptools.packages.find]
where = ["src"]  # Package ở thư mục src/

[tool.black]
line-length = 88           # Black format (PEP 8 style)
target-version = ['py38']  # Target Python 3.8+

[tool.ruff]
line-length = 88
target-version = "py38"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]

# === Cài đặt package từ source ===
# pip install -e .           # Editable mode (development)
# pip install .              # Regular install
# pip install .[dev]        # Với dev dependencies
# pip install -e ".[dev]"   # Editable + dev
```

---

### 11.6. Documentation

#### Docstring

```python
"""Module docstring - mô tả ngắn gọn về module này.

Mô tả chi tiết hơn về module, giải thích purpose, usage...
"""

# === Class docstring ===
class UserService:
    """Service quản lý users.

    Xử lý các operations liên quan đến users như create, update, delete.
    Dùng kết hợp với UserRepository để persist data.

    Attributes:
        repository: UserRepository instance để truy xuất database
        logger: Logger instance để ghi log

    Raises:
        ValueError: Khi user data không hợp lệ
        PermissionError: Khi user không có quyền thực hiện operation

    Example:
        >>> service = UserService(repository)
        >>> user = service.get_user(1)
        >>> print(user.name)
        'John'
    """

    def __init__(self, repository, logger=None):
        """Khởi tạo UserService.

        Args:
            repository: UserRepository instance (required)
            logger: Optional logger, mặc định None
        """
        self.repository = repository
        self.logger = logger

    def get_user(self, user_id: int) -> dict | None:
        """Lấy user theo ID.

        Args:
            user_id: ID của user cần lấy

        Returns:
            User dict hoặc None nếu không tìm thấy

        Example:
            >>> service.get_user(1)
            {'id': 1, 'name': 'John'}
        """
        return self.repository.find(user_id)
```

#### Docstring Formats

```python
# === Google Style (phổ biến nhất) ===
def func_google(arg1, arg2):
    """Mô tả ngắn gọn.

    Mô tả chi tiết hơn về function.

    Args:
        arg1: Mô tả arg1
        arg2: Mô tả arg2

    Returns:
        Mô tả giá trị trả về

    Raises:
        ValueError: Khi arg không hợp lệ

    Example:
        >>> func_google(1, 2)
        3
    """
    return arg1 + arg2

# === NumPy Style (phổ biến trong scientific Python) ===
def func_numpy(arg1, arg2):
    """
    Mô tả ngắn gọn.

    Parameters
    ----------
    arg1 : int
        Mô tả arg1
    arg2 : int
        Mô tả arg2

    Returns
    -------
    int
        Mô tả giá trị trả về
    """
    return arg1 + arg2

# === reStructuredText (dùng với Sphinx) ===
def func_rst(arg1, arg2):
    """
    Mô tả ngắn gọn.

    :param arg1: Mô tả arg1
    :type arg1: int
    :param arg2: Mô tả arg2
    :type arg2: int
    :returns: Mô tả giá trị trả về
    :rtype: int
    """
    return arg1 + arg2

# === Tools hỗ trợ generate doc ===
# pip install pdoc          # Tạo documentation từ docstrings
# pdoc module.py            # Generate HTML docs

# pip install sphinx        # Documentation generator chuyên nghiệp
# sphinx-quickstart        # Tạo sphinx project
# sphinx-apidoc -o docs/ mypackage/  # Auto-generate API docs
```

#### Comments

```python
# === Single line comment ===
# Comment giải thích code phía dưới

# === Inline comment ===
x = 1  # Gán giá trị cho x

# === Multi-line comment (docstring cũng là comment) ===
# Comment có thể viết trên nhiều dòng
# để giải thích logic phức tạp
# hoặc tắt code tạm thời

# === TODO comments ===
# TODO(username): Fix this later
# FIXME(username): This is broken
# NOTE(username): Consider this approach
# XXX: This code is wrong

# === Block comment cho function ===
# Calculate factorial with memoization
# Uses dynamic programming to optimize performance
def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = n * factorial(n - 1, memo)
    return memo[n]
```

---

### 11.8. Design Patterns

```python
# === Observer Pattern ===
# Subject thông báo cho các Observers khi có thay đổi
# Dùng trong: event handling, MVC, pub/sub

class EventEmitter:
    """Subject: quản lý và thông báo events cho observers"""
    def __init__(self):
        self._listeners = {}  # event_name -> list of callbacks

    def on(self, event, callback):
        """Đăng ký observer cho event"""
        self._listeners.setdefault(event, []).append(callback)

    def off(self, event, callback):
        """Hủy đăng ký observer"""
        if event in self._listeners:
            self._listeners[event].remove(callback)

    def emit(self, event, *args):
        """Thông báo cho tất cả observers của event"""
        for callback in self._listeners.get(event, []):
            callback(*args)

# Sử dụng
emitter = EventEmitter()

# Đăng ký observer (callback function)
emitter.on("user_created", lambda name: print(f"Welcome {name}!"))
emitter.on("user_created", lambda name: print(f"User {name} added to DB"))

# Emit event → tất cả observers được gọi
emitter.emit("user_created", "John")
# Output:
# Welcome John!
# User John added to DB

# === Strategy Pattern ===
# Đóng gói thuật toán, cho phép thay đổi thuật toán runtime
# Dùng trong: sorting, payment processing, validation

from abc import ABC, abstractmethod

class SortStrategy(ABC):
    """Abstract base class cho các strategies"""
    @abstractmethod
    def sort(self, data: list) -> list:
        """Sort data và return sorted result"""
        pass

class BubbleSort(SortStrategy):
    """Implementation Bubble Sort (chỉ để demo, dùng sorted() thực tế)"""
    def sort(self, data):
        sorted_data = data.copy()
        n = len(sorted_data)
        for i in range(n):
            for j in range(0, n-i-1):
                if sorted_data[j] > sorted_data[j+1]:
                    sorted_data[j], sorted_data[j+1] = sorted_data[j+1], sorted_data[j]
        return sorted_data

class QuickSort(SortStrategy):
    """Implementation Quick Sort"""
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class Sorter:
    """Context: sử dụng strategy được inject"""
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)

# Sử dụng
data = [64, 34, 25, 12, 22, 11, 90]

sorter = Sorter(BubbleSort())
print(sorter.sort(data))  # Output: [11, 12, 22, 25, 34, 64, 90]

sorter = Sorter(QuickSort())
print(sorter.sort(data))  # Output: [11, 12, 22, 25, 34, 64, 90]

# === Repository Pattern ===
# Tách logic truy xuất data khỏi business logic
# Dùng trong: data access layer, ORM

class UserRepository:
    """Repository: đóng gói data access logic"""
    def __init__(self):
        self._users = {}  # In-memory storage

    def save(self, user):
        """Lưu user vào storage"""
        self._users[user['id']] = user

    def find_by_id(self, id):
        """Tìm user theo ID"""
        return self._users.get(id)

    def find_all(self):
        """Lấy tất cả users"""
        return list(self._users.values())

    def delete(self, id):
        """Xóa user"""
        if id in self._users:
            del self._users[id]

# Sử dụng
repo = UserRepository()
repo.save({"id": 1, "name": "John"})
repo.save({"id": 2, "name": "Jane"})

print(repo.find_by_id(1))  # Output: {'id': 1, 'name': 'John'}
print(repo.find_all())     # Output: [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]

# === Decorator Pattern ===
# Thêm behavior cho object/function mà không modify class
# Python hỗ trợ native với @decorator syntax

import functools

def cache(func):
    """Decorator: cache kết quả của function (memoization)"""
    memo = {}  # Cache storage

    @functools.wraps(func)  # Giữ nguyên func metadata
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]

    return wrapper

@cache
def fibonacci(n):
    """Tính Fibonacci với memoization"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Không có cache: O(2^n), có cache: O(n)
print(fibonacci(100))  # Output: 354224848179261915075 (tính nhanh!)

# === Singleton Pattern (nhiều cách) ===
# Cách 1: Module-level singleton (đơn giản nhất trong Python)
# mysingleton.py
# class _Singleton:
#     def foo(self): pass
# singleton = _Singleton()  # Tạo 1 lần, import nhiều lần

# Cách 2: Class-based
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True (cùng 1 instance)

# === Factory Pattern ===
# Tạo object mà không specify exact class
class Car:
    def drive(self): print("Driving")

class Truck:
    def drive(self): print("Hauling")

def vehicle_factory(vehicle_type: str):
    """Factory: tạo vehicle theo type"""
    vehicles = {
        "car": Car,
        "truck": Truck,
    }
    return vehicles[vehicle_type]()

v = vehicle_factory("car")
v.drive()  # Output: Driving
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
# === Meta-programming - code tạo/thay đổi code tại runtime ===
# Python cho phép thao tác classes, functions, attributes tại runtime

# --- __new__ - kiểm soát quá trình TẠO object ---
# __new__ chạy TRƯỚC __init__, quyết định object nào được tạo
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Tạo object mới
        return cls._instance  # Trả về instance duy nhất

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True (cùng 1 object)

# --- __getattr__ vs __getattribute__ ---
# __getattr__: chỉ gọi khi attribute KHÔNG TÌM THẤY bình thường
# __getattribute__: gọi cho MỌI truy cập attribute (cẩn thận infinite loop!)

class DynamicConfig:
    """Config object trả về None cho mọi key chưa set."""
    def __init__(self):
        self._data = {}

    def __getattr__(self, name):
        # Chỉ gọi khi name không tồn tại trong __dict__
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)  # Internal attrs → bình thường
        else:
            self._data[name] = value  # Public attrs → lưu vào _data

config = DynamicConfig()
config.debug = True
config.port = 8080
print(config.debug)    # Output: True
print(config.port)     # Output: 8080
print(config.missing)  # Output: None (không lỗi, trả về None)

# --- __slots__ - tối ưu memory và tốc độ ---
# Mặc định: mỗi object có __dict__ (dict) → tốn memory
# __slots__: khai báo trước attributes → dùng tuple thay dict

class OptimizedUser:
    __slots__ = ['name', 'age']  # Chỉ cho phép 2 attributes này

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = OptimizedUser("John", 30)
print(user.name)       # Output: John
# user.email = "x"     # ❌ AttributeError: 'OptimizedUser' has no attribute 'email'
# print(user.__dict__)  # ❌ AttributeError: no __dict__ (tiết kiệm memory!)

# So sánh memory:
import sys
class Normal:
    def __init__(self, x): self.x = x

class Slotted:
    __slots__ = ['x']
    def __init__(self, x): self.x = x

print(sys.getsizeof(Normal(1).__dict__))  # Output: ~104 bytes (dict overhead)
# Slotted không có __dict__ → tiết kiệm ~40-50% memory mỗi instance

# --- Descriptors - kiểm soát truy cập attribute ---
# Descriptor = object có __get__, __set__, hoặc __delete__
# Dùng cho: validation, lazy loading, computed properties

class Validated:
    """Descriptor: validate giá trị khi gán."""
    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.name = name  # Tên attribute (Python 3.6+)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self  # Truy cập từ class → trả về descriptor
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"{self.name} must be >= {self.min_val}, got {value}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"{self.name} must be <= {self.max_val}, got {value}")
        obj.__dict__[self.name] = value

class Product:
    price = Validated(min_val=0)        # Giá >= 0
    quantity = Validated(min_val=0, max_val=10000)  # 0 <= quantity <= 10000

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price          # Gọi Validated.__set__
        self.quantity = quantity

p = Product("Laptop", 999, 50)
print(p.price)         # Output: 999
# p.price = -10        # ❌ ValueError: price must be >= 0, got -10

# --- Metaclass - class tạo class ---
# type() vừa là function kiểm tra kiểu, vừa là metaclass mặc định
# Metaclass kiểm soát quá trình TẠO class (không phải instance)

# Tạo class bằng type() (thay vì dùng class keyword)
MyClass = type('MyClass', (object,), {'x': 10, 'greet': lambda self: "hello"})
obj = MyClass()
print(obj.x)           # Output: 10
print(obj.greet())     # Output: hello

# Custom metaclass
class AutoReprMeta(type):
    """Metaclass tự động thêm __repr__ cho mọi class."""
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        # Tự thêm __repr__ nếu class chưa có
        if '__repr__' not in namespace:
            def auto_repr(self):
                attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
                return f"{name}({attrs})"
            cls.__repr__ = auto_repr
        return cls

class User(metaclass=AutoReprMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(User("John", 30))  # Output: User(name='John', age=30) (tự động!)

# ⚠️ Metaclass rất mạnh nhưng phức tạp
# Thường dùng decorator hoặc __init_subclass__ thay thế
# Chỉ dùng metaclass khi thực sự cần kiểm soát quá trình tạo class

# --- __init_subclass__ (Python 3.6+) - thay thế metaclass đơn giản ---
class Plugin:
    """Base class tự động đăng ký subclasses."""
    _registry = {}

    def __init_subclass__(cls, plugin_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        name = plugin_name or cls.__name__
        Plugin._registry[name] = cls
        print(f"Registered plugin: {name}")

class JSONPlugin(Plugin, plugin_name="json"):
    pass  # Output: Registered plugin: json

class XMLPlugin(Plugin, plugin_name="xml"):
    pass  # Output: Registered plugin: xml

print(Plugin._registry)
# Output: {'json': <class 'JSONPlugin'>, 'xml': <class 'XMLPlugin'>}
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

# === Infinite iterators ===
# count(start, step): đếm vô hạn từ start
counter = itertools.count(10)       # 10, 11, 12, ...
print(next(counter))                # Output: 10
print(next(counter))                # Output: 11

# cycle(iterable): lặp vô hạn qua iterable
cycler = itertools.cycle([1, 2, 3]) # 1, 2, 3, 1, 2, 3, ...
print([next(cycler) for _ in range(6)])  # Output: [1, 2, 3, 1, 2, 3]

# repeat(value, times): lặp value n lần (hoặc vô hạn nếu không có times)
repeated = list(itertools.repeat(5, 3))  # Lặp 5 ba lần
print(repeated)  # Output: [5, 5, 5]

# === Combinatoric iterators ===
# product: tích Cartesian (nested loops)
pairs = list(itertools.product([1, 2], [3, 4]))
print(pairs)  # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

# permutations: tất cả hoán vị
perms = list(itertools.permutations("ABC"))
print(len(perms))  # Output: 6 (3! = 6)
print(perms[:3])   # Output: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C')]

# combinations: tổ hợp (không lặp, không quan tâm thứ tự)
combs = list(itertools.combinations("ABC", 2))
print(combs)  # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]

# combinations_with_replacement: tổ hợp có lặp
combs_r = list(itertools.combinations_with_replacement("AB", 2))
print(combs_r)  # Output: [('A', 'A'), ('A', 'B'), ('B', 'B')]

# === Chain: nối nhiều iterables ===
chained = list(itertools.chain([1, 2], [3, 4], [5]))
print(chained)  # Output: [1, 2, 3, 4, 5]

# chain.from_iterable: nối từ iterable of iterables
nested = [[1, 2], [3, 4], [5, 6]]
flat = list(itertools.chain.from_iterable(nested))
print(flat)  # Output: [1, 2, 3, 4, 5, 6]

# === Filter/transform ===
# filterfalse: lọc phần tử mà predicate trả về False
evens = list(itertools.filterfalse(lambda x: x % 2, range(10)))
print(evens)  # Output: [0, 2, 4, 6, 8]

# islice: slice iterator (không load toàn bộ vào memory)
sliced = list(itertools.islice(range(100), 0, 10, 2))  # start=0, stop=10, step=2
print(sliced)  # Output: [0, 2, 4, 6, 8]

# takewhile: lấy phần tử khi điều kiện đúng
taken = list(itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6]))
print(taken)  # Output: [1, 2, 3, 4]

# dropwhile: bỏ phần tử khi điều kiện đúng, lấy phần còn lại
dropped = list(itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6]))
print(dropped)  # Output: [5, 6]

# groupby: nhóm phần tử liên tiếp theo key
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("c", 5)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"{key}: {list(group)}")
# Output:
# a: [('a', 1), ('a', 2)]
# b: [('b', 3), ('b', 4)]
# c: [('c', 5)]

# ⚠️ groupby chỉ nhóm phần tử LIÊN TIẾP - cần sort trước nếu muốn nhóm tất cả

# === Real-world: Batch processing ===
def batched(iterable, n):
    """Chia iterable thành batches kích thước n"""
    it = iter(iterable)
    while True:
        batch = list(itertools.islice(it, n))
        if not batch:
            break
        yield batch

data = range(10)
for batch in batched(data, 3):
    print(batch)
# Output:
# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]
# [9]
```

#### functools

```python
import functools

# === lru_cache - memoization (cache kết quả function) ===
@functools.lru_cache(maxsize=128)  # Cache tối đa 128 kết quả
def fib(n):
    """Fibonacci với memoization - O(n) thay vì O(2^n)"""
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))   # Output: 55
print(fib(100))  # Output: 354224848179261915075 (nhanh!)
print(fib.cache_info())  # Output: CacheInfo(hits=..., misses=..., maxsize=128, currsize=...)

# Python 3.9+: @functools.cache (unlimited cache)
@functools.cache
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# === partial - tạo function với args được fix sẵn ===
def power(base, exp):
    return base ** exp

square = functools.partial(power, exp=2)   # Fix exp=2
cube = functools.partial(power, exp=3)     # Fix exp=3

print(square(5))  # Output: 25 (5^2)
print(cube(3))    # Output: 27 (3^3)

# Dùng partial với sorted
from functools import partial
users = [{"name": "Charlie", "age": 30}, {"name": "Alice", "age": 25}, {"name": "Bob", "age": 35}]
sort_by_name = partial(sorted, key=lambda u: u["name"])
print([u["name"] for u in sort_by_name(users)])  # Output: ['Alice', 'Bob', 'Charlie']

# === reduce - fold/accumulate ===
from functools import reduce

total = reduce(lambda a, b: a + b, [1, 2, 3, 4])  # ((1+2)+3)+4
print(total)  # Output: 10

product = reduce(lambda a, b: a * b, [1, 2, 3, 4])  # ((1*2)*3)*4
print(product)  # Output: 24

# reduce với initial value
total_with_init = reduce(lambda a, b: a + b, [1, 2, 3], 100)  # 100+1+2+3
print(total_with_init)  # Output: 106

# === singledispatch - function overloading theo type ===
@functools.singledispatch
def process(arg):
    """Default handler"""
    print(f"Default: {arg}")

@process.register(int)
def process_int(arg):
    print(f"Integer: {arg * 2}")

@process.register(str)
def process_str(arg):
    print(f"String: {arg.upper()}")

@process.register(list)
def process_list(arg):
    print(f"List with {len(arg)} items")

process(42)          # Output: Integer: 84
process("hello")     # Output: String: HELLO
process([1, 2, 3])   # Output: List with 3 items
process(3.14)        # Output: Default: 3.14

# === wraps - preserve function metadata ===
def my_decorator(func):
    @functools.wraps(func)  # Giữ nguyên __name__, __doc__, __annotations__
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """My function docstring"""
    pass

print(my_function.__name__)  # Output: my_function (không phải 'wrapper')
print(my_function.__doc__)   # Output: My function docstring
```

### 18.3. I/O & System

```python
# === File operations với os.path ===
import os

print(os.path.exists("file.txt"))   # Output: True/False - kiểm tra tồn tại
print(os.path.isfile("file.txt"))   # Output: True/False - kiểm tra là file
print(os.path.isdir("folder"))      # Output: True/False - kiểm tra là directory
print(os.listdir("."))              # Output: ['file1.py', 'folder1', ...] - liệt kê thư mục

# os.walk: duyệt đệ quy qua thư mục
for root, dirs, files in os.walk("."):
    for file in files:
        filepath = os.path.join(root, file)  # Tạo full path
        print(filepath)  # Output: ./subdir/file.py

# === Path (Python 3.4+) - khuyến nghị hơn os.path ===
from pathlib import Path

p = Path(".")
py_files = list(p.glob("*.py"))  # Tìm tất cả .py files trong thư mục hiện tại
print(py_files)  # Output: [PosixPath('script.py'), ...]

all_py = list(p.rglob("*.py"))  # Tìm đệ quy
print(len(all_py))  # Output: số lượng .py files

# === Environment variables ===
import os

path = os.environ.get("PATH")  # Lấy PATH env var
print(os.getcwd())             # Output: /home/user/project (thư mục hiện tại)
print(os.getenv("HOME"))       # Output: /home/user

# === Command line arguments ===
import sys

print(sys.argv)  # Output: ['script.py', 'arg1', 'arg2'] (khi chạy: python script.py arg1 arg2)
print(sys.argv[0])  # Output: script.py (tên script)

# === argparse - parse command line arguments ===
import argparse

parser = argparse.ArgumentParser(description="My CLI tool")
parser.add_argument("-n", "--name", help="Your name", required=True)
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
parser.add_argument("--count", type=int, default=1, help="Number of times")

# args = parser.parse_args()  # Parse từ sys.argv
# Khi chạy: python script.py --name John --verbose --count 3
# args.name = "John", args.verbose = True, args.count = 3

# === subprocess - chạy external commands ===
import subprocess

# Chạy command đơn giản
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.returncode)  # Output: 0 (success)
print(result.stdout)      # Output: nội dung ls -la
print(result.stderr)      # Output: "" (không có error)

# Chạy với shell=True (cẩn thận với user input - command injection!)
result = subprocess.run("echo hello", shell=True, capture_output=True, text=True)
print(result.stdout)  # Output: hello\n

# ⚠️ Không dùng shell=True với user input - nguy cơ command injection!
# ❌ subprocess.run(f"ls {user_input}", shell=True)  # Nguy hiểm!
# ✅ subprocess.run(["ls", user_input])              # An toàn

# Kiểm tra exit code
try:
    subprocess.run(["false"], check=True)  # Raise nếu exit code != 0
except subprocess.CalledProcessError as e:
    print(f"Command failed: {e.returncode}")  # Output: Command failed: 1

# === Process info ===
import os

print(os.getpid())   # Output: 12345 (process ID hiện tại)
print(os.getppid())  # Output: 12344 (parent process ID)

# psutil (pip install psutil) cho thông tin chi tiết hơn
# import psutil
# proc = psutil.Process()
# print(proc.memory_info().rss)  # Resident Set Size (bytes)
# print(proc.cpu_percent())      # CPU usage %
```

---

### 18.6. Math & Numeric

```python
import math
import decimal
import random

# === Math functions ===
print(math.sqrt(16))          # Output: 4.0 (căn bậc 2)
print(math.pow(2, 10))       # Output: 1024.0 (2^10, luôn trả về float)
print(pow(2, 10))           # Output: 1024 (built-in, trả về int nếu có thể)

print(abs(-5))               # Output: 5 (giá trị tuyệt đối - built-in)
print(math.ceil(3.2))        # Output: 4 (làm tròn lên)
print(math.floor(3.8))       # Output: 3 (làm tròn xuống)
print(round(3.7))           # Output: 4 (làm tròn theo standard)
print(round(3.5))           # Output: 4 (làm tròn chẵn cho .5 - banker's rounding)
print(round(2.5))           # Output: 2 (làm tròn chẵn)

print(math.pi)               # Output: 3.141592653589793 (hằng số Pi)
print(math.e)                # Output: 2.718281828459045 (hằng số e)
print(math.sin(math.pi/2))   # Output: 1.0 (sin 90 độ)
print(math.log(100, 10))    # Output: 2.0 (log base 10 của 100)
print(math.log10(100))       # Output: 2.0 (log10)

# === Decimal - số thập phân chính xác ===
# Dùng khi cần precision cao (tài chính, tính toán chính xác)
from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
result = a + b
print(result)               # Output: 0.3 (chính xác!)

# ⚠️ Float không chính xác cho số thập phân
print(0.1 + 0.2)           # Output: 0.30000000000000004 (floating point error)

# Decimal với getcontext để set precision
from decimal import getcontext, ROUND_HALF_UP
getcontext().prec = 50  # 50 chữ số precision

# === Random ===
print(random.random())           # Output: 0.123456789 (float ngẫu nhiên 0.0-1.0)
print(random.randint(1, 100))   # Output: 42 (int ngẫu nhiên 1-100, inclusive)
print(random.randrange(1, 100)) # Output: 42 (int ngẫu nhiên 1-99, exclusive end)

print(random.choice([1, 2, 3])) # Output: 2 (chọn 1 phần tử ngẫu nhiên)

lst = [1, 2, 3, 4, 5]
random.shuffle(lst)            # Shuffle in-place
print(lst)                     # Output: [3, 1, 5, 2, 4] (ngẫu nhiên)

# Chọn n phần tử không trùng
samples = random.sample(range(100), 5)
print(samples)                  # Output: [23, 45, 67, 12, 89]

# Random với seed (để reproduce)
random.seed(42)
print(random.random())         # Output: 0.639426798... (luôn giống nhau với cùng seed)
random.seed(42)
print(random.random())         # Output: 0.639426798... (lặp lại)

# === Statistics (Python 3.4+) ===
import statistics

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(statistics.mean(data))    # Output: 5.5 (trung bình)
print(statistics.median(data)) # Output: 5.5 (trung vị)
print(statistics.stdev(data))  # Output: 3.02765 (standard deviation)
print(statistics.variance(data))  # Output: 9.16666... (variance)
print(statistics.mode([1, 2, 2, 3, 3, 3]))  # Output: 3 (mode - giá trị xuất hiện nhiều nhất)
```

### 18.7. Encoding

```python
import base64
import urllib.parse
import codecs

# === Base64 - encode/decode binary to ASCII ===
# Dùng cho: embed binary trong JSON/XML, email attachments, URL-safe encoding

encoded = base64.b64encode(b"Hello World")
print(encoded)                 # Output: b'SGVsbG8gV29ybGQ=' (ASCII text)

decoded = base64.b64decode(encoded)
print(decoded)                 # Output: b'Hello World'

# URL-safe Base64 (thay +/ bằng -_)
encoded_url = base64.urlsafe_b64encode(b"Hello World")
print(encoded_url)            # Output: b'SGVsbG8gV29ybGQ='

# === URL Encoding/Decoding ===
# Encode special characters cho URL
encoded = urllib.parse.quote("hello world")
print(encoded)                 # Output: hello%20world (space → %20)

encoded = urllib.parse.quote("user@email.com")
print(encoded)                # Output: user%40email.com (@ → %40)

# Decode ngược lại
decoded = urllib.parse.unquote("hello%20world")
print(decoded)                # Output: hello world

# Encode query parameters
query = urllib.parse.urlencode({"name": "John Doe", "age": 30})
print(query)                  # Output: name=John+Doe&age=30 (space → +)
# ⚠️ Dùng quote_plus cho thay thế space bằng +

# Parse query string
parsed = urllib.parse.parse_qs(query)
print(parsed)                 # Output: {'name': ['John Doe'], 'age': ['30']}

# === Unicode / UTF-8 Encoding ===
text = "Xin chào"  # Unicode string
print(text)                  # Output: Xin chào

# Encode to bytes
encoded = text.encode('utf-8')
print(encoded)               # Output: b'Xin ch\xc3\xa0o' (UTF-8 bytes)
print(len(encoded))          # Output: 11 (bytes)

# Decode back to string
decoded = encoded.decode('utf-8')
print(decoded)               # Output: Xin chào

# === Hex encoding ===
data = b"Hello"
hex_str = data.hex()                    # Bytes → hex string
print(hex_str)                          # Output: 48656c6c6f

recovered = bytes.fromhex(hex_str)      # Hex string → bytes
print(recovered)                        # Output: b'Hello'

# === HTML encoding ===
import html
escaped = html.escape("<script>alert('xss')</script>")
print(escaped)                          # Output: &lt;script&gt;...

unescaped = html.unescape(escaped)
print(unescaped)                        # Output: <script>alert('xss')</script>
```

---

## 19. Tầng 19: Ecosystem

### 19.1. Web Frameworks

#### Django

```python
# === Django - Full-featured framework (batteries included) ===
# pip install django
# Tạo project: django-admin startproject myproject
# Tạo app: python manage.py startapp myapp

# === urls.py - URL routing ===
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),          # Admin panel
    path('users/', views.user_list),           # GET /users/
    path('users/<int:pk>/', views.user_detail), # GET /users/1/
    path('api/', include('api.urls')),         # Include từ api/urls.py
]

# === views.py - Request handlers ===
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])  # Chỉ cho phép GET
def user_list(request):
    """Trả về danh sách users"""
    users = [{"id": 1, "name": "John"}]
    return JsonResponse({"users": users})  # Tự động serialize thành JSON

# Class-based view
from django.views import View
class UserView(View):
    def get(self, request, pk):
        return JsonResponse({"id": pk, "name": "John"})

    def post(self, request):
        import json
        data = json.loads(request.body)
        return JsonResponse({"id": 1, **data}, status=201)

# === models.py - Database models ===
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)   # VARCHAR(100)
    email = models.EmailField(unique=True)    # VARCHAR với email validation
    age = models.IntegerField(null=True, blank=True)  # Nullable int
    created_at = models.DateTimeField(auto_now_add=True)  # Tự set khi tạo
    updated_at = models.DateTimeField(auto_now=True)      # Tự update khi save

    class Meta:
        db_table = 'users'          # Tên bảng trong DB
        ordering = ['-created_at']  # Default ordering

    def __str__(self):
        return f"{self.name} ({self.email})"

# === Migrations ===
# python manage.py makemigrations  # Tạo migration files
# python manage.py migrate         # Apply migrations

# === ORM queries ===
# User.objects.all()                    # SELECT * FROM users
# User.objects.filter(name="John")      # WHERE name = 'John'
# User.objects.get(pk=1)               # WHERE id = 1 (raise nếu không tìm thấy)
# User.objects.create(name="Jane")     # INSERT INTO users
# User.objects.filter(age__gt=18)      # WHERE age > 18
```

#### Flask

```python
# === Flask - Microframework (minimal, flexible) ===
# pip install flask
from flask import Flask, request, jsonify, abort

app = Flask(__name__)  # Tạo Flask app, __name__ = module name

# === Route handlers ===
@app.route('/users', methods=['GET'])  # Chỉ cho phép GET
def get_users():
    """Trả về danh sách users"""
    users = [{"id": 1, "name": "John"}]
    return jsonify({"users": users})  # Serialize dict thành JSON response

@app.route('/users/<int:user_id>', methods=['GET'])  # URL parameter
def get_user(user_id):
    """Lấy user theo ID"""
    if user_id != 1:
        abort(404)  # Trả về 404 Not Found
    return jsonify({"id": user_id, "name": "John"})

@app.route('/users', methods=['POST'])  # POST request
def create_user():
    """Tạo user mới"""
    data = request.get_json()  # Parse JSON request body
    if not data or 'name' not in data:
        abort(400)  # Bad Request
    return jsonify({"id": 1, **data}), 201  # 201 Created

# === Error handlers ===
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# === Flask với SQLAlchemy ===
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # DB connection string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Tắt warning
db = SQLAlchemy(app)  # Khởi tạo SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-increment PK
    name = db.Column(db.String(100), nullable=False)  # NOT NULL
    email = db.Column(db.String(120), unique=True)    # UNIQUE

# Chạy: flask run --debug
# Hoặc: python -m flask run
```

#### FastAPI

```python
# === FastAPI - Modern async framework với auto-docs ===
# pip install fastapi uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI(title="My API", version="1.0.0")  # Tạo app với metadata

# === Pydantic models - request/response validation ===
class UserCreate(BaseModel):
    name: str                    # Required string
    email: str                   # Required string
    age: int | None = None       # Optional int, default None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

# === Route handlers ===
@app.get("/users", response_model=list[UserResponse])  # Validate response
async def get_users():
    """Trả về danh sách users"""
    return [{"id": 1, "name": "John", "email": "john@example.com"}]

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):  # Path parameter với type annotation
    """Lấy user theo ID"""
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, "name": "John", "email": "john@example.com"}

@app.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):  # Request body validation
    """Tạo user mới"""
    return {"id": 1, **user.dict()}

# === Dependency Injection ===
def get_db():
    """Dependency: tạo DB session"""
    db = {"connected": True}  # Giả lập DB
    try:
        yield db
    finally:
        pass  # db.close()

@app.get("/users/{user_id}/profile")
async def get_profile(user_id: int, db=Depends(get_db)):
    """Sử dụng DB dependency"""
    return {"user_id": user_id, "db_connected": db["connected"]}

# === Chạy server ===
# uvicorn main:app --reload --port 8000
# Docs tự động: http://localhost:8000/docs (Swagger UI)
# ReDoc: http://localhost:8000/redoc
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
# === Black - opinionated code formatter ===
# pip install black
# Chạy format:
black src/           # Format code trong thư mục src/
black --check src/   # Chỉ check, không format (dùng trong CI)
black --diff src/    # Show diff mà không thay đổi file
black --verbose src/ # Hiển thị chi tiết các files được format

# === Configuration ===
# Tạo pyproject.toml hoặc black.toml:
# [tool.black]
# line-length = 88           # PEP 8 standard
# target-version = ['py38']  # Target Python 3.8+
# include = '\.pyi?$'       # File patterns
# exclude = '''/(\.git|\.venv|build|dist)/'''  # Exclude patterns

# === VS Code integration ===
# settings.json: "python.formatting.provider": "black"
```

#### flake8 (Linter)

```bash
# === Flake8 - style checker + linting ===
# pip install flake8
flake8 src/                   # Check code trong src/
flake8 --max-line-length=88 src/  # Custom line length
flake8 --ignore=E501,W503 src/    # Ignore specific rules

# === Configuration ===
# .flake8 hoặc pyproject.toml:
# [flake8]
# max-line-length = 88
# ignore = E203, E501, W503
# exclude = .git,__pycache__,build

# === Common error codes ===
# E501: Line too long
# W503: Line break before binary operator
# F401: Module imported but unused
# F811: Redefinition of unused name

# === Ruff - thay thế nhanh hơn cho flake8 ===
# pip install ruff
ruff check src/           # Check như flake8 nhưng nhanh hơn 10-100x
ruff check --fix src/    # Auto-fix các issues
ruff format src/          # Format như Black nhưng nhanh hơn
```

#### mypy (Type Checker)

```bash
# === MyPy - Static type checker ===
# pip install mypy
mypy src/               # Type check với default settings
mypy --strict src/      # Strict mode (nghiêm ngặt nhất)
mypy --ignore-missing-imports src/  # Ignore lỗi import
mypy --warn-unused-ignores src/     # Warn về ignore không cần thiết

# === Configuration ===
# mypy.ini hoặc pyproject.toml:
# [mypy]
# python_version = 3.8
# warn_return_any = True
# warn_unused_configs = True
# disallow_untyped_defs = False
# ignore_missing_imports = True

# [tool.mypy]
# [[tool.mypy.overrides]]
# module = "numpy.*"
# ignore_missing_imports = True

# === Common type comments ===
# x: int = 5  # Inline type annotation
# def foo(x):
#     # type: (int) -> str
#     pass
```

#### pre-commit

```bash
# === Pre-commit - Git hooks tự động ===
# pip install pre-commit

# === Cài đặt ===
# Tạo .pre-commit-config.yaml:
cat > .pre-commit-config.yaml << 'EOF'
repos:
  # Format với Black
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
        args: [--check, --diff]  # Chỉ check trong pre-commit

  # Lint với Ruff
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
        args: [--fix]

  # Type check với MyPy
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]

  # Check trailing whitespace
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
EOF

# === Sử dụng ===
pre-commit install                    # Cài đặt git hooks
pre-commit run                        # Chạy tất cả hooks
pre-commit run black                  # Chỉ chạy black
pre-commit autoupdate                  # Update versions

# === Bypass hooks (khi cần) ===
git commit --no-verify  # Bypass pre-commit hooks
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
import cProfile
import timeit

# === cProfile - built-in function profiler ===
def slow_function():
    """Hàm tốn thời gian để demo"""
    total = 0
    for i in range(100000):
        total += i ** 2  # Square operation
    return total

# Chạy profiler trực tiếp
result = cProfile.run('slow_function()')
# Output:
#    100003 function calls in 0.051 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.042    0.042    0.051    0.051 <string>:1(<module>)
#   ...

# Profile và lưu vào file
cProfile.run('slow_function()', 'output.prof')
# File output.prof có thể visualize bằng:
# pip install snakeviz
# snakeviz output.prof  # Mở web UI

# Hoặc dùng pstats để phân tích
import pstats
p = pstats.Stats('output.prof')
p.sort_stats('cumulative').print_stats(10)  # Top 10 functions by cumulative time
# Output:
#    Ordered by: cumulative time
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.042    0.042    0.051    0.051 <string>:1(<module>)

# === timeit - precise benchmarking ===
# Đo thời gian thực thi với nhiều lần lặp

# Benchmark sum(range(1000))
result = timeit.timeit('sum(range(1000))', number=10000)
print(f"Time: {result:.4f}s")  # Output: Time: 0.2341s (tùy machine)

# Benchmark với setup code
result = timeit.timeit(
    'sorted(data)',
    setup='import random; data = [random.random() for _ in range(1000)]',
    number=1000
)
print(f"Time: {result:.4f}s")  # Output: Time: 0.1234s

# Benchmark nhiều approaches
results = {
    "list_comprehension": timeit.timeit('[x**2 for x in range(1000)]', number=1000),
    "for_loop": timeit.timeit('result=[]\nfor x in range(1000): result.append(x**2)', number=1000),
    "map": timeit.timeit('list(map(lambda x: x**2, range(1000)))', number=1000),
}
for method, time in results.items():
    print(f"{method}: {time:.4f}s")

# === line_profiler - line-by-line profiling ===
# pip install line_profiler
# Thêm @profile decorator vào function cần profile

# @profile
# def slow_function():
#     total = 0
#     for i in range(100000):
#         total += i ** 2
#     return total
#
# Chạy: kernprof -l -v script.py
# Output:
# Wrote profile results to script.py.lprof
# Timer unit: 1e-07 s
# File: script.py
# Function: slow_function at line 2
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#      2                                           def slow_function():
#      3         1         500.0    500.0     1.0      total = 0
#      4    100000    45000.0      0.5    90.0      for i in range(100000):
#      5    100000     5000.0      0.0     9.0          total += i ** 2

# === memory_profiler - memory usage profiling ===
# pip install memory-profiler
# Thêm @profile decorator

# @profile
# def memory_heavy():
#     data = [i for i in range(1000000)]  # Tạo list lớn
#     return sum(data)
#
# Chạy: python -m memory_profiler script.py
# Output:
# Line #  Mem usage  Increment  Line Contents
# ===========================================
#      3   45.2 MiB   45.2 MiB   data = [i for i in range(1000000)]

# === tracemalloc - built-in memory tracer ===
import tracemalloc

tracemalloc.start()  # Bắt đầu trace

# ... code cần đo ...
data = [i ** 2 for i in range(100000)]
snapshot = tracemalloc.take_snapshot()  # Chụp snapshot

# Top 5 lines consuming most memory
top_stats = snapshot.statistics('lineno')
print("Top 5 memory allocations:")
for stat in top_stats[:5]:
    print(stat)
# Output:
# .../script.py:6: size=5.7 MiB, count=100000

# Compare snapshots
snapshot1 = tracemalloc.take_snapshot()
data2 = [i ** 3 for i in range(100000)]
snapshot2 = tracemalloc.take_snapshot()

top_diff = snapshot2.compare_to(snapshot1, 'lineno')
for stat in top_diff[:3]:
    print(stat)
# Output:
# .../script.py:7: +3.8 MiB (size increase)
```

### 20.5. Documentation & Publishing

```python
# === Sphinx - Professional documentation generator ===
# pip install sphinx sphinx-rtd-theme

# Tạo project:
# sphinx-quickstart docs/  # Tạo cấu trúc docs
#   - Project name: My Package
#   - Author: Your Name
#   - Release: 1.0.0

# Cấu trúc:
# docs/
# ├── Makefile
# ├── conf.py          # Configuration
# ├── index.rst        # Main page
# ├── api.rst          # API docs
# └── _build/          # Generated HTML

# conf.py configuration:
# import os
# import sphinx_rtd_theme
# extensions = [
#     'sphinx.ext.autodoc',    # Auto-generate from docstrings
#     'sphinx.ext.napoleon',   # Google/NumPy docstring support
#     'sphinx.ext.viewcode',   # Show source code links
# ]
# html_theme = 'sphinx_rtd_theme'

# Build:
# cd docs && make html
# Kết quả trong docs/_build/html/

# === MkDocs - Simple documentation site ===
# pip install mkdocs mkdocs-material

# Tạo project:
# mkdocs new myproject
# cd myproject

# mkdocs.yml:
# site_name: My Package
# theme:
#   name: material
# nav:
#   - Home: index.md
#   - API: api.md

# Chạy:
# mkdocs serve       # Development server
# mkdocs build       # Build to site/

# === pdoc - Simple doc generator ===
# pip install pdoc

# Generate docs:
# pdoc mymodule --output-dir docs/
# Output: docs/mymodule.html

# Serve:
# pdoc --port 8000 mymodule

# === PyPI Publishing ===
# pip install build twine

# 1. Build package:
# python -m build
# Output: dist/mypackage-1.0.0.tar.gz, dist/mypackage-1.0.0-*.whl

# 2. Upload to PyPI:
# twine upload dist/*
# Hoặc test PyPI:
# twine upload --repository testpypi dist/*

# === Version management với setuptools-scm ===
# pip install setuptools-scm
# Thêm vào setup.py:
# setup(
#     use_scm_version=True,
#     setup_requires=['setuptools-scm'],
# )
```

### 20.6. Runtime & Environment

```bash
# === pyenv - Quản lý nhiều phiên bản Python ===
# macOS: brew install pyenv
# Linux: curl https://pyenv.run | bash

# Cài Python mới:
pyenv install 3.11.0   # Cài Python 3.11.0
pyenv install 3.12.0   # Cài Python 3.12.0

# Chọn phiên bản:
pyenv global 3.11.0     # Global (tất cả projects)
pyenv local 3.11.0     # Local (project hiện tại, tạo .python-version)
pyenv shell 3.11.0     # Shell (session hiện tại)

# Kiểm tra:
python --version        # Output: Python 3.11.0
pyenv versions         # List tất cả phiên bản đã cài

# === Python Implementations ===
# CPython - Reference implementation (mặc định)
# PyPy - JIT compiler, nhanh hơn cho một số workloads
# Jython - Chạy trên JVM
# IronPython - Chạy trên .NET
# MicroPython - Cho embedded systems

# === Docker ===
# python:3.11-slim - Image nhẹ
# python:3.11-alpine - Image nhẹ nhất (nhưng cần compiler)

# Dockerfile example:
# FROM python:3.11-slim
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# CMD ["python", "main.py"]

# === pipenv - Dependency management ===
# pip install pipenv
pipenv install requests    # Cài package vào Pipfile
pipenv install --dev pytest  # Dev dependency
pipenv shell               # Activate virtualenv
pipenv run python main.py  # Chạy command trong env

# === conda - Scientific Python distribution ===
# conda install numpy pandas scikit-learn
# conda create -n myenv python=3.11
# conda activate myenv

# === Python Implementations (continued) ===
# PyPy - JIT compiler, nhanh hơn cho một số workloads
# Jython - Python on JVM
# IronPython - Python on .NET
# MicroPython - Cho embedded devices

# === REPL ===
python -i           # Interactive mode - chạy Python interactive
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
