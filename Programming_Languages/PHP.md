# PHP Syntax Reference

## Mục Lục

1. [Phân Loại Ngôn Ngữ](#1-phân-loại-ngôn-ngữ)
2. [Tầng 1: Syntax & Semantics](#tầng-1-syntax--semantics)
   - [1.1 Khai Báo Biến](#11-khai-báo-biến)
   - [1.2 Khai Báo Hàm](#12-khai-báo-hàm)
   - [1.3 Vòng Lặp](#13-vòng-lặp)
   - [1.4 Điều Kiện](#14-điều-kiện)
3. [Tầng 2: Type System](#tầng-2-type-system)
   - [2.1 Kiểu Dữ Liệu Cơ Bản](#21-kiểu-dữ-liệu-cơ-bản)
   - [2.2 Enum](#22-enum)
   - [2.3 Nullable Types](#23-nullable-types)
   - [2.4 Null Safety](#24-null-safety)
   - [2.5 Generics](#25-generics)
   - [2.6 Collection Operations](#26-collection-operations)
   - [2.7 String Operations](#27-string-operations)
4. [Tầng 3: OOP & Type Relationships](#tầng-3-oop--type-relationships)
   - [3.1 Class/Object](#31-classobject)
   - [3.2 Kế Thừa & Đa Hình](#32-kế-thừa--đa-hình)
   - [3.3 Interface/Trait/Protocol](#33-interfacetraitprotocol)
   - [3.4 Visibility/Access Modifiers](#34-visibilityaccess-modifiers)
5. [Tầng 4: Memory Model](#tầng-4-memory-model)
   - [4.1 Memory Management](#41-memory-management)
   - [4.2 Property & Getter/Setter](#42-property--gettersetter)
6. [Tầng 5: Concurrency Model](#tầng-5-concurrency-model)
   - [5.1 Concurrency/Async](#51-concurrencyasync)
7. [Tầng 6: Paradigm](#tầng-6-paradigm)
   - [6.1 Functional Programming](#61-functional-programming)
8. [Tầng 7: Error Handling](#tầng-7-error-handling)
   - [8.1 Xử Lý Lỗi](#81-xử-lý-lỗi)
   - [8.2 Error Types](#82-error-types)
9. [Tầng 8: Module & Organization](#tầng-8-module--organization)
   - [8.1 Import/Module](#81-importmodule)
   - [8.2 Annotation/Attribute](#82-annotationattribute)
10. [Tầng 9: I/O & Networking](#tầng-9-io--networking)
    - [9.1 HTTP & Networking](#91-http--networking)
    - [9.2 File I/O](#92-file-io)
11. [Tầng 10: Data & Serialization](#tầng-10-data--serialization)
    - [10.1 JSON & Serialization](#101-json--serialization)
    - [10.2 Date & Time](#102-date--time)
    - [10.3 Regular Expression](#103-regular-expression)
12. [Tầng 11: Development Practices](#tầng-11-development-practices)
    - [11.1 Testing](#111-testing)
    - [11.2 Logging](#112-logging)
    - [11.3 Dependency Injection](#113-dependency-injection)
    - [11.4 Configuration](#114-configuration)
    - [11.5 Build & Package Management](#115-build--package-management)
    - [11.6 Documentation](#116-documentation)
13. [Tầng 12: Advanced Concepts](#tầng-12-advanced-concepts)
    - [12.1 Advanced Concepts](#121-advanced-concepts)
14. [Tầng 13: Memory Layout](#tầng-13-memory-layout)
    - [13.1 Struct Layout](#131-struct-layout)
15. [Tầng 14: Compilation Model](#tầng-14-compilation-model)
    - [14.1 Interpreter & Bytecode](#141-interpreter--bytecode)
16. [Tầng 15: Linking Model](#tầng-15-linking-model)
    - [15.1 Dynamic Loading](#151-dynamic-loading)
17. [Tầng 16: Runtime](#tầng-16-runtime)
    - [16.1 Stack & Call Stack](#161-stack--call-stack)
    - [16.2 Garbage Collector](#162-garbage-collector)
18. [Tầng 17: Language Design Patterns](#tầng-17-language-design-patterns)
    - [17.1 RAII Pattern](#171-raii-pattern)
    - [17.2 Data Transfer Object](#172-data-transfer-object)
19. [Tầng 18: Standard Library](#tầng-18-standard-library)
    - [18.1 Collections](#181-collections)
    - [18.2 Utilities](#182-utilities)
    - [18.3 I/O & System](#183-io--system)
    - [18.4 String & Regex](#184-string--regex)
20. [Tầng 19: Ecosystem](#tầng-19-ecosystem)
    - [19.1 Web Frameworks](#191-web-frameworks)
    - [19.2 Database & ORM](#192-database--orm)
    - [19.3 Testing](#193-testing)
    - [19.4 DevOps & Infrastructure](#194-devops--infrastructure)
    - [19.5 Security](#195-security)
21. [Tầng 20: Toolchain](#tầng-20-toolchain)
    - [20.1 Build & Package Management](#201-build--package-management)
    - [20.2 Code Quality](#202-code-quality)
    - [20.3 IDE & Debugging](#203-ide--debugging)
    - [20.4 Profiling](#204-profiling)

---

## 1. Phân Loại Ngôn Ngữ

| Thuộc tính | Giá trị |
| ---------- | -------- |
| **Loại** | Web Backend |
| **Biên dịch/Thông dịch** | Interpreted |
| **Typing** | Dynamic, Weak |
| **Paradigm** | Multi-paradigm (Procedural, OO) |
| **Use Cases** | Web backend (Laravel, Symfony), CMS (WordPress) |

### Khởi Chạy File PHP

```bash
# Chạy trực tiếp
php script.php

# Built-in server
php -S localhost:8000

# REPL
php -a
```

---

## Tầng 1: Syntax & Semantics

### 1.1. Khai Báo Biến (Variable Declaration)

#### Mutable - Biến thường

```php
$name = "John";
$age = 25;
$price = 19.99;
$isActive = true;
```

#### Immutable - Hằng số

```php
// Dùng const (PHP 5.3+)
const MAX_SIZE = 100;
const API_URL = "https://api.example.com";

// Dùng define (có thể dùng cho dynamic constant)
define("DEBUG_MODE", true);
define("DEFAULT_TIMEOUT", 30);

// Trong class
class Config {
    const VERSION = "1.0.0";
    public const PUBLIC_CONST = "value";
    private const PRIVATE_CONST = "secret";
}
```

#### Type Declaration (PHP 7.0+)

```php
function greet(string $name): string {
    return "Hello, $name";
}

function process(int $num, float $price, array $items): bool {
    return true;
}

// Union types (PHP 8.0+)
function setId(int|string $id): void {
    // ...
}

// Mixed type (PHP 8.0+)
function processData(mixed $data): mixed {
    return $data;
}
```

#### Type Inference

```php
// PHP là dynamic typing, tự suy luận kiểu
$value = "hello";      // string
$value = 42;           // int
$value = [1, 2, 3];   // array
```

#### Static Variable

```php
function counter(): int {
    static $count = 0;  // Giữ giá trị giữa các lần gọi
    $count++;
    return $count;
}

counter(); // 1
counter(); // 2
counter(); // 3
```

#### Global Variable

```php
$globalVar = "I'm global";

function accessGlobal(): string {
    global $globalVar;
    return $globalVar;
}

// Hoặc dùng $GLOBALS
function accessGlobal2(): string {
    return $GLOBALS['globalVar'];
}
```

#### Variable Variables

```php
$varName = "dynamic";
$$varName = "Hello";  // Tạo biến $dynamic = "Hello"
echo $dynamic;       // "Hello"
```

---

### 1.2. Khai Báo Hàm (Function Declaration)

#### Function cơ bản

```php
function greet(string $name): string {
    return "Hello, $name!";
}

// Không có return type
function sayHi($name) {
    echo "Hi, $name";
}

// Void return (PHP 7.1+)
function logMessage(string $msg): void {
    echo $msg;
}
```

#### Parameters

```php
// Required parameters
function add($a, $b) {
    return $a + $b;
}

// Default parameters
function greet($name = "Guest") {
    return "Hello, $name";
}

// Named arguments (PHP 8.0+)
function createUser(string $name, int $age, string $email) {
    // ...
}
createUser(
    name: "John",
    age: 25,
    email: "john@example.com"
);
```

#### Variadic Parameters

```php
function sum(...$numbers): int {
    return array_sum($numbers);
}

sum(1, 2, 3, 4); // 10

function merge(string $prefix, ...$items): array {
    return array_map(fn($item) => "$prefix.$item", $items);
}
```

#### Arrow Function (PHP 7.4+)

```php
$add = fn($a, $b) => $a + $b;

// Với typed parameters (PHP 8.0+)
$add = fn(int $a, int $b): int => $a + $b;
```

#### Closure

```php
$multiply = function($a) use ($multiplier) {
    return $a * $multiplier;
};

$multiplier = 2;
echo $multiply(5); // 10
```

#### Higher-Order Function

```php
function apply(int $value, callable $func): int {
    return $func($value);
}

$result = apply(5, fn($x) => $x * 2); // 10
```

#### Method trong Class

```php
class Calculator {
    public function add(int $a, int $b): int {
        return $a + $b;
    }

    // Static method
    public static function multiply(int $a, int $b): int {
        return $a * $b;
    }
}

// Gọi method
$calc = new Calculator();
echo $calc->add(2, 3);      // 5
echo Calculator::multiply(2, 3); // 6
```

#### Constructor & Destructor

```php
class User {
    public string $name;
    public ?string $email;

    // Constructor
    public function __construct(string $name, ?string $email = null) {
        $this->name = $name;
        $this->email = $email;
    }

    // Destructor
    public function __destruct() {
        // Cleanup code
    }
}
```

---

### 1.3. Vòng Lặp (Loops)

#### For Loop

```php
for ($i = 0; $i < 5; $i++) {
    echo $i . " ";
}
// Output: 0 1 2 3 4
```

#### While Loop

```php
$i = 0;
while ($i < 5) {
    echo $i++;
}
// Output: 0 1 2 3 4
```

#### Do-While

```php
$i = 0;
do {
    echo $i++;
} while ($i < 5);
// Output: 0 1 2 3 4
```

#### For-each

```php
$items = ['a', 'b', 'c'];

// Value only
foreach ($items as $item) {
    echo $item;
}

// Key and value
foreach ($items as $key => $item) {
    echo "$key: $item";
}

// Reference (&)
foreach ($items as &$item) {
    $item = strtoupper($item);
}
unset($item);  // Quan trọng: unset sau khi dùng reference
```

#### Iterator

```php
class MyIterator implements Iterator {
    private int $position = 0;
    private array $data = ['a', 'b', 'c'];

    public function current(): mixed {
        return $this->data[$this->position];
    }

    public function key(): int {
        return $this->position;
    }

    public function next(): void {
        $this->position++;
    }

    public function rewind(): void {
        $this->position = 0;
    }

    public function valid(): bool {
        return isset($this->data[$this->position]);
    }
}
```

#### Loop Control

```php
// Break
for ($i = 0; $i < 10; $i++) {
    if ($i === 5) break;
    echo $i;
}

// Continue
for ($i = 0; $i < 5; $i++) {
    if ($i === 2) continue;
    echo $i;
}

// Labeled loops
$matrix = [[1,2], [3,4]];
outer:
for ($i = 0; $i < 2; $i++) {
    for ($j = 0; $j < 2; $j++) {
        if ($matrix[$i][$j] === 2) break 2; // Thoát cả 2 loop
    }
}
```

---

### 1.4. Điều Kiện (Conditionals)

#### If-Else

```php
$age = 20;

if ($age >= 18) {
    echo "Adult";
} elseif ($age >= 13) {
    echo "Teenager";
} else {
    echo "Child";
}
```

#### Switch

```php
$day = date('N');

switch ($day) {
    case 1:
        echo "Monday";
        break;
    case 2:
        echo "Tuesday";
        break;
    case 6:
    case 7:
        echo "Weekend";
        break;
    default:
        echo "Weekday";
}

// Match expression (PHP 8.0+)
$result = match ($day) {
    1 => "Monday",
    2 => "Tuesday",
    6, 7 => "Weekend",
    default => "Weekday",
};
```

#### Ternary Operator

```php
$status = $age >= 18 ? "Adult" : "Minor";

// Null coalescing với ternary
$name = $user['name'] ?? "Guest";

// Short ternary (PHP 8.0+)
$value = $x ?: "default";  // Dùng $x nếu truthy, không thì "default"
```

#### Elvis Operator (PHP 8.0+)

```php
// Thực ra là null coalescing assignment
$value ??= "default";  // Chỉ gán nếu null
```

#### Null Coalescing

```php
$name = $user['name'] ?? "Guest";
$email = $user['email'] ?? $user['contact']['email'] ?? "no email";
```

#### Match Expression (PHP 8.0+)

```php
$status = match($code) {
    200 => "OK",
    404 => "Not Found",
    500 => "Server Error",
    default => "Unknown",
};

// Với conditions
$result = match(true) {
    $age < 13 => "Child",
    $age < 20 => "Teen",
    default => "Adult",
};
```

---

## Tầng 2: Type System

### 2.1. Kiểu Dữ Liệu Cơ Bản (Primitive Types)

#### Integer

```php
$int = 42;
$hex = 0x1A;       // 26
$binary = 0b1010;  // 10
$octal = 052;      // 42

// PHP 8.0+ numeric string
var_dump(is_numeric("42"));  // true
var_dump(intval("42"));       // 42
```

#### Float

```php
$float = 3.14;
$scientific = 1.2e3;  // 1200

// Float precision
var_dump(0.1 + 0.2);   // 0.3 (gần đúng!)
```

#### Boolean

```php
$bool = true;
$bool = false;

// Truthy/Falsy values
// Falsy: 0, 0.0, "", "0", null, [], false
// Truthy: "0" (string), -1, etc.
```

#### String

```php
$str = "Hello";
$str = 'Hello';

// Single vs Double quotes
$name = "John";
"$name";   // "John" (interpolate)
'$name';   // "$name" (literal)
```

#### Array

```php
// Indexed array
$arr = [1, 2, 3];
$arr = array(1, 2, 3);

// Associative array
$user = [
    'name' => 'John',
    'age' => 25,
];

// Multidimensional
$matrix = [
    [1, 2, 3],
    [4, 5, 6],
];
```

#### Object

```php
$obj = new stdClass();
$obj->name = 'John';

// Từ array
$obj = (object)['name' => 'John'];
```

#### Callable/Closure

```php
$func = function($x) { return $x * 2; };

// Callable type
function callIt(callable $fn) {
    return $fn(5);
}
```

#### Resource

```php
$file = fopen("test.txt", "r");  // Resource
fclose($file);
```

#### Never (PHP 8.1+)

```php
function redirect(string $url): never {
    header("Location: $url");
    exit();
}
```

#### Void (PHP 7.1+)

```php
function logMessage(string $msg): void {
    echo $msg;
    // Không return gì
}
```

---

### 2.2. Enum (PHP 8.1+)

#### Basic Enum

```php
enum Status {
    case Pending;
    case Active;
    case Completed;
    case Failed;
}

$status = Status::Active;

switch ($status) {
    case Status::Pending:
        echo "Waiting...";
        break;
    case Status::Active:
        echo "Running";
        break;
}
```

#### Enum with Values

```php
enum Status: string {
    case Pending = 'pending';
    case Active = 'active';
    case Completed = 'completed';

    public function label(): string {
        return match($this) {
            self::Pending => 'Chờ xử lý',
            self::Active => 'Hoạt động',
            self::Completed => 'Hoàn thành',
        };
    }
}

echo Status::Active->value;     // 'active'
echo Status::Active->label();    // 'Hoạt động'
```

#### Enum with Methods

```php
enum HttpCode: int {
    case OK = 200;
    case NotFound = 404;
    case ServerError = 500;

    public function isSuccess(): bool {
        return $this->value >= 200 && $this->value < 300;
    }

    public static function fromValue(int $value): ?self {
        return self::tryFrom($value);
    }
}
```

#### Backed Enum

```php
enum OrderStatus: string {
    case Pending = 'pending';
    case Paid = 'paid';
    case Shipped = 'shipped';
    case Delivered = 'delivered';

    public function canCancel(): bool {
        return $this === self::Pending;
    }
}

// Convert
$status = OrderStatus::from('paid');      // Paid
$value = OrderStatus::Paid->value;         // 'paid'
$name = OrderStatus::Paid->name;          // 'Paid'
```

---

### 2.3. Nullable Types

#### Nullable

```php
// PHP 7.1+
function getUser(?int $id): ?string {
    if ($id === null) {
        return null;
    }
    return "User $id";
}

// Null default
function greet(?string $name = null): string {
    return "Hello, " . ($name ?? "Guest");
}
```

#### Null Check

```php
$value = null;

if ($value === null) {
    echo "No value";
}

// Hoặc dùng null coalescing
echo $value ?? "default";
```

#### Null-safe Operator (PHP 8.0+)

```php
// Trước PHP 8.0
$country = null;
if ($user !== null) {
    if ($user->getAddress() !== null) {
        $country = $user->getAddress()->getCountry();
    }
}

// PHP 8.0+
$country = $user?->getAddress()?->getCountry();
```

---

### 2.4. Null Safety

#### Elvis Operator

```php
$name = $user ?? "Guest";
$value = $data['name'] ?? $default ?? "default";
```

#### Null-safe Operator (PHP 8.0+)

```php
$result = $user?->getProfile()?->getAvatar()?->getUrl();
```

#### Null Coalescing Assignment (PHP 7.4+)

```php
$user['name'] ??= "Guest";  // Chỉ gán nếu null
```

---

### 2.5. Generics

#### PHP không có Generics như Java/C#

Nhưng có thể dùng:

```php
// 1. DocBlock annotations (thường dùng với IDE)
/**
 * @template T
 * @param T $value
 * @return T
 */
function identity($value) {
    return $value;
}

// 2. PHPStan/Psalm kiểu static analysis
// 3. Union types (PHP 8.0+)
function process(int|string $value): int|string {
    return $value;
}

// 4. Custom generic-like class
class Container {
    /** @var mixed */
    private $value;

    public function set(mixed $value): self {
        $this->value = $value;
        return $this;
    }

    public function get(): mixed {
        return $this->value;
    }
}
```

---

### 2.6. Collection Operations

PHP sử dụng các hàm array_* hoặc class từ SPL.

#### Map/Transform

```php
$numbers = [1, 2, 3, 4, 5];

// Dùng array_map
$squared = array_map(fn($n) => $n * $n, $numbers);
// [1, 4, 9, 16, 25]

// Với key
$keys = ['a', 'b', 'c'];
$values = array_map(fn($k, $v) => strtoupper($v), $keys, $numbers);
```

#### Filter

```php
$numbers = [1, 2, 3, 4, 5];

$evens = array_filter($numbers, fn($n) => $n % 2 === 0);
// [2, 4]

// Filter với key
$assoc = ['a' => 1, 'b' => 2, 'c' => 3];
$result = array_filter($assoc, fn($v, $k) => $k !== 'b', ARRAY_FILTER_USE_BOTH);
```

#### Reduce/Fold

```php
$numbers = [1, 2, 3, 4, 5];

$sum = array_reduce($numbers, fn($carry, $item) => $carry + $item, 0);
// 15

$product = array_reduce($numbers, fn($carry, $item) => $carry * $item, 1);
// 120
```

#### FlatMap

```php
$words = ['hello', 'world'];

// Tách mỗi word thành các ký tự
$chars = array_merge(...array_map('str_split', $words));
// ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
```

#### Sort

```php
$numbers = [3, 1, 4, 1, 5, 9, 2, 6];

sort($numbers);           // Sắp xếp tăng, thay đổi array
rsort($numbers);          // Sắp xếp giảm

asort($numbers);          // Sắp xếp theo value, giữ key
ksort($numbers);          // Sắp xếp theo key

// Với callback
usort($numbers, fn($a, $b) => $a <=> $b);  // Spaceship operator
usort($numbers, fn($a, $b) => $b - $a);    // Giảm dần
```

#### Find/First/Last

```php
$numbers = [1, 2, 3, 4, 5];

$first = reset($numbers);        // 1
$last = end($numbers);          // 5

$found = array_find($numbers, fn($n) => $n > 3);     // 4
$key = array_find_key($numbers, fn($n) => $n > 3);   // 3
```

#### Any/All/None

```php
$numbers = [1, 2, 3, 4, 5];

$hasEven = array_any($numbers, fn($n) => $n % 2 === 0);  // true (PHP 8.4+)
$allPositive = array_all($numbers, fn($n) => $n > 0);  // true (PHP 8.4+)

// Trước PHP 8.4
$hasEven = in_array(true, array_map(fn($n) => $n % 2 === 0, $numbers));
$allPositive = !in_array(false, array_map(fn($n) => $n > 0, $numbers));
```

#### GroupBy

```php
$users = [
    ['name' => 'John', 'role' => 'admin'],
    ['name' => 'Jane', 'role' => 'user'],
    ['name' => 'Bob', 'role' => 'admin'],
];

$grouped = [];
foreach ($users as $user) {
    $grouped[$user['role']][] = $user;
}
```

#### Chunk

```php
$numbers = [1, 2, 3, 4, 5, 6, 7, 8];

$chunks = array_chunk($numbers, 3);
// [[1,2,3], [4,5,6], [7,8]]
```

#### Zip

```php
$names = ['a', 'b', 'c'];
$values = [1, 2, 3];

$zipped = array_map(null, $names, $values);
// [['a', 1], ['b', 2], ['c', 3]]

// Hoặc dùng array_combine
$combined = array_combine($names, $values);
// ['a' => 1, 'b' => 2, 'c' => 3]
```

---

### 2.7. String Operations

#### Concatenation

```php
$firstName = "John";
$lastName = "Doe";

$fullName = $firstName . " " . $lastName;
// "John Doe"

// Với .=
$greeting = "Hello";
$greeting .= " World";  // "Hello World"
```

#### Interpolation

```php
$name = "John";

// Double quotes - biến được interpolate
echo "Hello, $name";           // Hello, John
echo "Hello, {$name}";          // Hello, John

// Single quotes - không interpolate
echo 'Hello, $name';            // Hello, $name

// Complex syntax
$user = ['name' => 'John', 'age' => 25];
echo "Hello, {$user['name']}"; // Hello, John
```

#### Template String (heredoc/nowdoc)

```php
// Heredoc - interpolate
$html = <<<HTML
<div class="container">
    <h1>Welcome, $name!</h1>
    <p>Your age: {$user['age']}</p>
</div>
HTML;

// Nowdoc - không interpolate
$plain = <<<'PLAIN'
This is plain text.
$name will not be replaced.
PLAIN;
```

#### Split

```php
$str = "apple,banana,cherry";
$fruits = explode(",", $str);
// ['apple', 'banana', 'cherry']

// Với limit
$parts = explode(",", $str, 2);
// ['apple', 'banana,cherry']

// str_split cho từng ký tự
$chars = str_split($str);
// ['a', 'p', 'p', 'l', 'e', ...]
```

#### Join

```php
$fruits = ['apple', 'banana', 'cherry'];
$str = implode(", ", $fruits);
// "apple, banana, cherry"

// join() là alias của implode
$str = join("-", $fruits);
// "apple-banana-cherry"
```

#### Replace

```php
$str = "Hello World";

// String replace
str_replace("World", "PHP", $str);     // "Hello PHP"

// Case insensitive
str_ireplace("hello", "Hi", $str);    // "Hi World"

// Multiple replacements
str_replace(["hello", "world"], ["Hi", "PHP"], $str);

// Regex replace
preg_replace('/\d+/', '#', "test123");  // "test#"

// Callback replace
preg_replace_callback('/\d+/', fn($m) => (int)$m[0] * 2, "test5"); // "test10"
```

#### Trim

```php
$str = "   Hello World   ";

trim($str);      // "Hello World"
ltrim($str);     // "Hello World   "
rtrim($str);     // "   Hello World"

// Trim specific characters
trim($str, " H"); // "ello World"
```

#### Upper/Lower Case

```php
$str = "Hello World";

strtoupper($str);    // "HELLO WORLD"
strtolower($str);    // "hello world"
ucfirst($str);       // "Hello world" - viết hoa chữ cái đầu
ucwords($str);       // "Hello World" - viết hoa mỗi từ
```

#### Regex Match

```php
$str = "Email: test@example.com";

// preg_match - tìm 1 match
if (preg_match('/(\w+)@(\w+\.\w+)/', $str, $matches)) {
    echo $matches[0];    // Full match: test@example.com
    echo $matches[1];    // Group 1: test
    echo $matches[2];    // Group 2: example.com
}

// preg_match_all - tìm tất cả
preg_match_all('/\d+/', "123 abc 456", $matches);
// $matches[0] = ['123', '456']

// preg_split
$parts = preg_split('/\s+/', "hello world test");
// ['hello', 'world', 'test']
```

#### Substring

```php
$str = "Hello World";

substr($str, 0, 5);      // "Hello" - từ vị trí 0, length 5
substr($str, 6);         // "World" - từ vị trí 6 đến cuối
substr($str, -5);        // "World" - 5 ký tự cuối

// mb_substr cho multibyte
$str = "Xin chào";
mb_substr($str, 0, 4);  // "Xin "
```

#### Length

```php
$str = "Hello";

strlen($str);        // 5 bytes
mb_strlen($str);     // 5 ký tự (cho UTF-8)
```

---

## Tầng 3: OOP & Type Relationships

### 3.1. Class/Object

#### Class Definition

```php
class User {
    // Properties
    public string $name;
    protected int $age;
    private string $email;

    // Static property
    public static int $userCount = 0;

    // Constants
    const STATUS_ACTIVE = 'active';
    const STATUS_INACTIVE = 'inactive';

    // Constructor
    public function __construct(string $name, int $age = 0) {
        $this->name = $name;
        $this->age = $age;
        self::$userCount++;
    }

    // Methods
    public function getName(): string {
        return $this->name;
    }

    public function setEmail(string $email): void {
        $this->email = $email;
    }

    // Static method
    public static function getUserCount(): int {
        return self::$userCount;
    }
}

// Tạo object
$user = new User("John", 25);
echo $user->getName();
```

#### Data Class (PHP 8.0+ - Named Arguments)

```php
// PHP không có data class như Kotlin, nhưng có thể dùng:
class UserDTO {
    public function __construct(
        public string $name,
        public string $email,
        public ?int $age = null
    ) {}
}

// Tạo với named arguments
$user = new UserDTO(
    name: "John",
    email: "john@example.com"
);
```

#### Singleton

```php
class Singleton {
    private static ?Singleton $instance = null;

    private function __construct() {}

    public static function getInstance(): Singleton {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    // Prevent cloning
    private function __clone() {}

    // Prevent unserialization
    public function __wakeup() {
        throw new \Exception("Cannot unserialize singleton");
    }
}
```

#### Factory Method

```php
class UserFactory {
    public static function createAdmin(string $name): User {
        $user = new User($name);
        $user->setRole('admin');
        return $user;
    }

    public static function createGuest(): User {
        return new User('Guest');
    }
}
```

#### Builder Pattern

```php
class UserBuilder {
    private string $name;
    private ?string $email = null;
    private ?int $age = null;
    private array $roles = ['user'];

    public function __construct(string $name) {
        $this->name = $name;
    }

    public function withEmail(string $email): self {
        $this->email = $email;
        return $this;
    }

    public function withAge(int $age): self {
        $this->age = $age;
        return $this;
    }

    public function withRole(string $role): self {
        $this->roles[] = $role;
        return $this;
    }

    public function build(): User {
        $user = new User($this->name);
        if ($this->email) $user->setEmail($this->email);
        if ($this->age) $user->setAge($this->age);
        $user->setRoles($this->roles);
        return $user;
    }
}

$user = (new UserBuilder('John'))
    ->withEmail('john@example.com')
    ->withAge(25)
    ->withRole('admin')
    ->build();
```

---

### 3.2. Kế Thừa & Đa Hình (Inheritance & Polymorphism)

#### Inheritance

```php
class Animal {
    protected string $name;

    public function __construct(string $name) {
        $this->name = $name;
    }

    public function speak(): string {
        return "Some sound";
    }
}

class Dog extends Animal {
    public function speak(): string {
        return "Woof!";
    }
}

$dog = new Dog("Buddy");
echo $dog->speak(); // "Woof!"
```

#### Override

```php
class ParentClass {
    public function greet(): string {
        return "Hello";
    }

    // Gọi parent method
    public function process(): string {
        return parent::greet() . ", World";
    }
}

class ChildClass extends ParentClass {
    public function greet(): string {
        return "Hi";
    }
}
```

#### Abstract Class

```php
abstract class Shape {
    abstract public function area(): float;

    public function describe(): string {
        return "Area: " . $this->area();
    }
}

class Circle extends Shape {
    private float $radius;

    public function __construct(float $radius) {
        $this->radius = $radius;
    }

    public function area(): float {
        return pi() * $this->radius ** 2;
    }
}
```

#### Final Class/Method

```php
final class Config {
    // Không thể extends
}

class MyClass {
    final public function process() {
        // Không thể override
    }
}
```

#### Polymorphism

```php
interface Shape {
    public function area(): float;
}

class Circle implements Shape {
    public function __construct(private float $radius) {}
    public function area(): float {
        return pi() * $this->radius ** 2;
    }
}

class Square implements Shape {
    public function __construct(private float $side) {}
    public function area(): float {
        return $this->side ** 2;
    }
}

function printArea(Shape $shape): void {
    echo $shape->area();
}
```

---

### 3.3. Interface/Trait/Protocol

#### Interface

```php
interface JsonSerializable {
    public function jsonSerialize(): mixed;
}

interface Cacheable {
    public function get(string $key): mixed;
    public function set(string $key, mixed $value): void;
    public function delete(string $key): bool;
}

// Implement multiple interfaces
class FileCache implements Cacheable, JsonSerializable {
    public function get(string $key): mixed {}
    public function set(string $key, mixed $value): void {}
    public function delete(string $key): bool {}
    public function jsonSerialize(): mixed {}
}
```

#### Interface với Default Implementation (PHP 8.0+)

```php
interface Logger {
    public function log(string $message): void;

    // Default implementation
    public function info(string $message): void {
        $this->log("[INFO] $message");
    }

    public function error(string $message): void {
        $this->log("[ERROR] $message");
    }
}
```

#### Trait

```php
trait LoggerTrait {
    private array $logs = [];

    public function log(string $message): void {
        $this->logs[] = $message;
    }

    public function getLogs(): array {
        return $this->logs;
    }
}

trait TimestampTrait {
    public function getTimestamp(): string {
        return date('Y-m-d H:i:s');
    }
}

class UserService {
    use LoggerTrait;
    use TimestampTrait;

    public function createUser(string $name): void {
        $this->log("User created: $name at " . $this->getTimestamp());
    }
}
```

#### Trait Conflicts

```php
trait A {
    public function hello(): string {
        return "A: Hello";
    }
}

trait B {
    public function hello(): string {
        return "B: Hello";
    }
}

class MyClass {
    use A, B {
        B::hello insteadof A;  // Dùng B::hello thay cho A
        A::hello as helloA;    // Đổi tên A::hello thành helloA
    }
}
```

---

### 3.4. Visibility/Access Modifiers

```php
class User {
    public string $name;       // Truy cập mọi nơi
    protected int $age;        // Class và class kế thừa
    private string $email;     // Chỉ trong class đó

    // Property visibility (PHP 7.4+)
    public readonly string $id;  // Chỉ đọc

    // Method visibility
    public function getName(): string { return $this->name; }
    protected function setAge(int $age): void { $this->age = $age; }
    private function validateEmail(): bool { /* ... */ }
}
```

#### Default Visibility

```php
// Trong class - mặc định là public
class MyClass {
    function method() {}  // public
}

// Trong namespace/global - mặc định là public
function globalFunction() {}  // public
```

---

## Tầng 4: Memory Model

### 4.1. Memory Management

#### Garbage Collection

PHP sử dụng automatic garbage collection:

```php
// Reference counting
$a = "hello";
$b = $a;  // $a and $b cùng reference
unset($a); // Giảm reference count

// Circular references được GC xử lý tự động
```

#### Weak Reference (PHP 7.4+)

```php
$obj = new stdClass();
$weakRef = WeakReference::create($obj);

if ($weakRef->get()) {
    echo "Object still exists";
}

unset($obj);  // Object được giải phóng
var_dump($weakRef->get());  // null
```

#### Memory Limit

```php
// Trong php.ini
memory_limit = 256M

// Trong code
ini_set('memory_limit', '512M');
echo memory_get_usage();
echo memory_get_peak_usage();
```

---

### 4.2. Property & Getter/Setter

#### Public Property

```php
class User {
    public string $name = 'Guest';
    public ?string $email = null;
}

$user = new User();
$user->name = "John";  // Direct access
echo $user->name;
```

#### Getter/Setter

```php
class User {
    private string $name;
    private int $age;

    public function getName(): string {
        return $this->name;
    }

    public function setName(string $name): void {
        $this->name = $name;
    }

    // Magic methods (PHP 8.0+)
    public function __get(string $name): mixed {
        if ($name === 'age') {
            return $this->age;
        }
        throw new \Error("Property $name does not exist");
    }

    public function __set(string $name, mixed $value): void {
        if ($name === 'age') {
            $this->age = $value;
        }
    }
}
```

#### Readonly Properties (PHP 8.1+)

```php
class User {
    public function __construct(
        public readonly string $id,
        public readonly string $name
    ) {}
}

$user = new User("1", "John");
// $user->id = "2";  // Error!
```

#### Lazy Properties (PHP 8.4+)

```php
class HeavyObject {
    public function __construct(
        public lazy string $data = null
    ) {}

    public function initialize(): void {
        $this->data = computeHeavyData();
    }
}
```

---

## Tầng 5: Concurrency Model

### 5.1. Concurrency/Async

#### Threads

PHP không có built-in thread tốt, nhưng có thể dùng:

```php
// Parallel extension (PECL - cần cài đặt)
use Parallel\Runtime;
use Parallel\Future;

$runtime = new Runtime();
$future = $runtime->run(function() {
    return heavyComputation();
});

$result = $future->cancel(); // Chờ kết quả
```

#### Async với ReactPHP / Swoole

```php
// Swoole - Async HTTP Server
$http = new Swoole\Http\Server("0.0.0.0", 9501);

$http->on("request", function ($request, $response) {
    $response->header("Content-Type", "text/plain");
    $response->end("Hello World");
});

$http->start();

// Async MySQL (Swoole)
Co::create(function() {
    $mysql = new Co\MySQL;
    $mysql->connect([
        'host' => '127.0.0.1',
        'port' => 3306,
        'user' => 'root',
        'password' => '',
        'database' => 'test',
    ]);
    $res = $mysql->query('SELECT * FROM users');
});
```

#### Promise/Future

```php
// Dùng ReactPHP Promise
use React\Promise\Deferred;

function asyncOperation(): Promise {
    $deferred = new Deferred();

    // Simulate async work
    $client->request('GET', 'http://example.com')->then(
        function ($response) use ($deferred) {
            $deferred->resolve($response);
        },
        function ($error) use ($deferred) {
            $deferred->reject($error);
        }
    );

    return $deferred->promise();
}

// Sử dụng
asyncOperation()
    ->then(function($result) { echo $result; })
    ->otherwise(function($error) { echo $error; });
```

#### Fibers (PHP 8.1+)

```php
$fiber = new Fiber(function(): void {
    $value = Fiber::suspend("suspended value");
    echo "Resumed with: $value\n";
});

$value = $fiber->start(); // "suspended value"
$fiber->resume("resuming"); // "Resumed with: resuming"
```

#### Async/Await (simulated với Fiber)

```php
function fetchUser(int $id): Fiber {
    return new Fiber(function() use ($id) {
        // Simulate async request
        $result = yield asyncHttpGet("/users/$id");
        return $result;
    });
}
```

#### Parallel Processing

```php
// Dùng pcntl (Process Control)
$pid = pcntl_fork();

if ($pid == -1) {
    die("Cannot fork");
} else if ($pid) {
    // Parent process
    pcntl_wait($status);
} else {
    // Child process
    doChildWork();
    exit();
}
```

---

## Tầng 6: Paradigm

### 6.1. Functional Programming

#### Pure Function

```php
function add(int $a, int $b): int {
    return $a + $b;  // Không có side effect
}
```

#### First-Class Function

```php
$fn = function($x) { return $x * 2; };

function apply(callable $fn, $value) {
    return $fn($value);
}
```

#### Immutability

```php
// Thay vì mutate
$arr = [1, 2, 3];
$newArr = [...$arr, 4];  // [1, 2, 3, 4]

// Array với immutable operations
$newArr = array_map(fn($x) => $x * 2, $arr);
```

#### Function Composition

```php
function compose(callable ...$fns): callable {
    return fn($x) => array_reduce(
        array_reverse($fns),
        fn($acc, $fn) => $fn($acc),
        $x
    );
}

$process = compose(
    fn($x) => $x + 1,
    fn($x) => $x * 2,
    fn($x) => $x - 3
);

echo $process(5); // ((5 + 1) * 2) - 3 = 9
```

#### Currying

```php
function curriedAdd(int $a): callable {
    return fn(int $b) => $a + $b;
}

$add5 = curriedAdd(5);
echo $add5(3);  // 8
```

#### Partial Application

```php
function partial(callable $fn, ...$args): callable {
    return fn(...$more) => $fn(...$args, ...$more);
}

$mul = fn($a, $b) => $a * $b;
$mulBy2 = partial($mul, 2);
echo $mulBy2(5);  // 10
```

---

## Tầng 7: Error Handling

### 7.1. Xử Lý Lỗi (Error Handling)

#### Try-Catch

```php
try {
    $result = divide(10, 0);
} catch (DivisionByZeroError $e) {
    echo "Cannot divide by zero: " . $e->getMessage();
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
} finally {
    echo "Cleanup here";
}
```

#### Throw Exception

```php
function validate(int $age): void {
    if ($age < 0) {
        throw new \InvalidArgumentException("Age cannot be negative");
    }
}
```

#### Custom Exception

```php
class ValidationException extends \Exception {}

function process(array $data): void {
    if (!isset($data['name'])) {
        throw new ValidationException("Name is required");
    }
}

try {
    process([]);
} catch (ValidationException $e) {
    echo $e->getMessage();
}
```

#### Try-with-resources (PHP 8.0+)

```php
// Sử dụng try-with-resources cho file handling
try {
    $resource = fopen('file.txt', 'r');
    if ($resource === false) {
        throw new Exception("Cannot open file");
    }
    // Use resource
} finally {
    if (isset($resource)) {
        fclose($resource);
    }
}
```

#### Error Propagation

```php
function divide(int $a, int $b): int {
    if ($b === 0) {
        throw new \DivisionByZeroError("Cannot divide by zero");
    }
    return $a / $b;
}

function calculate(): int {
    return divide(10, 0); // Error propagate lên
}
```

---

### 7.2. Error Types

```php
// Throwable interface
try {
    // code
} catch (\Error $e) {
    // Bắt Error (Fatal, TypeError, etc.)
} catch (\Exception $e) {
    // Bắt Exception
}
```

#### Error Types trong PHP

```php
// TypeError
function add(int $a, int $b): int { return $a + $b; }
add("1", 2);  // TypeError

// ValueError
$arr = [];
$arr[-1];  // ValueError (PHP 8.0+)

// ArithmeticError
intdiv(1, 0);  // ArithmeticError

// DivisionByZeroError
$a = 1 / 0;  // DivisionByZeroError
```

---

## Tầng 8: Module & Organization

### 8.1. Import/Module

#### Require/Include

```php
// Include file
include 'header.php';      // Warning nếu lỗi
require 'header.php';       // Fatal error nếu lỗi

// Include once
include_once 'config.php';
require_once 'config.php';
```

#### Namespace

```php
// file: App/Controllers/UserController.php
namespace App\Controllers;

class UserController {
    // ...
}
```

#### Import

```php
use App\Models\User;
use App\Models\User as UserModel;
use App\Controllers\{UserController, PostController};

// Import hàm
use function App\Helpers\formatDate;

// Import constant
use const App\Config\MAX_SIZE;
```

#### Autoloading (PSR-4)

```php
// composer.json
{
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    }
}

// Trong code, không cần require
new App\Models\User();  // Tự động load
```

#### Selective Import

```php
// Chỉ import những gì cần
use App\Models\User;
use App\Models\Post;
use App\Services\AuthService;
```

#### Re-export

```php
// Trong file index.php của module
use App\Models\User;
use App\Models\Post;

// Re-export để dùng ở nơi khác
class_alias(User::class, 'User');
```

---

### 8.2. Annotation/Attribute

#### Attributes (PHP 8.0+)

```php
#[Attribute]
class MyAttribute {
    public function __construct(
        public string $value = ''
    ) {}
}

#[MyAttribute('test')]
class MyClass {
    #[MyAttribute('property')]
    public string $prop = '';
}

#[MyAttribute]
function myFunction() {}

// Reflect
$ref = new ReflectionClass(MyClass::class);
$attrs = $ref->getAttributes();
```

#### Built-in Attributes

```php
// #[Deprecated]
#[Deprecated('Use NewClass instead')]
class OldClass {}

// #[ReturnTypeWillChange]
class MyIterator implements Iterator {
    #[ReturnTypeWillChange]
    public function current() { return null; }
    // ...
}

// #[NamedArgument]
class Config {
    public function __construct(
        public string $host = 'localhost',
        public int $port = 80
    ) {}
}
$config = new Config(port: 8080);
```

---

## Tầng 9: I/O & Networking

### 9.1. HTTP & Networking

#### Built-in cURL

```php
// GET request
$ch = curl_init('https://api.example.com/data');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

// POST request
$ch = curl_init('https://api.example.com/create');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(['name' => 'John']));
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
$response = curl_exec($ch);
curl_close($ch);
```

#### File Get Contents

```php
// GET
$response = file_get_contents('https://api.example.com/data');

// POST với context
$context = stream_context_create([
    'http' => [
        'method' => 'POST',
        'header' => "Content-Type: application/json\r\n",
        'content' => json_encode(['name' => 'John'])
    ]
]);
$response = file_get_contents('https://api.example.com', false, $context);
```

#### Guzzle HTTP (thư viện phổ biến)

```php
use GuzzleHttp\Client;

$client = new Client([
    'base_uri' => 'https://api.example.com',
    'timeout'  => 2.0,
]);

// GET
$response = $client->get('/users');
$data = $response->getBody()->getContents();

// POST
$response = $client->post('/users', [
    'json' => ['name' => 'John', 'email' => 'john@example.com']
]);

// Với async
$promise = $client->getAsync('/users');
$response = $promise->wait();
```

---

### 9.2. File I/O

#### Read File

```php
// Toàn bộ file
$content = file_get_contents('data.txt');

// Đọc từng dòng
$lines = file('data.txt');  // Array of lines

// Dùng fopen
$handle = fopen('data.txt', 'r');
while (($line = fgets($handle)) !== false) {
    echo $line;
}
fclose($handle);
```

#### Write File

```php
// Ghi đè
file_put_contents('data.txt', 'Hello World');

// Nối thêm
file_put_contents('data.txt', "New line\n", FILE_APPEND);

// Dùng fopen
$handle = fopen('data.txt', 'w');
fwrite($handle, 'Hello');
fclose($handle);
```

#### File Path

```php
$path = '/var/www/html/images/photo.jpg';

basename($path);        // "photo.jpg"
dirname($path);          // "/var/www/html/images"
pathinfo($path);         // ['dirname', 'basename', 'extension', 'filename']
pathinfo($path, PATHINFO_EXTENSION);  // "jpg"

// Real path
realpath('relative/path');  // Absolute path
```

#### Stream

```php
// Read from stream
$handle = fopen('php://stdin', 'r');
$line = fgets($handle);

// Memory stream
$handle = fopen('php://memory', 'w+');
fwrite($handle, 'Hello');
rewind($handle);
echo fread($handle, 1024);
fclose($handle);

// Temp stream
$temp = fopen('php://temp', 'w+');
```

#### Async File I/O

```php
// Swoole async file
Swoole\Runtime::enableCoroutine();

Co\run(function() {
    $content = Co\readFile('test.txt');
    Co\writeFile('output.txt', $content);
});
```

---

## Tầng 10: Data & Serialization

### 10.1. JSON & Serialization

#### JSON Encode/Decode

```php
$data = ['name' => 'John', 'age' => 25, 'active' => true];

// Encode
$json = json_encode($data);
$json = json_encode($data, JSON_PRETTY_PRINT);  // Format đẹp

// Decode
$obj = json_decode($json);           // stdClass
$arr = json_decode($json, true);     // Array

// Error handling
json_decode('{invalid}');
if (json_last_error() !== JSON_ERROR_NONE) {
    echo "JSON Error: " . json_last_error_msg();
}
```

#### Serialization

```php
$obj = new stdClass();
$obj->name = 'John';
$obj->age = 25;

// Serialize
$serialized = serialize($obj);
// O:8:"stdClass":2:{s:4:"name";s:4:"John";s:3:"age";i:25;}

// Unserialize
$unserialized = unserialize($serialized);

// Với class tùy chỉnh
class User {
    public function __sleep() {
        // Return properties to serialize
        return ['name', 'email'];
    }

    public function __wakeup() {
        // Reconnect or reinitialize
    }
}

// JsonSerializable interface
class Person implements JsonSerializable {
    public function __construct(
        public string $name,
        private string $ssn  // Không serialize
    ) {}

    public function jsonSerialize(): array {
        return ['name' => $this->name];
    }
}

$json = json_encode(new Person('John', '123-45-6789'));
// {"name":"John"}
```

---

### 10.2. Date & Time

#### DateTime Class

```php
$now = new DateTime();
echo $now->format('Y-m-d H:i:s');  // 2024-01-15 10:30:00

// Tạo từ string
$date = new DateTime('2024-01-15');
$date = DateTime::createFromFormat('d/m/Y', '15/01/2024');

// Date interval
$start = new DateTime('2024-01-01');
$end = new DateTime('2024-01-15');
$interval = $start->diff($end);
echo $interval->days;  // 14
```

#### DateTimeImmutable (PHP 5.5+)

```php
$date = new DateTimeImmutable('2024-01-01');
$newDate = $date->modify('+1 day');  // Tạo instance mới, không thay đổi $date
```

#### Timestamp

```php
// Current timestamp
time();           // Unix timestamp (giây)
microtime(true);  // Unix timestamp với microseconds

// Từ timestamp
$date = new DateTime('@' . time());

// Tạo DateTime từ timestamp
$date = DateTime::createFromFormat('U', '1705312800');
```

#### DateInterval

```php
$date = new DateTime();
$date->add(new DateInterval('P1D'));      // +1 day
$date->sub(new DateInterval('P1W'));      // -1 week

// Tạo DateInterval
$interval = new DateInterval('P2DT3H4M'); // 2 days, 3 hours, 4 minutes
```

#### DateTimeZone

```php
$tz = new DateTimeZone('Asia/Ho_Chi_Minh');
$date = new DateTime('now', $tz);

// Convert timezone
$date = new DateTime('2024-01-15 10:00:00', new DateTimeZone('UTC'));
$date->setTimezone(new DateTimeZone('Asia/Ho_Chi_Minh'));
```

#### Carbon Library (thường dùng)

```php
use Carbon\Carbon;

$now = Carbon::now();
$tomorrow = Carbon::tomorrow();
$yesterday = Carbon::yesterday();

$date = Carbon::parse('2024-01-15');
echo $date->diffForHumans();  // "2 days ago"

$date->addDays(5);
$date->subMonths(2);
$date->startOfDay();
$date->endOfMonth();
```

---

### 10.3. Regular Expression

#### preg_* functions

```php
$pattern = '/\d{3}-\d{4}/';
$subject = 'My phone: 1234-5678';

// Match
preg_match($pattern, $subject, $matches);
// $matches[0] = '1234-5678'

// Match all
preg_match_all($pattern, $subject, $matches);

// Replace
$result = preg_replace('/\d+/', '#', 'Call 911 for help');
// "Call # for help"

// Replace with callback
$result = preg_replace_callback('/\d+/', function($m) {
    return (int)$m[0] * 2;
}, 'test5');
// "test10"

// Split
$parts = preg_split('/\s+/', 'hello   world test');
// ['hello', 'world', 'test']

// Grep (lọc array)
$items = ['test1', 'hello', 'test2', 'world'];
$filtered = preg_grep('/test/', $items);
// ['test1', 'test2']
```

#### Pattern Modifiers

```php
// i - case insensitive
preg_match('/hello/i', 'HELLO');  // true

// m - multiline (^ $ match line start/end)
preg_match('/^test/m', "line1\ntest");

// s - dotall (. match newline)
preg_match('/a.b/s', "a\nb");  // true

// x - extended (allow whitespace and comments)
$pattern = '/(
    \d{3}  # area code
    -
    \d{4}  # number
)/x';
```

#### Named Capture Groups

```php
preg_match('/(?<area>\d{3})-(?<number>\d{4})/', '123-4567', $matches);
// $matches['area'] = '123'
// $matches['number'] = '4567'
```

---

## Tầng 11: Development Practices

### 11.1. Testing

#### PHPUnit

```php
// tests/UserTest.php
use PHPUnit\Framework\TestCase;

class UserTest extends TestCase {
    private User $user;

    protected function setUp(): void {
        $this->user = new User('John');
    }

    public function testGetNameReturnsCorrectName(): void {
        $this->assertEquals('John', $this->user->getName());
    }

    public function testSetEmail(): void {
        $this->user->setEmail('test@example.com');
        $this->assertEquals('test@example.com', $this->user->getEmail());
    }

    public function testExceptionIsThrown(): void {
        $this->expectException(\InvalidArgumentException::class);
        $this->user->setEmail('invalid');
    }

    // Data providers
    /**
     * @dataProvider additionProvider
     */
    public function testAdd(int $a, int $b, int $expected): void {
        $this->assertEquals($expected, $a + $b);
    }

    public static function additionProvider(): array {
        return [
            [1, 2, 3],
            [0, 0, 0],
            [-1, 1, 0],
        ];
    }

    protected function tearDown(): void {
        // Cleanup
    }
}
```

#### Mocking

```php
use PHPUnit\Framework\TestCase;

class ServiceTest extends TestCase {
    public function testApiCall(): void {
        $mockClient = $this->createMock(ApiClient::class);
        $mockClient->method('get')
            ->willReturn(['data' => 'test']);

        $service = new MyService($mockClient);
        $result = $service->fetchData();

        $this->assertEquals('test', $result['data']);
    }

    // Partial mock
    public function testPartialMock(): void {
        $mock = $this->getMockBuilder(User::class)
            ->onlyMethods(['validate'])
            ->getMock();
        $mock->expects($this->once())
            ->method('validate')
            ->willReturn(true);
    }
}
```

#### Assertions

```php
$this->assertEquals($expected, $actual);
$this->assertNotEquals($expected, $actual);
$this->assertSame($expected, $actual);    // === comparison
$this->assertTrue($condition);
$this->assertFalse($condition);
$this->assertNull($value);
$this->assertNotNull($value);
$this->assertContains($needle, $haystack);
$this->assertArrayHasKey($key, $array);
$this->assertInstanceOf(ClassName::class, $object);
$this->assertMatchesRegularExpression('/pattern/', $string);
$this->assertCount(3, $array);
```

---

### 11.2. Logging

#### Native Error Logging

```php
// Error log
error_log("Error message");

// To specific file
error_log("Message", 3, "/var/log/app.log");

// Custom error handler
set_error_handler(function($errno, $errstr, $errfile, $errline) {
    error_log("Error [$errno]: $errstr in $errfile:$errline");
});
```

#### Monolog (thư viện phổ biến)

```php
use Monolog\Logger;
use Monolog\Handler\StreamHandler;
use Monolog\Handler\FirePHPHandler;

// Create logger
$log = new Logger('app');
$log->pushHandler(new StreamHandler('app.log', Logger::DEBUG));
$log->pushHandler(new FirePHPHandler());

// Log messages
$log->debug('Debug message');
$log->info('Info message');
$log->warning('Warning message');
$log->error('Error message', ['exception' => $e]);

// Structured logging
$log->info('User logged in', [
    'user_id' => 123,
    'ip' => $_SERVER['REMOTE_ADDR']
]);
```

---

### 11.3. Dependency Injection

#### Constructor Injection

```php
class UserService {
    public function __construct(
        private UserRepository $repository,
        private Mailer $mailer
    ) {}
}
```

#### Setter Injection

```php
class CacheService {
    private ?Cache $cache = null;

    public function setCache(Cache $cache): void {
        $this->cache = $cache;
    }
}
```

#### Interface Injection

```php
interface LoggerInterface {
    public function log(string $message): void;
}

class Application {
    private LoggerInterface $logger;

    public function setLogger(LoggerInterface $logger): void {
        $this->logger = $logger;
    }
}
```

#### Service Container (PSR-11)

```php
use Psr\Container\ContainerInterface;

class Container implements ContainerInterface {
    private array $services = [];

    public function get(string $id): mixed {
        if (!$this->has($id)) {
            throw new NotFoundException("Service not found: $id");
        }
        return $this->services[$id]($this);
    }

    public function has(string $id): bool {
        return isset($this->services[$id]);
    }

    public function register(string $id, callable $factory): void {
        $this->services[$id] = $factory;
    }
}
```

---

### 11.4. Configuration

#### Environment Variables

```php
// .env file
DATABASE_HOST=localhost
DATABASE_PORT=3306
API_KEY=secret

// Trong code
$host = $_ENV['DATABASE_HOST'] ?? 'localhost';
$apiKey = getenv('API_KEY');

// Dùng Dotenv
require_once 'vendor/autoload.php';
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$host = $_ENV['DATABASE_HOST'];
```

#### Config File

```php
// config/database.php
return [
    'driver' => 'mysql',
    'host' => $_ENV['DB_HOST'] ?? 'localhost',
    'database' => $_ENV['DB_NAME'],
    'username' => $_ENV['DB_USER'],
    'password' => $_ENV['DB_PASS'],
];

// Load config
$config = require 'config/database.php';
```

#### Command Line Args

```php
// $argv[0] = script name
// $argv[1], $argv[2], ... = arguments

// php script.php --env=production --debug

for ($i = 1; $i < $argc; $i++) {
    $arg = $argv[$i];
    if (str_starts_with($arg, '--')) {
        [$key, $value] = explode('=', substr($arg, 2), 2);
        $options[$key] = $value;
    }
}
```

---

### 11.5. Build & Package Management

#### Composer (Dependency Manager)

```bash
# Initialize project
composer init

# Add dependency
composer require laravel/framework
composer require --dev phpunit/phpunit

# Install
composer install
composer update
```

#### composer.json

```json
{
    "name": "vendor/project",
    "description": "My PHP Project",
    "require": {
        "php": "^8.0",
        "laravel/framework": "^10.0"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    },
    "scripts": {
        "test": "phpunit",
        "lint": "phpcs src"
    }
}
```

#### PHP-CS-Fixer (Formatter)

```bash
# Install
composer require --dev friendsofphp/php-cs-fixer

# Run
vendor/bin/php-cs-fixer fix src/
vendor/bin/php-cs-fixer fix --rules=@PSR12 src/
```

---

### 11.6. Documentation

#### Comment

```php
// Single line comment

# Shell style comment

/*
 * Multi-line
 * comment
 */
```

#### Doc Comment

```php
/**
 * Calculates the sum of two numbers.
 *
 * @param int $a First number
 * @param int $b Second number
 * @return int The sum
 */
function add(int $a, int $b): int {
    return $a + $b;
}
```

---

## Tầng 12: Advanced Concepts

### 12.1. Advanced Concepts

#### Reflection

```php
class User {
    public string $name;
    private int $age;
}

// Get class info
$ref = new ReflectionClass(User::class);
$ref->getName();              // "User"
$ref->getProperties();         // [ReflectionProperty]
$ref->getMethods();           // [ReflectionMethod]

// Get property info
$prop = $ref->getProperty('age');
$prop->isPrivate();           // true
$prop->setAccessible(true);
$prop->setValue($user, 25);

// Get method info
$method = $ref->getMethod('getName');
$method->isPublic();          // true
```

#### Metadata/Introspection

```php
// Lấy thông tin kiểu lúc runtime
class Product {
    public string $name;
    public float $price;
}

$ref = new ReflectionClass(Product::class);

// Kiểm tra property
foreach ($ref->getProperties() as $property) {
    echo $property->getName() . ": " .
         $property->getType()->getName() . "\n";
}

// Kiểm tra method
$ref->hasMethod('__construct');
```

#### Magic Methods

```php
class MagicClass {
    private array $data = [];

    // Khi gọi không tồn tại
    public function __call(string $name, array $args): mixed {
        if (str_starts_with($name, 'get')) {
            $key = strtolower(substr($name, 3));
            return $this->data[$key] ?? null;
        }
    }

    // Khi gọi static không tồn tại
    public static function __callStatic(string $name, array $args): mixed {
        // ...
    }

    // Khi set property không tồn tại
    public function __set(string $name, mixed $value): void {
        $this->data[$name] = $value;
    }

    // Khi kiểm tra property
    public function __isset(string $name): bool {
        return isset($this->data[$name]);
    }

    // Khi unset property
    public function __unset(string $name): void {
        unset($this->data[$name]);
    }

    // Khi convert sang string
    public function __toString(): string {
        return json_encode($this->data);
    }

    // Khi clone
    public function __clone(): void {
        $this->data = [];
    }

    // Khi serialize
    public function __sleep(): array {
        return ['data'];
    }

    // Khi unserialize
    public function __wakeup(): void {
        // Reconnect or reinitialize
    }
}
```

#### FFI (Foreign Function Interface) (PHP 7.4+)

```php
// Cần enable trong php.ini: ffi.enable=true

if (FFI::isLoaded()) {
    // Gọi C functions
    $libc = FFI::load("libc.so.6");
    $printf = $libc->printf;
    $printf("Hello %s\n", "World");
}
```

#### Fibers (PHP 8.1+)

```php
// Xem thêm ở Concurrency
```

#### Lazy Objects (PHP 8.4+)

```php
// Tạo object lazy
class HeavyService {
    public function __construct(
        public lazy string $data = null
    ) {}

    public function initialize(): void {
        $this->data = computeExpensiveData();
    }
}
```

---

## Tầng 13: Memory Layout

### 3.1. Struct Layout

#### PHP không có Struct

PHP là ngôn ngữ thuần hướng đối tượng, không có struct như C. Tuy nhiên có thể dùng:

```php
// Dùng class đơn giản thay struct
class Point {
    public function __construct(
        public float $x = 0.0,
        public float $y = 0.0,
    ) {}
}

// Hoặc dùng stdClass
$point = (object) ['x' => 1.0, 'y' => 2.0];
```

#### Memory Layout

```php
// PHP sử dụng zval structure cho mỗi value
// Bao gồm: type, value, is_ref, refcount

$a = "hello";  // Tạo zval mới
$b = $a;       // Tăng refcount, không copy
$b = "world";  // Tạo zval mới cho $b (copy-on-write)

// Object luôn là reference
$obj1 = new stdClass();
$obj2 = $obj1;  // Cùng reference, không copy
$obj2->name = "test";
echo $obj1->name; // "test"
```

---

## Tầng 14: Compilation Model

### 3.2. Interpreter & Bytecode

#### PHP là Interpreted Language

```php
// PHP chạy qua Zend Engine
// 1. Lexical analysis -> tokens
// 2. Parsing -> AST
// 3. Compilation -> OPcodes (bytecode)
// 4. Execution -> Zend VM

// Xem opcode với VLD (Visual Dump)
```

#### OPcache (PHP 5.5+)

```php
// OPcache lưu bytecode vào memory
// Cấu hình trong php.ini:

// opcache.enable=1
// opcache.memory_consumption=128
// opcache.max_accelerated_files=10000

// Kiểm tra status
opcache_get_status();
```

#### JIT (PHP 8.0+)

```php
// JIT compilation trong PHP 8.0+
// Cấu hình:

// opcache.jit_buffer_size=100M
// opcache.jit=Tracing

// Kiểm tra JIT
opcache_get_status()['jit'];
```

---

## Tầng 15: Linking Model

### 3.3. Dynamic Loading

#### Extension Loading

```php
// Load extension động
dl('gd.so');  // Deprecated trong PHP 8+
// Nên dùng php.ini

// Kiểm tra extension đã load
extension_loaded('gd');           // true/false
get_loaded_extensions();          // Array các extension

// Lấy version
phpversion('gd');
```

#### autoload (PSR-4)

```php
// composer.json autoload
// "autoload": {
//     "psr-4": {
//         "App\\": "app/"
//     }
// }

// Hoặc đăng ký manual
spl_autoload_register(function ($class) {
    $prefix = 'App\\';
    $base_dir = __DIR__ . '/app/';

    $len = strlen($prefix);
    if (strncmp($prefix, $class, $len) !== 0) return;

    $relativeClass = substr($class, $len);
    $file = $base_dir . str_replace('\\', '/', $relativeClass) . '.php';

    if (file_exists($file)) require $file;
});
```

---

## Tầng 16: Runtime

### 3.4. Stack & Call Stack

#### Call Stack

```php
// PHP có call stack limit (mặc định 1000)
// Tăng limit
ini_set('xdebug.max_nesting_level', 500);

// Xem stack trace
debug_print_backtrace();

// Exception stack trace
try {
    // code
} catch (Exception $e) {
    $e->getTrace();      // Array của stack frames
    $e->getTraceAsString();
}
```

#### Exception Unwinding

```php
function level3() {
    throw new Exception("Error in level3");
}

function level2() {
    level3();  // Exception sẽ propagate lên
}

function level1() {
    try {
        level2();
    } catch (Exception $e) {
        echo "Caught: " . $e->getMessage();
        throw $e;  // Re-throw
    } finally {
        echo "Always executed\n";  // Cleanup
    }
}
```

### 3.5. Garbage Collector

#### Reference Counting

```php
// PHP dùng refcount cho GC
// Mỗi variable có refcount

$a = "hello";  // refcount = 1
$b = $a;       // refcount = 2
unset($a);     // refcount = 1

// Cycle garbage collector tự động chạy
// Khi refcount > 0 nhưng không thể reach

// Kiểm tra GC
gc_enabled();           // true
gc_collect_cycles();   // Số cycles thu gom được
```

---

## Tầng 17: Language Design Patterns

### 3.6. RAII Pattern

#### PHP không có RAII thực sự

```php
// PHP dùng __destructor cho cleanup
class FileHandle {
    private $handle;

    public function __construct(string $filename) {
        $this->handle = fopen($filename, 'r');
    }

    public function __destruct() {
        if ($this->handle) {
            fclose($this->handle);
        }
    }
}

// PHP 8.0+ dùng try-with-resources
try {
    $handle = fopen('file.txt', 'r');
    // Tự động gọi __destruct khi thoát scope
} finally {
    // Hoặc dùng finally
}
```

### 3.7. Data Transfer Object (DTO)

```php
// Dùng array hoặc class
class UserDTO {
    public function __construct(
        public readonly int $id,
        public readonly string $name,
        public readonly ?string $email,
    ) {}

    public static function fromArray(array $data): self {
        return new self(
            id: $data['id'],
            name: $data['name'],
            email: $data['email'] ?? null,
        );
    }

    public function toArray(): array {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
        ];
    }
}

// JSON serialization
$json = json_encode(new UserDTO(1, 'John', 'john@example.com'));
```

---

## Tầng 18: Standard Library

### 3.8. Collections

#### Arrays (vừa là List vừa là Map)

```php
// List/ArrayList
$list = [1, 2, 3];
$list[] = 4;
count($list);  // 4

// Map/HashMap
$map = ['a' => 1, 'b' => 2];
$map['c'] = 3;

// Set (dùng array với null values)
$set = [1 => true, 2 => true, 3 => true];

// Stack
$stack = [];
array_push($stack, 1, 2, 3);
$top = array_pop($stack);

// Queue
$queue = [];
array_push($queue, 1, 2, 3);
$item = array_shift($queue);
```

### 3.9. Utilities

#### Option/Result (thủ công)

```php
// PHP không có built-in Option/Result
// Dùng array hoặc null

function findUser(int $id): ?User {
    // Return User hoặc null
}

// Dùng union type (PHP 8.0+)
function findUser(int $id): User|null {
    return null;
}

// Result pattern với exceptions
try {
    $user = findUser(1);
} catch (UserNotFoundException $e) {
    // Handle error
}
```

#### Iterator

```php
// Dùng Iterator interface
class RangeIterator implements Iterator {
    private int $current = 0;
    private int $max;

    public function __construct(int $max) {
        $this->max = $max;
    }

    public function current(): int { return $this->current; }
    public function key(): int { return $this->current; }
    public function next(): void { $this->current++; }
    public function rewind(): void { $this->current = 0; }
    public function valid(): bool { return $this->current < $this->max; }
}

foreach (new RangeIterator(5) as $i) {
    echo $i; // 0,1,2,3,4
}
```

### 3.10. I/O & System

```php
// File
$content = file_get_contents('file.txt');
file_put_contents('file.txt', 'content');

// Process
$output = [];
$returnVar = 0;
exec('ls -la', $output, $returnVar);

// Environment
$env = getenv('PATH');
putenv('MY_VAR=value');

// Command line
$argv = $GLOBALS['argv'];  // Arguments
$argc = $GLOBALS['argc']; // Count

// Time
$now = time();
$date = date('Y-m-d H:i:s');
```

### 3.11. String & Regex

```php
// String methods
$str = "Hello World";
strlen($str);           // 11
strtoupper($str);       // HELLO WORLD
strtolower($str);       // hello world
trim($str);             // Remove whitespace
explode(' ', $str);     // ['Hello', 'World']
implode(' ', ['a','b']);// 'a b'
substr($str, 0, 5);     // 'Hello'
str_replace('World', 'PHP', $str); // 'Hello PHP'

// Regex
preg_match('/(\w+) (\w+)/', $str, $matches);
preg_replace('/\d/', '#', $str);
preg_split('/\s+/', $str);
```

---

## Tầng 19: Ecosystem

### 3.12. Web Frameworks

#### Popular Frameworks

```php
// Laravel (most popular)
$router->get('/user/{id}', [UserController::class, 'show']);

// Symfony (enterprise)
use Symfony\Component\Routing\Annotation\Route;
class UserController {
    #[Route('/user/{id}', methods: ['GET'])]
    public function show(int $id): Response { }
}

// Slim (microframework)
$app->get('/hello/{name}', function ($request, $response, $args) {
    return $response->write("Hello " . $args['name']);
});
```

### 3.13. Database & ORM

```php
// PDO (native)
$pdo = new PDO('mysql:host=localhost;dbname=test', 'user', 'pass');
$stmt = $pdo->prepare('SELECT * FROM users WHERE id = ?');
$stmt->execute([$id]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

// Eloquent (Laravel ORM)
$user = User::find($id);
$users = User::where('active', true)->get();

// Doctrine ORM
$entityManager->find(User::class, $id);
$query = $entityManager->createQuery('SELECT u FROM User u');
```

### 3.14. Testing

```php
// PHPUnit
use PHPUnit\Framework\TestCase;

class UserTest extends TestCase {
    public function testCreateUser(): void {
        $user = new User('John', 'john@example.com');
        $this->assertEquals('John', $user->getName());
        $this->assertNotNull($user->getEmail());
    }

    public function testException(): void {
        $this->expectException(InvalidArgumentException::class);
        throw new InvalidArgumentException('Invalid email');
    }
}

// Mock với PHPUnit
$mock = $this->createMock(UserRepository::class);
$mock->method('find')->willReturn(new User('Mocked'));
```

### 3.15. DevOps & Infrastructure

```php
// Docker (Dockerfile)
// FROM php:8.2-cli
// RUN docker-php-ext-install pdo mysql
// COPY . /app
// CMD ["php", "server.php"]

// Kubernetes (deployment.yaml)
// apiVersion: apps/v1
// kind: Deployment
// spec:
//   replicas: 3
//   template:
//     spec:
//       containers:
//         - name: php-app
//           image: myapp:php8.2

// Composer scripts cho CI/CD
// "scripts": {
//     "test": "phpunit",
//     "lint": "phpcs src",
//     "fix": "phpcbf src"
// }
```

### 3.16. Security

```php
// Password hashing
$hash = password_hash('password', PASSWORD_BCRYPT);
password_verify('password', $hash);

// JWT (dùng firebase/php-jwt)
use Firebase\JWT\JWT;
$payload = ['user_id' => 1, 'exp' => time() + 3600];
$token = JWT::encode($payload, 'secret_key', 'HS256');

// Input sanitization
$name = htmlspecialchars($_POST['name'], ENT_QUOTES, 'UTF-8');
$email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);

// SQL injection prevention (dùng prepared statements)
$stmt = $pdo->prepare('SELECT * FROM users WHERE id = ?');
$stmt->execute([$id]);
```

---

## Tầng 20: Toolchain

### 3.17. Build & Package Management

#### Composer

```php
// composer.json
{
    "name": "vendor/project",
    "require": {
        "php": "^8.1",
        "laravel/framework": "^10.0",
        "guzzlehttp/guzzle": "^7.0"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/"
        }
    }
}

// Commands
// composer install
// composer update
// composer require vendor/package
// composer dump-autoload
```

### 3.18. Code Quality

```php
// PHP_CodeSniffer (linting)
phpcs src/ --standard=PSR12

// PHP-CS-Fixer (formatter)
php-cs-fixer fix src/ --rules=@PSR12

// PHPStan (static analysis)
phpstan analyse src/ --level=5

// Psalm (type checking)
psalm src/

// Rector (automated refactoring)
vendor/bin/rector process src/
```

### 3.19. IDE & Debugging

```php
// Xdebug configuration (php.ini)
// xdebug.mode=debug
// xdebug.start_with_request=yes
// xdebug.client_host=localhost
// xdebug.client_port=9003

// Debug trong code
var_dump($variable);
print_r($variable);

// Xdebug
xdebug_print_function_stack();

// PHPStorm features:
// - PHP type inference
// - PHPUnit integration
// - Composer support
// - Xdebug integration
```

### 3.20. Profiling

```php
// Xdebug profiling
// xdebug.mode=profile
// xdebug.output_dir=/tmp/profiler

// Tideways/XHGui
composer require tideways/php-profiler extension

// Built-in performance monitoring
$start = microtime(true);
// code to measure
$duration = microtime(true) - $start;

// PHP 8.2+ performance hints
// #[\SensitiveParameter]
function process(?string $input) { }
```

---

## Tổng Kết

PHP là ngôn ngữ:
- **Dynamic typing** với optional type declarations (PHP 7.0+)
- **Weak typing** có implicit conversion
- **Multi-paradigm**: Procedural + OOP + Functional
- **Rich ecosystem**: Laravel, Symfony, WordPress
- **Modern features**: Attributes (8.0), Named Arguments (8.0), Match (8.0), Enums (8.1), Fibers (8.1), Readonly (8.1)

### PHP Version History

| Version | Release Date | Key Features |
|---------|---------------|--------------|
| PHP 7.0 | 2015-12-03 | Type declarations, null coalescing |
| PHP 7.4 | 2019-11-28 | Arrow functions, typed properties |
| PHP 8.0 | 2020-11-26 | Attributes, named arguments, match |
| PHP 8.1 | 2021-12-06 | Enums, Fibers, readonly properties |
| PHP 8.2 | 2022-12-08 | Readonly classes, DNF types |
| PHP 8.3 | 2023-11-23 | Typed class constants, json_validate |
| PHP 8.4 | 2024-11-21 | Lazy objects, array_find |
