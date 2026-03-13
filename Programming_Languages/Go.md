# Go Syntax Reference

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
   - [3.1 Struct/Object](#31-structobject)
   - [3.2 Kế Thừa & Đa Hình](#32-kế-thừa--đa-hình)
   - [3.3 Interface](#33-interface)
   - [3.4 Visibility](#34-visibility)
4. [Tầng 4: Memory Model](#tầng-4-memory-model)
   - [4.1 Memory Management](#41-memory-management)
   - [4.2 Property & Getter/Setter](#42-property--gettersetter)
5. [Tầng 5: Concurrency Model](#tầng-5-concurrency-model)
   - [5.1 Concurrency/Goroutine](#51-concurrencygoroutine)
6. [Tầng 6: Paradigm](#tầng-6-paradigm)
   - [6.1 Functional Programming](#61-functional-programming)
7. [Tầng 7: Error Handling](#tầng-7-error-handling)
   - [7.1 Xử Lý Lỗi](#71-xử-lý-lỗi)
   - [7.2 Error Types](#72-error-types)
8. [Tầng 8: Module & Organization](#tầng-8-module--organization)
   - [8.1 Import/Module](#81-importmodule)
   - [8.2 Package](#82-package)
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
    - [14.2 Go Compiler](#142-go-compiler)
15. [Tầng 15: Linking Model](#tầng-15-linking-model)
    - [15.1 Linking](#151-linking)
16. [Tầng 16: Runtime](#tầng-16-runtime)
    - [16.1 Go Runtime](#161-go-runtime)
    - [16.2 Panic/Defer](#162-panicdefer)
17. [Tầng 17: Language Design Patterns](#tầng-17-language-design-patterns)
    - [17.1 Duck Typing](#171-duck-typing)
    - [17.2 Zero Value](#172-zero-value)
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

### Chạy File Go

```bash
# Chạy trực tiếp
go run main.go

# Build
go build main.go
go build -o myapp main.go

# Install
go install

# Module
go mod init github.com/username/project
go mod tidy
```

### Đặc điểm Go

- **Typing**: Static typing, Strong typing
- **Paradigm**: Concurrent, Imperative, Functional (limited)
- **Execution**: Compiled (AOT), Statically linked
- **Memory Safety**: No GC (manual) but has GC for heap
- **Use Cases**: Web servers, Cloud services, DevOps tools, Microservices

---

## 1. Tầng 1: Syntax & Semantics

### 1.1. Khai Báo Biến (Variable Declaration)

#### Mutable - Biến thường

```go
// Khai báo biến với type inference
var x = 10
var name = "Go"
var isActive = true
var prices = []float64{1.5, 2.0, 3.5}

// Explicit type
var x int = 10
var name string = "Go"
var isActive bool = true

// Short declaration (trong function)
x := 10
name := "Go"
isActive := true
```

#### Immutable - Hằng số

```go
// Constants
const MaxSize = 100
const Pi = 3.14159

// Constant with type
const AppName string = "MyApp"

// Iota (constant generator)
const (
    Monday = iota
    Tuesday
    Wednesday
)
// Monday=0, Tuesday=1, Wednesday=2
```

#### Zero Value

```go
// Zero values (default)
var i int      // 0
var s string   // ""
var b bool     // false
var p *int     // nil
var arr []int  // nil
```

---

### 1.2. Khai Báo Hàm (Function Declaration)

#### Function cơ bản

```go
// Function không có return
func greet() {
    fmt.Println("Hello!")
}

// Function có return
func add(a int, b int) int {
    return a + b
}

// Multiple return values
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}

// Named return values
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return // naked return
}

// Function với variadic
func sum(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}

sum(1, 2, 3, 4, 5) // 15
```

#### Parameters

```go
// Default parameters (Go không có, dùng options pattern)
func greet(name string) string {
    return "Hello, " + name + "!"
}

// Named arguments (dùng struct)
type UserParams struct {
    Name  string
    Age   int
    Email string
}

func createUser(params UserParams) User {
    return User{
        Name:  params.Name,
        Age:   params.Age,
        Email: params.Email,
    }
}

createUser(UserParams{Name: "John", Age: 30})

// Pointer parameter
func modify(s *string) {
    *s = "modified"
}
```

#### Closure

```go
// Closure
square := func(x int) int {
    return x * x
}

// Closure capture variables
func outer(x int) func(int) int {
    return func(y int) int {
        return x + y // capture x from outer
    }
}

closure := outer(10)
closure(5) // 15
```

#### Higher-Order Function

```go
// Function nhận function khác làm tham số
func applyTwice(func(int) int, x int) int {
    return func(func(int) int, x int) int {
        return func(x int) int {
            return x + x
        }(x)
    }(func(x int) int { return x + 5 }, x)
}

// Function trả về function
func multiplier(factor int) func(int) int {
    return func(x int) int {
        return x * factor
    }
}

double := multiplier(2)
double(5) // 10
```

#### Method

```go
type Rectangle struct {
    Width  int
    Height int
}

// Method với receiver
func (r Rectangle) Area() int {
    return r.Width * r.Height
}

// Pointer receiver (có thể modify)
func (r *Rectangle) Resize(width, height int) {
    r.Width = width
    r.Height = height
}
```

---

### 1.3. Vòng Lặp (Loops)

#### For Loop

```go
// For cơ bản
for i := 0; i < 5; i++ {
    fmt.Println(i) // 0, 1, 2, 3, 4
}

// For với range
fruits := []string{"apple", "banana", "cherry"}
for i, fruit := range fruits {
    fmt.Printf("%d: %s\n", i, fruit)
}

// For với map
m := map[string]int{"a": 1, "b": 2}
for key, value := range m {
    fmt.Println(key, value)
}

// For với channel
ch := make(chan int)
go func() {
    ch <- 1
    ch <- 2
    close(ch)
}()
for v := range ch {
    fmt.Println(v)
}
```

#### While (for không có điều kiện)

```go
// While-style
n := 5
for n > 0 {
    fmt.Println(n)
    n--
}

// Infinite loop
for {
    fmt.Println("loop")
    break
}
```

#### Loop Control

```go
// Break
for i := 0; i < 10; i++ {
    if i == 5 {
        break
    }
    fmt.Println(i) // 0, 1, 2, 3, 4
}

// Continue
for i := 0; i < 5; i++ {
    if i == 2 {
        continue
    }
    fmt.Println(i) // 0, 1, 3, 4
}

// Label
outer:
    for i := 0; i < 3; i++ {
        for j := 0; j < 3; j++ {
            if j == 1 {
                break outer
            }
        }
    }
```

---

### 1.4. Điều Kiện (Conditionals)

#### If-Else

```go
age := 18
if age >= 18 {
    fmt.Println("Adult")
} else {
    fmt.Println("Minor")
}

// Else if
score := 85
var grade string
if score >= 90 {
    grade = "A"
} else if score >= 80 {
    grade = "B"
} else if score >= 70 {
    grade = "C"
} else {
    grade = "F"
}
```

#### Switch

```go
// Switch cơ bản
func httpStatus(status int) string {
    switch status {
    case 200:
        return "OK"
    case 404:
        return "Not Found"
    case 500:
        return "Server Error"
    default:
        return "Unknown"
    }
}

// Switch với multiple values
func httpStatusMulti(status int) string {
    switch status {
    case 200, 201, 202:
        return "Success"
    case 400, 401, 403:
        return "Client Error"
    default:
        return "Unknown"
    }
}

// Switch với expression
func grade(score int) string {
    switch {
    case score >= 90:
        return "A"
    case score >= 80:
        return "B"
    case score >= 70:
        return "C"
    default:
        return "F"
    }
}
```

#### Type Switch

```go
func typeSwitch(x interface{}) string {
    switch v := x.(type) {
    case int:
        return "int"
    case string:
        return "string"
    case bool:
        return "bool"
    default:
        return "unknown"
    }
}
```

---

## 2. Tầng 2: Type System

### 2.1. Kiểu Dữ Liệu Cơ Bản (Primitive Types)

#### Integer

```go
// Signed integers
var i8 int8 = 10
var i16 int16 = 10
var i32 int32 = 10
var i64 int64 = 10

// Unsigned integers
var u8 uint8 = 10
var u16 uint16 = 10
var u32 uint32 = 10
var u64 uint64 = 10

// Default
var i int = 10 // int32 hoặc int64 (platform dependent)
var u uint = 10

// Literals
hex := 0xFF       // 255
binary := 0b1010  // 10
octal := 0o777    // 511

// Operations
5 + 3    // 8
5 - 3    // 2
5 * 3    // 15
5 / 3    // 1 (integer division)
5 % 3    // 2
```

#### Float

```go
// Float
var f32 float32 = 3.14
var f64 float64 = 3.14 // Default

// Special values
var inf = math.Inf(1)
var negInf = math.Inf(-1)
var nan = math.NaN()

// Operations
3.14 + 1.0
3.14 * 2.0
3.14 / 2.0
```

#### Boolean

```go
var isActive bool = true
var isDeleted bool = false

// Operations
true && false // false
true || false // true
!true         // false
```

#### String

```go
// String
var s1 string = "Hello"
var s2 string = `Multi
line
string`

// String methods
s := "Hello World"
len(s)                    // 11
strings.ToUpper(s)        // "HELLO WORLD"
strings.ToLower(s)        // "hello world"
strings.TrimSpace(s)       // "Hello World"
strings.Split(s, " ")     // ["Hello", "World"]
strings.Replace(s, "World", "Go", 1) // "Hello Go"
strings.Contains(s, "World") // true
strings.Index(s, "World")   // 6
strings.HasPrefix(s, "Hello") // true
strings.HasSuffix(s, "World") // true

// String concatenation
"Hello " + "World"
fmt.Sprintf("Hello %s", "World")
strings.Join([]string{"Hello", "World"}, " ")

// Rune (UTF-8)
r := []rune("Hello")
r[0] // 'H'
```

#### Array

```go
// Fixed-size array
var arr [3]int = [3]int{1, 2, 3}
arr := [3]int{1, 2, 3}

// Array literal
arr := [...]int{1, 2, 3} // size inferred

// Access
arr[0]  // 1
len(arr)
cap(arr)

// Multi-dimensional
matrix := [2][3]int{
    {1, 2, 3},
    {4, 5, 6},
}
```

#### Slice

```go
// Slice (dynamic array)
var s []int
s = make([]int, 0, 10) // capacity 10
s = []int{1, 2, 3}

// From array
arr := [5]int{1, 2, 3, 4, 5}
slice := arr[1:4] // [2, 3, 4]

// Methods
append(slice, 4)
copy(dst, src)

// Slicing
s := []int{0, 1, 2, 3, 4}
s[1:3]   // [1, 2]
s[:3]    // [0, 1, 2]
s[3:]    // [3, 4]
s[:]     // [0, 1, 2, 3, 4]
```

#### Map

```go
// Map
m := make(map[string]int)
m := map[string]int{
    "a": 1,
    "b": 2,
}

// Access
v := m["key"]
v, ok := m["key"] // v=value, ok=exists

// Operations
m["new"] = 3
delete(m, "key")
len(m)

// Iterate
for k, v := range m {
    fmt.Println(k, v)
}
```

#### Pointer

```go
// Pointer
var p *int
i := 42
p = &i

// Dereference
*p // 42

// Pointer to struct
type Person struct {
    Name string
}

person := &Person{Name: "John"}
person.Name // "John"
```

---

### 2.2. Enum

```go
// Go không có enum, dùng const + iota
type Color int

const (
    Red Color = iota
    Green
    Blue
)

// Với giá trị tùy chỉnh
type Status int

const (
    Pending Status = iota
    Approved
    Rejected
)

// String conversion
func (c Color) String() string {
    switch c {
    case Red:
        return "Red"
    case Green:
        return "Green"
    case Blue:
        return "Blue"
    default:
        return "Unknown"
    }
}
```

---

### 2.3. Nullable Types

```go
// Go không có nullable types nhưng dùng pointers
var s *string // nil

// Dùng pointers cho nullable
func getName() *string {
    name := "John"
    return &name
}

// Interface với nil
var reader io.Reader // nil

// Check nil
if reader == nil {
    // ...
}
```

---

### 2.4. Null Safety

```go
// Check nil trước khi sử dụng
func printValue(p *int) {
    if p != nil {
        fmt.Println(*p)
    }
}

// Dùng comma-ok idiom
m := map[string]int{"a": 1}
if v, ok := m["a"]; ok {
    fmt.Println(v)
}

// Dùng empty string thay vì nil
var s string // "" (zero value)
```

---

### 2.5. Generics

```go
// Generic function (Go 1.18+)
func first[T any](slice []T) *T {
    if len(slice) == 0 {
        return nil
    }
    return &slice[0]
}

// Generic type
type Container[T any] struct {
    Value T
}

func main() {
    intContainer := Container[int]{Value: 42}
    strContainer := Container[string]{Value: "hello"}
}

// Generic constraints
type Number interface {
    int | int32 | int64 | float32 | float64
}

func sum[T Number](nums []T) T {
    var total T
    for _, n := range nums {
        total += n
    }
    return total
}
```

---

### 2.6. Collection Operations

#### Map/Transform

```go
numbers := []int{1, 2, 3, 4, 5}

// Manual map (vì Go không có built-in)
squared := make([]int, len(numbers))
for i, n := range numbers {
    squared[i] = n * n
}

// Dùng function
func mapSlice[T any, R any](slice []T, fn func(T) R) []R {
    result := make([]R, len(slice))
    for i, v := range slice {
        result[i] = fn(v)
    }
    return result
}

squared := mapSlice(numbers, func(x int) int { return x * x })
```

#### Filter

```go
// Manual filter
func filterSlice[T any](slice []T, fn func(T) bool) []T {
    result := make([]T, 0)
    for _, v := range slice {
        if fn(v) {
            result = append(result, v)
        }
    }
    return result
}

evens := filterSlice(numbers, func(x int) bool { return x%2 == 0 })
```

#### Reduce/Fold

```go
// Manual reduce
func reduce[T any, R any](slice []T, init R, fn func(R, T) R) R {
    result := init
    for _, v := range slice {
        result = fn(result, v)
    }
    return result
}

total := reduce(numbers, 0, func(acc, x int) int { return acc + x }) // 15
```

#### Sort

```go
import "sort"

numbers := []int{3, 1, 4, 1, 5, 9, 2, 6}

// sort (in-place)
sort.Ints(numbers) // ascending
sort.Slice(numbers, func(i, j int) bool {
    return numbers[i] > numbers[j]
}) // descending

// Sort with custom type
type Person struct {
    Name string
    Age  int
}

people := []Person{{"John", 30}, {"Jane", 25}}
sort.Slice(people, func(i, j int) bool {
    return people[i].Age < people[j].Age
})
```

#### Find

```go
// Find first
func find[T any](slice []T, fn func(T) bool) (T, bool) {
    for _, v := range slice {
        if fn(v) {
            return v, true
        }
    }
    var zero T
    return zero, false
}

val, ok := find(numbers, func(x int) bool { return x > 3 }) // 4, true
```

---

### 2.7. String Operations

#### Concatenation

```go
// Dùng +
"Hello " + "World"

// Dùng fmt.Sprintf
s := fmt.Sprintf("Hello %s", "World")

// Dùng strings.Builder
var sb strings.Builder
sb.WriteString("Hello ")
sb.WriteString("World")
s := sb.String()

// Dùng strings.Join
parts := []string{"Hello", "World"}
s := strings.Join(parts, " ")
```

#### Interpolation

```go
name := "Go"
version := 1.21

// fmt.Sprintf
fmt.Sprintf("Welcome to %s %d", name, version)

// fmt with verbs
fmt.Sprintf("%.2f", 3.14159)  // "3.14"
fmt.Sprintf("%05d", 42)        // "00042"
fmt.Sprintf("%v", []int{1,2,3}) // "[1 2 3]"
```

#### Regex

```go
import "regexp"

text := "My email is john@example.com"

// Match
re := regexp.MustCompile(`[\w.-]+@[\w.-]+`)
match := re.FindString(text)

// Find all
matches := re.FindAllString(text, -1)

// Replace
replaced := re.ReplaceAllString(text, "[email]")

// Split
parts := re.Split(text, -1)
```

#### Substring

```go
s := "Hello World"

// Slicing
s[0:5]  // "Hello"
s[:5]   // "Hello"
s[6:]   // "World"
s[6:11] // "World"

// Methods
strings.Index(s, "World")       // 6
strings.Contains(s, "World")    // true
strings.HasPrefix(s, "Hello")  // true
strings.HasSuffix(s, "World")  // true
strings.Contains(s, "World")    // true
```

---

## 3. Tầng 3: OOP & Type Relationships

### 3.1. Struct/Object

#### Struct Definition

```go
// Basic struct
type User struct {
    Name  string
    Email string
    Age   int
    Active bool
}

// Create instance
user := User{
    Name:  "John",
    Email: "john@example.com",
    Age:   30,
}

// Or
user := User{Name: "John", Age: 30}

// Pointer to struct
user := &User{Name: "John", Age: 30}

// Anonymous struct
person := struct {
    Name string
    Age  int
}{
    Name: "John",
    Age:  30,
}
```

#### Struct Methods

```go
type Rectangle struct {
    Width  int
    Height int
}

// Value receiver
func (r Rectangle) Area() int {
    return r.Width * r.Height
}

// Pointer receiver
func (r *Rectangle) Resize(width, height int) {
    r.Width = width
    r.Height = height
}

// Constructor (factory function)
func NewRectangle(width, height int) *Rectangle {
    return &Rectangle{
        Width:  width,
        Height: height,
    }
}
```

#### Embedded Struct (Composition)

```go
type Person struct {
    Name string
    Age  int
}

type Employee struct {
    Person  // Embedded (like inheritance)
    Company string
    Salary  float64
}

emp := Employee{
    Person: Person{Name: "John", Age: 30},
    Company: "ACME",
}
emp.Name       // "John"
emp.Person.Name // "John"
```

---

### 3.2. Kế Thừa & Đa Hình

Go không có traditional inheritance. Dùng composition và interface.

#### Composition

```go
type Animal struct {
    Name string
}

func (a Animal) Speak() string {
    return "..."
}

type Dog struct {
    Animal  // Embedded
    Breed  string
}

func (d Dog) Speak() string {
    return "Woof!"
}

dog := Dog{
    Animal: Animal{Name: "Buddy"},
    Breed:  "Golden Retriever",
}
dog.Name   // "Buddy"
dog.Speak() // "Woof!"
```

#### Polymorphism với Interface

```go
type Speaker interface {
    Speak() string
}

func makeSpeak(s Speaker) string {
    return s.Speak()
}

type Dog struct{}
func (d Dog) Speak() string { return "Woof!" }

type Cat struct{}
func (c Cat) Speak() string { return "Meow!" }

makeSpeak(Dog{}) // "Woof!"
makeSpeak(Cat{}) // "Meow!"
```

---

### 3.3. Interface

#### Interface Definition

```go
// Interface với methods
type Drawable interface {
    Draw()
}

type Circle struct {
    Radius float64
}

func (c Circle) Draw() {
    fmt.Printf("Drawing circle with radius %.2f\n", c.Radius)
}

type Square struct {
    Side float64
}

func (s Square) Draw() {
    fmt.Printf("Drawing square with side %.2f\n", s.Side)
}

// Polymorphism
func render(d Drawable) {
    d.Draw()
}
```

#### Empty Interface

```go
// interface{} (any type)
var i interface{}
i = 42
i = "hello"
i = []int{1, 2, 3}

// Type assertion
var i interface{} = "hello"
s := i.(string)

// Type switch
switch v := i.(type) {
case int:
    fmt.Println("int:", v)
case string:
    fmt.Println("string:", v)
}
```

#### Common Interfaces

```go
// Stringer
type Stringer interface {
    String() string
}

// Error
type Error interface {
    Error() string
}

// Reader/Writer
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}
```

---

### 3.4. Visibility

```go
// Go không có access modifiers
// Dùng capitalization:
// - Uppercase: exported (public)
// - Lowercase: unexported (private)

// Exported (public)
type User struct {
    Name  string // public
    email string // private (within package)
}

// Package-level visibility
// File trong cùng package có thể truy cập private members
```

---

## 4. Tầng 4: Memory Model

### 4.1. Memory Management

```go
// Go has garbage collection
// Manual memory management không cần thiết

// Stack vs Heap
// - Stack: local variables, small
// - Heap: dynamically allocated, garbage collected

// Escape analysis
// Compiler quyết định allocation location

// unsafe package (rarely needed)
import "unsafe"

ptr := unsafe.Pointer(&i)
```

### 4.2. Property & Getter/Setter

```go
// Go không có properties nhưng dùng methods
type Temperature struct {
    celsius float64
}

// Getter (tên trùng với field, không có Get prefix)
func (t Temperature) Celsius() float64 {
    return t.celsius
}

func (t *Temperature) SetCelsius(v float64) {
    t.celsius = v
}

// Computed property
func (t Temperature) Fahrenheit() float64 {
    return t.celsius*9/5 + 32
}

temp := &Temperature{}
temp.SetCelsius(25)
temp.Fahrenheit() // 77
```

---

## 5. Tầng 5: Concurrency Model

### 5.1. Concurrency/Goroutine

#### Goroutine

```go
// Goroutine (lightweight thread)
go func() {
    fmt.Println("Hello from goroutine")
}()

// Named function
go doWork()

func doWork() {
    // ...
}
```

#### Channel

```go
// Create channel
ch := make(chan int)

// Send/Receive
ch <- 42       // Send
value := <-ch // Receive

// Buffered channel
ch := make(chan int, 10)

// Close channel
close(ch)

// Range over channel
for v := range ch {
    fmt.Println(v)
}

// Select
select {
case v := <-ch1:
    fmt.Println("Received from ch1:", v)
case v := <-ch2:
    fmt.Println("Received from ch2:", v)
case <-time.After(time.Second):
    fmt.Println("Timeout")
default:
    fmt.Println("No message")
}
```

#### WaitGroup

```go
import "sync"

var wg sync.WaitGroup

for i := 0; i < 5; i++ {
    wg.Add(1)
    go func(i int) {
        defer wg.Done()
        fmt.Println("Goroutine", i)
    }(i)
}

wg.Wait() // Wait for all goroutines
```

#### Mutex

```go
import "sync"

type Counter struct {
    mu    sync.Mutex
    value int
}

func (c *Counter) Increment() {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.value++
}

func (c *Counter) Value() int {
    c.mu.Lock()
    defer c.mu.Unlock()
    return c.value
}
```

#### Context

```go
import "context"

func longRunningTask(ctx context.Context) error {
    select {
    case <-ctx.Done():
        return ctx.Err()
    case <-time.After(2 * time.Second):
        return nil
    }
}

ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()

if err := longRunningTask(ctx); err != nil {
    fmt.Println("Task failed:", err)
}
```

---

## 6. Tầng 6: Paradigm

### 6.1. Functional Programming

Go có một số tính năng functional nhưng không phải pure FP language.

#### First-Class Function

```go
// Function là values
var add func(int, int) int = func(a, b int) int {
    return a + b
}

// Function nhận function
func apply(fn func(int) int, x int) int {
    return fn(x)
}
```

#### Closure

```go
func multiplier(factor int) func(int) int {
    return func(x int) int {
        return x * factor
    }
}

double := multiplier(2)
double(5) // 10
```

#### Immutable (limited)

```go
// Go không có built-in immutability
// Dùng không mutate original data

// Instead of mutating
func addEvens(numbers []int) []int {
    result := make([]int, 0)
    for _, n := range numbers {
        if n%2 == 0 {
            result = append(result, n*2)
        }
    }
    return result
}
```

---

## 7. Tầng 7: Error Handling

### 7.1. Xử Lý Lỗi (Error Handling)

#### Error Returns

```go
// Function trả về error
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}

// Handling
result, err := divide(10, 0)
if err != nil {
    fmt.Println("Error:", err)
    return
}
fmt.Println("Result:", result)

// Error checking pattern
if err := doSomething(); err != nil {
    return fmt.Errorf("doSomething failed: %w", err)
}
```

#### Custom Errors

```go
// Custom error type
type ValidationError struct {
    Field   string
    Message string
}

func (e ValidationError) Error() string {
    return fmt.Sprintf("%s: %s", e.Field, e.Message)
}

func validateEmail(email string) error {
    if !strings.Contains(email, "@") {
        return ValidationError{
            Field:   "email",
            Message: "invalid email format",
        }
    }
    return nil
}
```

### 7.2. Error Types

```go
// Built-in error interface
type Error interface {
    Error() string
}

// Common errors
var (
    ErrNotFound  = errors.New("not found")
    ErrInvalid   = errors.New("invalid argument")
)

// Sentinel errors
if err == ErrNotFound {
    // handle
}
```

---

## 8. Tầng 8: Module & Organization

### 8.1. Import/Module

```go
// Standard library
import "fmt"
import "strings"

// External packages
import "github.com/gin-gonic/gin"

// Alias
import (
    f "fmt"
    str "strings"
)

// Dot import (avoid)
import . "fmt"

// Blank identifier (side effects)
import _ "image/png"

// Relative import (rare)
import "./mypackage"
```

### 8.2. Package

```go
// package declaration
package main

// Multiple files in same package share code
// main.go, utils.go trong cùng package main

// Init function (chạy trước main)
func init() {
    // initialization
}
```

---

## 9. Tầng 9: I/O & Networking

### 9.1. HTTP & Networking

#### net/http

```go
import "net/http"

// Server
http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("Hello, World!"))
})

http.ListenAndServe(":8080", nil)

// Client
resp, err := http.Get("https://example.com")
if err != nil {
    // handle error
}
defer resp.Body.Close()

body, err := io.ReadAll(resp.Body)

// POST request
resp, err := http.Post(
    "https://api.example.com/users",
    "application/json",
    strings.NewReader(`{"name":"John"}`),
)

// With headers
client := &http.Client{}
req, _ := http.NewRequest("GET", "url", nil)
req.Header.Add("Authorization", "Bearer token")
resp, _ := client.Do(req)
```

#### Third-party (gin, chi, fiber)

```go
// Gin
import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()

    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{
            "message": "pong",
        })
    })

    r.GET("/users", func(c *gin.Context) {
        c.JSON(200, []User{
            {Name: "John"},
        })
    })

    r.POST("/users", func(c *gin.Context) {
        var user User
        c.ShouldBindJSON(&user)
        c.JSON(201, user)
    })

    r.Run()
}
```

### 9.2. File I/O

#### Read File

```go
import (
    "os"
    "io"
    "bufio"
)

// Read all
content, err := os.ReadFile("file.txt")

// Read with bufio
file, _ := os.Open("file.txt")
defer file.Close()

reader := bufio.NewReader(file)
for {
    line, _, err := reader.ReadLine()
    if err != nil {
        break
    }
    fmt.Println(string(line))
}

// Read with scanner
file, _ := os.Open("file.txt")
defer file.Close()

scanner := bufio.NewScanner(file)
for scanner.Scan() {
    fmt.Println(scanner.Text())
}
```

#### Write File

```go
import "os"

// Write
os.WriteFile("output.txt", []byte("Hello World"), 0644)

// Append
f, _ := os.OpenFile("log.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
defer f.Close()
f.WriteString("New log entry\n")

// With bufio
writer := bufio.NewWriter(f)
writer.WriteString("Line 1\n")
writer.Flush()
```

#### Path

```go
import "path/filepath"

filepath.Join("dir", "subdir", "file.txt")  // "dir/subdir/file.txt"
filepath.Base("path/to/file.txt")            // "file.txt"
filepath.Dir("path/to/file.txt")            // "path/to"
filepath.Ext("file.txt")                    // ".txt"
filepath.IsAbs("/path/to/file")             // true
```

---

## 10. Tầng 10: Data & Serialization

### 10.1. JSON & Serialization

```go
import "encoding/json"

type User struct {
    Name   string `json:"name"`
    Age    int    `json:"age"`
    Email  string `json:"email,omitempty"`
}

// Marshal (encode)
user := User{Name: "John", Age: 30}
jsonStr, _ := json.Marshal(user)
jsonStr, _ = json.MarshalIndent(user, "", "  ")

// Unmarshal (decode)
var parsed User
json.Unmarshal(jsonStr, &parsed)

// From string
jsonStr := `{"name":"John","age":30}`
json.Unmarshal([]byte(jsonStr), &parsed)

// Decoder/Encoder
dec := json.NewDecoder(strings.NewReader(jsonStr))
dec.Decode(&parsed)

enc := json.NewEncoder(os.Stdout)
enc.Encode(user)
```

### 10.2. Date & Time

```go
import "time"

// Current time
now := time.Now()

// Parse
t, _ := time.Parse("2006-01-02", "2024-01-15")
t, _ = time.Parse("2006-01-02T15:04:05Z07:00", "2024-01-15T10:30:00Z")

// Format
t.Format("2006-01-02 15:04:05")  // "2024-01-15 10:30:00"

// Arithmetic
tomorrow := now.AddDate(0, 0, 1)
yesterday := now.Add(-24 * time.Hour)

// Duration
later := now.Add(30 * time.Minute)

// Compare
t1.Before(t2)
t1.After(t2)
t1.Equal(t2)

// Unix timestamp
timestamp := now.Unix()
time.Unix(timestamp, 0)
```

### 10.3. Regular Expression

```go
import "regexp"

text := "My email is john@example.com"

// Compile
re := regexp.MustCompile(`[\w.-]+@[\w.-]+`)

// Match
match := re.Find all
matchesString(text)

// Find := re.FindAllString(text, -1)

// Replace
replaced := re.ReplaceAllString(text, "[email]")

// Split
parts := re.Split(text, -1)

// Named groups
re := regexp.MustCompile(`(?P<user>[\w.-]+)@(?P<domain>[\w.-]+)`)
match := re.FindStringSubmatch(text)
result := re.SubexpNames()
for i, name := range result {
    if i > 0 && name != "" && match[i] != "" {
        fmt.Printf("%s: %s\n", name, match[i])
    }
}
```

---

## 11. Tầng 11: Development Practices

### 11.1. Testing

#### Unit Tests

```go
// file_test.go
import "testing"

func TestAdd(t *testing.T) {
    result := add(2, 3)
    if result != 5 {
        t.Errorf("Expected 5, got %d", result)
    }
}

func TestDivide(t *testing.T) {
    _, err := divide(10, 0)
    if err == nil {
        t.Error("Expected error for division by zero")
    }
}

func TestTableDriven(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive", 2, 3, 5},
        {"negative", -1, -1, -2},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := add(tt.a, tt.b)
            if result != tt.expected {
                t.Errorf("Expected %d, got %d", tt.expected, result)
            }
        })
    }
}
```

#### Benchmarks

```go
import "testing"

func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        add(2, 3)
    }
}

func BenchmarkParallel(b *testing.B) {
    b.RunParallel(func(pb *testing.PB) {
        for pb.Next() {
            add(2, 3)
        }
    })
}
```

#### Mocks

```go
// Interface for mocking
type Repository interface {
    Get(id string) (User, error)
}

// Real implementation
type DBRepository struct{}

func (r DBRepository) Get(id string) (User, error) {
    // database query
    return User{}, nil
}

// Mock implementation
type MockRepository struct {
    GetFunc func(id string) (User, error)
}

func (m MockRepository) Get(id string) (User, error) {
    return m.GetFunc(id)
}

// Test
func TestGetUser(t *testing.T) {
    mock := MockRepository{
        GetFunc: func(id string) (User, error) {
            return User{Name: "John"}, nil
        },
    }

    service := NewService(mock)
    user, err := service.GetUser("1")
    if err != nil {
        t.Error(err)
    }
    if user.Name != "John" {
        t.Errorf("Expected John, got %s", user.Name)
    }
}
```

### 11.2. Logging

```go
import "log"

// Basic
log.Println("Info message")
log.Printf("User: %s", "John")

// Flags
log.SetFlags(log.Ldate | log.Ltime | log.Lshortfile)

// Fatal (exit after log)
log.Fatal("Fatal message")
log.Fatalf("Fatal: %v", err)

// Panic (panic after log)
log.Panic("Panic message")

// Structured logging (zerolog, zap)
```

### 11.3. Configuration

```go
import (
    "os"
    "strconv"
)

// Environment variables
dbHost := getEnv("DB_HOST", "localhost")
dbPort, _ := strconv.Atoi(getEnv("DB_PORT", "5432"))

func getEnv(key, defaultValue string) string {
    if value := os.Getenv(key); value != "" {
        return value
    }
    return defaultValue
}

// Viper (popular config library)
import "github.com/spf13/viper"

viper.SetConfigName("config")
viper.AddConfigPath(".")
viper.ReadInConfig()

dbHost := viper.GetString("database.host")
```

### 11.4. Build & Package Management

```bash
# Go modules
go mod init github.com/username/project
go mod tidy

# Dependencies
go get github.com/gin-gonic/gin
go get github.com/gin-gonic/gin@v1.9.0

# Build
go build -o myapp
go build -ldflags="-s -w" # strip symbols

# Cross-compile
GOOS=linux GOARCH=amd64 go build

# Test
go test ./...
go test -v ./...
go test -cover ./...

# Benchmark
go test -bench=.
```

---

## 12. Tầng 12: Advanced Concepts

### 12.1. Advanced Concepts

#### Reflection

```go
import "reflect"

func printType(v interface{}) {
    t := reflect.TypeOf(v)
    fmt.Printf("Type: %s\n", t)

    if v := reflect.ValueOf(v); v.Kind() == reflect.Struct {
        for i := 0; i < v.NumField(); i++ {
            f := v.Field(i)
            fmt.Printf("Field %d: %s = %v\n", i, t.Field(i).Name, f)
        }
    }
}
```

#### Unsafe

```go
import "unsafe"

func intToBytes(i int64) []byte {
    bytes := make([]byte, 8)
    *(*int64)(unsafe.Pointer(&bytes[0])) = i
    return bytes
}
```

#### CGO

```go
import "C"

func printC() {
    C.puts(C.CString("Hello from C"))
}
```

---

## 13. Tầng 13: Memory Layout

### 13.1. Struct Layout

```go
// Default: compiler optimizes field order
type Person struct {
    Name string
    Age  int
    ID   int64
}

// Zero padding tự động thêm

// struct without padding (rare)
type Packed struct {
    A int8  // 1 byte
    B int64 // 8 bytes
    C int8  // 1 byte
}

// Manual reordering để minimize padding
type Optimized struct {
    A int64 // 8 bytes - aligned
    B int8  // 1 byte
    C int7  // 1 byte - pad 6 bytes
}
```

### 13.2. Memory Alignment

```go
// Go aligns fields to their natural boundaries
// int64 aligned to 8 bytes
// int32 aligned to 4 bytes

// alignof
var x int64
unsafe.Alignof(x) // 8
```

---

## 14. Tầng 14: Compilation Model

### 14.1. Compilation

```bash
# Compile
go build main.go
go build -o app main.go

# Với flags
go build -ldflags="-s -w -X main.version=1.0.0" main.go

# Cross-compile
GOOS=linux GOARCH=amd64 go build
GOOS=windows GOARCH=386 go build

# Compile to WASM
GOOS=js GOARCH=wasm go build -o main.wasm
```

### 14.2. Go Compiler

```bash
# Go toolchain
go version
go env GOVERSION

# Build modes
go build -buildmode=c-archive
go build -buildmode=c-shared

# Trimming (Go 1.19+)
go build -trimpath
```

---

## 15. Tầng 15: Linking Model

### 15.1. Linking

```go
// Static linking (default)
go build -ldflags="-linkmode=internal"

// Dynamic linking
go build -ldflags="-linkmode=external"
```

---

## 16. Tầng 16: Runtime

### 16.1. Go Runtime

```go
// Go runtime handles:
// - Goroutine scheduling
// - Garbage collection
// - Memory management
// - Concurrency primitives

// GOMAXPROCS
runtime.GOMAXPROCS(4)

// NumCPU
runtime.NumCPU()

// GC
runtime.GC()
debug.FreeOSMemory()
```

### 16.2. Panic/Defer

```go
// Panic (throw exception)
func safeCall() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered:", r)
        }
    }()
    panic("something went wrong")
}

// Defer (always executed)
func readFile(name string) {
    file, _ := os.Open(name)
    defer file.Close()
    // ...
}

// Deferred function run in LIFO order
func example() {
    defer fmt.Println("1")
    defer fmt.Println("2")
    defer fmt.Println("3")
}
// Output: 3, 2, 1
```

---

## 17. Tầng 17: Language Design Patterns

### 17.1. Duck Typing

```go
// Go's interface là structural typing
type Duck interface {
    Quack()
}

type Person struct{}

func (p Person) Quack() {
    fmt.Println("Person quacking!")
}

func makeQuack(d Duck) {
    d.Quack()
}

makeQuack(Person{}) // Works!
```

### 17.2. Zero Value

```go
// Zero values
var i int      // 0
var f float64  // 0.0
var s string   // ""
var b bool     // false
var p *int     // nil
var arr []int  // nil
var m map[int]int // nil

// Zero value useful for pointers và interfaces
```

---

## 18. Tầng 18: Standard Library

### 18.1. Collections

```go
// Slice
s := []int{1, 2, 3}
s = append(s, 4)

// Map
m := make(map[string]int)
m["key"] = 1

// Struct
type Point struct{ X, Y int }

// Channel
ch := make(chan int, 10)
```

### 18.2. Utilities

#### Strings

```go
import "strings"

strings.Split("a,b,c", ",")
strings.Join([]string{"a", "b"}, "-")
strings.Contains("hello", "lo")
strings.TrimSpace("  hello  ")
strings.ToLower("HELLO")
strings.ToUpper("hello")
```

#### Conversion

```go
import "strconv"

i, _ := strconv.Atoi("42")
s := strconv.Itoa(42)
b, _ := strconv.ParseBool("true")
s := strconv.FormatBool(true)
f, _ := strconv.ParseFloat("3.14", 64)
s := strconv.FormatFloat(3.14, 'f', -1, 64)
```

### 18.3. I/O & System

```go
import (
    "os"
    "os/exec"
    "flag"
)

os.Args           // command line args
os.Exit(0)        // exit
os.Getenv("PATH") // environment variable

// Command
cmd := exec.Command("ls", "-la")
output, _ := cmd.Output()

// Flag
name := flag.String("name", "default", "description")
flag.Parse()
```

---

## 19. Tầng 19: Ecosystem

### 19.1. Web Frameworks

#### Gin

```go
import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()

    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{"message": "pong"})
    })

    r.GET("/users/:id", func(c *gin.Context) {
        id := c.Param("id")
        c.JSON(200, gin.H{"id": id})
    })

    r.POST("/users", func(c *gin.Context) {
        var user User
        c.ShouldBindJSON(&user)
        c.JSON(201, user)
    })

    r.Run()
}
```

#### Echo

```go
import "github.com/labstack/echo/v4"

func main() {
    e := echo.New()

    e.GET("/", func(c echo.Context) error {
        return c.String(200, "Hello!")
    })

    e.Start(":1323")
}
```

### 19.2. Database & ORM

#### GORM

```go
import "gorm.io/gorm"

type User struct {
    gorm.Model
    Name  string
    Email string `gorm:"uniqueIndex"`
}

db, _ := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})

db.AutoMigrate(&User{})

// Create
db.Create(&User{Name: "John", Email: "john@example.com"})

// Read
var user User
db.First(&user, 1)
db.Where("name = ?", "John").First(&user)

// Update
db.Model(&user).Update("Name", "Jane")

// Delete
db.Delete(&user)
```

#### SQLx

```go
import "github.com/jmoiron/sqlx"

db, _ := sqlx.Connect("postgres", "user=foo dbname=bar")

type User struct {
    ID   int    `db:"id"`
    Name string `db:"name"`
}

var users []User
db.Select(&users, "SELECT * FROM users")

db.MustExec("INSERT INTO users (name) VALUES ($1)", "John")
```

### 19.3. Testing

```go
import "testing"

// Assertions (require testify)
import "github.com/stretchr/testify/assert"
import "github.com/stretchr/testify/require"

func TestExample(t *testing.T) {
    assert.Equal(t, 4, 2+2, "they should be equal")
    require.NoError(t, err)
}
```

---

## 20. Tầng 20: Toolchain

### 20.1. Build & Package Management

```bash
# Go modules
go mod init github.com/user/project
go mod tidy

# Update dependencies
go get -u
go get -u ./...

# Lint
go vet
golint ./...
staticcheck ./...

# Format
go fmt
gofmt -w .

# Build
go build
go build -o app
go build -ldflags="-s -w"

# Test
go test
go test -v
go test -cover

# Documentation
go doc fmt
godoc -http=:6060
```

### 20.2. Code Quality

```bash
# gofmt
gofmt -w src/
gofmt -d src/ # diff only

# go vet
go vet ./...

# golint
golint ./...

# staticcheck
staticcheck ./...

# golangci-lint (all-in-one)
golangci-lint run

# goimports (format + imports)
goimports -w src/
```

### 20.3. IDE & Debugging

```go
// VS Code / GoLand debugging
// Set breakpoints in IDE

// Delve debugger
dlv debug main.go
dlv test ./...

// Print debugging
fmt.Printf("%+v\n", value)

// log
log.Printf("Debug: %v", value)
```

---

## Tổng Kết

Go là ngôn ngữ:

- **Static typing** với type inference
- **Simplicity** - ít keywords, dễ học
- **Concurrent** - goroutines và channels
- **Compiled** - fast execution, static linking
- **No inheritance** - dùng composition và interface

### Go Version History

| Version | Release Date | Key Features                                           |
|---------|-------------|-------------------------------------------------------|
| Go 1.0  | 2012-03-28  | First stable release                                  |
| Go 1.1  | 2013-05-13  | Race detector                                         |
| Go 1.5  | 2015-08-19  | Internal packages, GC improvements                    |
| Go 1.9  | 2017-08-24  | Type aliases                                          |
| Go 1.11 | 2018-08-24  | Go modules                                            |
| Go 1.13 | 2019-09-03  | Errors improvements                                   |
| Go 1.14 | 2020-02-25  | Module support stable                                 |
| Go 1.16 | 2021-02-16  | io/fs, embed                                         |
| Go 1.18 | 2022-03-15  | Generics (type parameters)                           |
| Go 1.20 | 2023-02-01  | Profile-guided optimization                           |
| Go 1.21 | 2023-08-08  | slices, maps, cmp packages                           |
| Go 1.22 | 2024-02-06  | Range over integers, HTTP routing improvements        |
