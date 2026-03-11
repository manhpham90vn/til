# C++ Syntax Reference

## Mục Lục

0. [Phân Loại Ngôn Ngữ](#0-phân-loại-ngôn-ngữ)
1. [Tầng 1: Syntax & Semantics](#tầng-1-syntax--semantics)
   - [1.1 Khai Báo Biến](#11-khai-báo-biến)
   - [1.2 Khai Báo Hàm](#12-khai-báo-hàm)
   - [1.3 Vòng Lặp](#13-vòng-lặp)
   - [1.4 Điều Kiện](#14-điều-kiện)
2. [Tầng 2: Type System](#tầng-2-type-system)
   - [2.1 Kiểu Dữ Liệu Cơ Bản](#21-kiểu-dữ-liệu-cơ-bản)
   - [2.2 Enum](#22-enum)
   - [2.3 Nullable Types](#23-nullable-types)
   - [2.4 Null Safety](#24-null-safety)
   - [2.5 Templates/Generics](#25-templatesgenerics)
   - [2.6 Collection Operations](#26-collection-operations)
   - [2.7 String Operations](#27-string-operations)
3. [Tầng 3: OOP & Type Relationships](#tầng-3-oop--type-relationships)
   - [3.1 Class & Object](#31-class--object)
   - [3.2 Kế Thừa & Đa Hình](#32-kế-thừa--đa-hình)
   - [3.3 Interface/Abstract Class](#33-interfaceabstract-class)
   - [3.4 Visibility](#34-visibility)
4. [Tầng 4: Memory Model](#tầng-4-memory-model)
   - [4.1 Smart Pointers](#41-smart-pointers)
   - [4.2 RAII](#42-raii)
   - [4.3 Move Semantics](#43-move-semantics)
5. [Tầng 5: Concurrency Model](#tầng-5-concurrency-model)
   - [5.1 Thread](#51-thread)
   - [5.2 Async/Future](#52-asyncfuture)
   - [5.3 Mutex & Lock](#53-mutex--lock)
6. [Tầng 6: Paradigm](#tầng-6-paradigm)
   - [6.1 Functional Programming](#61-functional-programming)
   - [6.2 Lambda Expressions](#62-lambda-expressions)
7. [Tầng 7: Error Handling](#tầng-7-error-handling)
   - [7.1 Exception](#71-exception)
   - [7.2 Error Codes](#72-error-codes)
8. [Tầng 8: Module & Organization](#tầng-8-module--organization)
   - [8.1 Include/Import](#81-includeimport)
   - [8.2 Namespace](#82-namespace)
   - [8.3 Header Files](#83-header-files)
9. [Tầng 9: I/O & Networking](#tầng-9-io--networking)
   - [9.1 HTTP & Networking](#91-http--networking)
   - [9.2 File I/O](#92-file-io)
   - [9.3 Stream I/O](#93-stream-io)
10. [Tầng 10: Data & Serialization](#tầng-10-data--serialization)
    - [10.1 JSON & Serialization](#101-json--serialization)
    - [10.2 Date & Time](#102-date--time)
    - [10.3 Regular Expression](#103-regular-expression)
11. [Tầng 11: Development Practices](#tầng-11-development-practices)
    - [11.1 Testing](#111-testing)
    - [11.2 Logging](#112-logging)
    - [11.3 Configuration](#113-configuration)
    - [11.4 Build & Package Management](#114-build--package-management)
12. [Tầng 12: Advanced Concepts](#tầng-12-advanced-concepts)
    - [12.1 Templates](#121-templates)
    - [12.2 Concepts (C++20)](#122-concepts-c20)
    - [12.3 Variadic Templates](#123-variadic-templates)
13. [Tầng 13: Memory Layout](#tầng-13-memory-layout)
    - [13.1 Struct Layout](#131-struct-layout)
    - [13.2 Memory Alignment](#132-memory-alignment)
    - [13.3 Padding](#133-padding)
14. [Tầng 14: Compilation Model](#tầng-14-compilation-model)
    - [14.1 Compilation](#141-compilation)
    - [14.2 Templates Instantiation](#142-templates-instantiation)
    - [14.3 Inline](#143-inline)
15. [Tầng 15: Linking Model](#tầng-15-linking-model)
    - [15.1 Static Linking](#151-static-linking)
    - [15.2 Dynamic Linking](#152-dynamic-linking)
16. [Tầng 16: Runtime](#tầng-16-runtime)
    - [16.1 Stack & Heap](#161-stack--heap)
    - [16.2 Virtual Destructor](#162-virtual-destructor)
    - [16.3 RTTI](#163-rtti)
17. [Tầng 17: Language Design Patterns](#tầng-17-language-design-patterns)
    - [17.1 RAII](#171-raii)
    - [17.2 Rule of Zero/Three/Five](#172-rule-of-zerothreefive)
    - [17.3 CRTP](#173-crtp)
18. [Tầng 18: Standard Library](#tầng-18-standard-library)
    - [18.1 Collections](#181-collections)
    - [18.2 Utilities](#182-utilities)
    - [18.3 I/O & System](#183-io--system)
19. [Tầng 19: Ecosystem](#tầng-19-ecosystem)
    - [19.1 Frameworks](#191-frameworks)
    - [19.2 Libraries](#192-libraries)
    - [19.3 Build Systems](#193-build-systems)
20. [Tầng 20: Toolchain](#tầng-20-toolchain)
    - [20.1 Compiler](#201-compiler)
    - [20.2 Debugging](#202-debugging)
    - [20.3 Code Quality](#203-code-quality)

---

## 0. Phân Loại Ngôn Ngữ

### Chạy File C++

```bash
# Compile và chạy (C++11 trở lên)
g++ -std=c++17 -o main main.cpp && ./main

# Với CMake
mkdir build && cd build
cmake ..
make
./my_project

# Với make
g++ -std=c++20 -O2 -Wall -Wextra main.cpp -o main

# Các cờ compiler phổ biến
# -std=c++11/14/17/20/23  : Tiêu chuẩn C++
# -O2/-O3                 : Tối ưu hóa
# -Wall -Wextra           : Cảnh báo đầy đủ
# -g                      : Debug symbols
# -pthread                : Thread support
```

### Đặc điểm C++

- **Typing**: Static, Strong typing với type inference (auto, decltype)
- **Paradigm**: Multi-paradigm (OOP, Generic, Functional, Procedural)
- **Execution**: Compiled (AOT), Native code
- **Memory Safety**: Manual với RAII, Smart pointers (không GC)
- **Use Cases**: Systems programming, Game development, Embedded, High-performance applications, GUI applications

---

## 1. Tầng 1: Syntax & Semantics

### 1.1. Khai Báo Biến (Variable Declaration)

#### Mutable - Biến thường

```cpp
// Khai báo với type inference (C++11+)
auto x = 10;                    // int
auto name = "C++";              // const char*
auto is_active = true;          // bool
auto prices = std::vector<double>{1.5, 2.0, 3.5};

// Explicit type
int x = 10;
std::string name = "C++";
bool is_active = true;
std::vector<double> prices = {1.5, 2.0, 3.5};

// Mutable
int counter = 0;
counter += 1;

// Reference
int a = 10;
int& ref = a;
ref = 20;  // a = 20
```

#### Immutable - Hằng số

```cpp
// const (compile-time)
const int MAX_SIZE = 100;
const double PI = 3.14159;

// constexpr (C++11+) - compile-time evaluation
constexpr int MAX_SIZE = 100;
constexpr double square(double x) { return x * x; }

// consteval (C++20+) - compile-time execution bắt buộc
consteval int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

// inline const (C++17+)
inline const int BUFFER_SIZE = 1024;
```

#### Global Variable

```cpp
// Global variable
int global_counter = 0;

void increment() {
    global_counter++;
}

// Static global (file scope)
static int file_scope_counter = 0;

// Inline variable (C++17+) - có thể định nghĩa trong header
inline int global_id = 42;
```

---

### 1.2. Khai Báo Hàm (Function Declaration)

#### Function cơ bản

```cpp
// Function không có return
void greet() {
    std::cout << "Hello!" << std::endl;
}

// Function có return
int add(int a, int b) {
    return a + b;
}

// Function với reference return
int& get_counter() {
    static int counter = 0;
    return counter;
}

// Trailing return type (C++11+)
auto add_auto(int a, int b) -> int {
    return a + b;
}

// Function với noexcept (C++11+)
int divide(int a, int b) noexcept {
    return a / b;
}
```

#### Parameters

```cpp
// Pass by value
void set_value(int x) {
    x = 10;  // Chỉ thay đổi bản sao
}

// Pass by reference
void set_value(int& x) {
    x = 10;  // Thay đổi giá trị gốc
}

// Pass by const reference (không copy, không sửa)
void print(const std::string& str) {
    std::cout << str << std::endl;
}

// Pass by pointer
void set_pointer(int* ptr) {
    if (ptr) {
        *ptr = 10;
    }
}

// Pass by rvalue reference (C++11+)
void append(std::string&& str) {
    // Di chuyển string thay vì copy
}

// Default parameters
void configure(std::string name, int port = 8080, bool ssl = false) {
    // ...
}

// Variadic parameters (C-style, tránh dùng)
void print_values(const char* format, ...) {
    va_list args;
    va_start(args, format);
    // ...
    va_end(args);
}
```

#### Overloading

```cpp
// Function overloading
int max(int a, int b) {
    return (a > b) ? a : b;
}

double max(double a, double b) {
    return (a > b) ? a : b;
}

template<typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}
```

---

### 1.3. Vòng Lặp (Loops)

#### For loop

```cpp
// C-style for
for (int i = 0; i < 10; i++) {
    std::cout << i << " ";
}

// Range-based for (C++11+)
std::vector<int> nums = {1, 2, 3, 4, 5};
for (int n : nums) {
    std::cout << n << " ";
}

// Với auto
for (const auto& n : nums) {
    std::cout << n << " ";
}

// Với initializer (C++20+)
for (std::vector<int> nums = {1, 2, 3}; const auto& n : nums) {
    // ...
}
```

#### While loop

```cpp
int count = 0;
while (count < 5) {
    std::cout << count++;
}

// Do-while
do {
    std::cout << count--;
} while (count > 0);
```

#### Iterator-based

```cpp
std::vector<int> nums = {1, 2, 3, 4, 5};

// Iterator
for (auto it = nums.begin(); it != nums.end(); ++it) {
    std::cout << *it << " ";
}

// Reverse iterator
for (auto it = nums.rbegin(); it != nums.rend(); ++it) {
    std::cout << *it << " ";
}
```

---

### 1.4. Điều Kiện (Conditionals)

#### If-else

```cpp
int x = 10;

if (x > 0) {
    std::cout << "Positive";
} else if (x < 0) {
    std::cout << "Negative";
} else {
    std::cout << "Zero";
}

// If với initializer (C++17+)
if (auto result = get_value(); result > 0) {
    // Sử dụng result
}
```

#### Switch-case

```cpp
int day = 3;
switch (day) {
    case 1:
        std::cout << "Monday";
        break;
    case 2:
        std::cout << "Tuesday";
        break;
    case 3:
        std::cout << "Wednesday";
        break;
    default:
        std::cout << "Unknown";
}

// Switch expression (C++17+ với std::string, C++20+ tổng quát)
std::string day_name = [day]() {
    switch (day) {
        case 1: return "Monday";
        case 2: return "Tuesday";
        default: return "Unknown";
    }
}();

// Switch expression (C++23)
std::string day_name = std::to_array({
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
}).at(day - 1);
```

#### Ternary operator

```cpp
int x = 10;
std::string result = (x > 0) ? "Positive" : "Non-positive";
```

---

## 2. Tầng 2: Type System

### 2.1. Kiểu Dữ Liệu Cơ Bản (Primitive Types)

```cpp
// Integer
int i = 42;
long long ll = 9223372036854775807;
short s = 32767;
unsigned int ui = 42;

// Floating point
float f = 3.14f;
double d = 3.14159;
long double ld = 3.14159L;

// Character
char c = 'A';
wchar_t wc = L'A';      // Wide character
char8_t c8 = 'A';       // C++20: UTF-8
char16_t c16 = u'A';    // C++11: UTF-16
char32_t c32 = U'A';    // C++11: UTF-32

// Boolean
bool b = true;

// Void
void* ptr = nullptr;

// Pointer
int* p = nullptr;
int** pp = nullptr;

// Reference
int& ref = i;
```

#### Type Inference

```cpp
// auto (C++11+)
auto x = 42;                    // int
auto y = 3.14;                  // double
auto z = std::vector<int>{};    // std::vector<int>

// decltype (C++11+)
int x = 5;
decltype(x) y = 10;             // int

decltype(auto) get_ref() {
    static int x = 5;
    return x;                    // Returns int&
}
```

#### Size & Limits

```cpp
#include <limits>
#include <cstdint>

std::cout << sizeof(int) << " bytes" << std::endl;
std::cout << std::numeric_limits<int>::max() << std::endl;
std::cout << std::numeric_limits<double>::epsilon() << std::endl;

int64_t large_number = 9223372036854775807LL;
```

---

### 2.2. Enum

```cpp
// C-style enum
enum Color {
    RED,
    GREEN,
    BLUE
};

Color c = RED;

// Enum với kiểu cụ thể (C++11+)
enum class Priority : int {
    LOW = 1,
    MEDIUM = 2,
    HIGH = 3
};

Priority p = Priority::HIGH;
int value = static_cast<int>(p);  // 3

// Enum với underlying type (C++11+)
enum class Status : unsigned char {
    OK = 0,
    ERROR = 1,
    PENDING = 2
};

// Enum with methods (C++11+)
enum class Result {
    Success,
    Failure
};

constexpr const char* to_string(Result r) {
    switch (r) {
        case Result::Success: return "Success";
        case Result::Failure: return "Failure";
    }
}
```

---

### 2.3. Nullable Types

```cpp
// Pointer có thể null
int* ptr = nullptr;

// std::optional (C++17+)
#include <optional>

std::optional<int> find_value(const std::vector<int>& vec, int target) {
    for (const auto& val : vec) {
        if (val == target) return val;
    }
    return std::nullopt;
}

// Sử dụng optional
std::optional<int> result = find_value({1, 2, 3}, 2);
if (result) {
    std::cout << *result << std::endl;
}

// Hoặc dùng value_or
int value = result.value_or(-1);
```

---

### 2.4. Null Safety

```cpp
// C++ không có built-in null safety như Kotlin/Rust
// Phải dùng thủ công

// Kiểm tra pointer trước khi sử dụng
int* ptr = get_pointer();
if (ptr != nullptr) {
    // Sử dụng ptr
}

// Dùng std::optional thay vì null pointer (C++17+)
std::optional<std::string> get_name() {
    // Return nullopt nếu không có name
}

// dùng std::unique_ptr để quản lý memory
#include <memory>

std::unique_ptr<MyClass> obj = std::make_unique<MyClass>();
// Tự động giải phóng khi ra khỏi scope

// Dùng references khi không muốn null
void process(const MyClass& obj);  // Không bao giờ null
```

---

### 2.5. Templates/Generics

```cpp
// Function template
template<typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

// Template với nhiều type
template<typename T, typename U>
auto add(T a, U b) -> decltype(a + b) {
    return a + b;
}

// Class template
template<typename T>
class Box {
private:
    T value;
public:
    Box(T v) : value(v) {}
    T get() const { return value; }
};

// Template với default type
template<typename T = int>
class Container {
    std::vector<T> data;
public:
    void add(T item) { data.push_back(item); }
};

// Template parameter với constraint (C++20+)
template<std::ranges::range R>
void process_range(R&& r) {
    // ...
}

// Template với non-type parameter (C++17+)
template<std::size_t N>
class FixedArray {
    int data[N];
public:
    static constexpr std::size_t size() { return N; }
};

FixedArray<100> arr;  // Array có 100 phần tử
```

---

### 2.6. Collection Operations

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

std::vector<int> nums = {5, 2, 8, 1, 9};

// Map/Transform
std::vector<int> doubled;
std::transform(nums.begin(), nums.end(), std::back_inserter(doubled),
    [](int x) { return x * 2; });

// Hoặc dùng ranges (C++20+)
#include <ranges>
auto doubled = nums | std::views::transform([](int x) { return x * 2; });

// Filter
std::vector<int> evens;
std::copy_if(nums.begin(), nums.end(), std::back_inserter(evens),
    [](int x) { return x % 2 == 0; });

// Filter với ranges (C++20+)
auto evens = nums | std::views::filter([](int x) { return x % 2 == 0; });

// Reduce/Fold
int sum = std::accumulate(nums.begin(), nums.end(), 0);
int product = std::accumulate(nums.begin(), nums.end(), 1,
    [](int acc, int x) { return acc * x; });

// Sort
std::sort(nums.begin(), nums.end());
std::sort(nums.begin(), nums.end(), std::greater<int>());  // Giảm dần
std::sort(nums.begin(), nums.end(), [](int a, int b) {
    return a > b;
});

// Find
auto it = std::find(nums.begin(), nums.end(), 5);
if (it != nums.end()) {
    // Tìm thấy
}

// Any/All/None
bool has_even = std::any_of(nums.begin(), nums.end(),
    [](int x) { return x % 2 == 0; });
bool all_positive = std::all_of(nums.begin(), nums.end(),
    [](int x) { return x > 0; });

// Remove-if (thực tế di chuyển các phần tử)
nums.erase(std::remove_if(nums.begin(), nums.end(),
    [](int x) { return x < 5; }), nums.end());

// Chaining với ranges (C++20+)
auto result = nums
    | std::views::filter([](int x) { return x > 0; })
    | std::views::transform([](int x) { return x * 2; })
    | std::views::take(5);
```

---

### 2.7. String Operations

```cpp
#include <string>
#include <sstream>

// Khởi tạo
std::string s1 = "Hello";
std::string s2("World");
std::string s3 = std::string("C++") + " is powerful";

// Concatenation
std::string full = s1 + " " + s2;
full += "!";

// Interpolation (C++26 - chưa widely available)
std::string msg = std::format("Hello {}!", name);

// Format với std::format (C++20+)
#include <format>
std::string msg = std::format("Name: {}, Age: {}", name, age);

// String to number
int i = std::stoi("42");
double d = std::stod("3.14");
long long ll = std::stoll("9223372036854775807");

// Number to string
std::string si = std::to_string(42);
std::string sd = std::to_string(3.14);

// String comparison
if (s1 == s2) { /* equal */ }
if (s1 != s2) { /* not equal */ }
if (s1 < s2) { /* lexicographical */ }

// Substring
std::string sub = s1.substr(0, 3);  // "Hel"

// Find
size_t pos = s1.find("lo");         // 3
size_t pos_r = s1.rfind("l");       // 3 (tìm từ cuối)

// Replace
std::string s = "Hello World";
s.replace(6, 5, "C++");             // "Hello C++"

// Split (C++23 hoặc dùng stringstream)
#include <sstream>
std::istringstream iss("one,two,three");
std::string token;
while (std::getline(iss, token, ',')) {
    // process token
}

// Trim
#include <algorithm>
// C++20: std::string_view::trim
std::string_view sv = "   hello   ";
sv = sv.trim();  // "hello"

// Case conversion
std::string lower = "HELLO";
std::transform(lower.begin(), lower.end(), lower.begin(), ::tolower);
```

---

## 3. Tầng 3: OOP & Type Relationships

### 3.1. Class & Object

```cpp
class Rectangle {
private:
    double width_;
    double height_;

public:
    // Constructor
    Rectangle() : width_(0), height_(0) {}
    Rectangle(double w, double h) : width_(w), height_(h) {}

    // Copy constructor
    Rectangle(const Rectangle& other)
        : width_(other.width_), height_(other.height_) {}

    // Move constructor (C++11+)
    Rectangle(Rectangle&& other) noexcept
        : width_(std::move(other.width_)),
          height_(std::move(other.height_)) {}

    // Destructor
    ~Rectangle() = default;

    // Copy assignment
    Rectangle& operator=(const Rectangle& other) {
        if (this != &other) {
            width_ = other.width_;
            height_ = other.height_;
        }
        return *this;
    }

    // Move assignment (C++11+)
    Rectangle& operator=(Rectangle&& other) noexcept {
        if (this != &other) {
            width_ = std::move(other.width_);
            height_ = std::move(other.height_);
        }
        return *this;
    }

    // Getter/Setter
    double width() const { return width_; }
    double height() const { return height_; }
    void set_width(double w) { width_ = w; }
    void set_height(double h) { height_ = h; }

    // Method
    double area() const { return width_ * height_; }

    // Const method
    void print() const {
        std::cout << "Rectangle: " << width_ << "x" << height_ << std::endl;
    }
};

// Sử dụng
Rectangle r1(10, 5);
Rectangle r2 = r1;           // Copy
Rectangle r3 = std::move(r1);  // Move

std::cout << r2.area() << std::endl;
```

#### Struct

```cpp
// Struct (mặc định public)
struct Point {
    double x = 0;
    double y = 0;

    // Constructor
    Point() = default;
    Point(double x, double y) : x(x), y(y) {}

    // Method
    double distance() const { return std::sqrt(x*x + y*y); }
};

// Aggregate initialization (C++17+)
Point p1{1.0, 2.0};
Point p2 = {3.0, 4.0};
```

#### Singleton

```cpp
class Singleton {
private:
    static std::unique_ptr<Singleton> instance_;
    int value_;

    Singleton() : value_(42) {}

public:
    // Delete copy/move
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;

    static Singleton& get_instance() {
        if (!instance_) {
            instance_ = std::unique_ptr<Singleton>(new Singleton());
        }
        return *instance_;
    }

    int get_value() const { return value_; }
};

std::unique_ptr<Singleton> Singleton::instance_ = nullptr;
```

---

### 3.2. Kế Thừa & Đa Hình (Inheritance & Polymorphism)

```cpp
// Base class
class Animal {
protected:
    std::string name_;

public:
    Animal(const std::string& name) : name_(name) {}

    // Virtual method cho polymorphism
    virtual void speak() const {
        std::cout << "..." << std::endl;
    }

    // Virtual destructor (quan trọng!)
    virtual ~Animal() = default;

    // Pure virtual - Abstract method
    virtual std::string get_species() const = 0;
};

// Derived class
class Dog : public Animal {
public:
    Dog(const std::string& name) : Animal(name) {}

    void speak() const override {
        std::cout << name_ << " says: Woof!" << std::endl;
    }

    std::string get_species() const override {
        return "Canis familiaris";
    }
};

class Cat : public Animal {
public:
    Cat(const std::string& name) : Animal(name) {}

    void speak() const override {
        std::cout << name_ << " says: Meow!" << std::endl;
    }

    std::string get_species() const override {
        return "Felis catus";
    }
};

// Sử dụng polymorphism
void make_speak(Animal& animal) {
    animal.speak();  // Gọi method đúng type
}

Animal* animal = new Dog("Buddy");
animal->speak();  // Output: Buddy says: Woof!
delete animal;

// Smart pointer với polymorphism
#include <memory>
std::unique_ptr<Animal> animal2 = std::make_unique<Cat>("Whiskers");
animal2->speak();  // Output: Whiskers says: Meow!
```

#### Multiple Inheritance

```cpp
class Printable {
public:
    virtual void print() const = 0;
    virtual ~Printable() = default;
};

class Logger {
public:
    virtual void log(const std::string& msg) const = 0;
    virtual ~Logger() = default;
};

class FileHandler : public Printable, public Logger {
public:
    void print() const override {
        std::cout << "FileHandler" << std::endl;
    }

    void log(const std::string& msg) const override {
        std::cout << "[LOG] " << msg << std::endl;
    }
};

// Virtual inheritance (tránh diamond problem)
class Base {
public:
    virtual void process() = 0;
    virtual ~Base() = default;
};

class Derived1 : virtual public Base {
public:
    void process() override { std::cout << "Derived1" << std::endl; }
};

class Derived2 : virtual public Base {
public:
    void process() override { std::cout << "Derived2" << std::endl; }
};

class MultiDerived : public Derived1, public Derived2 {
    // Chỉ có một Base instance
};
```

---

### 3.3. Interface/Abstract Class

```cpp
// Interface (pure abstract class)
class Drawable {
public:
    virtual void draw() const = 0;
    virtual void resize(double factor) = 0;
    virtual ~Drawable() = default;
};

class Circle : public Drawable {
private:
    double radius_;

public:
    Circle(double r) : radius_(r) {}

    void draw() const override {
        std::cout << "Drawing circle with radius " << radius_ << std::endl;
    }

    void resize(double factor) override {
        radius_ *= factor;
    }
};

// Abstract class (có cả implementation)
class Shape {
protected:
    std::string color_ = "white";

public:
    virtual double area() const = 0;
    virtual void draw() const = 0;
    virtual ~Shape() = default;

    // Có thể có implementation
    void set_color(const std::string& color) {
        color_ = color;
    }

    std::string get_color() const {
        return color_;
    }
};
```

---

### 3.4. Visibility

```cpp
class MyClass {
private:           // Chỉ class này
    int private_data_;

protected:         // Class này và derived class
    int protected_data_;

public:            // Ai cũng truy cập được
    int public_data_;

public:            // Có thể khai báo nhiều lần
    void public_method();

private:
    void private_method();
};

// Friend class/function
class FriendDemo {
    friend class FriendClass;
    friend void friend_function(FriendDemo&);

private:
    int secret_ = 42;
};

class FriendClass {
public:
    void access(FriendDemo& obj) {
        // Có thể truy cập private
        obj.secret_ = 100;
    }
};
```

---

## 4. Tầng 4: Memory Model

### 4.1. Smart Pointers

```cpp
#include <memory>

// std::unique_ptr - single owner
std::unique_ptr<int> uptr = std::make_unique<int>(42);
std::unique_ptr<MyClass> obj = std::make_unique<MyClass>(args);

// Custom deleter
auto deleter = [](FILE* f) { fclose(f); };
std::unique_ptr<FILE, decltype(deleter)> file(fopen("a.txt", "r"), deleter);

// Release ownership
int* raw = uptr.release();
delete raw;

// std::shared_ptr - shared ownership
std::shared_ptr<int> sptr1 = std::make_shared<int>(42);
std::shared_ptr<int> sptr2 = sptr1;  // Reference count = 2
std::weak_ptr<int> wptr = sptr1;    // Weak reference

// Check weak_ptr
if (auto locked = wptr.lock()) {
    // Sử dụng locked
}

// Reference count
std::cout << sptr1.use_count() << std::endl;  // 2

// Custom deleter với shared_ptr
std::shared_ptr<FILE> file = std::shared_ptr<FILE>(
    fopen("a.txt", "r"),
    [](FILE* f) { fclose(f); }
);

// std::weak_ptr - non-owning reference
std::weak_ptr<int> wptr2;
{
    std::shared_ptr<int> sptr = std::make_shared<int>(100);
    wptr2 = sptr;
    // Sptr bị destroy nhưng wptr2 vẫn tồn tại
}
// Kiểm tra còn valid
if (!wptr2.expired()) {
    auto sp = wptr2.lock();
    // Sử dụng sp
}
```

---

### 4.2. RAII (Resource Acquisition Is Initialization)

```cpp
// RAII - Resource được acquire trong constructor
// Resource được release trong destructor

class FileGuard {
private:
    std::string filename_;
    std::fstream file_;

public:
    FileGuard(const std::string& name)
        : filename_(name) {
        file_.open(name, std::ios::in | std::ios::out);
        if (!file_.is_open()) {
            throw std::runtime_error("Cannot open file");
        }
    }

    ~FileGuard() {
        if (file_.is_open()) {
            file_.close();
        }
    }

    // Copy/Move - disable hoặc implement đúng
    FileGuard(const FileGuard&) = delete;
    FileGuard& operator=(const FileGuard&) = delete;
    FileGuard(FileGuard&&) = default;
    FileGuard& operator=(FileGuard&&) = default;

    void write(const std::string& data) {
        file_ << data;
    }
};

// Sử dụng - tự động đóng file khi ra khỏi scope
void process() {
    FileGuard guard("data.txt");
    guard.write("Hello");
    // File tự động đóng khi guard bị destroy
}
```

---

### 4.3. Move Semantics

```cpp
#include <utility>

class Buffer {
private:
    int* data_;
    size_t size_;

public:
    Buffer(size_t size) : size_(size) {
        data_ = new int[size];
    }

    // Copy constructor
    Buffer(const Buffer& other) : size_(other.size_) {
        data_ = new int[size_];
        std::copy(other.data_, other.data_ + size_, data_);
    }

    // Move constructor (C++11+)
    Buffer(Buffer&& other) noexcept
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
    }

    // Copy assignment
    Buffer& operator=(const Buffer& other) {
        if (this != &other) {
            delete[] data_;
            size_ = other.size_;
            data_ = new int[size_];
            std::copy(other.data_, other.data_ + size_, data_);
        }
        return *this;
    }

    // Move assignment (C++11+)
    Buffer& operator=(Buffer&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            size_ = other.size_;
            other.data_ = nullptr;
            other.size_ = 0;
        }
        return *this;
    }

    ~Buffer() {
        delete[] data_;
    }
};

// std::move usage
Buffer b1(100);
Buffer b2 = std::move(b1);  // Move, b1 không còn valid

// std::swap
std::swap(a, b);  // Efficient với move semantics
```

---

## 5. Tầng 5: Concurrency Model

### 5.1. Thread

```cpp
#include <thread>
#include <functional>

// Thread cơ bản
void worker(int id) {
    std::cout << "Worker " << id << " running" << std::endl;
}

std::thread t1(worker, 1);
std::thread t2(worker, 2);
t1.join();
t2.join();

// Thread với lambda
int result = 0;
std::thread t([&result]() {
    result = calculate();
});
t.join();

// Thread với member function
class Worker {
public:
    void run() { /* ... */ }
};

Worker w;
std::thread t(&Worker::run, &w);

// Detached thread
std::thread daemon([]() {
    // Background work
    std::this_thread::sleep_for(std::chrono::seconds(1));
});
daemon.detach();

// Thread ID
std::thread::id id = std::this_thread::get_id();

// Hardware concurrency
unsigned int cores = std::thread::hardware_concurrency();
```

---

### 5.2. Async/Future

```cpp
#include <future>
#include <async>

// std::async
std::future<int> fut = std::async([]() {
    return compute();
});

int result = fut.get();  // Blocking cho đến khi có kết quả

// Async với std::launch
std::future<int> fut2 = std::async(std::launch::async, []() {
    return heavy_computation();
});

// std::promise - communication channel
void async_worker(std::promise<int>& prom) {
    try {
        int result = do_work();
        prom.set_value(result);
    } catch (...) {
        prom.set_exception(std::current_exception());
    }
}

std::promise<int> prom;
std::future<int> fut = prom.get_future();
std::thread t(async_worker, std::ref(prom));
int result = fut.get();
t.join();

// std::packaged_task
std::packaged_task<int(int, int)> task([](int a, int b) {
    return a + b;
});
std::future<int> fut3 = task.get_future();
task(10, 20);
std::cout << fut3.get() << std::endl;
```

---

### 5.3. Mutex & Lock

```cpp
#include <mutex>
#include <shared_mutex>

// std::mutex
std::mutex mtx;
mtx.lock();
try {
    // Critical section
} catch (...) {
    mtx.unlock();
    throw;
}
mtx.unlock();

// std::lock_guard - RAII lock
{
    std::lock_guard<std::mutex> lock(mtx);
    // Tự động unlock khi ra khỏi scope
}

// std::unique_lock - flexible lock
{
    std::unique_lock<std::mutex> lock(mtx);
    if (lock.owns_lock()) {
        // Do work
    }
    lock.unlock();
    // Do non-critical work
    lock.lock();
}

// std::shared_mutex (C++17+) - Reader-Writer lock
std::shared_mutex rw_mtx;

void reader() {
    std::shared_lock lock(rw_mtx);  // Multiple readers allowed
    // Read data
}

void writer() {
    std::unique_lock lock(rw_mtx);  // Exclusive access
    // Write data
}

// std::scoped_lock (C++17+) - Multiple mutexes
std::mutex m1, m2;
{
    std::scoped_lock lock(m1, m2);
    // Lock cả hai mutex an toàn
}
```

---

## 6. Tầng 6: Paradigm

### 6.1. Functional Programming

```cpp
#include <functional>

// std::function - function as value
std::function<int(int, int)> add = [](int a, int b) {
    return a + b;
};

// Pure function
int pure_add(int a, int b) {
    return a + b;  // Không có side effect
}

// Immutability
const int MAX_SIZE = 100;  // Constexpr

// Function composition (C++20 ranges)
#include <ranges>
auto compose = std::views::transform([](int x) { return x * 2; })
             | std::views::filter([](int x) { return x > 0; });

// Partial application (C++20)
std::function<int(int)> multiply_by_5 = std::bind(
    std::multiplies<int>(), std::placeholders::_1, 5
);

// Currying với lambda
auto curried_add = [](int a) {
    return [a](int b) { return a + b; };
};

auto add5 = curried_add(5);
int result = add5(3);  // 8
```

---

### 6.2. Lambda Expressions

```cpp
#include <algorithm>

// Lambda cơ bản
auto add = [](int a, int b] { return a + b; };
int result = add(1, 2);

// Lambda với capture
int multiplier = 10;
auto multiply = [multiplier](int x) { return x * multiplier; };

// Capture by reference
auto increment = [&multiplier]() { multiplier++; };

// Capture by move (C++14+)
auto ptr = std::make_unique<int>(42);
auto capture_move = [p = std::move(ptr)]() { return *p; };

// Mutable lambda
int counter = 0;
auto count = [counter]() mutable {
    return ++counter;
};

// Generic lambda (C++14+)
auto generic_add = [](auto a, auto b) { return a + b; };

// Lambda với return type
auto get_string = []() -> std::string { return "Hello"; };

// Capture this
class Counter {
    int count_ = 0;
public:
    auto increment() {
        return [this]() { count_++; };
    }
};

// Lambda as parameter
void process(std::vector<int>& v, std::function<bool(int)> pred) {
    std::copy_if(v.begin(), v.end(), v.begin(), pred);
}

// STL algorithms with lambda
std::vector<int> nums = {5, 2, 8, 1, 9};
std::sort(nums.begin(), nums.end(), [](int a, int b) { return a > b; });
```

---

## 7. Tầng 7: Error Handling

### 7.1. Exception

```cpp
#include <stdexcept>

// Throw exception
void divide(int a, int b) {
    if (b == 0) {
        throw std::invalid_argument("Division by zero");
    }
    std::cout << a / b << std::endl;
}

// Try-catch
try {
    divide(10, 0);
} catch (const std::invalid_argument& e) {
    std::cerr << "Error: " << e.what() << std::endl;
} catch (const std::exception& e) {
    std::cerr << "General error: " << e.what() << std::endl;
} catch (...) {
    std::cerr << "Unknown error" << std::endl;
}

// Custom exception
class MyException : public std::exception {
    std::string msg_;
public:
    MyException(const std::string& msg) : msg_(msg) {}

    const char* what() const noexcept override {
        return msg_.c_str();
    }
};

// noexcept function
void safe_function() noexcept {
    // Không throw exception
}

// noexcept with specification
int risky() noexcept(false) {
    // Có thể throw
}

// noexcept operator (C++17+)
constexpr bool is_nothrow = noexcept(int(1));
```

---

### 7.2. Error Codes

```cpp
#include <system_error>

// std::error_code
std::error_code ec = std::make_error_code(std::errc::file_not_found);
if (ec) {
    std::cerr << ec.message() << std::endl;
}

// Return error code
std::expected<int, std::error_code> divide_safe(int a, int b) {
    if (b == 0) {
        return std::unexpected(std::make_error_code(std::errc::invalid_argument));
    }
    return a / b;
}

// std::expected (C++23, có thể dùng std::optional trước C++23)
#include <expected>
std::expected<int, std::string> find_value(int x) {
    if (x < 0) {
        return std::unexpected("Negative value");
    }
    return x * 2;
}

// Using expected
auto result = find_value(10);
if (result) {
    std::cout << *result << std::endl;
} else {
    std::cerr << result.error() << std::endl;
}
```

---

## 8. Tầng 8: Module & Organization

### 8.1. Include/Import

```cpp C
//-style include
#include <iostream>      // System header
#include "my_header.h"   // Local header

// C++20 modules (hiện đại)
import std.core;        // Import standard library module (C++20)
import std.io;          // C++23
import my_module;       // Import custom module

// Module partition (C++20)
export module my_module:part1;  // Partition
export import :part1;           // Re-export partition
```

---

### 8.2. Namespace

```cpp
// Namespace definition
namespace myproject {
    class MyClass { /* ... */ };
    void function() { /* ... */ }
}

// Namespace nested
namespace outer {
    namespace inner {
        void func() { /* ... */ }
    }
}

// Alias
namespace proj = myproject::subproject;

// Anonymous namespace (file scope)
namespace {
    void internal_function() { /* Chỉ available trong file này */ }
}

// using declarations
using std::cout;
using std::endl;

// using directives
using namespace std;  // Tránh dùng trong header

// Nested using
namespace ns {
    using std::string;
}

// inline namespace (C++11+)
namespace lib {
    inline namespace v1 {
        void func() { std::cout << "v1\n"; }
    }
    namespace v2 {
        void func() { std::cout << "v2\n"; }
    }
}
```

---

### 8.3. Header Files

```cpp
// header.h - Header guard
#ifndef HEADER_H
#define HEADER_H

// Include guard truyền thống
// Hoặc dùng #pragma once (supported by most compilers)

// Declaration
class MyClass {
public:
    void method();
    inline void inline_method() { /* ... */ }
    static constexpr int MAX = 100;  // Inline variable
};

#endif

// header.hpp - Template implementation thường để trong .hpp

// Forward declaration
class ForwardDeclared;
void function_accepting(ForwardDeclared* ptr);

// Export module (C++20)
export module mymodule;  // Module interface unit
export {
    void exported_func();
    class ExportedClass;
}
```

---

## 9. Tầng 9: I/O & Networking

### 9.1. HTTP & Networking

```cpp
// C++ không có built-in HTTP client
// Thường dùng thư viện bên ngoài: libcurl, Boost.Beast, cpp-httplib

// libcurl example
#include <curl/curl.h>

size_t write_callback(char* ptr, size_t size, size_t nmemb, void* userdata) {
    std::string* response = static_cast<std::string*>(userdata);
    response->append(ptr, size * nmemb);
    return size * nmemb;
}

void http_get(const std::string& url) {
    CURL* curl = curl_easy_init();
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);

    std::string response;
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

    CURLcode res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);
}

// cpp-httplib (header-only)
#include "httplib.h"

httplib::Client cli("https://api.example.com");
auto res = cli.Get("/endpoint");
if (res && res->status == 200) {
    std::cout << res->body << std::endl;
}
```

---

### 9.2. File I/O

```cpp
#include <fstream>

// Đọc file
std::ifstream file("data.txt");
if (!file.is_open()) {
    throw std::runtime_error("Cannot open file");
}

std::string content;
std::getline(file, content);
file.close();

// Hoặc dùng std::ifstream với string
std::ifstream file("data.txt");
std::string content((std::istreambuf_iterator<char>(file)),
                     std::istreambuf_iterator<char>());

// Ghi file
std::ofstream out("output.txt");
out << "Hello, World!" << std::endl;
out.close();

// Binary I/O
struct Data {
    int id;
    char name[32];
};

Data d = {1, "test"};
std::ofstream out("data.bin", std::ios::binary);
out.write(reinterpret_cast<char*>(&d), sizeof(d));

// File mode
std::fstream file("data.txt",
    std::ios::in | std::ios::out | std::ios::app);

// C++17 filesystem
#include <filesystem>
namespace fs = std::filesystem;

fs::path p = "dir/file.txt";
if (fs::exists(p)) {
    std::cout << fs::file_size(p) << std::endl;
}
fs::create_directory("newdir");
```

---

### 9.3. Stream I/O

```cpp
#include <sstream>
#include <iostream>

// std::istringstream - string to stream
std::string input = "10 20 30";
std::istringstream iss(input);
int num;
while (iss >> num) {
    std::cout << num << " ";
}

// std::ostringstream - stream to string
std::ostringstream oss;
oss << "Value: " << 42 << ", " << 3.14;
std::string result = oss.str();

// std::stringstream - both
std::stringstream ss;
ss << 123 << " " << 4.56;
int a; double b;
ss >> a >> b;

// Formatted output
std::cout << std::setprecision(2) << std::fixed << 3.14159 << std::endl;

// std::format (C++20+)
#include <format>
std::string s = std::format("{} + {} = {}", 1, 2, 3);
```

---

## 10. Tầng 10: Data & Serialization

### 10.1. JSON & Serialization

```cpp
// Thư viện phổ biến: nlohmann/json, rapidjson

// nlohmann/json
#include <nlohmann/json.hpp>
using json = nlohmann::json;

// Tạo JSON
json j;
j["name"] = "John";
j["age"] = 30;
j["is_student"] = false;
j["scores"] = {85, 90, 78};
j["address"] = {
    {"city", "NYC"},
    {"zip", "10001"}
};

// Parse từ string
json j2 = json::parse(R"({"key": "value"})");

// Parse từ file
std::ifstream i("data.json");
json j3;
i >> j3;

// Convert to string
std::string s = j.dump();
std::string pretty = j.dump(4);

// Access
std::string name = j["name"];
int age = j.value("age", 0);  // Default value
bool has_email = j.contains("email");

// Iterate
for (auto& [key, value] : j.items()) {
    std::cout << key << ": " << value << std::endl;
}

// Serialize to file
std::ofstream o("data.json");
o << std::setw(4) << j << std::endl;

// Binary serialization
std::vector<std::uint8_t> bytes = json::to_bson(j);
json j_from_bytes = json::from_bson(bytes);
```

---

### 10.2. Date & Time

```cpp
#include <chrono>
#include <iomanip>
#include <ctime>

// std::chrono
using namespace std::chrono;

// Current time
auto now = std::chrono::system_clock::now();
auto now_time_t = std::chrono::system_clock::to_time_t(now);

// Duration
auto duration = std::chrono::seconds(60);
auto minutes = std::chrono::duration_cast<std::chrono::minutes>(duration);

// Time point
auto tp = system_clock::time_point_cast<hours>(now);

// Calendar time (C++20)
#include <chrono>
auto date = std::chrono::year_month_day{
    std::chrono::floor<std::chrono::days>(now)
};

// Formatting (C++20)
std::string s = std::format("{:%Y-%m-%d}", now);

// Legacy C-style (vẫn được dùng)
std::time_t t = std::time(nullptr);
std::tm* tm_ptr = std::localtime(&t);
std::cout << std::put_time(tm_ptr, "%Y-%m-%d %H:%M:%S") << std::endl;

// Duration arithmetic
auto start = steady_clock::now();
do_work();
auto end = steady_clock::now();
auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
std::cout << "Elapsed: " << elapsed.count() << "ms" << std::endl;
```

---

### 10.3. Regular Expression

```cpp
#include <regex>

std::string text = "Email: test@example.com, Phone: 123-456-7890";

// Regex pattern
std::regex email_pattern(R"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})");

// Match
if (std::regex_match(text, email_pattern)) {
    std::cout << "Valid email" << std::endl;
}

// Search
std::smatch match;
if (std::regex_search(text, match, email_pattern)) {
    std::cout << "Found: " << match[0] << std::endl;
}

// Find all
std::sregex_iterator it(text.begin(), text.end(), email_pattern);
std::sregex_iterator end;
for (; it != end; ++it) {
    std::cout << it->str() << std::endl;
}

// Replace
std::string result = std::regex_replace(text, email_pattern, "[EMAIL]");
std::cout << result << std::endl;

// Regex options
std::regex pattern("test", std::regex::icase);  // Case insensitive
```

---

## 11. Tầng 11: Development Practices

### 11.1. Testing

```cpp
// Google Test
#include <gtest/gtest.h>

class MathTest : public ::testing::Test {
protected:
    void SetUp() override { /* ... */ }
};

TEST_F(MathTest, Addition) {
    EXPECT_EQ(2 + 2, 4);
    EXPECT_NE(2 + 2, 5);
}

TEST(Advanced, Factorial) {
    EXPECT_THROW(throw_exception(), std::exception);
    EXPECT_NO_THROW(no_exception());
}

// Catch2
#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

TEST_CASE("Vector operations", "[vector]") {
    std::vector<int> v;
    REQUIRE(v.empty());

    v.push_back(1);
    CHECK(v.size() == 1);
    CHECK(v[0] == 1);
}

// doctest - Lightweight
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>

TEST_CASE("Addition") {
    REQUIRE(1 + 1 == 2);
}
```

---

### 11.2. Logging

```cpp
// spdlog - Popular logging library
#include <spdlog/spdlog.h>
#include <spdlog/sinks/rotating_file_sink.h>

int main() {
    // Console logger
    spdlog::info("Starting application");
    spdlog::warn("Warning: {}", message);
    spdlog::error("Error: {}", error_msg);

    // File logger
    auto rotating = spdlog::rotating_logger_mt(
        "file_logger", "logs/app.log", 1024 * 1024 * 10, 3);
    rotating->info("Logged to file");

    // Custom format
    spdlog::set_pattern("[%Y-%m-%d %H:%M:%S] [%^%l%$] %v");
}

// Boost.Log
#include <boost/log/trivial.hpp>
BOOST_LOG_TRIVIAL(info) << "Info message";
```

---

### 11.3. Configuration

```cpp
// JSON config với nlohmann/json
#include <nlohmann/json.hpp>
#include <fstream>

class Config {
public:
    int port;
    std::string host;
    bool debug;

    static Config load(const std::string& path) {
        std::ifstream file(path);
        json j;
        file >> j;

        Config c;
        c.port = j.value("port", 8080);
        c.host = j.value("host", "localhost");
        c.debug = j.value("debug", false);
        return c;
    }
};

// Environment variables
#include <cstdlib>
const char* env_var = std::getenv("MY_VAR");
if (env_var) {
    std::string value = env_var;
}

// CLI11 for command-line parsing
#include <CLI/CLI.hpp>

CLI::App app{"My Application"};
std::string name = "World";
int port = 8080;
app.add_option("-n,--name", name, "Name to greet");
app.add_option("-p,--port", port, "Port number");

CLI11_PARSE(app, argc, argv);
```

---

### 11.4. Build & Package Management

```bash
# CMakeLists.txt
cmake_minimum_required(VERSION 3.16)
project(MyProject VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find packages
find_package(Threads REQUIRED)
find_package(Boost 1.70 REQUIRED)

# Executable
add_executable(my_app src/main.cpp)

# Link libraries
target_link_libraries(my_app PRIVATE Threads::Threads)

# Install
install(TARGETS my_app DESTINATION bin)

# vcpkg - Package manager
# vcpkg install nlohmann-json
# vcpkg install spdlog
# vcpkg integrate install

# conan
# conanfile.txt
# [requires]
# nlohmann_json/3.10.5
# spdlog/1.11.0

# Header-only libraries
# Thêm target_include_directories
```

---

## 12. Tầng 12: Advanced Concepts

### 12.1. Templates

```cpp
// Variadic template
template<typename T>
T sum(T value) {
    return value;
}

template<typename T, typename... Args>
T sum(T first, Args... args) {
    return first + sum(args...);
}

int result = sum(1, 2, 3, 4, 5);  // 15

// Template specialization
template<typename T>
class Container {
public:
    void process() { std::cout << "generic\n"; }
};

template<>
class Container<int> {
public:
    void process() { std::cout << "int specialization\n"; }
};

// Partial specialization
template<typename T>
class SmartPointer {
public:
    void process() { std::cout << "generic\n"; }
};

template<typename T>
class SmartPointer<T*> {
public:
    void process() { std::cout << "pointer\n"; }
};

// Template metaprogramming
template<int N>
struct Factorial {
    static constexpr int value = N * Factorial<N - 1>::value;
};

template<>
struct Factorial<0> {
    static constexpr int value = 1;
};

static_assert(Factorial<5>::value == 120);
```

---

### 12.2. Concepts (C++20)

```cpp
#include <concepts>

// Concept definition
template<typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

template<typename T>
concept Addable = requires(T a, T b) {
    a + b;
};

// Using concepts
template<Numeric T>
T add(T a, T b) {
    return a + b;
}

// Requires clause
template<typename T>
    requires std::integral<T>
T divide(T a, T b) {
    return b != 0 ? a / b : 0;
}

// Requires expression
template<typename T>
    requires requires(T a) { {a + a} -> std::same_as<T>; }
T double_value(T a) {
    return a + a;
}

// Constrained templates
template<std::ranges::range R>
void process_range(R&& r) { /* ... */ }

template<std::input_iterator It>
void advance_it(It& it, typename std::iterator_traits<It>::difference_type n) {
    std::advance(it, n);
}
```

---

### 12.3. Variadic Templates

```cpp
// Tuple implementation
template<typename... Types>
class Tuple;

template<>
class Tuple<> {};

template<typename T, typename... Types>
class Tuple<T, Types...> : private Tuple<Types...> {
    T head_;
public:
    Tuple() : head_(), Tuple<Types...>() {}
    Tuple(T h, Types... t) : head_(h), Tuple<Types...>(t...) {}

    T& head() { return head_; }
    const T& head() const { return head_; }
    Tuple<Types...>& tail() { return *this; }
};

// Perfect forwarding
template<typename F, typename... Args>
decltype(auto) invoke(F&& f, Args&&... args) {
    return std::forward<F>(f)(std::forward<Args>(args)...);
}

// Type list
template<typename... Types>
struct TypeList {};

template<typename List>
struct Length;

template<typename... Types>
struct Length<TypeList<Types...>> {
    static constexpr std::size_t value = sizeof...(Types);
};
```

---

## 13. Tầng 13: Memory Layout

### 13.1. Struct Layout

```cpp
struct Simple {
    int a;      // Offset 0
    double b;   // Offset 8 (padding)
    int c;      // Offset 16
};

// #pragma pack - Packed struct
#pragma pack(push, 1)
struct Packed {
    int a;      // Offset 0
    double b;   // Offset 4
    int c;      // Offset 12
};
#pragma pack(pop)

// alignas (C++11+)
struct Aligned {
    alignas(16) int data[4];
};

// Bit fields
struct Flags {
    unsigned int enabled : 1;
    unsigned int visible : 1;
    unsigned int mode : 4;
};
```

---

### 13.2. Memory Alignment

```cpp
#include <align>

// alignas
struct alignas(16) AlignedStruct {
    int a;
    double b;
};

// std::align
void* aligned_allocate(size_t size, size_t alignment) {
    void* ptr = malloc(size + alignment);
    if (!ptr) return nullptr;

    void* aligned = std::align(alignment, size, ptr, size);
    if (!aligned) {
        free(ptr);
        return nullptr;
    }
    return aligned;
}

// alignof
static_assert(alignof(double) == 8);
static_assert(alignof(AlignedStruct) == 16);
```

---

### 13.3. Padding

```cpp
// Compiler-generated padding
struct WithPadding {
    char a;     // +0 (1 byte)
               // +1-2 (2 bytes padding for alignment)
    short b;    // +2 (2 bytes)
               // +4 (4 bytes padding)
    int c;      // +4 (4 bytes)
    char d;     // +8 (1 byte)
               // +9-11 (3 bytes padding for array alignment)
};
// Total: 12 bytes, alignof = 4

// reorder fields để minimize padding
struct Optimized {
    int c;      // +0 (4 bytes)
    short b;    // +4 (2 bytes)
    char a;     // +6 (1 byte)
    char d;     // +7 (1 byte)
};
// Total: 8 bytes (better!)

// [[no_unique_address]] (C++20)
struct Container {
    [[no_unique_address]] SmallObject small;
};
// small có thể share address với Container
```

---

## 14. Tầng 14: Compilation Model

### 14.1. Compilation

```bash
# Preprocess
g++ -E main.cpp -o main.i

# Compile to assembly
g++ -S main.cpp -o main.s
g++ -S main.cpp -o main.o

# Compile to object
g++ -c main.cpp -o main.o

# Link
g++ main.o other.o -o executable

# Full pipeline
g++ -std=c++20 -O2 -Wall -Wextra -g main.cpp -o main

# Pipeline: Preprocess -> Compile -> Assemble -> Link
```

---

### 14.2. Templates Instantiation

```cpp
// Templates được instantiate tại compile time
// Header-only libraries: template definitions trong .h file

// Explicit instantiation
template class std::vector<int>;  // Tạo code cho int

// Explicit instantiation declaration
extern template class std::vector<std::string>;

// Template instantiation units
// - inclusion model: definitions trong mỗi translation unit
// - separation model: explicit instantiation ở một file

// Two-phase lookup
template<typename T>
void process(const T& container) {
    // Phase 1: Dependent names chờ đến instantiation
    // Phase 2: Non-dependent names được resolved ngay
}
```

---

### 14.3. Inline

```cpp
// inline function
inline int max(int a, int b) {
    return a > b ? a : b;
}

// inline variable (C++17+)
inline constexpr int MAX_SIZE = 100;

// inline namespace
inline namespace v2 {
    void func() { /* ... */ }
}

// inline hint to compiler
// - Multiple definitions allowed across translation units
// - Compiler có thể inline hoặc không
// - Thường đặt definitions trong header

// constexpr implies inline (C++17+)
constexpr int square(int x) {  // Cũng là inline
    return x * x;
}
```

---

## 15. Tầng 15: Linking Model

### 15.1. Static Linking

```bash
# Compile to object files
g++ -c a.cpp -o a.o
g++ -c b.cpp -o b.o

# Static library (.a trên Linux)
ar rcs libmylib.a a.o b.o

# Link với static library
g++ main.o -L. -lmylib -o main
# Hoặc
g++ main.o ./libmylib.a -o main

# Link order matters!
g++ -o program lib1.a lib2.a
# lib2.a phải đứng sau các library mà nó cung cấp
```

---

### 15.2. Dynamic Linking

```cpp
// Shared library (.so trên Linux, .dll trên Windows, .dylib trên macOS)

// Compile for shared library
g++ -fPIC -shared mylib.cpp -o libmylib.so

// Compile executable
g++ main.cpp -L. -lmylib -o main

// Runtime: set library path
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.

// dlopen API
#include <dlfcn.h>

void* handle = dlopen("./libmylib.so", RTLD_LAZY);
if (!handle) {
    std::cerr << dlerror() << std::endl;
    return;
}

using FuncPtr = int(*)(int, int);
FuncPtr add = (FuncPtr)dlsym(handle, "add");
int result = add(1, 2);

dlclose(handle);

// CMake
add_library(mylib SHARED mylib.cpp)
```

---

## 16. Tầng 16: Runtime

### 16.1. Stack & Heap

```cpp
// Stack allocation (automatic, fast)
void function() {
    int x = 10;           // Stack
    int arr[100];         // Stack
    std::vector<int> v;  // Stack pointer, heap data
}

// Heap allocation (manual/smart pointer)
void allocate() {
    int* p = new int(10);    // Heap
    delete p;                 // Manual

    auto uptr = std::make_unique<int>(10);  // Smart pointer
    // Tự động giải phóng
}

// Placement new
void* buffer = ::operator new(sizeof(MyClass));
MyClass* obj = new(buffer) MyClass(args);
obj->~MyClass();
::operator delete(buffer);
```

---

### 16.2. Virtual Destructor

```cpp
class Base {
public:
    virtual ~Base() = default;  // Virtual destructor!
    virtual void process() = 0;
};

class Derived : public Base {
    std::string data_;
public:
    ~Derived() override {
        // Cleanup được gọi khi delete qua base pointer
    }

    void process() override {}
};

Base* obj = new Derived();
delete obj;  // Gọi ~Derived() rồi ~Base()

// Nếu không có virtual destructor
// Chỉ gọi ~Base(), memory leak!
```

---

### 16.3. RTTI (Run-Time Type Information)

```cpp
#include <typeinfo>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void derived_only() {}
};

Base* base = new Derived();

// typeid
if (typeid(*base) == typeid(Derived)) {
    Derived* d = static_cast<Derived*>(base);
    d->derived_only();
}

// dynamic_cast
Derived* d = dynamic_cast<Derived*>(base);
if (d) {
    d->derived_only();
}

// Kiểm tra type trước
Base* b = get_object();
if (dynamic_cast<Derived*>(b)) {
    // b là Derived hoặc Derived subclass
}

// RTTI có overhead, có thể disable với -fno-rtti
```

---

## 17. Tầng 17: Language Design Patterns

### 17.1. RAII

```cpp
// Đã trình bày ở section 4.2

// Common RAII patterns
template<typename T>
class ScopedPointer {
    T* ptr_;
public:
    explicit ScopedPointer(T* p) : ptr_(p) {}
    ~ScopedPointer() { delete ptr_; }

    T* operator->() { return ptr_; }
    T& operator*() { return *ptr_; }
};

class MutexGuard {
    std::mutex& mtx_;
public:
    explicit MutexGuard(std::mutex& m) : mtx_(m) { mtx_.lock(); }
    ~MutexGuard() { mtx_.unlock(); }
};
```

---

### 17.2. Rule of Zero/Three/Five

```cpp
// Rule of Zero: Nếu không cần custom, để compiler generate
class RuleOfZero {
    std::vector<int> data_;
public:
    void add(int x) { data_.push_back(x); }
};
// Compiler generated: copy, move, destructor đều đúng

// Rule of Three: Nếu cần custom cho một trong ba
class RuleOfThree {
    int* data_;
public:
    RuleOfThree() : data_(new int(0)) {}
    ~RuleOfThree() { delete data_; }

    // Copy constructor
    RuleOfThree(const RuleOfThree& other)
        : data_(new int(*other.data_)) {}

    // Copy assignment
    RuleOfThree& operator=(const RuleOfThree& other) {
        if (this != &other) {
            *data_ = *other.data_;
        }
        return *this;
    }
};

// Rule of Five: Thêm move constructor và move assignment (C++11+)
class RuleOfFive {
    int* data_;
public:
    RuleOfFive() : data_(new int(0)) {}
    ~RuleOfFive() { delete data_; }

    RuleOfFive(const RuleOfFive&) = default;
    RuleOfFive& operator=(const RuleOfFive&) = default;

    RuleOfFive(RuleOfFive&& other) noexcept
        : data_(other.data_) {
        other.data_ = nullptr;
    }

    RuleOfFive& operator=(RuleOfFive&& other) noexcept {
        if (this != &other) {
            delete data_;
            data_ = other.data_;
            other.data_ = nullptr;
        }
        return *this;
    }
};

// Rule of Six: Thêm comparison (C++20)
class RuleOfSix {
    // operator<=>, operator==
};
```

---

### 17.3. CRTP (Curiously Recurring Template Pattern)

```cpp
// Static polymorphism without virtual
template<typename Derived>
class Base {
public:
    void interface() {
        // Gọi method của Derived
        static_cast<Derived*>(this)->implementation();
    }

    void implementation() {
        std::cout << "Base implementation\n";
    }
};

class Derived : public Base<Derived> {
public:
    void implementation() {
        std::cout << "Derived implementation\n";
    }
};

// Usage
Derived d;
d.interface();  // Calls Derived::implementation

// CRPT for mixin
template<typename Base>
class Printable : public Base {
public:
    void print() const {
        std::cout << "Printable\n";
    }
};

class MyClass : public Printable<MyClass> {};
```

---

## 18. Tầng 18: Standard Library

### 18.1. Collections

```cpp
#include <vector>
#include <list>
#include <deque>
#include <array>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <stack>

// vector - Dynamic array
std::vector<int> v = {1, 2, 3};
v.push_back(4);
v.pop_back();

// list - Doubly linked list
std::list<int> lst = {1, 2, 3};

// deque - Double-ended queue
std::deque<int> dq = {1, 2, 3};
dq.push_front(0);

// array - Fixed-size array (C++11+)
std::array<int, 4> arr = {1, 2, 3, 4};

// set - Ordered set
std::set<std::string> s = {"apple", "banana"};
s.insert("orange");

// map - Ordered key-value
std::map<std::string, int> m;
m["one"] = 1;
m.insert({"two", 2});

// unordered_set - Hash set (O(1) avg)
std::unordered_set<int> uset = {1, 2, 3};

// unordered_map - Hash map (O(1) avg)
std::unordered_map<std::string, int> umap;

// queue/priority_queue
std::queue<int> q;
std::priority_queue<int> pq;

// stack
std::stack<int> st;
```

---

### 18.2. Utilities

```cpp
#include <utility>
#include <optional>
#include <variant>
#include <any>
#include <functional>
#include <memory>

// std::pair
auto p = std::make_pair(1, "one");

// std::tuple
auto t = std::make_tuple(1, "two", 3.0);
int a = std::get<0>(t);

// std::optional
std::optional<int> find(const std::vector<int>& v, int target) {
    for (auto it = v.begin(); it != v.end(); ++it) {
        if (*it == target) return it - v.begin();
    }
    return std::nullopt;
}

// std::variant (C++17+)
std::variant<int, std::string, double> v = 42;
v = "hello";
if (std::holds_alternative<std::string>(v)) {
    std::string s = std::get<std::string>(v);
}

// std::any (C++17+)
std::any a = 42;
int value = std::any_cast<int>(a);

// std::function
std::function<int(int, int)> func = [](int a, int b) {
    return a + b;
};
```

---

### 18.3. I/O & System

```cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

// cout/cin
std::cout << "Hello" << std::endl;
std::cin >> value;

// File I/O
std::ifstream in("file.txt");
std::ofstream out("file.txt");

// String stream
std::ostringstream oss;
oss << 42 << " " << 3.14;

// Format (C++20)
std::string s = std::format("{:.2f}", 3.14159);

// Environment
#include <cstdlib>
char* env = getenv("PATH");

// Process
#include <cstdlib>
int result = system("ls -la");

// Random
#include <random>
std::random_device rd;
std::mt19937 gen(rd());
std::uniform_int_distribution<> dis(1, 6);
int dice = dis(gen);
```

---

## 19. Tầng 19: Ecosystem

### 19.1. Frameworks

```cpp
// Qt - Cross-platform GUI
#include <QApplication>
#include <QLabel>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QLabel label("Hello Qt!");
    label.show();
    return app.exec();
}

// SFML - Simple and Fast Multimedia Library
#include <SFML/Graphics.hpp>

sf::RenderWindow window(sf::VideoMode(800, 600), "SFML");
sf::CircleShape shape(100.f);
shape.setFillColor(sf::Color::Green);

// SDL2 - C library (thường dùng với wrapper)
#include <SDL2/SDL.h>
SDL_Init(SDL_INIT_VIDEO);

// Boost - Large library collection
#include <boost/asio.hpp>
#include <boost/shared_ptr.hpp>
```

---

### 19.2. Libraries

```cpp
// Popular C++ libraries:
// - Boost: utilities, algorithms, containers
// - STL: standard library
// - Qt: GUI
// - Boost.Asio: networking
// - Eigen: linear algebra
// - nlohmann/json: JSON
// - spdlog: logging
// - fmt: formatting
// - Catch2/doctest: testing
// - Abseil: Google's utilities
// - Folly: Facebook's utilities

// Install via vcpkg:
// vcpkg install boost qt5 eigen nlohmann-json spdlog fmt catch2
```

---

### 19.3. Build Systems

```bash
# CMake
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build

# Bazel
bazel build //main:binary

# Meson
meson setup builddir
meson compile -C builddir

# Conan + CMake
conan install . --build=missing
cmake --build build

# vcpkg
vcpkg install [packages]
cmake -B build -DCMAKE_TOOLCHAIN_FILE=[vcpkg]/scripts/buildsystems/vcpkg.cmake
```

---

## 20. Tầng 20: Toolchain

### 20.1. Compiler

```bash
# GCC
g++ -std=c++20 -O2 -Wall -Wextra -o main main.cpp

# Clang
clang++ -std=c++20 -O2 -Wall -Wextra -o main main.cpp

# MSVC
cl /std:c++20 /O2 /W4 main.cpp

# Compiler flags
# -std=c++11/14/17/20/23
# -O0/-O1/-O2/-O3/-Os
# -Wall -Wextra -Werror -Wpedantic
# -g -ggdb
# -fPIC (position independent code)
# -fvisibility=hidden
# -march=native
```

---

### 20.2. Debugging

```bash
# GDB
gdb ./main
# Commands: run, break, next, step, print, bt, info locals

# LLDB
lldb ./main

# Valgrind (memory debugging)
valgrind --leak-check=full ./main

# AddressSanitizer (ASAN)
g++ -fsanitize=address -g main.cpp -o main
./main

# UBSan (undefined behavior)
g++ -fsanitize=undefined main.cpp -o main

# Static analysis
clang++ --analyze main.cpp
cppcheck main.cpp
```

---

### 20.3. Code Quality

```bash
# Clang Format
clang-format -i main.cpp
# .clang-format config file

# Clang Tidy
clang-tidy main.cpp -checks=modernize-*

# Cppcheck (static analysis)
cppcheck --enable=all main.cpp

# CppClobber (mutation testing)

# Doxygen (documentation)
doxygen Doxyfile

# CMake tools
cmake --build build --target clang-tidy
cmake --build build --target cppcheck
```

---

## Tóm Tắt

### Ưu Điểm C++
- **Hiệu năng cao**: Native code, zero-overhead abstractions
- **Kiểm soát bộ nhớ**: Manual memory management với RAII
- **Multi-paradigm**: OOP, Generic, Functional đều được hỗ trợ
- **Rich standard library**: STL rất mạnh
- **Large ecosystem**: Nhiều thư viện, framework
- **Portability**: Cross-platform

### Nhược Điểm C++
- **Phức tạp**: Cú pháp dài dòng, nhiều quy tắc
- **No built-in null safety**: Dễ gặp null pointer errors
- **Manual memory management**: Có thể gây leak nếu không cẩn thận
- **Long compile times**: Template instantiation có thể chậm
- **Undefined behavior**: Cần hiểu sâu để tránh

### C++ Standards Timeline
- **C++11**: Modern C++ (auto, lambda, move, smart pointers)
- **C++14**: Minor improvements (generic lambdas, return type deduction)
- **C++17**: Big features (filesystem, optional, variant, if constexpr)
- **C++20**: Major (concepts, ranges, modules, coroutines)
- **C++23**: Further improvements (std::format improvements, std::print)
- **C++26**: Upcoming (string literals as template params, etc.)
