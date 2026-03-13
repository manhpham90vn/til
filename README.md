# Tổng Hợp So Sánh Syntax

## Mục Lục

1. [Phân Loại Ngôn Ngữ](#1-phân-loại-ngôn-ngữ)
2. [Cấu Trúc Khái Niệm Theo Tầng](#2-cấu-trúc-khái-niệm-theo-tầng)

### Các Tầng Khái Niệm

- [Tầng 1: Syntax & Semantics](#tầng-1-syntax--semantics-cú-pháp--ngữ-nghĩa)
- [Tầng 2: Type System](#tầng-2-type-system-hệ-thống-kiểu)
- [Tầng 3: OOP & Type Relationships](#tầng-3-oop--type-relationships-oop--quan-hệ-kiểu)
- [Tầng 4: Memory Model](#tầng-4-memory-model-mô-hình-bộ-nhớ)
- [Tầng 5: Concurrency Model](#tầng-5-concurrency-model-mô-hình-đồng-thời)
- [Tầng 6: Paradigm](#tầng-6-paradigm-mô-hình-lập-trình)
- [Tầng 7: Error Handling](#tầng-7-error-handling-xử-lý-lỗi)
- [Tầng 8: Module & Organization](#tầng-8-module--organization-tổ-chức--module)
- [Tầng 9: I/O & Networking](#tầng-9-io--networking-nhậpxuất--mạng)
- [Tầng 10: Data & Serialization](#tầng-10-data--serialization-dữ-liệu--serialization)
- [Tầng 11: Development Practices](#tầng-11-development-practices-thực-hành-phát-triển)
- [Tầng 12: Advanced Concepts](#tầng-12-advanced-concepts-khái-niệm-nâng-cao)
- [Tầng 13: Memory Layout](#tầng-13-memory-layout-bố-trí-bộ-nhớ)
- [Tầng 14: Compilation Model](#tầng-14-compilation-model-mô-hình-biên-dịch)
- [Tầng 15: Linking Model](#tầng-15-linking-model-mô-hình-liên-kết)
- [Tầng 16: Runtime](#tầng-16-runtime)
- [Tầng 17: Language Design Patterns](#tầng-17-language-design-patterns-mẫu-thiết-kế-ngôn-ngữ)
- [Tầng 18: Standard Library](#tầng-18-standard-library-thư-viện-chuẩn)
- [Tầng 19: Ecosystem](#tầng-19-ecosystem-hệ-sinh-thái)
- [Tầng 20: Toolchain](#tầng-20-toolchain-công-cụ-phát-triển)

---

## 1. Phân Loại Ngôn Ngữ

### Theo Loại Ngôn Ngữ

| Ngôn ngữ       | Loại                | Biên dịch/Thông dịch | Typing            |
| -------------- | ------------------- | -------------------- | ----------------- |
| [**C**](C.md)          | Systems Programming | Compiled (AOT)       | Static, Weak      |
| [**C++**](C++.md)        | Systems Programming | Compiled (AOT)       | Static, Strong    |
| [**Java**](Java.md)       | Enterprise/JVM      | Compiled (Bytecode)  | Static, Strong    |
| [**Rust**](Rust.md)       | Systems Programming | Compiled (AOT)       | Static, Strong    |
| [**Go**](Go.md)         | Systems/Server      | Compiled (AOT)       | Static, Strong    |
| [**Python**](Python.md)     | General Purpose     | Interpreted/Bytecode | Dynamic, Strong   |
| [**TypeScript**](TypeScript.md) | Web/JS Superset     | Transpiled to JS     | Static (optional) |
| [**JavaScript**](JavaScript.md) | Web Scripting       | Interpreted/JIT      | Dynamic, Duck     |
| **Swift**      | iOS/macOS           | Compiled (AOT)       | Static, Strong    |
| **Kotlin**     | Android/JVM         | Compiled (Bytecode)  | Static, Strong    |
| **Dart**       | Flutter/Web         | Compiled (AOT/JIT)   | Static, Strong    |
| [**PHP**](PHP.md)        | Web Backend         | Interpreted          | Dynamic, Weak     |

### Theo Paradigm

| Ngôn ngữ       | Paradigm                                           |
| -------------- | -------------------------------------------------- |
| **C**          | Procedural, Imperative                             |
| **C++**        | Multi-paradigm (Procedural, OO, Generic)           |
| **Java**       | Object-Oriented, (Functional từ Java 8+)           |
| **Rust**       | Multi-paradigm (Functional, OO, Imperative)        |
| **Go**         | Concurrent, Imperative, Procedural                 |
| **Python**     | Multi-paradigm (Functional, OO, Procedural)        |
| **TypeScript** | Object-Oriented, Functional                        |
| **JavaScript** | Multi-paradigm (Prototype-based, Functional)       |
| **Swift**      | Multi-paradigm (Protocol-oriented, Functional, OO) |
| **Kotlin**     | Multi-paradigm (Functional, OO)                    |
| **Dart**       | Multi-paradigm (Class-based, Functional)           |
| **PHP**        | Multi-paradigm (Procedural, OO)                    |

### Ecosystem & Use Cases

| Ngôn ngữ       | Use Cases                                                      |
| -------------- | -------------------------------------------------------------- |
| **C**          | Systems programming, Embedded systems, OS kernels, Drivers    |
| **C++**        | Systems programming, Game engines, High-performance apps      |
| **Java**       | Enterprise apps, Android, Backend (Spring), Big Data          |
| **Rust**       | Systems programming, WebAssembly, CLI tools, Blockchain        |
| **Go**         | Backend servers, Cloud services, DevOps tools, Microservices   |
| **Python**     | Data science, ML/AI, Automation, Web (Django/Flask), Scripting |
| **TypeScript** | Frontend (React, Vue, Angular), Node.js, Enterprise apps       |
| **JavaScript** | Frontend web, Node.js, Mobile (React Native)                   |
| **Swift**      | iOS/macOS apps, Apple ecosystem                                |
| **Kotlin**    | Android, Backend (Spring), Multiplatform                       |
| **Dart**       | Flutter (Cross-platform mobile), Web                           |
| **PHP**        | Web backend (Laravel, Symfony), CMS (WordPress)                |

---

## 2. Cấu Trúc Khái Niệm Theo Tầng

### Tầng 1: Syntax & Semantics (Cú pháp & Ngữ nghĩa)

#### 1.1. Khai Báo Biến (Variable Declaration)

- **Mutable** - Biến có thể thay đổi giá trị
- **Immutable** - Biến không thể thay đổi sau khi khởi tạo
- **Type Annotation** - Khai báo kiểu dữ liệu tường minh
- **Type Inference** - Ngôn ngữ tự suy luận kiểu
- **Constant** - Hằng số compile-time
- **Static Variable** - Biến tĩnh (class-level)
- **Global Variable** - Biến toàn cục
- **Shadowing** - Biến cùng tên trong scope nhỏ
- **Scope** - Phạm vi biến (block/function/global scope)
- **Hoisting** - Đưa khai báo lên đầu scope (JavaScript)

#### 1.2. Khai Báo Hàm (Function Declaration)

- **Function** - Hàm thông thường
- **Return Type** - Kiểu dữ liệu trả về
- **Parameters** - Tham số đầu vào
- **Arrow Function** - Hàm mũi tên (inline/lambda)
- **Method** - Hàm trong class/struct
- **Constructor** - Hàm khởi tạo
- **Destructor** - Hàm hủy (giải phóng tài nguyên)
- **Variadic Parameters** - Tham số không xác định trước
- **Default Parameters** - Tham số mặc định
- **Named Parameters** - Tham số có tên
- **Closure** - Hàm closure (capture biến bên ngoài)
- **Higher-Order Function** - Hàm nhận/trả về hàm khác
- **Function Overloading** - Hàm cùng tên, tham số khác (C++, Java, Kotlin)
- **Inline Function** - Hàm inline (Kotlin, C++)
- **Tail Recursive Function** - Hàm đệ quy đuôi (Kotlin tailrec, Scala)

#### 1.3. Vòng Lặp (Loops)

- **For Loop** - Vòng lặp với số lần xác định
- **For-each/Range** - Duyệt qua collection
- **While Loop** - Vòng lặp với điều kiện
- **Infinite Loop** - Vòng lặp vô hạn
- **Do-While** - Thực hiện ít nhất 1 lần
- **Loop Control** - Break, continue, labeled loops
- **Iterator** - Duyệt qua iterator
- **List Comprehension** - Tạo list từ iterable (Python)
- **Stream Loop** - Duyệt qua stream (Java/Go)
- **Generator/Yield** - Hàm sinh giá trị lười biếng (Python, JS, Kotlin)

#### 1.4. Điều Kiện (Conditionals)

- **If-Else** - Rẽ nhánh cơ bản
- **Switch/Match** - Rẽ nhánh nhiều trường hợp
- **Ternary** - Toán tử điều kiện ngắn
- **Pattern Matching** - So khớp pattern (Rust, Swift, Kotlin)
- **Guarded Condition** - Điều kiện bảo vệ trong if
- **Early Return** - Trả về sớm
- **Elvis Operator** - Toán tử Elvis (??)
- **Null Coalescing** - Giá trị mặc định khi null
- **When Expression** - Biểu thức when (Kotlin)
- **Guard Let** - Unwrap an toàn với guard (Swift)

#### 1.5. Destructuring & Spread (Phân rã & Toán tử mở rộng)

- **Destructuring Assignment** - Phân rã giá trị từ array/object (JS/TS, Python, Rust, Kotlin)
- **Spread Operator** - Toán tử mở rộng (...) (JS/TS, Kotlin)
- **Rest Parameters** - Gom các tham số còn lại
- **Tuple Destructuring** - Phân rã tuple (Rust, Python, Swift)
- **Struct/Object Destructuring** - Phân rã struct/object

---

### Tầng 2: Type System (Hệ thống kiểu)

#### 2.1. Kiểu Dữ Liệu Cơ Bản (Primitive Types)

- **Integer** - Số nguyên (int, i32, u64...)
- **Float** - Số thực (float, f64, Double)
- **Boolean** - Đúng/Sai (bool, boolean)
- **String** - Chuỗi ký tự (String, str, string)
- **Character** - Ký tự đơn (char, rune)
- **Byte** - Byte (u8, byte)
- **Array** - Mảng cố định kích thước
- **List/ArrayList** - Danh sách (dynamic array)
- **Set** - Tập hợp không trùng lặp
- **Map/Dict/HashMap** - Từ điển (key-value)
- **Tuple** - Bộ giá trị
- **Range** - Khoảng giá trị
- **Void/Unit/Nothing** - Kiểu rỗng / không có giá trị
- **Any/Object** - Kiểu gốc (top type)

#### 2.2. Enum

- **Basic Enum** - Enum cơ bản
- **Enum with Values** - Enum có giá trị
- **Enum with Methods** - Enum có phương thức
- **Associated Values** - Giá trị đi kèm (Swift)
- **Pattern Matching Enum** - So khớp enum
- **Sealed Interface** - Interface giới hạn implement (Kotlin, Java 17+)

#### 2.3. Nullable/Option Types

- **Nullable** - Có thể null
- **Optional** - Giá trị có hoặc không
- **Null Check** - Kiểm tra null
- **Unwrap** - Lấy giá trị từ optional
- **Safe Unwrap** - Unwrap an toàn
- **None/Null Representation** - Cách biểu diễn không có giá trị
- **Optional Chaining** - Chuỗi gọi optional

#### 2.4. Null Safety

- **Elvis Operator** - Toán tử Elvis (??)
- **Safe Call** - Gọi an toàn (?.)
- **Non-null Assertion** - Khẳng định không null
- **Let/Apply/Also** - Scope functions với null
- **Null Object Pattern** - Pattern thay thế null

#### 2.5. Generics

- **Generic Function** - Hàm generic
- **Generic Class** - Class generic
- **Type Constraint** - Ràng buộc kiểu
- **Generic Trait** - Trait generic
- **Where Clause** - Điều kiện ràng buộc
- **Bounds** - Giới hạn kiểu
- **Covariance/Contravariance** - Biến đổi kiểu
- **Type Erasure** - Xóa kiểu (Java)

#### 2.8. Union & Intersection Types (Kiểu hợp & Kiểu giao)

- **Union Type** - Kiểu hợp (A | B) (TypeScript, Python)
- **Intersection Type** - Kiểu giao (A & B) (TypeScript)
- **Tagged Union** - Union có nhãn (Rust enum, TypeScript discriminated union)
- **Type Narrowing** - Thu hẹp kiểu qua kiểm tra điều kiện
- **Type Guard** - Hàm kiểm tra kiểu (TypeScript)
- **Type Alias** - Đặt tên alias cho kiểu

#### 2.6. Collection Operations

- **Map/Transform** - Biến đổi từng phần tử
- **Filter** - Lọc phần tử
- **Reduce/Fold** - Gộp thành một giá trị
- **FlatMap** - Biến đổi và làm phẳng
- **Sort** - Sắp xếp
- **GroupBy** - Nhóm theo key
- **Find/First/Last** - Tìm phần tử
- **Any/All/None** - Kiểm tra điều kiện
- **Take/Skip** - Lấy/bỏ phần tử
- **Chunk** - Chia thành chunks
- **Zip** - Kết hợp 2 collections

#### 2.7. String Operations

- **Concatenation** - Nối chuỗi
- **Interpolation** - Chèn biến vào chuỗi
- **Template String** - Chuỗi template
- **Split** - Tách chuỗi
- **Join** - Nối mảng thành chuỗi
- **Replace** - Thay thế
- **Trim** - Cắt khoảng trắng
- **Upper/Lower Case** - Chữ hoa/thường
- **Regex Match** - So khớp regex
- **Substring** - Lấy chuỗi con
- **Length** - Độ dài chuỗi
- **Multi-line String** - Chuỗi nhiều dòng (raw string, triple quotes)
- **String Builder** - Xây dựng chuỗi hiệu quả (StringBuilder, StringBuffer)

---

### Tầng 3: OOP & Type Relationships (OOP & Quan hệ kiểu)

#### 3.1. Struct/Class/Object

- **Struct** - Cấu trúc dữ liệu (value type)
- **Class** - Lớp đối tượng (reference type)
- **Constructor** - Hàm tạo đối tượng
- **Data Class** - Class chỉ chứa dữ liệu
- **Object** - Thực thể của class
- **Singleton** - Class chỉ có 1 instance
- **Factory Method** - Phương thức tạo đối tượng
- **Builder Pattern** - Pattern xây dựng đối tượng
- **Static Member** - Thành phần tĩnh (class-level)
- **Instance Member** - Thành phần instance
- **Inner Class** - Class bên trong (có tham chiếu outer)
- **Nested Class** - Class lồng nhau (static, không tham chiếu outer)
- **Anonymous Class** - Class ẩn danh (Java, Kotlin object expression)
- **Companion Object** - Object đồng hành (Kotlin)

#### 3.2. Kế Thừa & Đa Hình (Inheritance & Polymorphism)

- **Inheritance** - Kế thừa từ class cha
- **Superclass/Parent** - Class cha
- **Subclass/Child** - Class con
- **Override** - Ghi đè phương thức
- **Super** - Tham chiếu đến class cha
- **Abstract Class** - Class trừu tượng
- **Sealed Class** - Class giới hạn kế thừa
- **Final Class** - Class không thể kế thừa
- **Polymorphism** - Đa hình
- **Method Overloading** - Nạp chồng phương thức (cùng tên, tham số khác)
- **Composition** - Thành phần hơn là kế thừa
- **Diamond Problem** - Vấn đề đa kế thừa hình thoi (C++, Python MRO)

#### 3.3. Interface/Trait/Protocol

- **Interface** - Định nghĩa contract
- **Trait** - Code reuse (Rust)
- **Protocol** - Contract (Swift, Go)
- **Abstract Method** - Phương thức trừu tượng
- **Default Implementation** - Triển khai mặc định
- **Static Method** - Phương thức tĩnh trong interface
- **Multiple Interface** - Implement nhiều interface
- **Interface Extension** - Mở rộng interface
- **Mixin** - Tái sử dụng code qua mixin (Python, Dart, PHP Trait)
- **Delegation** - Ủy quyền implementation (Kotlin `by`, Go embedding)

#### 3.4. Visibility/Access Modifiers

- **Private** - Chỉ trong cùng file/class
- **Public** - Có thể truy cập từ bên ngoài
- **Protected** - Kế thừa được
- **Internal** - Trong cùng module/project
- **Fileprivate** - Trong cùng file (Swift)
- **Open** - Có thể override (Swift/Kotlin)
- **Default Access** - Quyền truy cập mặc định

---

### Tầng 4: Memory Model (Mô hình bộ nhớ)

#### 4.1. Memory Management

- **Ownership** - Sở hữu (Rust)
- **Borrowing** - Mượn (Rust)
- **Lifetime** - Thời gian sống của tham chiếu
- **Reference Counting** - Đếm tham chiếu (Arc)
- **Garbage Collection** - Thu gom rác
- **Weak Reference** - Tham chiếu yếu
- **Smart Pointer** - Con trỏ thông minh
- **RAII** - Resource Acquisition Is Initialization
- **Stack vs Heap** - Bộ nhớ stack và heap
- **Value Type vs Reference Type** - Kiểu giá trị và kiểu tham chiếu
- **Copy-on-Write** - Sao chép khi ghi (Swift, Rust Cow)

#### 4.2. Property & Getter/Setter

- **Property** - Thuộc tính
- **Getter** - Lấy giá trị
- **Setter** - Đặt giá trị
- **Computed Property** - Thuộc tính tính toán
- **Lazy Property** - Thuộc tính trì hoãn
- **Late Init** - Khởi tạo muộn
- **Backing Field** - Trường lưu trữ

#### 4.3. Memory Safety (An toàn bộ nhớ)

- **Buffer Overflow** - Tràn bộ đệm
- **Dangling Pointer** - Con trỏ lơ lửng
- **Memory Leak** - Rò rỉ bộ nhớ
- **Use-After-Free** - Sử dụng sau khi giải phóng
- **Double Free** - Giải phóng hai lần

---

### Tầng 5: Concurrency Model (Mô hình đồng thời)

#### 5.1. Concurrency/Async

- **Async/Await** - Hàm bất đồng bộ
- **Thread** - Luồng
- **Coroutine** - Coroutine
- **Goroutine** - Goroutine (Go)
- **Future/Promise** - Hứa hẹn kết quả tương lai
- **Task** - Công việc bất đồng bộ
- **Channel** - Kênh truyền tin (Go, Kotlin)
- **Mutex/Lock** - Khóa đồng bộ
- **Atomic** - Biến nguyên tử
- **Await All/Any** - Chờ nhiều task
- **Race Condition** - Điều kiện tranh chấp
- **Deadlock Prevention** - Phòng tránh deadlock
- **Event Loop** - Vòng lặp sự kiện (JS, Dart, Python asyncio)
- **Callback Queue** - Hàng đợi callback
- **Microtask/Macrotask** - Phân loại task trong event loop (JS)
- **Thread Pool** - Nhóm luồng tái sử dụng
- **Semaphore** - Đếm số luồng truy cập đồng thời
- **Barrier** - Rào chắn đồng bộ
- **Read-Write Lock** - Khóa đọc/ghi riêng
- **Structured Concurrency** - Đồng thời có cấu trúc (Kotlin, Swift)

---

### Tầng 6: Paradigm (Mô hình lập trình)

#### 6.1. Functional Programming

- **Pure Function** - Hàm thuần túy (không side effect)
- **Immutability** - Bất biến
- **First-Class Function** - Hàm như giá trị
- **Currying** - Chuyển hàm nhiều tham số thành chuỗi
- **Partial Application** - Áp dụng một phần
- **Function Composition** - Kết hợp hàm
- **Monad** - Monad pattern
- **Functor** - Functor pattern

#### 6.2. Reactive Programming (Lập trình phản ứng)

- **Observable/Stream** - Luồng dữ liệu phản ứng
- **Observer/Subscriber** - Người quan sát/đăng ký
- **Operators** - Toán tử biến đổi stream (map, filter, merge)
- **Backpressure** - Kiểm soát tốc độ dữ liệu
- **Hot/Cold Observable** - Observable nóng/lạnh
- **Flow/StateFlow** - Reactive stream (Kotlin)
- **Combine** - Framework reactive (Swift)
- **RxJS/RxJava** - Reactive Extensions

---

### Tầng 7: Error Handling (Xử lý lỗi)

#### 7.1. Xử Lý Lỗi (Error Handling)

- **Try-Catch** - Bắt exception
- **Result/Option** - Return error as value
- **Error Return** - Trả về lỗi
- **Throw Exception** - Ném ngoại lệ
- **Custom Exception** - Exception tự định nghĩa
- **Finally Block** - Luôn thực thi dù có lỗi
- **Try-with-resources** - Tự động đóng tài nguyên
- **Error Propagation** - Truyền lỗi lên trên
- **Recover** - Khôi phục từ panic (Rust)
- **Defer** - Thực thi khi thoát scope (Go, Swift)
- **Assertion** - Khẳng định điều kiện (assert, precondition)
- **Guard** - Kiểm tra điều kiện và thoát sớm (Swift guard)

#### 7.2. Error Types & Patterns

- **Checked Exception** - Exception bắt buộc xử lý
- **Unchecked Exception** - Exception không bắt buộc
- **Custom Error Type** - Kiểu lỗi tự định nghĩa
- **Error Union** - Hợp các kiểu lỗi
- **Panic** - Lỗi nghiêm trọng (Rust)
- **Error Wrapping** - Bao bọc lỗi thêm context (Go %w, Rust .context())
- **Stack Trace** - Vết ngăn xếp lỗi

---

### Tầng 8: Module & Organization (Tổ chức & Module)

#### 8.1. Import/Export & Module

- **Import** - Nhập module
- **Export** - Xuất module
- **Package** - Gói code
- **Module Alias** - Đặt tên alias cho module
- **Selective Import** - Chỉ nhập phần cần thiết
- **Default Export** - Xuất mặc định
- **Re-export** - Xuất lại từ module khác
- **Namespace** - Không gian tên
- **Circular Dependency** - Phụ thuộc vòng
- **Monorepo/Multi-module** - Tổ chức dự án đa module

#### 8.2. Extension Methods

- **Extension Function** - Mở rộng class không sửa
- **Extension Property** - Mở rộng property
- **Implicit Receiver** - Receiver ngầm định
- **Type Extension** - Mở rộng kiểu dữ liệu

#### 8.3. Operator Overloading

- **Arithmetic Operators** - Toán tử số học
- **Comparison Operators** - Toán tử so sánh
- **Logical Operators** - Toán tử logic
- **Custom Operators** - Toán tử tự định nghĩa
- **Infix Functions** - Hàm infix (Kotlin)
- **Subscript Operator** - Toán tử truy cập [] (Kotlin, Swift, C++)

---

### Tầng 9: I/O & Networking (Nhập/Xuất & Mạng)

#### 9.1. HTTP & Networking

- **HTTP Request** - Gửi request
- **HTTP Response** - Nhận response
- **Headers** - Header của request/response
- **Query Parameters** - Tham số truy vấn
- **Path Parameters** - Tham số đường dẫn
- **Request Body** - Nội dung request
- **Authentication** - Xác thực
- **HTTP Client** - Thư viện gọi HTTP
- **WebSocket** - Giao tiếp hai chiều realtime
- **SSE (Server-Sent Events)** - Server gửi sự kiện một chiều
- **Middleware** - Xử lý trung gian trong request pipeline

#### 9.2. File I/O

- **Read File** - Đọc file
- **Write File** - Ghi file
- **File Path** - Đường dẫn file
- **Stream** - Luồng dữ liệu
- **Buffer** - Bộ đệm
- **Async File I/O** - Đọc/ghi bất đồng bộ

#### 9.3. Database Access (Truy cập cơ sở dữ liệu)

- **Connection Pool** - Nhóm kết nối tái sử dụng
- **Prepared Statement** - Câu lệnh chuẩn bị sẵn
- **Transaction** - Giao dịch (commit/rollback)
- **Connection String** - Chuỗi kết nối

#### 9.4. CLI I/O (Nhập/Xuất dòng lệnh)

- **Stdin/Stdout/Stderr** - Luồng nhập/xuất chuẩn
- **Command Line Parsing** - Phân tích tham số dòng lệnh
- **ANSI Colors** - Màu sắc terminal
- **Interactive Prompt** - Tương tác với người dùng qua terminal

---

### Tầng 10: Data & Serialization (Dữ liệu & Serialization)

#### 10.1. JSON & Serialization

- **Serialize** - Chuyển object thành JSON
- **Deserialize** - Chuyển JSON thành object
- **JSON Encoder/Decoder** - Bộ mã hóa/giải mã
- **Field Mapping** - Ánh xạ trường
- **Naming Strategy** - Quy tắc đặt tên
- **Protobuf** - Protocol Buffers (Google)
- **MessagePack** - Binary serialization format
- **YAML/TOML** - Định dạng cấu hình
- **Binary Serialization** - Serialization dạng nhị phân
- **XML Parsing** - Phân tích XML
- **CSV Parsing** - Phân tích CSV

#### 10.2. Date & Time

- **Current Date/Time** - Thời gian hiện tại
- **Parse/Format** - Chuyển đổi định dạng
- **Timezone** - Múi giờ
- **Duration** - Khoảng thời gian
- **Date Arithmetic** - Tính toán ngày tháng
- **Timestamp** - Dấu thời gian (Unix timestamp)
- **Calendar** - Lịch (Calendar API)

#### 10.3. Regular Expression

- **Pattern** - Mẫu regex
- **Match** - So khớp
- **Replace** - Thay thế
- **Capture Group** - Nhóm bắt
- **Split** - Tách bằng regex

---

### Tầng 11: Development Practices (Thực hành phát triển)

#### 11.1. Annotation/Decorator

- **Annotation** - Chú thích metadata
- **Decorator** - Bổ sung chức năng (Python)
- **Attribute** - Thuộc tính (C#, Swift)
- **Macro** - Macro (Rust)
- **Compile-time** - Thời điểm biên dịch
- **Runtime** - Thời điểm chạy

#### 11.2. Testing

- **Unit Test** - Test đơn vị
- **Integration Test** - Test tích hợp
- **E2E Test** - Test đầu cuối
- **Mock** - Tạo đối tượng giả
- **Stub** - Thay thế implementation
- **Assertion** - Khẳng định kết quả
- **Test Suite** - Bộ test
- **Before/After Hook** - Thiết lập/cleanup
- **Table-Driven Tests** - Test dạng bảng (Go)
- **Snapshot Testing** - So sánh với kết quả lưu trước
- **Code Coverage** - Độ bao phủ code

#### 11.3. Logging

- **Log Levels** - Cấp độ log (debug, info, warn, error)
- **Logger** - Công cụ ghi log
- **Formatted Log** - Log có định dạng
- **Structured Logging** - Log có cấu trúc

#### 11.4. Dependency Injection

- **Constructor Injection** - Tiêm vào constructor
- **Setter Injection** - Tiêm qua setter
- **Interface Injection** - Tiêm interface
- **Service Container** - Container quản lý dependency
- **Factory** - Factory tạo dependency

#### 11.5. Configuration

- **Environment Variables** - Biến môi trường
- **Config File** - File cấu hình
- **Command Line Args** - Tham số dòng lệnh
- **Secret Management** - Quản lý secrets

#### 11.6. Build & Package Management

- **Dependency Manager** - Quản lý thư viện
- **Build Tool** - Công cụ build
- **Linter** - Kiểm tra code style
- **Formatter** - Định dạng code

#### 11.7. Documentation

- **Comment** - Bình luận
- **Doc Comment** - Bình luận tài liệu
- **Type Documentation** - Tài liệu kiểu
- **README** - Tài liệu project

#### 11.8. Design Patterns (Mẫu thiết kế)

- **Observer Pattern** - Mẫu quan sát
- **Strategy Pattern** - Mẫu chiến lược
- **Builder Pattern** - Mẫu xây dựng
- **Repository Pattern** - Mẫu kho dữ liệu
- **Adapter Pattern** - Mẫu chuyển đổi
- **Facade Pattern** - Mẫu mặt tiền
- **Decorator Pattern** - Mẫu trang trí
- **Singleton Pattern** - Mẫu đơn thể

---

### Tầng 12: Advanced Concepts (Khái niệm nâng cao)

#### 12.1. Advanced Concepts

- **Reflection** - Siêu lập trình (Java, Python, PHP)
- **Metadata/Introspection** - Lấy thông tin kiểu lúc runtime
- **Pointer/Reference** - Con trỏ (Rust, Go, C, Swift)
- **Unsafe Code** - Code không an toàn (Rust)
- **Custom Allocator** - Cấp phát bộ nhớ tùy chỉnh
- **Macro/Template** - Meta-programming
- **FFI (Foreign Function Interface)** - Gọi code từ ngôn ngữ khác
- **Coroutine/Fiber** - Lightweight threads
- **Actor Model** - Mô hình actor
- **Type Classes** - Lớp kiểu (Haskell-like)
- **Lazy Evaluation** - Đánh giá lười biếng
- **Tail Call Optimization (TCO)** - Tối ưu gọi đuôi
- **Continuations** - Tiếp tục
- **Software Transactional Memory (STM)** - Bộ nhớ giao dịch
- **Zero-cost Abstractions** - Trừu tượng không chi phí
- **Move Semantics** - Ngữ nghĩa di chuyển
- **Lock-free Data Structures** - Cấu trúc dữ liệu không khóa
- **Domain-Specific Language (DSL)** - Ngôn ngữ miền cụ thể
- **Compile-time Metaprogramming** - Lập trình meta lúc biên dịch (Rust proc_macro, C++ template metaprogramming)
- **Code Generation** - Sinh code tự động (Java annotation processing, Go generate)
- **Phantom Types** - Kiểu ảo để đảm bảo an toàn tại compile-time

---

### Tầng 13: Memory Layout (Bố trí bộ nhớ)

#### 13.1. Struct Layout

- **Struct Packing** - Sắp xếp fields không padding
- **Field Order** - Thứ tự fields ảnh hưởng kích thước
- **Alignment** - Căn chỉnh bộ nhớ
- **Size Of** - Kích thước struct
- **Memory Layout** - Cách struct được lưu trong memory

#### 13.2. Object Layout

- **Header** - Object header (metadata, GC info)
- **Object Header** - Class pointer, sync block
- **Array Layout** - Cách array được lưu
- **String Layout** - Cách string được lưu (UTF-8, UTF-16)

#### 13.3. VTable (Virtual Table)

- **Virtual Method Table** - Bảng phương thức ảo
- **Method Dispatch** - Cách gọi phương thức ảo
- **Interface VTable** - VTable cho interface
- **Multiple Inheritance** - VTable với đa kế thừa

#### 13.4. Cache Locality

- **Spatial Locality** - Dữ liệu gần nhau trong memory
- **Temporal Locality** - Dữ liệu được dùng gần nhau về thời gian
- **Cache Line** - Đơn vị cache (thường 64 bytes)
- **Prefetching** - Tải trước dữ liệu vào cache
- **False Sharing** - Chia sẻ false giữa các CPU cores

#### 13.5. Padding

- **Struct Padding** - Thêm bytes để căn chỉnh
- **Alignment Padding** - Padding cho alignment requirements
- **Packed Struct** - Struct không padding
- **Memory Alignment** - Căn chỉnh theo yêu cầu

---

### Tầng 14: Compilation Model (Mô hình biên dịch)

#### 14.1. Interpreter

- **AST Interpreter** - Diễn giải AST trực tiếp
- **Bytecode Interpreter** - Diễn giải bytecode
- **Threaded Code** - Interpreted code dạng threaded
- **Indirect Threaded** - Threading gián tiếp

#### 14.2. Bytecode

- **Bytecode VM** - Virtual machine chạy bytecode
- **Instruction Set** - Tập lệnh bytecode
- **Bytecode Optimization** - Tối ưu bytecode
- **Constant Pool** - Pool các hằng số
- **Frame Layout** - Bố cục frame trong bytecode

#### 14.3. JIT (Just-in-Time)

- **Baseline JIT** - JIT cơ bản
- **Optimizing JIT** - JIT với tối ưu
- **Inline Caching** - Cache kết quả inline
- **Type Specialization** - Chuyên biệt theo kiểu
- **Deoptimization** - Bỏ tối ưu khi cần
- **On-Stack Replacement** - Thay đổi code đang chạy

#### 14.4. AOT (Ahead-of-Time)

- **Native Compilation** - Biên dịch ra native code
- **Link-Time Optimization** - Tối ưu lúc link
- **Whole Program Analysis** - Phân tích toàn chương trình
- **Code Generation** - Sinh code máy
- **Architecture Specific** - Tối ưu theo kiến trúc CPU

---

### Tầng 15: Linking Model (Mô hình liên kết)

#### 15.1. Static Linking

- **Static Library** - Thư viện tĩnh (.a, .lib)
- **Linker** - Trình liên kết
- **Symbol Resolution** - Phân giải symbol
- **Relocation** - Điều chỉnh địa chỉ
- **Symbol Table** - Bảng symbol

#### 15.2. Dynamic Linking

- **Dynamic Library** - Thư viện động (.so, .dll, .dylib)
- **Shared Library** - Thư viện chia sẻ
- **Dynamic Loader** - Trình tải động
- **Symbol Resolution** - Phân giải symbol lúc load
- **Lazy Binding** - Liên kết lazy
- **PLT/GOT** - Procedure Linkage Table / Global Offset Table

#### 15.3. Symbol Resolution

- **Symbol Visibility** - Visibility của symbol
- **Symbol Collision** - Xung đột symbol
- **Name Mangling** - Đổi tên hàm (C++)
- **Symbol Versioning** - Phiên bản symbol
- **Export/Import** - Xuất/Nhập symbol

---

### Tầng 16: Runtime

#### 16.1. Stack Frame

- **Frame Layout** - Bố cục stack frame
- **Return Address** - Địa chỉ quay về
- **Saved Registers** - Các register được lưu
- **Local Variables** - Biến cục bộ
- **Stack Pointer** - Con trỏ stack
- **Frame Pointer** - Con trỏ frame

#### 16.2. Call Stack

- **Call Graph** - Đồ thị gọi hàm
- **Stack Unwinding** - Unwind stack
- **Tail Call** - Gọi đuôi
- **Recursion** - Đệ quy
- **Stack Overflow** - Tràn stack

#### 16.3. Exception Unwinding

- **Stack Unwinding** - Unwind khi exception
- **Unwind Tables** - Bảng unwind (SEH, DWARF)
- **Cleanup Code** - Code cleanup trong unwind
- **Catch Blocks** - Khối bắt exception
- **Exception Propagation** - Truyền exception

#### 16.4. Garbage Collector Internals

- **Mark & Sweep** - Đánh dấu và quét
- **Generational GC** - GC thế hệ
- **Reference Counting** - Đếm tham chiếu
- **Tracing** - Truy vết object
- **Memory Compaction** - Nén bộ nhớ
- **Write Barrier** - Rào chắn ghi
- **Root Set** - Tập root (stack, heap, registers)
- **Object Headers** - Header của object trong GC

#### 16.5. Memory Regions (Vùng bộ nhớ)

- **Stack** - Vùng stack (biến cục bộ, frame)
- **Heap** - Vùng heap (cấp phát động)
- **BSS Segment** - Vùng biến chưa khởi tạo
- **Data Segment** - Vùng biến đã khởi tạo
- **Text Segment** - Vùng mã lệnh (code)
- **Memory-Mapped I/O** - Ánh xạ bộ nhớ I/O

---

### Tầng 17: Language Design Patterns (Mẫu thiết kế ngôn ngữ)

#### 17.1. Zero-Cost Abstractions

- **Abstraction Overhead** - Chi phí của trừu tượng
- **Inlining** - Inline code
- **Monomorphization** - Sinh code cụ thể (generics)
- **LLVM Optimization** - Tối ưu từ LLVM
- **Zero-Cost** - Không overhead runtime

#### 17.2. RAII (Resource Acquisition Is Initialization)

- **Resource Management** - Quản lý tài nguyên
- **Constructor/Destructor** - Constructor hủy
- **Scope-Based** - Quản lý theo scope
- **Smart Pointers** - Con trỏ thông minh
- **File Handles** - Handle file
- **Database Connections** - Kết nối database

#### 17.3. Ownership

- **Move Semantics** - Ngữ nghĩa di chuyển
- **Borrowing** - Mượn (mutable/immutable)
- **Lifetimes** - Thời gian sống
- **Ownership Transfer** - Chuyển giao sở hữu
- **Aliasing** - Tên gọi nhiều
- **Borrow Checker** - Trình kiểm tra borrow

#### 17.4. Algebraic Data Type (ADT)

- **Sum Type** - Tổng (enum với data)
- **Product Type** - Tích (struct/tuple)
- **Pattern Matching** - So khớp pattern
- **Exhaustive Matching** - So khớp đầy đủ
- **Tagged Union** - Union có tag
- **Option/Maybe** - Kiểu có thể null
- **Result/Either** - Kiểu error

---

### Tầng 18: Standard Library (Thư viện chuẩn)

#### 18.1. Collections & Data Structures

- **Vector/ArrayList** - Danh sách động
- **HashMap/HashSet** - Map và Set
- **LinkedList** - Danh sách liên kết
- **Queue/Deque** - Hàng đợi
- **Stack** - Ngăn xếp
- **Tree/TreeMap** - Cấu trúc cây
- **Heap/Priority Queue** - Heap và hàng đợi ưu tiên
- **BTreeMap/BTreeSet** - Map/Set có thứ tự (Rust, Java TreeMap)
- **ConcurrentHashMap** - Map an toàn đa luồng (Java, Go sync.Map)

#### 18.2. Utilities

- **Option/Result** - Xử lý null và error
- **Iterator** - Duyệt qua collection
- **Range** - Khoảng giá trị
- **Lazy** - Đánh giá lười biếng
- **OnceCell** - Khởi tạo một lần

#### 18.3. Concurrency Primitives

- **Thread** - Luồng
- **Mutex/RwLock** - Khóa
- **Channel** - Kênh truyền tin
- **Atomic** - Biến nguyên tử
- **Future/Task** - Task bất đồng bộ
- **Scoped Thread** - Thread với scope

#### 18.4. I/O & System

- **File/Path** - Thao tác file
- **Process** - Quản lý process
- **Environment** - Biến môi trường
- **Command Line** - Xử lý argument
- **Time/Duration** - Thời gian

#### 18.5. String & Text

- **String/Str** - Chuỗi
- **Regex** - Biểu thức chính quy
- **Formatter** - Định dạng

#### 18.6. Math & Numeric (Toán học & Số)

- **Math Functions** - Hàm toán học (abs, sqrt, pow, sin, cos)
- **BigInteger/BigDecimal** - Số lớn tùy ý
- **Random** - Sinh số ngẫu nhiên
- **Numeric Conversion** - Chuyển đổi kiểu số

#### 18.7. Encoding (Mã hóa)

- **Base64** - Mã hóa/giải mã Base64
- **URL Encoding** - Mã hóa URL (percent encoding)
- **Unicode/UTF-8** - Xử lý Unicode và UTF-8
- **Hex Encoding** - Mã hóa hex

---

### Tầng 19: Ecosystem (Hệ sinh thái)

#### 19.1. Web Frameworks

- **Backend Framework** - Framework web backend
- **Frontend Framework** - Framework web frontend
- **API Framework** - Framework xây dựng API
- **Microservices** - Hỗ trợ microservices
- **GraphQL** - Thư viện GraphQL

#### 19.2. Database & ORM

- **ORM** - Object-Relational Mapping
- **Query Builder** - Xây dựng truy vấn
- **Database Driver** - Driver kết nối database
- **Migration** - Quản lý migration
- **Schema** - Định nghĩa schema

#### 19.3. Testing

- **Unit Test Framework** - Framework test đơn vị
- **Mock Library** - Thư viện mock
- **Property Testing** - Test thuộc tính
- **Benchmark** - Đo hiệu năng
- **Fuzzing** - Fuzz testing

#### 19.4. DevOps & Infrastructure

- **Container** - Container hóa (Docker)
- **Kubernetes** - Orchestration
- **CI/CD** - Continuous Integration/Deployment
- **Infrastructure as Code** - IaC
- **Monitoring** - Giám sát
- **Logging** - Ghi log

#### 19.5. Networking & Communication

- **HTTP Client/Server** - Client/server HTTP
- **WebSocket** - Giao thức WebSocket
- **gRPC** - gRPC framework
- **Message Queue** - Hàng đợi tin nhắn
- **Web Framework** - Framework web

#### 19.6. Security & Cryptography

- **Authentication** - Xác thực
- **Authorization** - Phân quyền
- **Encryption** - Mã hóa
- **Hashing** - Băm mật khẩu
- **JWT** - JSON Web Token
- **TLS/SSL** - Bảo mật transport

#### 19.7. Data Science & ML

- **NumPy-like** - Tính toán mảng
- **Pandas-like** - Xử lý dữ liệu
- **ML Framework** - Framework ML
- **Data Visualization** - Trực quan hóa

---

### Tầng 20: Toolchain (Công cụ phát triển)

#### 20.1. Compiler & Build

- **Compiler** - Trình biên dịch
- **Linker** - Trình liên kết
- **Build System** - Hệ thống build
- **Package Manager** - Quản lý package
- **Dependency Resolution** - Phân giải phụ thuộc

#### 20.2. Code Quality

- **Linter** - Kiểm tra code style
- **Formatter** - Định dạng code
- **Type Checker** - Kiểm tra kiểu
- **Static Analyzer** - Phân tích tĩnh

#### 20.3. IDE & Editor

- **Language Server** - LSP server
- **Debug Adapter** - Debug protocol
- **Code Completion** - Tự động hoàn thành
- **Refactoring Tools** - Công cụ refactor

#### 20.4. Version Control

- **Version Control** - Quản lý phiên bản
- **Git Hooks** - Git hooks
- **Merge Tool** - Công cụ merge
- **Diff Tool** - Công cụ so sánh

#### 20.5. Documentation & Publishing

- **Doc Generator** - Sinh tài liệu
- **Package Registry** - Registry package
- **Release Tool** - Công cụ release

#### 20.6. Runtime & Environment

- **VM** - Virtual Machine
- **Interpreter** - Trình thông dịch
- **JIT** - Just-in-Time compiler
- **Runtime** - Thời gian chạy
- **REPL** - Read-Eval-Print Loop

#### 20.7. Profiling & Debugging

- **Profiler** - Công cụ profile
- **Debugger** - Công cụ debug
- **Memory Profiler** - Profile bộ nhớ
- **Trace Tool** - Công cụ trace

---


