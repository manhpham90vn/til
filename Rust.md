# Rust Syntax Reference

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
   - [2.5 Generics](#25-generics)
   - [2.6 Collection Operations](#26-collection-operations)
   - [2.7 String Operations](#27-string-operations)
3. [Tầng 3: OOP & Type Relationships](#tầng-3-oop--type-relationships)
   - [3.1 Struct & Object](#31-struct--object)
   - [3.2 Kế Thừa & Đa Hình](#32-kế-thừa--đa-hình)
   - [3.3 Trait](#33-trait)
   - [3.4 Visibility](#34-visibility)
4. [Tầng 4: Memory Model](#tầng-4-memory-model)
   - [4.1 Ownership & Borrowing](#41-ownership--borrowing)
   - [4.2 Lifetime](#42-lifetime)
5. [Tầng 5: Concurrency Model](#tầng-5-concurrency-model)
   - [5.1 Concurrency/Async](#51-concurrencyasync)
6. [Tầng 6: Paradigm](#tầng-6-paradigm)
   - [6.1 Functional Programming](#61-functional-programming)
7. [Tầng 7: Error Handling](#tầng-7-error-handling)
   - [7.1 Xử Lý Lỗi](#71-xử-lý-lỗi)
   - [7.2 Error Types](#72-error-types)
8. [Tầng 8: Module & Organization](#tầng-8-module--organization)
   - [8.1 Import/Module](#81-importmodule)
   - [8.2 Traits & Generics](#82-traits--generics)
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
    - [11.3 Configuration](#113-configuration)
    - [11.4 Build & Package Management](#114-build--package-management)
12. [Tầng 12: Advanced Concepts](#tầng-12-advanced-concepts)
    - [12.1 Advanced Concepts](#121-advanced-concepts)
13. [Tầng 13: Memory Layout](#tầng-13-memory-layout)
    - [13.1 Struct Layout](#131-struct-layout)
    - [13.2 Memory Alignment](#132-memory-alignment)
14. [Tầng 14: Compilation Model](#tầng-14-compilation-model)
    - [14.1 Compilation](#141-compilation)
    - [14.2 Cargo](#142-cargo)
15. [Tầng 15: Linking Model](#tầng-15-linking-model)
    - [15.1 Linking](#151-linking)
16. [Tầng 16: Runtime](#tầng-16-runtime)
    - [16.1 No Runtime](#16-no-runtime)
    - [16.2 Panic Handling](#162-panic-handling)
17. [Tầng 17: Language Design Patterns](#tầng-17-language-design-patterns)
    - [17.1 RAII](#171-raii)
    - [17.2 Move Semantics](#172-move-semantics)
18. [Tầng 18: Standard Library](#tầng-18-standard-library)
    - [18.1 Collections](#181-collections)
    - [18.2 Utilities](#182-utilities)
    - [18.3 I/O & System](#183-io--system)
19. [Tầng 19: Ecosystem](#tầng-19-ecosystem)
    - [19.1 Web Frameworks](#191-web-frameworks)
    - [19.2 Database & ORM](#192-database--orm)
    - [19.3 Testing](#193-testing)
20. [Tầng 20: Toolchain](#tầng-20-toolchain)
    - [20.1 Build & Package Management](#201-build--package-management)
    - [20.2 Code Quality](#202-code-quality)
    - [20.3 IDE & Debugging](#203-ide--debugging)

---

## 0. Phân Loại Ngôn Ngữ

### Chạy File Rust

```bash
# Compile và chạy
rustc main.rs && ./main

# Với Cargo (khuyến nghị)
cargo new my_project
cd my_project
cargo run

# Build release
cargo build --release

# Check code
cargo check

# Format code
cargo fmt
```

### Đặc điểm Rust

- **Typing**: Static, Strong typing với type inference
- **Paradigm**: Multi-paradigm (Functional, OOP, Systems)
- **Execution**: Compiled (AOT), No runtime, Zero-cost abstractions
- **Memory Safety**: Ownership, Borrowing, Lifetime (không GC)
- **Use Cases**: Systems programming, WebAssembly, CLI tools, Web backends, Embedded

---

## 1. Tầng 1: Syntax & Semantics

### 1.1. Khai Báo Biến (Variable Declaration)

#### Mutable - Biến thường

```rust
// Khai báo biến với type inference
let x = 10;
let name = "Rust";
let is_active = true;
let prices = vec![1.5, 2.0, 3.5];

// Explicit type
let x: i32 = 10;
let name: &str = "Rust";
let is_active: bool = true;

// Mutable
let mut counter = 0;
counter += 1;
```

#### Immutable - Hằng số

```rust
// Constants (compile-time)
const MAX_SIZE: u32 = 100;
const PI: f64 = 3.14159;

// Static ( có địa chỉ cố định)
static MAX_RETRIES: u32 = 3;
```

#### Global Variable

```rust
// Global với lazy initialization
use std::sync::LazyLock;

static GLOBAL_DATA: LazyLock<Mutex<i32>> = LazyLock::new(|| Mutex::new(42));

fn access_global() {
    let data = GLOBAL_DATA.lock().unwrap();
    println!("Global: {}", data);
}
```

---

### 1.2. Khai Báo Hàm (Function Declaration)

#### Function cơ bản

```rust
// Function không có return
fn greet() {
    println!("Hello!");
}

// Function có return
fn add(a: i32, b: i32) -> i32 {
    a + b
}

// Function với explicit return
fn add_explicit(a: i32, b: i32) -> i32 {
    return a + b;
}

// Docstring
fn calculate_area(width: f64, height: f64) -> f64 {
    /// Calculate rectangle area.
    ///
    /// # Arguments
    /// * `width` - Width of rectangle
    /// * `height` - Height of rectangle
    ///
    /// # Returns
    /// Area of rectangle
    width * height
}
```

#### Parameters

```rust
// Default parameters (Rust không có, dùng trait hoặc builder)
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}

// Named arguments (Rust không có trực tiếp, dùng struct)
struct UserParams {
    name: String,
    age: u32,
}

fn create_user(params: UserParams) -> User {
    User {
        name: params.name,
        age: params.age,
    }
}

// *args (dùng Vec)
fn sum_all(numbers: &[i32]) -> i32 {
    numbers.iter().sum()
}

// **kwargs (dùng HashMap)
use std::collections::HashMap;

fn print_info(info: HashMap<String, String>) {
    for (key, value) in info {
        println!("{}: {}", key, value);
    }
}
```

#### Closure

```rust
// Closure (anonymous function)
let square = |x: i32| x * x;
let add = |a: i32, b: i32| a + b;

// Closure với mutable
let mut counter = 0;
let mut increment = || counter += 1;
increment();
increment();
println!("{}", counter); // 2

// Closure captures variables
let x = 10;
let closure = |y| x + y;
closure(5); // 15

// Closure với move
let data = vec![1, 2, 3];
let moved = move || println!("{:?}", data);
// data đã bị move vào closure
```

#### Higher-Order Function

```rust
// Function nhận function khác làm tham số
fn apply_twice<F>(func: F, x: i32) -> i32
where
    F: Fn(i32) -> i32,
{
    func(func(x))
}

fn add_five(x: i32) -> i32 {
    x + 5
}

fn main() {
    let result = apply_twice(add_five, 10); // 20
}

// Function trả về function
fn multiplier(factor: i32) -> impl Fn(i32) -> i32 {
    move |x| x * factor
}

fn main() {
    let double = multiplier(2);
    double(5); // 10
}
```

#### Method trong Struct/Impl

```rust
struct Calculator;

impl Calculator {
    // Associated function (static method)
    fn new() -> Self {
        Calculator
    }

    // Instance method
    fn multiply(&self, a: i32, b: i32) -> i32 {
        a * b
    }
}
```

#### Constructor & Destructor

```rust
struct Resource {
    name: String,
}

impl Resource {
    fn new(name: &str) -> Self {
        println!("Creating {}", name);
        Resource {
            name: name.to_string(),
        }
    }
}

// Drop trait cho destructor
impl Drop for Resource {
    fn drop(&mut self) {
        println!("Dropping {}", self.name);
    }
}
```

---

### 1.3. Vòng Lặp (Loops)

#### For Loop

```rust
// For với range
for i in 0..5 {
    println!("{}", i); // 0, 1, 2, 3, 4
}

for i in 1..=5 {
    println!("{}", i); // 1, 2, 3, 4, 5
}

// For với iter
let fruits = vec!["apple", "banana", "cherry"];
for fruit in fruits.iter() {
    println!("{}", fruit);
}

// For với enumerate
for (i, fruit) in fruits.iter().enumerate() {
    println!("{}: {}", i, fruit);
}

// For với iter mutable
let mut nums = vec![1, 2, 3];
for num in nums.iter_mut() {
    *num *= 2;
}
```

#### While Loop

```rust
let mut count = 0;
while count < 5 {
    println!("{}", count);
    count += 1;
}

// While với break/continue
let mut input = String::new();
loop {
    println!("Enter 'quit' to exit: ");
    std::io::stdin().read_line(&mut input).unwrap();
    if input.trim() == "quit" {
        break;
    }
    println!("You entered: {}", input);
    input.clear();
}
```

#### Iterator Methods

```rust
let numbers: Vec<i32> = (1..=5).collect();

// Map
let squared: Vec<i32> = numbers.iter().map(|x| x * x).collect();

// Filter
let evens: Vec<&i32> = numbers.iter().filter(|x| *x % 2 == 0).collect();

// Filter map
let result: Vec<i32> = numbers.iter().filter_map(|x| Some(x * 2)).collect();

// Take/Skip
let first_three: Vec<i32> = (1..=10).take(3).collect(); // 1, 2, 3
let skip_three: Vec<i32> = (1..=10).skip(3).collect();  // 4, 5, 6, 7, 8, 9, 10
```

#### Loop Control

```rust
// Break
for i in 0..10 {
    if i == 5 {
        break;
    }
    println!("{}", i); // 0, 1, 2, 3, 4
}

// Continue
for i in 0..5 {
    if i == 2 {
        continue;
    }
    println!("{}", i); // 0, 1, 3, 4
}

// Break với label
'outer: for i in 0..3 {
    for j in 0..3 {
        if j == 1 {
            break 'outer;
        }
    }
}

// Loop như expression
let result = loop {
    break 42;
};
```

---

### 1.4. Điều Kiện (Conditionals)

#### If-Else

```rust
let age = 18;
if age >= 18 {
    println!("Adult");
} else {
    println!("Minor");
}

// Else if
let score = 85;
let grade = if score >= 90 {
    "A"
} else if score >= 80 {
    "B"
} else if score >= 70 {
    "C"
} else {
    "F"
};

// If as expression
let status = if age >= 18 { "adult" } else { "minor" };
```

#### Match Expression

```rust
// Match (tương tự switch-case nhưng mạnh hơn)
fn http_status(status: u16) -> &'static str {
    match status {
        200 => "OK",
        404 => "Not Found",
        500 => "Server Error",
        _ => "Unknown",
    }
}

// Match với multiple values
fn http_status_multi(status: u16) -> &'static str {
    match status {
        200 | 201 | 202 => "Success",
        400 | 401 | 403 => "Client Error",
        500..=599 => "Server Error",
        _ => "Unknown",
    }
}

// Match với binding
fn describe_point(x: i32, y: i32) -> String {
    match (x, y) {
        (0, 0) => "Origin".to_string(),
        (x, 0) => format!("On X-axis at {}", x),
        (0, y) => format!("On Y-axis at {}", y),
        (x, y) => format!("Point at ({}, {})", x, y),
    }
}

// Match với guard
fn classify(n: i32) -> &'static str {
    match n {
        x if x < 0 => "negative",
        0 => "zero",
        x if x > 0 => "positive",
        _ => unreachable!(),
    }
}

// Match as expression
let msg = match opt {
    Some(x) => format!("Got {}", x),
    None => "Nothing".to_string(),
};
```

#### If-Let & While-Let

```rust
// If-let
let some_value: Option<i32> = Some(5);
if let Some(x) = some_value {
    println!("Got value: {}", x);
}

// While-let
let mut stack = Some(5);
while let Some(top) = stack {
    println!("Popped: {}", top);
    stack = None; // Exit loop
}
```

---

## 2. Tầng 2: Type System

### 2.1. Kiểu Dữ Liệu Cơ Bản (Primitive Types)

#### Integer

```rust
// Integer types
let x: i8 = 10;
let y: i16 = 10;
let z: i32 = 10;      // Default for integers
let w: i64 = 10;
let u: i128 = 10;

let a: u8 = 10;
let b: u16 = 10;
let c: u32 = 10;      // Default for positive
let d: u64 = 10;
let e: u128 = 10;

// Literals
let hex = 0xFF;       // 255
let binary = 0b1010;  // 10
let octal = 0o777;    // 511

// Underscore for readability
let million = 1_000_000;

// Operations
5 + 3    // 8
5 - 3    // 2
5 * 3    // 15
5 / 3    // 1 (integer division)
5 % 3    // 2
5i32.pow(2)  // 25 (exponentiation)

// Overflow checking
// use std::num::Wrapping for wrapping operations
```

#### Float

```rust
// Float
let x: f32 = 3.14;
let y: f64 = 3.14;  // Default

// Scientific notation
let scientific: f64 = 1.5e10;

// Special values
let inf: f64 = f64::INFINITY;
let neg_inf: f64 = f64::NEG_INFINITY;
let nan: f64 = f64::NAN;

// Check
inf.is_infinite();
nan.is_nan();

// Operations
3.14 + 1.0;  // 4.14
3.14 * 2.0;  // 6.28
3.14 / 2.0;  // 1.57
```

#### Boolean

```rust
let is_active = true;
let is_deleted = false;

// Operations
true && false;  // false
true || false;   // true
!true;           // false
```

#### Char

```rust
let c: char = 'a';
let emoji: char = '😀';

// Escape
let newline: char = '\n';
let tab: char = '\t';
let unicode: char = '\u{1F600}';
```

#### String

```rust
// &str (string slice - borrowed)
let s1: &str = "Hello";
let s2 = "World";

// String (owned)
let mut s = String::new();
s.push_str("Hello");
s.push(' ');
s.push_str("World");

// From
let s = String::from("Hello");
let s = "Hello".to_string();

// String methods
let s = "Hello World";
s.len();                    // 11
s.to_uppercase();           // "HELLO WORLD"
s.to_lowercase();           // "hello world"
s.contains("World");        // true
s.find("World");            // Some(6)
s.starts_with("Hello");     // true
s.ends_with("World");       // true
s.trim();                   // "Hello World"
s.split_whitespace().collect::<Vec<_>>();  // ["Hello", "World"]
s.replace("World", "Rust"); // "Hello Rust"
```

#### Array

```rust
// Fixed-size array
let arr: [i32; 3] = [1, 2, 3];
let arr = [1, 2, 3];  // Type inference

// With default value
let arr = [0; 5];  // [0, 0, 0, 0, 0]

// Access
arr[0];  // 1
arr.len();
arr.is_empty();

// Slicing
&arr[1..3];  // [2, 3]
&arr[..3];   // [1, 2, 3]
&arr[1..];   // [2, 3]
```

#### Tuple

```rust
let point = (10, 20);
let coords = (1, 2, 3);
let single = (1,);  // Tuple với 1 element

// Access
let (x, y) = point;  // Destructuring
let first = point.0;
let second = point.1;

// Mixed types
let mixed = (42, "hello", 3.14);
```

#### Slice

```rust
let arr = [1, 2, 3, 4, 5];
let slice: &[i32] = &arr[1..4];  // [2, 3, 4]

// Dynamic slice
let vec = vec![1, 2, 3, 4, 5];
let slice: &[i32] = &vec;
```

---

### 2.2. Enum

```rust
// Basic Enum
enum Color {
    Red,
    Green,
    Blue,
}

let color = Color::Red;
match color {
    Color::Red => println!("Red"),
    Color::Green => println!("Green"),
    Color::Blue => println!("Blue"),
}

// Enum with values
enum Status {
    Pending,
    Approved = 200,
    Rejected = 400,
}

Status::Pending as i32;  // 0
Status::Approved as i32;  // 200

// Enum with data
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(u8, u8, u8),
}

let m = Message::Move { x: 10, y: 20 };
match m {
    Message::Quit => println!("Quit"),
    Message::Move { x, y } => println!("Move to ({}, {})", x, y),
    Message::Write(s) => println!("Write: {}", s),
    Message::ChangeColor(r, g, b) => println!("Color: {}, {}, {}", r, g, b),
}

// Enum with methods
enum Status {
    Pending,
    Approved,
    Rejected,
}

impl Status {
    fn as_str(&self) -> &str {
        match self {
            Status::Pending => "pending",
            Status::Approved => "approved",
            Status::Rejected => "rejected",
        }
    }
}
```

---

### 2.3. Nullable Types

```rust
// Option<T> (thay thế cho null)
let some_value: Option<i32> = Some(5);
let no_value: Option<i32> = None;

// Pattern matching
match some_value {
    Some(x) => println!("Got: {}", x),
    None => println!("Nothing"),
}

// Unwrap
let x = some_value.unwrap();       // Panic if None
let x = some_value.unwrap_or(0);   // Default if None
let x = some_value.unwrap_or_else(|| calculate_default());

// Check
if some_value.is_some() { }
if some_value.is_none() { }

// Map
let doubled = some_value.map(|x| x * 2);  // Some(10)
let result = some_value.and_then(|x| Some(x * 2));  // Chain
```

---

### 2.4. Null Safety

```rust
// Rust không có null, dùng Option<T>

// Safe access
let name: Option<String> = Some("John".to_string());

// Dùng ?
fn get_name() -> Option<String> {
    let name = Some("John".to_string())?;
    Some(name.to_uppercase())
}

// Elvis operator (Rust dùng unwrap_or)
let name = None;
let result = name.unwrap_or("Unknown");

// Safe navigation (Rust dùng ? hoặc if let)
struct User {
    address: Option<Address>,
}

struct Address {
    city: Option<String>,
}

let user = User {
    address: Some(Address {
        city: Some("NYC".to_string()),
    }),
};

// Dùng nested Option
let city = user.address.as_ref().and_then(|a| a.city.as_ref()).cloned();
```

---

### 2.5. Generics

```rust
// Generic struct
struct Container<T> {
    value: T,
}

impl<T> Container<T> {
    fn new(value: T) -> Self {
        Container { value }
    }

    fn get(&self) -> &T {
        &self.value
    }
}

let int_container = Container::new(42);
let str_container = Container::new("hello");

// Generic function
fn first<T>(lst: &[T]) -> Option<&T> {
    lst.first()
}

// Generic constraints
fn largest<T: PartialOrd>(lst: &[T]) -> Option<&T> {
    lst.iter().max_by(|a, b| a.partial_cmp(b).unwrap())
}

// Multiple constraints
fn print_display<T: std::fmt::Display + std::fmt::Debug>(item: T) {
    println!("Display: {}, Debug: {:?}", item, item);
}

// Where clause
fn some_function<T, U>(t: T, u: U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
    // ...
}

// Generic Enum
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

---

### 2.6. Collection Operations

#### Map/Transform

```rust
let numbers = vec![1, 2, 3, 4, 5];

// Map
let squared: Vec<i32> = numbers.iter().map(|x| x * x).collect();

// Map to different type
let strings: Vec<String> = numbers.iter().map(|x| x.to_string()).collect();

// Enumerate transform
let indexed: Vec<(usize, &i32)> = numbers.iter().enumerate().collect();
```

#### Filter

```rust
let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Filter
let evens: Vec<&i32> = numbers.iter().filter(|x| *x % 2 == 0).collect();

// Filter map
let result: Vec<i32> = numbers.iter().filter_map(|x| {
    if *x % 2 == 0 { Some(x * 2) } else { None }
}).collect();
```

#### Reduce/Fold

```rust
let numbers = vec![1, 2, 3, 4, 5];

// fold
let total = numbers.iter().fold(0, |acc, x| acc + x);  // 15

// sum (convenience)
let total: i32 = numbers.iter().sum();

// product
let product = numbers.iter().product::<i32>();  // 120
```

#### FlatMap

```rust
let nested = vec![vec![1, 2], vec![3, 4], vec![5, 6]];

// flatten
let flattened: Vec<i32> = nested.iter().flatten().cloned().collect();
// [1, 2, 3, 4, 5, 6]

// flat_map
let words = vec!["hello", "world"];
let chars: Vec<char> = words.iter().flat_map(|s| s.chars()).collect();
```

#### Sort

```rust
let mut numbers = vec![3, 1, 4, 1, 5, 9, 2, 6];

// sort
numbers.sort();  // In-place
let sorted = vec![1, 1, 2, 3, 4, 5, 6, 9];

// sort_by
let mut words = vec!["banana", "apple", "cherry"];
words.sort_by(|a, b| a.len().cmp(&b.len()));  // ["apple", "banana", "cherry"]

// sort_by_key
let mut users = vec!["john", "alice", "bob"];
users.sort_by_key(|s| s.len());  // ["john", "bob", "alice"]

// sorted (returns new Vec)
let sorted: Vec<&i32> = numbers.iter().sorted().collect();
```

#### Find/First/Last

```rust
let numbers = vec![1, 2, 3, 4, 5];

// Find first
let result = numbers.iter().find(|x| **x > 3);  // Some(&4)

// Position
let pos = numbers.iter().position(|x| *x == 3);  // Some(2)

// Last
let last = numbers.last();  // Some(&5)

// Index
let third = numbers.get(2);  // Some(&3)
let tenth = numbers.get(9);  // None
```

#### Any/All

```rust
let numbers = vec![1, 2, 3, 4, 5];

numbers.iter().any(|x| *x > 3);  // true
numbers.iter().all(|x| *x > 0);  // true
numbers.iter().all(|x| *x > 10);  // false
```

#### GroupBy (dùng itertools)

```rust
use itertools::Itertools;

let data = vec![("a", 1), ("a", 2), ("b", 3), ("b", 4)];

// Group by
for (key, group) in &data.into_iter().group_by(|x| x.0) {
    println!("{}: {:?}", key, group.collect::<Vec<_>>());
}
```

#### Chunk

```rust
let numbers: Vec<i32> = (1..=7).collect();

// chunks
let chunks: Vec<&[i32]> = numbers.chunks(3).collect();
// [[1,2,3], [4,5,6], [7]]

// chunks_mut (mutable)
let mut numbers: Vec<i32> = vec![1, 2, 3, 4, 5];
for chunk in numbers.chunks_mut(2) {
    for x in chunk.iter_mut() {
        *x *= 2;
    }
}
```

#### Zip

```rust
let names = vec!["Alice", "Bob", "Charlie"];
let ages = vec![25, 30, 35];

// Zip
let combined: Vec<(&str, i32)> = names.iter().zip(ages.iter()).collect();
// [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

// Unzip
let (n, a): (Vec<&str>, Vec<i32>) = names.iter().zip(ages.iter()).unzip();
```

---

### 2.7. String Operations

#### Concatenation

```rust
// Dùng format!
let s = format!("Hello {}!", "World");

// String + &str
let mut s = String::from("Hello ");
s += "World";

// String + String
let s1 = String::from("Hello");
let s2 = String::from("World");
let s = format!("{} {}", s1, s2);
```

#### Interpolation

```rust
let name = "Rust";
let version = 2024;

format!("Welcome to {} {}", name, version);  // "Welcome to Rust 2024"

// Format spec
format!("{:.2}", 3.14159);  // "3.14"
format!("{:05}", 42);      // "00042"
format!("{:?}", vec![1, 2, 3]);  // "[1, 2, 3]"
```

#### Template String

```rust
// Rust dùng format! với positional/named arguments
let template = "Hello {name}!";
format!(template, name = "World");  // "Hello World!"

// Với index
let s = "{0} {1} {0}".format("Hello", "World");
```

#### Split & Join

```rust
let text = "hello world rust";

// Split
let words: Vec<&str> = text.split_whitespace().collect();
let parts: Vec<&str> = text.split('o').collect();

// Join (không có trực tiếp, dùng join)
let words = vec!["hello", "world"];
let s = words.join(" ");  // "hello world"
```

#### Replace

```rust
let text = "Hello World World";

text.replace("World", "Rust");      // "Hello Rust Rust"
text.replacen("World", "Rust", 1);   // "Hello Rust World"

// Regex replace
use regex::Regex;

let re = Regex::new(r"\d+").unwrap();
let result = re.replace_all("test 123 abc 456", "#");
// "test # abc #"
```

#### Regex

```rust
use regex::Regex;

let text = "My email is john@example.com";

// Match
let re = Regex::new(r"[\w.-]+@[\w.-]+").unwrap();
if let Some(m) = re.find(text) {
    println!("{}", m.as_str());  // "john@example.com"
}

// Find all
let emails: Vec<&str> = re.find_iter(text).map(|m| m.as_str()).collect();

// Capture groups
let re = Regex::new(r"(?P<user>[\w.-]+)@(?P<domain>[\w.-]+)").unwrap();
if let Some(caps) = re.captures(text) {
    println!("{}", &caps["user"]);  // "john"
    println!("{}", &caps["domain"]); // "example.com"
}

// Replace
let re = Regex::new(r"\d+").unwrap();
let result = re.replace_all("test 123 abc 456", "#");
```

#### Substring

```rust
let text = "Hello World";

// Slicing
&text[0..5];     // "Hello"
&text[..5];      // "Hello"
&text[6..];      // "World"
&text[-5..];     // "World"

// methods
text.find("World");            // Some(6)
text.starts_with("Hello");     // true
text.ends_with("World");       // true
text.contains("World");        // true
```

---

## 3. Tầng 3: OOP & Type Relationships

### 3.1. Struct & Object

#### Struct Definition

```rust
// Basic struct
struct User {
    name: String,
    email: String,
    age: u32,
    active: bool,
}

// Create instance
let user = User {
    name: String::from("John"),
    email: "john@example.com".to_string(),
    age: 30,
    active: true,
};

// Tuple struct
struct Color(u8, u8, u8);
let red = Color(255, 0, 0);
let r = red.0;

// Unit struct
struct Marker;
```

#### Struct Methods

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    // Associated function (constructor)
    fn new(width: u32, height: u32) -> Self {
        Rectangle { width, height }
    }

    // Instance method (borrow)
    fn area(&self) -> u32 {
        self.width * self.height
    }

    // Mutable method
    fn resize(&mut self, new_width: u32, new_height: u32) {
        self.width = new_width;
        self.height = new_height;
    }

    // Static method
    fn square(size: u32) -> Self {
        Rectangle {
            width: size,
            height: size,
        }
    }
}
```

#### Data Struct (C-like)

```rust
// derive macro cho common traits
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
struct Point {
    x: i32,
    y: i32,
}

// Default
#[derive(Default)]
struct Config {
    host: String,
    port: u16,
}

let config = Config::default();
```

#### Singleton (không có built-in)

```rust
// Dùng static với LazyLock hoặc OnceLock
use std::sync::OnceLock;

static INSTANCE: OnceLock<Singleton> = OnceLock::new();

struct Singleton {
    data: String,
}

impl Singleton {
    fn get() -> &'static Singleton {
        INSTANCE.get_or_init(|| Singleton {
            data: "Initialized".to_string(),
        })
    }
}
```

#### Factory Method

```rust
struct User {
    name: String,
    email: String,
}

impl User {
    fn new(name: String) -> Self {
        User {
            name,
            email: format!("{}@example.com", name.to_lowercase()),
        }
    }

    fn from_dict(data: &serde_json::Value) -> Option<Self> {
        Some(User {
            name: data["name"].as_str()?.to_string(),
            email: data["email"].as_str()?.to_string(),
        })
    }
}
```

---

### 3.2. Kế Thừa & Đa Hình (Inheritance & Polymorphism)

#### Trait Objects (Dynamic Dispatch)

```rust
// Trait (interface)
trait Drawable {
    fn draw(&self);
}

struct Circle {
    radius: f64,
}

impl Drawable for Circle {
    fn draw(&self) {
        println!("Drawing circle with radius {}", self.radius);
    }
}

struct Square {
    side: f64,
}

impl Drawable for Square {
    fn draw(&self) {
        println!("Drawing square with side {}", self.side);
    }
}

// Polymorphism với trait object
fn render(shape: &dyn Drawable) {
    shape.draw();
}

let circle = Circle { radius: 5.0 };
let square = Square { side: 10.0 };
render(&circle);
render(&square);
```

#### Static Dispatch (Generics)

```rust
fn render<T: Drawable>(shape: &T) {
    shape.draw();
}

// Hoặc với impl Trait
fn render(shape: &impl Drawable) {
    shape.draw();
}
```

#### Trait Inheritance

```rust
trait Printable: Debug + Display {
    fn print(&self) {
        println!("{}", self);
    }
}
```

---

### 3.3. Trait

#### Trait Definition

```rust
trait Summary {
    fn summarize(&self) -> String;

    // Default implementation
    fn summarize_author(&self) -> String {
        String::from("(Unknown)")
    }
}

impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{}, by {}", self.title, self.author)
    }
}
```

#### Common Traits

```rust
// Debug (for {:?})
#[derive(Debug)]
struct Point { x: i32, y: i32 }

// Display (for {})
use std::fmt;
impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

// Clone
#[derive(Clone)]
struct Point { x: i32, y: i32 }

// Copy (cho primitive-like types)
#[derive(Copy, Clone)]
struct Point { x: i32, y: i32 }

// Default
#[derive(Default)]
struct Config { port: u16 }

// PartialEq, Eq
#[derive(PartialEq, Eq)]
struct Point { x: i32, y: i32 }

// PartialOrd, Ord
#[derive(PartialOrd, Ord)]
struct Version { major: u32, minor: u32 }

// Hash
use std::hash::Hash;
#[derive(Hash)]
struct Point { x: i32, y: i32 }
```

---

### 3.4. Visibility

```rust
// Default là public cho modules
mod my_module {
    pub fn public_fn() {}      // Public
    fn private_fn() {}        // Private (trong module)

    pub mod inner {
        pub fn public_inner() {}

        pub(crate) fn crate_public() {}  // Public trong crate

        pub(super) fn super_public() {}  // Public trong parent

        pub(in crate::my_module) fn limited() {}  // Public trong path
    }
}

// Struct fields
pub struct User {
    pub name: String,           // Public
    pub(crate) email: String,   // Crate-public
    age: u32,                   // Private (default)
}
```

---

## 4. Tầng 4: Memory Model

### 4.1. Ownership & Borrowing

#### Ownership Rules

```rust
// 1. Mỗi giá trị có một biến sở hữu (owner)
// 2. Khi owner ra khỏi scope, giá trị bị drop

fn main() {
    let s1 = String::from("hello");  // s1 owns String
    let s2 = s1;                     // ownership moves to s2
    // println!("{}", s1);  // ERROR: s1 no longer valid
    println!("{}", s2);  // OK
}

// Copy types (implement Copy trait)
let x = 5;
let y = x;  // Copy, both valid
println!("{} {}", x, y);  // OK
```

#### Borrowing

```rust
// Immutable borrow
fn calculate_length(s: &String) -> usize {
    s.len()
}

let s1 = String::from("hello");
let len = calculate_length(&s1);  // Borrow s1
println!("{}", s1);  // s1 still valid

// Mutable borrow
fn modify(s: &mut String) {
    s.push_str(" world");
}

let mut s = String::from("hello");
modify(&mut s);
println!("{}", s);  // "hello world"

// Rules:
// - Chỉ có 1 mutable borrow HOẶC nhiều immutable borrows
// - Borrow không sống lâu hơn owner
```

#### Reference

```rust
// &
let s = String::from("hello");
let r = &s;  // Immutable reference
let r2 = &s;  // Multiple immutable OK
println!("{}", r);

// &mut
let mut s = String::from("hello");
let r = &mut s;
r.push_str(" world");
println!("{}", s);

// Dereference
let x = 5;
let r = &x;
assert_eq!(*r, 5);
```

---

### 4.2. Lifetime

#### Lifetime Annotations

```rust
// Lifetime parameters
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// Struct với lifetime
struct Excerpt<'a> {
    part: &'a str,
}

impl<'a> Excerpt<'a> {
    fn announce_and_return(&self, announcement: &str) -> &str {
        println!("{}", announcement);
        self.part
    }
}
```

#### Static Lifetime

```rust
// 'static - tồn tại suốt chương trình
let s: &'static str = "Hello";
static CONSTANT: &'static str = "Global";

// Lifetime elision (compiler infers)
fn first(s: &str) -> &str { s }  // inferred as fn first<'a>(s: &'a str) -> &'a str
```

---

## 5. Tầng 5: Concurrency Model

### 5.1. Concurrency/Async

#### Threads

```rust
use std::thread;
use std::time::Duration;

fn worker(name: &str, delay: u64) {
    println!("{} started", name);
    thread::sleep(Duration::from_secs(delay));
    println!("{} finished", name);
}

fn main() {
    // Tạo thread
    let handle = thread::spawn(|| {
        worker("Thread-1", 2);
    });

    let handle2 = thread::spawn(|| {
        worker("Thread-1", 1);
    });

    handle.join().unwrap();
    handle2.join().unwrap();
}

// Với data
let data = vec![1, 2, 3];
let handle = thread::spawn(move || {
    println!("{:?}", data);
});
```

#### Thread Pool

```rust
// Dùng crossbeam hoặc rayon
use rayon::prelude::*;

let numbers = vec![1, 2, 3, 4];

// Parallel iterator
let result: Vec<i32> = numbers.par_iter().map(|x| x * 2).collect();

// Parallel for_each
numbers.par_iter().for_each(|x| {
    println!("{}", x);
});

// Parallel reduce
let sum: i32 = (0..1000).par_sum();
```

#### Mutex & Arc

```rust
use std::sync::{Arc, Mutex};
use std::thread;

let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];

for _ in 0..10 {
    let counter = Arc::clone(&counter);
    let handle = thread::spawn(move || {
        let mut num = counter.lock().unwrap();
        *num += 1;
    });
    handles.push(handle);
}

for handle in handles {
    handle.join().unwrap();
}

println!("{}", *counter.lock().unwrap());  // 10
```

#### Channels

```rust
use std::sync::mpsc;
use std::thread;

let (tx, rx) = mpsc::channel();

thread::spawn(move || {
    tx.send("Hello from thread").unwrap();
});

let received = rx.recv().unwrap();
println!("{}", received);

// Multiple producers
let (tx, rx) = mpsc::channel();
let tx2 = tx.clone();

thread::spawn(move || tx.send("from t1").unwrap());
thread::spawn(move || tx2.send("from t2").unwrap());

for msg in rx {
    println!("{}", msg);
}
```

#### Async/Await

```rust
// async-std hoặc tokio
use tokio;

#[tokio::main]
async fn main() {
    // Single task
    let result = fetch_data().await;
    println!("{:?}", result);

    // Multiple tasks
    let results = tokio::join!(
        fetch_data(),
        fetch_data(),
    );

    // Parallel spawn
    let task1 = tokio::spawn(async { fetch_data().await });
    let task2 = tokio::spawn(async { fetch_data().await });
}

async fn fetch_data() -> Result<String, reqwest::Error> {
    reqwest::get("https://example.com")
        .await?
        .text()
        .await
}
```

---

## 6. Tầng 6: Paradigm

### 6.1. Functional Programming

#### Pure Function

```rust
// Pure function - không có side effects
fn add(a: i32, b: i32) -> i32 {
    a + b
}

// Impure function - có side effects
use std::io::{self, Write};

fn impure_add(a: i32, b: i32) -> i32 {
    println!("Adding {} and {}", a, b);  // side effect
    a + b
}
```

#### Immutability

```rust
// Dùng let thay vì let mut
let x = 5;
// x = 6;  // Error

// Dùng các methods trả về giá trị mới
let s = "Hello";
let s_upper = s.to_uppercase();  // "HELLO" - s unchanged

let v = vec![1, 2, 3];
let v2 = v.iter().map(|x| x * 2).collect::<Vec<_>>();  // v2 = [2, 4, 6]
```

#### First-Class Function

```rust
// Function là first-class citizens
fn apply<F>(func: F, x: i32) -> i32
where
    F: Fn(i32) -> i32,
{
    func(x)
}

fn double(x: i32) -> i32 {
    x * 2
}

fn main() {
    apply(double, 5);  // 10
    apply(|x| x * x, 5);  // 25
}
```

#### Function Composition

```rust
// Compose function
fn compose<A, B, C, F, G>(f: F, g: G) -> impl Fn(A) -> C
where
    F: Fn(A) -> B,
    G: Fn(B) -> C,
{
    move |x| g(f(x))
}

fn main() {
    let f = compose(|x: i32| x + 1, |x: i32| x * 2);
    f(3);  // (3 + 1) * 2 = 8
}
```

#### Currying

```rust
// Curried function
fn add(a: i32) -> impl Fn(i32) -> i32 {
    move |b| a + b
}

fn main() {
    let add_5 = add(5);
    add_5(3);  // 8
    add(1)(2);  // 3
}
```

#### Partial Application

```rust
fn power(base: i32, exponent: i32) -> i32 {
    base.pow(exponent as u32)
}

fn main() {
    let square = |x| power(x, 2);
    let cube = |x| power(x, 3);

    square(5);  // 25
    cube(5);    // 125
}
```

---

## 7. Tầng 7: Error Handling

### 7.1. Xử Lý Lỗi (Error Handling)

#### Result

```rust
// Result<T, E>
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("Division by zero".to_string())
    } else {
        Ok(a / b)
    }
}

// Pattern matching
match divide(10.0, 2.0) {
    Ok(result) => println!("Result: {}", result),
    Err(e) => println!("Error: {}", e),
}

// Unwrap
let result = divide(10.0, 0.0).unwrap();  // Panic

// unwrap_or
let result = divide(10.0, 0.0).unwrap_or(0.0);

// ?
fn read_file() -> Result<String, std::io::Error> {
    let content = std::fs::read_to_string("file.txt")?;
    Ok(content)
}
```

#### Panic

```rust
// Panic
panic!("Something went wrong");

// Assert
assert!(condition, "message");
assert_eq!(a, b);
assert_ne!(a, b);

// Unwrap variants
let value = some_option.unwrap();        // Panic if None
let value = some_option.unwrap_or(default);
let value = some_option.expect("msg");   // Custom message
```

#### Custom Error

```rust
use std::fmt;

#[derive(Debug)]
pub struct ValidationError {
    pub field: String,
    pub message: String,
}

impl fmt::Display for ValidationError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}: {}", self.field, self.message)
    }
}

impl std::error::Error for ValidationError {}

// Usage
fn validate_email(email: &str) -> Result<(), ValidationError> {
    if !email.contains('@') {
        return Err(ValidationError {
            field: "email".to_string(),
            message: "Invalid email format".to_string(),
        });
    }
    Ok(())
}
```

---

### 7.2. Error Types

#### Built-in Error Types

```rust
use std::error::Error;
use std::fmt;

// std::io::Error
std::fs::File::open("nonexistent").err();  // Some(Error)

// std::num::ParseIntError
"abc".parse::<i32>().err();

// std::env::VarError
std::env::var("MISSING").err();

// Custom với thiserror
use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),

    #[error("Parse error: {0}")]
    Parse(#[from] std::num::ParseIntError),

    #[error("Custom: {message}")]
    Custom { message: String },
}
```

---

## 8. Tầng 8: Module & Organization

### 8.1. Import/Module

#### Module System

```rust
// lib.rs hoặc main.rs

mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {
            println!("Added to waitlist");
        }

        fn seat_at_table() {}
    }

    pub mod serving {
        pub fn take_order() {}

        pub fn serve_order() {}

        pub fn take_payment() {}
    }
}

// Sử dụng
fn eat_at_restaurant() {
    // Absolute path
    crate::front_of_house::hosting::add_to_waitlist();

    // Relative path
    front_of_house::serving::take_order();
}

// Use
use crate::front_of_house::hosting;
hosting::add_to_waitlist();
```

#### Re-exports

```rust
pub use crate::front_of_house::hosting;
```

---

### 8.2. Traits & Generics

```rust
// Trait definition
pub trait Summary {
    fn summarize(&self) -> String;
}

// Implement trait
pub struct Article {
    pub title: String,
    pub author: String,
}

impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{} by {}", self.title, self.author)
    }
}

// Generic trait
pub trait Container<T> {
    fn add(&mut self, item: T);
    fn get(&self, index: usize) -> Option<&T>;
}
```

---

## 9. Tầng 9: I/O & Networking

### 9.1. HTTP & Networking

#### reqwest

```rust
// GET request
let response = reqwest::blocking::get("https://example.com")
    .unwrap()
    .text()
    .unwrap();

// POST request
let client = reqwest::blocking::Client::new();
let response = client.post("https://api.example.com/users")
    .json(&serde_json::json!({
        "name": "John",
        "email": "john@example.com"
    }))
    .send()
    .unwrap();

// With headers
let response = client.get("https://api.example.com")
    .header("Authorization", "Bearer token")
    .send()
    .unwrap();

// Error handling
match response.status() {
    reqwest::StatusCode::OK => println!("Success"),
    reqwest::StatusCode::NOT_FOUND => println!("Not found"),
    _ => println!("Error"),
}
```

#### async HTTP (tokio)

```rust
#[tokio::main]
async fn main() -> Result<(), reqwest::Error> {
    let client = reqwest::Client::new();

    // GET
    let response = client.get("https://example.com")
        .send()
        .await?;

    // POST
    let response = client.post("https://api.example.com/users")
        .json(&serde_json::json!({"name": "John"}))
        .send()
        .await?;

    // Multiple requests
    let results = tokio::join!(
        client.get("https://example.com/1").send(),
        client.get("https://example.com/2").send(),
    );

    Ok(())
}
```

---

### 9.2. File I/O

#### Read File

```rust
use std::fs;
use std::io;

// Read all
let content = fs::read_to_string("file.txt").unwrap();

// Read as bytes
let bytes = fs::read("file.bin").unwrap();

// Read line by line
let file = fs::File::open("file.txt").unwrap();
let reader = io::BufReader::new(file);
for line in io::BufRead::lines(reader) {
    println!("{}", line.unwrap());
}
```

#### Write File

```rust
use std::fs;

// Write
fs::write("output.txt", "Hello World").unwrap();

// Append
use std::fs::OpenOptions;
let mut file = OpenOptions::new()
    .append(true)
    .open("log.txt")
    .unwrap();
use std::io::Write;
writeln!(file, "New log entry").unwrap();

// Binary write
fs::write("output.bin", b"\x00\x01\x02").unwrap();
```

#### Path

```rust
use std::path::Path;
use std::fs;

let path = Path::new("file.txt");

// Check existence
path.exists();
path.is_file();
path.is_dir();

// Get info
path.extension();  // Some("txt")
path.file_stem();   // Some("file")
path.parent();      // Some("...")

// Glob
for entry in glob::glob("*.txt").unwrap() {
    println!("{:?}", entry);
}
```

#### JSON

```rust
use serde::{Deserialize, Serialize};
use serde_json;

#[derive(Debug, Serialize, Deserialize)]
struct User {
    name: String,
    email: String,
}

// Serialize to JSON string
let user = User {
    name: "John".to_string(),
    email: "john@example.com".to_string(),
};
let json_str = serde_json::to_string(&user).unwrap();

// Deserialize
let parsed: User = serde_json::from_str(&json_str).unwrap();

// Pretty print
let json_str = serde_json::to_string_pretty(&user).unwrap();

// Read/Write file
let json = serde_json::to_string_pretty(&user).unwrap();
std::fs::write("user.json", json).unwrap();

let content = std::fs::read_to_string("user.json").unwrap();
let user: User = serde_json::from_str(&content).unwrap();
```

---

## 10. Tầng 10: Data & Serialization

### 10.1. JSON & Serialization

```rust
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct User {
    name: String,
    age: u32,
    active: bool,
}

fn main() {
    let user = User {
        name: "John".to_string(),
        age: 30,
        active: true,
    };

    // Serialize
    let json = serde_json::to_string(&user).unwrap();
    println!("{}", json);

    // Deserialize
    let parsed: User = serde_json::from_str(&json).unwrap();
    println!("{:?}", parsed);

    // With JSON value
    let value: serde_json::Value = serde_json::from_str(r#"{"name": "John"}"#).unwrap();
    println!("{}", value["name"]);
}
```

### 10.2. Date & Time

```rust
use chrono::{DateTime, Utc, Local, NaiveDate, NaiveTime};

// Current
let now = Utc::now();
let local = Local::now();

// Create
let dt = DateTime::parse_from_rfc3339("2024-01-15T10:30:00Z").unwrap();
let date = NaiveDate::from_ymd_opt(2024, 1, 15).unwrap();
let time = NaiveTime::from_hms_opt(10, 30, 0).unwrap();

// Format
println!("{}", now.format("%Y-%m-%d %H:%M:%S"));  // "2024-01-15 10:30:00"

// Parse
let dt = DateTime::parse_from_str("2024-01-15 10:30:00", "%Y-%m-%d %H:%M:%S").unwrap();

// Arithmetic
use chrono::Duration;
let tomorrow = now + Duration::days(1);
let last_week = now - Duration::weeks(1);

// Compare
let dt1 = Utc::now();
let dt2 = Utc::now();
let diff = dt2.signed_duration_since(dt1);
```

### 10.3. Regular Expression

```rust
use regex::Regex;

fn main() {
    let text = "My email is john@example.com";

    // Match
    let re = Regex::new(r"[\w.-]+@[\w.-]+").unwrap();
    if let Some(m) = re.find(text) {
        println!("Found: {}", m.as_str());
    }

    // Find all
    let emails: Vec<&str> = re.find_iter(text).map(|m| m.as_str()).collect();
    println!("{:?}", emails);

    // Capture groups
    let re = Regex::new(r"(?P<user>[\w.-]+)@(?P<domain>[\w.-]+)").unwrap();
    let caps = re.captures(text).unwrap();
    println!("User: {}, Domain: {}", &caps["user"], &caps["domain"]);

    // Replace
    let re = Regex::new(r"\d+").unwrap();
    let result = re.replace_all("test 123 abc 456", "#");
    println!("{}", result);  // "test # abc #"
}
```

---

## 11. Tầng 11: Development Practices

### 11.1. Testing

#### Unit Tests

```rust
// Trong cùng file
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn another() {
        assert!(true);
    }

    #[test]
    #[should_panic]
    fn it_panics() {
        panic!("This test panics");
    }

    #[test]
    fn result_test() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err("Math failed".to_string())
        }
    }
}
```

#### Integration Tests

```rust
// tests/integration_test.rs
use my_crate::add;

#[test]
fn test_add() {
    assert_eq!(add(2, 2), 4);
}
```

#### Doc Tests

```rust
/// Example
///
/// ```
/// let result = my_crate::add(2, 2);
/// assert_eq!(result, 4);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

#### Benchmark

```rust
// cargo bench
#[bench]
fn bench_add(b: &mut Bencher) {
    b.iter(|| add(2, 2));
}
```

### 11.2. Logging

```rust
use log::{info, warn, error, debug};

fn main() {
    env_logger::init();

    debug!("Debug message");
    info!("Info message");
    warn!("Warning message");
    error!("Error message");
}
```

### 11.3. Configuration

#### Environment Variables

```rust
use std::env;

// Read
let db_host = env::var("DB_HOST").unwrap_or_else(|_| "localhost".to_string());
let db_port: u16 = env::var("DB_PORT")
    .unwrap_or("5432".to_string())
    .parse()
    .unwrap_or(5432);

// .env file
dotenvy::dotenv().ok();
let api_key = env::var("API_KEY").unwrap();
```

### 11.4. Build & Package Management

```bash
# Cargo
cargo new my_project
cargo build
cargo run
cargo test
cargo bench
cargo doc
cargo publish
```

---

## 12. Tầng 12: Advanced Concepts

### 12.1. Advanced Concepts

#### Reflection (limited)

```rust
// Rust không có runtime reflection
// Dùng Any trait
use std::any::Any;

fn print_type<T: Any>(value: &T) {
    if let Some(string) = value.type_id() {
        println!("Type: {:?}", string);
    }
}
```

#### Macro

```rust
// Declarative macro
macro_rules! vec {
    ( $( $x:expr ),* ) => {
        {
            let mut temp_vec = Vec::new();
            $(
                temp_vec.push($x);
            )*
            temp_vec
        }
    };
}

// Usage
let v = vec![1, 2, 3];

// Procedural macro
#[derive(Debug)]
struct Point { x: i32, y: i32 }
```

#### Unsafe Code

```rust
unsafe fn dangerous() {
    // Unsafe operations
}

// Dereference raw pointer
let mut num = 5;
let r = &mut num as *mut i32;
unsafe {
    *r = 10;
}

// Call unsafe function
unsafe {
    dangerous();
}
```

---

## 13. Tầng 13: Memory Layout

### 13.1. Struct Layout

```rust
// Default: Rust organizes fields for optimal size
#[repr(C)]
struct MyStruct {
    a: u8,   // 1 byte + 7 padding
    b: u32,  // 4 bytes
    c: u8,   // 1 byte + 3 padding
}

// C-like (no padding)
#[repr(C, packed)]
struct Packed {
    a: u8,
    b: u32,
    c: u8,
}
```

### 13.2. Memory Alignment

```rust
// Default alignment
#[repr(align(16))]
struct Aligned {
    value: u64,
}
```

---

## 14. Tầng 14: Compilation Model

### 14.1. Compilation

```bash
# Compile
rustc main.rs

# Với optimizations
rustc -O main.rs

# Compile to different targets
rustc --target x86_64-unknown-linux-gnu main.rs
```

### 14.2. Cargo

```toml
# Cargo.toml
[package]
name = "my_crate"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = "1.0"
serde_json = "1.0"
tokio = { version = "1.0", features = ["full"] }

[dev-dependencies]
criterion = "0.5"

[build-dependencies]

[features]
default = ["fast"]
fast = []
slow = []

[[bin]]
name = "my_binary"
path = "src/main.rs"
```

---

## 15. Tầng 15: Linking Model

### 15.1. Linking

```rust
// Static linking (default)
#[link(name = "ssl")]
extern "C" {
    pub fn SSL_connect(s: *mut SSL) -> c_int;
}

// Dynamic linking
// Dùng std::process::Command để load DLL/so
```

---

## 16. Tầng 16: Runtime

### 16.1. No Runtime

```rust
// Rust không có runtime như GC
// Code compiled thành native binary
// Không có overhead

fn main() {
    println!("Hello, no runtime!");
}
```

### 16.2. Panic Handling

```rust
// Default: unwind
#[panic = "unwind"]
fn main() { }

// Abort on panic
#[panic = "abort"]
fn main() { }

// Catch panic
use std::panic;

let result = panic::catch_unwind(|| {
    panic!("Test panic");
});

if result.is_err() {
    println!("Caught panic");
}
```

---

## 17. Tầng 17: Language Design Patterns

### 17.1. RAII

```rust
struct File {
    file: std::fs::File,
}

impl File {
    fn open(path: &str) -> std::io::Result<Self> {
        Ok(File {
            file: std::fs::File::open(path)?,
        })
    }
}

impl Drop for File {
    fn drop(&mut self) {
        // Cleanup khi ra khỏi scope
        println!("Closing file");
    }
}

fn main() {
    let _file = File::open("test.txt").unwrap();
    // File auto closed khi _file dropped
}
```

### 17.2. Move Semantics

```rust
fn consume(s: String) {
    println!("{}", s);
}  // s dropped

fn main() {
    let s = String::from("hello");
    consume(s);
    // s đã bị move, không thể dùng lại
}
```

---

## 18. Tầng 18: Standard Library

### 18.1. Collections

```rust
// Vec - dynamic array
let mut v = Vec::new();
v.push(1);
v.push(2);
let third = v.get(2);

// vec! macro
let v = vec![1, 2, 3];

// HashMap
use std::collections::HashMap;
let mut map = HashMap::new();
map.insert("key", "value");
let value = map.get("key");

// BTreeMap (ordered)
use std::collections::BTreeMap;

// HashSet
use std::collections::HashSet;
let mut set = HashSet::new();
set.insert(1);

// VecDeque
use std::collections::VecDeque;
let mut deque = VecDeque::new();
deque.push_front(0);
deque.push_back(1);

// BinaryHeap (max heap)
use std::collections::BinaryHeap;
let mut heap = BinaryHeap::new();
heap.push(3);
heap.push(1);
heap.push(5);
```

### 18.2. Utilities

#### Option & Result

```rust
// Option methods
let x = Some(5);
x.is_some();
x.is_none();
x.map(|v| v * 2);           // Some(10)
x.filter(|v| *v > 3);       // Some(5)
x.or(Some(0));              // Some(5)
x.unwrap_or(0);             // 5

// Result methods
let x: Result<i32, &str> = Ok(5);
x.is_ok();
x.is_err();
x.map(|v| v * 2);           // Ok(10)
x.map_err(|e| e);           // Ok(5)
x.unwrap_or(0);             // 5
x.ok();                     // Some(5)
x.err();                    // None
```

#### Iterator

```rust
// Iterator traits and methods
let v = vec![1, 2, 3, 4, 5];

v.iter().next();        // Some(&1)
v.iter().count();       // 5
v.iter().sum::<i32>();  // 15
v.iter().product::<i32>(); // 120

// Lazy methods
v.iter().map(|x| x * 2).filter(|x| *x > 4).collect::<Vec<_>>();
```

### 18.3. I/O & System

```rust
// Command line args
use std::env;
let args: Vec<String> = env::args().collect();

// Environment
env::var("PATH").ok();
env::current_dir().ok();

// Process
use std::process::Command;
let output = Command::new("ls")
    .arg("-la")
    .output()
    .unwrap();

// Subprocess
std::process::exit(0);
```

---

## 19. Tầng 19: Ecosystem

### 19.1. Web Frameworks

#### Actix-web

```rust
use actix_web::{web, App, HttpResponse, HttpServer, Responder};

async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello!")
}

async fn get_users() -> impl Responder {
    HttpResponse::Ok().json(vec![
        serde_json::json!({"name": "John"})
    ])
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/", web::get().to(hello))
            .route("/users", web::get().to(get_users))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
```

#### Axum

```rust
use axum::{
    routing::get,
    Router,
};

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(|| async { "Hello, World!" }))
        .route("/users", get(|| async { serde_json::json!([]) }));

    axum::Server::bind(&"0.0.0.0:3000".parse().unwrap())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```

### 19.2. Database & ORM

#### Diesel

```rust
// Schema
table! {
    users {
        id -> Integer,
        name -> VarChar,
        email -> VarChar,
    }
}

use diesel::prelude::*;

pub fn create_user(conn: &mut SqliteConnection, name: &str, email: &str) -> User {
    let new_user = NewUser { name, email };
    diesel::insert_into(users::table)
        .values(&new_user)
        .get_result(conn)
        .expect("Error creating user")
}
```

#### SQLx

```rust
use sqlx::{SqlitePool, Row};

#[derive(Debug)]
struct User {
    id: i64,
    name: String,
}

async fn get_users(pool: &SqlitePool) -> Result<Vec<User>, sqlx::Error> {
    let rows = sqlx::query("SELECT id, name FROM users")
        .fetch_all(pool)
        .await?;

    let users = rows
        .iter()
        .map(|row| User {
            id: row.get("id"),
            name: row.get("name"),
        })
        .collect();

    Ok(users)
}
```

### 19.3. Testing

```rust
// Mock với mockall
#[cfg(test)]
mod tests {
    use mockall::predicate::*;
    use mockall::*;

    #[mock]
    trait MyTrait {
        fn do_something(&self, x: i32) -> i32;
    }

    #[test]
    fn test_mock() {
        let mut mock = MockMyTrait::new();
        mock.expect_do_something()
            .with(eq(5))
            .returning(|x| x * 2);

        assert_eq!(mock.do_something(5), 10);
    }
}
```

---

## 20. Tầng 20: Toolchain

### 20.1. Build & Package Management

```bash
# Rustup
rustup update
rustup self update
rustup toolchain list
rustup target add x86_64-unknown-linux-gnu

# Cargo
cargo new my_project
cargo build
cargo build --release
cargo run
cargo test
cargo test --release
cargo bench
cargo doc --open
cargo publish

# Dependencies
cargo tree           # Show dependency tree
cargo outdated      # Check for outdated deps
cargo update        # Update Cargo.lock

# Workspace
cargo workspace     # Manage multiple crates
```

### 20.2. Code Quality

```bash
# Clippy (linter)
cargo clippy
cargo clippy -- -D warnings

# Rustfmt (formatter)
cargo fmt
cargo fmt -- --check

# Miri (undefined behavior detector)
cargo +nightly miri test

# Security audit
cargo audit
```

### 20.3. IDE & Debugging

```rust
// Debug
println!("Debug: {:?}", value);

// dbg! macro (Rust 1.32+)
let x = 5;
dbg!(x);

// assert!
assert_eq!(a, b);
assert_ne!(a, b);

// VS Code / CLion debugging
// Set breakpoints in IDE
```

---

## Tổng Kết

Rust là ngôn ngữ:

- **Static typing** với type inference mạnh
- **Memory safety** không cần GC (ownership, borrowing, lifetime)
- **Zero-cost abstractions** với high-level features
- **Concurrent** với fearless concurrency
- **Systems programming** nhưng an toàn
- **Modern features**: Pattern matching, Traits, Generics, Async/Await

### Rust Version History

| Version  | Release Date | Key Features                                |
|----------|-------------|---------------------------------------------|
| Rust 1.0 | 2015-05-15  | First stable release                       |
| Rust 1.19| 2017-07-20 | Basic concurrency primitives               |
| Rust 1.31| 2018-12-19 | Rust 2018 edition                          |
| Rust 1.39| 2019-11-07 | async/await stability                       |
| Rust 1.56| 2021-10-21 | Rust 2021 edition                           |
| Rust 1.68| 2022-03-24 | Pinning, const generics                    |
| Rust 1.70| 2023-06-01 | Once-cell, std::sync::OnceLock             |
| Rust 1.75| 2024-02-08 | Rust 2024 edition (planned)                |
