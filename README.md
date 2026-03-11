# Tổng Hợp So Sánh Syntax

## Mục Lục

1. [Phân Loại Ngôn Ngữ](#1-phân-loại-ngôn-ngữ)
2. [Danh Sách Khái Niệm & Trường Hợp Sử Dụng](#2-danh-sách-khái-niệm--trường-hợp-sử-dụng)

---

## 1. Phân Loại Ngôn Ngữ

### Theo Loại Ngôn Ngữ

| Ngôn ngữ       | Loại                | Biên dịch/Thông dịch | Typing            |
| -------------- | ------------------- | -------------------- | ----------------- |
| **Rust**       | Systems Programming | Compiled (AOT)       | Static, Strong    |
| **Go**         | Systems/Server      | Compiled (AOT)       | Static, Strong    |
| **Python**     | General Purpose     | Interpreted/Bytecode | Dynamic, Strong   |
| **TypeScript** | Web/JS Superset     | Transpiled to JS     | Static (optional) |
| **JavaScript** | Web Scripting       | Interpreted/JIT      | Dynamic, Duck     |
| **Swift**      | iOS/macOS           | Compiled (AOT)       | Static, Strong    |
| **Kotlin**     | Android/JVM         | Compiled (Bytecode)  | Static, Strong    |
| **Dart**       | Flutter/Web         | Compiled (AOT/JIT)   | Static, Strong    |
| **PHP**        | Web Backend         | Interpreted          | Dynamic, Weak     |

### Theo Paradigm

| Ngôn ngữ       | Paradigm                                           |
| -------------- | -------------------------------------------------- |
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
| **Rust**       | Systems programming, WebAssembly, CLI tools, Blockchain        |
| **Go**         | Backend servers, Cloud services, DevOps tools, Microservices   |
| **Python**     | Data science, ML/AI, Automation, Web (Django/Flask), Scripting |
| **TypeScript** | Frontend (React, Vue, Angular), Node.js, Enterprise apps       |
| **JavaScript** | Frontend web, Node.js, Mobile (React Native)                   |
| **Swift**      | iOS/macOS apps, Apple ecosystem                                |
| **Kotlin**     | Android, Backend (Spring), Multiplatform                       |
| **Dart**       | Flutter (Cross-platform mobile), Web                           |
| **PHP**        | Web backend (Laravel, Symfony), CMS (WordPress)                |

---

## 2. Danh Sách Khái Niệm & Trường Hợp Sử Dụng

### 2.1. Khai Báo Biến (Variable Declaration)

- **Mutable** - Biến có thể thay đổi giá trị
- **Immutable** - Biến không thể thay đổi sau khi khởi tạo
- **Type Annotation** - Khai báo kiểu dữ liệu tường minh
- **Type Inference** - Ngôn ngữ tự suy luận kiểu
- **Constant** - Hằng số compile-time
- **Static Variable** - Biến tĩnh (class-level)
- **Global Variable** - Biến toàn cục
- **Shadowing** - Biến cùng tên trong scope nhỏ

### 2.2. Khai Báo Hàm (Function Declaration)

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

### 2.3. Vòng Lặp (Loops)

- **For Loop** - Vòng lặp với số lần xác định
- **For-each/Range** - Duyệt qua collection
- **While Loop** - Vòng lặp với điều kiện
- **Infinite Loop** - Vòng lặp vô hạn
- **Do-While** - Thực hiện ít nhất 1 lần
- **Loop Control** - Break, continue, labeled loops
- **Iterator** - Duyệt qua iterator
- **List Comprehension** - Tạo list từ iterable (Python)
- **Stream Loop** - Duyệt qua stream (Java/Go)

### 2.4. Điều Kiện (Conditionals)

- **If-Else** - Rẽ nhánh cơ bản
- **Switch/Match** - Rẽ nhánh nhiều trường hợp
- **Ternary** - Toán tử điều kiện ngắn
- **Pattern Matching** - So khớp pattern (Rust, Swift, Kotlin)
- **Guarded Condition** - Điều kiện bảo vệ trong if
- **Early Return** - Trả về sớm
- **Elvis Operator** - Toán tử Elvis (??)
- **Null Coalescing** - Giá trị mặc định khi null

### 2.5. Struct/Class/Object

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

### 2.6. Kế Thừa & Đa Hình (Inheritance & Polymorphism)

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

### 2.7. Interface/Trait/Protocol

- **Interface** - Định nghĩa contract
- **Trait** - Code reuse (Rust)
- **Protocol** - Contract (Swift, Go)
- **Abstract Method** - Phương thức trừu tượng
- **Default Implementation** - Triển khai mặc định
- **Static Method** - Phương thức tĩnh trong interface
- **Multiple Interface** - Implement nhiều interface
- **Interface Extension** - Mở rộng interface

### 2.8. Enum

- **Basic Enum** - Enum cơ bản
- **Enum with Values** - Enum có giá trị
- **Enum with Methods** - Enum có phương thức
- **Associated Values** - Giá trị đi kèm (Swift)
- **Pattern Matching Enum** - So khớp enum

### 2.9. Nullable/Option Types

- **Nullable** - Có thể null
- **Optional** - Giá trị có hoặc không
- **Null Check** - Kiểm tra null
- **Unwrap** - Lấy giá trị từ optional
- **Safe Unwrap** - Unwrap an toàn
- **None/Null Representation** - Cách biểu diễn không có giá trị
- **Optional Chaining** - Chuỗi gọi optional

### 2.10. Xử Lý Lỗi (Error Handling)

- **Try-Catch** - Bắt exception
- **Result/Option** - Return error as value
- **Error Return** - Trả về lỗi
- **Throw Exception** - Ném ngoại lệ
- **Custom Exception** - Exception tự định nghĩa
- **Finally Block** - Luôn thực thi dù có lỗi
- **Try-with-resources** - Tự động đóng tài nguyên
- **Error Propagation** - Truyền lỗi lên trên
- **Recover** - Khôi phục từ panic (Rust)

### 2.11. Generics

- **Generic Function** - Hàm generic
- **Generic Class** - Class generic
- **Type Constraint** - Ràng buộc kiểu
- **Generic Trait** - Trait generic
- **Where Clause** - Điều kiện ràng buộc
- **Bounds** - Giới hạn kiểu
- **Covariance/Contravariance** - Biến đổi kiểu
- **Type Erasure** - Xóa kiểu (Java)

### 2.12. Collection Operations

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

### 2.13. String Operations

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

### 2.14. Concurrency/Async

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

### 2.15. Visibility/Access Modifiers

- **Private** - Chỉ trong cùng file/class
- **Public** - Có thể truy cập từ bên ngoài
- **Protected** - Kế thừa được
- **Internal** - Trong cùng module/project
- **Fileprivate** - Trong cùng file (Swift)
- **Open** - Có thể override (Swift/Kotlin)
- **Default Access** - Quyền truy cập mặc định

### 2.16. Import/Export & Module

- **Import** - Nhập module
- **Export** - Xuất module
- **Package** - Gói code
- **Module Alias** - Đặt tên alias cho module
- **Selective Import** - Chỉ nhập phần cần thiết
- **Default Export** - Xuất mặc định
- **Re-export** - Xuất lại từ module khác
- **Namespace** - Không gian tên

### 2.17. Kiểu Dữ Liệu Cơ Bản (Primitive Types)

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

### 2.18. Null Safety

- **Elvis Operator** - Toán tử Elvis (??)
- **Safe Call** - Gọi an toàn (?.)
- **Non-null Assertion** - Khẳng định không null
- **Let/Apply/Also** - Scope functions với null
- **Null Object Pattern** - Pattern thay thế null

### 2.19. Property & Getter/Setter

- **Property** - Thuộc tính
- **Getter** - Lấy giá trị
- **Setter** - Đặt giá trị
- **Computed Property** - Thuộc tính tính toán
- **Lazy Property** - Thuộc tính trì hoãn
- **Late Init** - Khởi tạo muộn
- **Backing Field** - Trường lưu trữ

### 2.20. Functional Programming

- **Pure Function** - Hàm thuần túy (không side effect)
- **Immutability** - Bất biến
- **First-Class Function** - Hàm như giá trị
- **Currying** - Chuyển hàm nhiều tham số thành chuỗi
- **Partial Application** - Áp dụng một phần
- **Function Composition** - Kết hợp hàm
- **Monad** - Monad pattern
- **Functor** - Functor pattern

### 2.21. Memory Management

- **Ownership** - Sở hữu (Rust)
- **Borrowing** - Mượn (Rust)
- **Lifetime** - Thời gian sống của tham chiếu
- **Reference Counting** - Đếm tham chiếu (Arc)
- **Garbage Collection** - Thu gom rác
- **Weak Reference** - Tham chiếu yếu
- **Smart Pointer** - Con trỏ thông minh
- **RAII** - Resource Acquisition Is Initialization

### 2.22. Annotation/Decorator

- **Annotation** - Chú thích metadata
- **Decorator** - Bổ sung chức năng (Python)
- **Attribute** - Thuộc tính (C#, Swift)
- **Macro** - Macro (Rust)
- **Compile-time** - Thời điểm biên dịch
- **Runtime** - Thời điểm chạy

### 2.23. Extension Methods

- **Extension Function** - Mở rộng class không sửa
- **Extension Property** - Mở rộng property
- **Implicit Receiver** - Receiver ngầm định
- **Type Extension** - Mở rộng kiểu dữ liệu

### 2.24. Operator Overloading

- **Arithmetic Operators** - Toán tử số học
- **Comparison Operators** - Toán tử so sánh
- **Logical Operators** - Toán tử logic
- **Custom Operators** - Toán tử tự định nghĩa
- **Infix Functions** - Hàm infix (Kotlin)

### 2.25. HTTP & Networking

- **HTTP Request** - Gửi request
- **HTTP Response** - Nhận response
- **Headers** - Header của request/response
- **Query Parameters** - Tham số truy vấn
- **Path Parameters** - Tham số đường dẫn
- **Request Body** - Nội dung request
- **Authentication** - Xác thực
- **HTTP Client** - Thư viện gọi HTTP

### 2.26. File I/O

- **Read File** - Đọc file
- **Write File** - Ghi file
- **File Path** - Đường dẫn file
- **Stream** - Luồng dữ liệu
- **Buffer** - Bộ đệm
- **Async File I/O** - Đọc/ghi bất đồng bộ

### 2.27. JSON & Serialization

- **Serialize** - Chuyển object thành JSON
- **Deserialize** - Chuyển JSON thành object
- **JSON Encoder/Decoder** - Bộ mã hóa/giải mã
- **Field Mapping** - Ánh xạ trường
- **Naming Strategy** - Quy tắc đặt tên

### 2.28. Date & Time

- **Current Date/Time** - Thời gian hiện tại
- **Parse/Format** - Chuyển đổi định dạng
- **Timezone** - Múi giờ
- **Duration** - Khoảng thời gian
- **Date Arithmetic** - Tính toán ngày tháng

### 2.29. Regular Expression

- **Pattern** - Mẫu regex
- **Match** - So khớp
- **Replace** - Thay thế
- **Capture Group** - Nhóm bắt
- **Split** - Tách bằng regex

### 2.30. Testing

- **Unit Test** - Test đơn vị
- **Integration Test** - Test tích hợp
- **E2E Test** - Test đầu cuối
- **Mock** - Tạo đối tượng giả
- **Stub** - Thay thế implementation
- **Assertion** - Khẳng định kết quả
- **Test Suite** - Bộ test
- **Before/After Hook** - Thiết lập/cleanup

### 2.31. Logging

- **Log Levels** - Cấp độ log (debug, info, warn, error)
- **Logger** - Công cụ ghi log
- **Formatted Log** - Log có định dạng
- **Structured Logging** - Log có cấu trúc

### 2.32. Dependency Injection

- **Constructor Injection** - Tiêm vào constructor
- **Setter Injection** - Tiêm qua setter
- **Interface Injection** - Tiêm interface
- **Service Container** - Container quản lý dependency
- **Factory** - Factory tạo dependency

### 2.33. Configuration

- **Environment Variables** - Biến môi trường
- **Config File** - File cấu hình
- **Command Line Args** - Tham số dòng lệnh
- **Secret Management** - Quản lý secrets

### 2.34. Build & Package Management

- **Dependency Manager** - Quản lý thư viện
- **Build Tool** - Công cụ build
- **Linter** - Kiểm tra code style
- **Formatter** - Định dạng code

### 2.35. Documentation

- **Comment** - Bình luận
- **Doc Comment** - Bình luận tài liệu
- **Type Documentation** - Tài liệu kiểu
- **README** - Tài liệu project

### 2.36. Error Types & Patterns

- **Checked Exception** - Exception bắt buộc xử lý
- **Unchecked Exception** - Exception không bắt buộc
- **Custom Error Type** - Kiểu lỗi tự định nghĩa
- **Error Union** - Hợp các kiểu lỗi
- **Panic** - Lỗi nghiêm trọng (Rust)

### 2.37. Advanced Concepts

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

---
