# PHP Syntax Reference

## Mục Lục

1. [Phân Loại Ngôn Ngữ](#1-phân-loại-ngôn-ngữ)
2. [Khai Báo Biến](#21-khai-báo-biến)
3. [Khai Báo Hàm](#22-khai-báo-hàm)
4. [Vòng Lặp](#23-vòng-lặp)
5. [Điều Kiện](#24-điều-kiện)
6. [Class/Object](#25-classobject)
7. [Kế Thừa & Đa Hình](#26-kế-thừa--đa-hình)
8. [Interface](#27-interface)
9. [Enum](#28-enum)
10. [Nullable Types](#29-nullable-types)
11. [Xử Lý Lỗi](#210-xử-lý-lỗi)
12. [Generics](#211-generics)
13. [Collection Operations](#212-collection-operations)
14. [String Operations](#213-string-operations)
15. [Concurrency/Async](#214-concurrencyasync)
16. [Visibility](#215-visibility)
17. [Import/Module](#216-importmodule)
18. [Kiểu Dữ Liệu Cơ Bản](#217-kiểu-dữ-liệu-cơ-bản)
19. [Null Safety](#218-null-safety)
19. [Property & Getter/Setter](#219-property--gettersetter)
20. [Functional Programming](#220-functional-programming)
21. [Memory Management](#221-memory-management)
22. [Annotation/Attribute](#222-annotationattribute)
23. [Trait](#223-trait)
24. [Operator Overloading](#224-operator-overloading)
25. [HTTP & Networking](#225-http--networking)
26. [File I/O](#226-file-io)
27. [JSON & Serialization](#227-json--serialization)
28. [Date & Time](#228-date--time)
29. [Regular Expression](#229-regular-expression)
30. [Testing](#230-testing)
31. [Logging](#231-logging)
32. [Dependency Injection](#232-dependency-injection)
33. [Configuration](#233-configuration)
34. [Build & Package Management](#234-build--package-management)
35. [Documentation](#235-documentation)
36. [Error Types](#236-error-types)
37. [Advanced Concepts](#237-advanced-concepts)

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

## 2.1. Khai Báo Biến (Variable Declaration)

### Mutable - Biến thường

```php
$name = "John";
$age = 25;
$price = 19.99;
$isActive = true;
```

### Immutable - Hằng số

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

### Type Declaration (PHP 7.0+)

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

### Type Inference

```php
// PHP là dynamic typing, tự suy luận kiểu
$value = "hello";      // string
$value = 42;           // int
$value = [1, 2, 3];   // array
```

### Static Variable

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

### Global Variable

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

### Variable Variables

```php
$varName = "dynamic";
$$varName = "Hello";  // Tạo biến $dynamic = "Hello"
echo $dynamic;       // "Hello"
```

---

## 2.2. Khai Báo Hàm (Function Declaration)

### Function cơ bản

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

### Parameters

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

### Variadic Parameters

```php
function sum(...$numbers): int {
    return array_sum($numbers);
}

sum(1, 2, 3, 4); // 10

function merge(string $prefix, ...$items): array {
    return array_map(fn($item) => "$prefix.$item", $items);
}
```

### Arrow Function (PHP 7.4+)

```php
$add = fn($a, $b) => $a + $b;

// Với typed parameters (PHP 8.0+)
$add = fn(int $a, int $b): int => $a + $b;
```

### Closure

```php
$multiply = function($a) use ($multiplier) {
    return $a * $multiplier;
};

$multiplier = 2;
echo $multiply(5); // 10
```

### Higher-Order Function

```php
function apply(int $value, callable $func): int {
    return $func($value);
}

$result = apply(5, fn($x) => $x * 2); // 10
```

### Method trong Class

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

### Constructor & Destructor

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

## 2.3. Vòng Lặp (Loops)

### For Loop

```php
for ($i = 0; $i < 5; $i++) {
    echo $i . " ";
}
// Output: 0 1 2 3 4
```

### While Loop

```php
$i = 0;
while ($i < 5) {
    echo $i++;
}
// Output: 0 1 2 3 4
```

### Do-While

```php
$i = 0;
do {
    echo $i++;
} while ($i < 5);
// Output: 0 1 2 3 4
```

### For-each

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

### Iterator

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

### Loop Control

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
        // Hoặc dùng: break outer; (với label)
    }
}
```

---

## 2.4. Điều Kiện (Conditionals)

### If-Else

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

### Switch

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

### Ternary Operator

```php
$status = $age >= 18 ? "Adult" : "Minor";

// Null coalescing với ternary
$name = $user['name'] ?? "Guest";

// Short ternary (PHP 8.0+)
$value = $x ?: "default";  // Dùng $x nếu truthy, không thì "default"
```

### Elvis Operator (PHP 8.0+)

```php
// Thực ra là null coalescing assignment
$value ??= "default";  // Chỉ gán nếu null
```

### Null Coalescing

```php
$name = $user['name'] ?? "Guest";
$email = $user['email'] ?? $user['contact']['email'] ?? "no email";
```

### Match Expression (PHP 8.0+)

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

## 2.5. Class/Object

### Class Definition

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

### Data Class (PHP 8.0+ - Named Arguments)

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

### Singleton

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

### Factory Method

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

### Builder Pattern

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

## 2.6. Kế Thừa & Đa Hình (Inheritance & Polymorphism)

### Inheritance

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

### Override

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

### Abstract Class

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

### Final Class/Method

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

### Interface (xem thêm 2.7)

---

## 2.7. Interface/Trait/Protocol

### Interface

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

### Interface với Default Implementation (PHP 8.0+)

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

### Trait

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

### Trait Conflicts

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

## 2.8. Enum (PHP 8.1+)

### Basic Enum

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

### Enum with Values

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

### Enum with Methods

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

### Backed Enum

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

## 2.9. Nullable Types

### Nullable

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

### Null Check

```php
$value = null;

if ($value === null) {
    echo "No value";
}

// Hoặc dùng null coalescing
echo $value ?? "default";
```

### Null-safe Operator (PHP 8.0+)

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

## 2.10. Xử Lý Lỗi (Error Handling)

### Try-Catch

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

### Throw Exception

```php
function validate(int $age): void {
    if ($age < 0) {
        throw new \InvalidArgumentException("Age cannot be negative");
    }
}
```

### Custom Exception

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

### Error Types

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

### Try-Catch với Reflection

```php
function safeCall(callable $fn, ...$args): mixed {
    try {
        return $fn(...$args);
    } catch (\Throwable $e) {
        return null;
    }
}
```

---

## 2.11. Generics

### PHP không có Generics như Java/C#

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

## 2.12. Collection Operations

PHP sử dụng các hàm array_* hoặc class từ SPL.

### Map/Transform

```php
$numbers = [1, 2, 3, 4, 5];

// Dùng array_map
$squared = array_map(fn($n) => $n * $n, $numbers);
// [1, 4, 9, 16, 25]

// Với key
$keys = ['a', 'b', 'c'];
$values = array_map(fn($k, $v) => strtoupper($v), $keys, $numbers);
// ['A' => 1, 'B' => 2, 'C' => 3] (chỉ là ví dụ)
```

### Filter

```php
$numbers = [1, 2, 3, 4, 5];

$evens = array_filter($numbers, fn($n) => $n % 2 === 0);
// [2, 4]

// Filter với key
$assoc = ['a' => 1, 'b' => 2, 'c' => 3];
$result = array_filter($assoc, fn($v, $k) => $k !== 'b', ARRAY_FILTER_USE_BOTH);
```

### Reduce/Fold

```php
$numbers = [1, 2, 3, 4, 5];

$sum = array_reduce($numbers, fn($carry, $item) => $carry + $item, 0);
// 15

$product = array_reduce($numbers, fn($carry, $item) => $carry * $item, 1);
// 120
```

### FlatMap

```php
$words = ['hello', 'world'];

// Tách mỗi word thành các ký tự
$chars = array_merge(...array_map('str_split', $words));
// ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
```

### Sort

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

### Find/First/Last

```php
$numbers = [1, 2, 3, 4, 5];

$first = reset($numbers);        // 1
$last = end($numbers);          // 5

$found = array_find($numbers, fn($n) => $n > 3);     // 4
$key = array_find_key($numbers, fn($n) => $n > 3);   // 3
```

### Any/All/None

```php
$numbers = [1, 2, 3, 4, 5];

$hasEven = array_any($numbers, fn($n) => $n % 2 === 0);  // true (PHP 8.4+)
$allPositive = array_all($numbers, fn($n) => $n > 0);  // true (PHP 8.4+)

// Trước PHP 8.4
$hasEven = in_array(true, array_map(fn($n) => $n % 2 === 0, $numbers));
$allPositive = !in_array(false, array_map(fn($n) => $n > 0, $numbers));
```

### GroupBy

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

### Chunk

```php
$numbers = [1, 2, 3, 4, 5, 6, 7, 8];

$chunks = array_chunk($numbers, 3);
// [[1,2,3], [4,5,6], [7,8]]
```

### Zip

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

## 2.13. String Operations

### Concatenation

```php
$firstName = "John";
$lastName = "Doe";

$fullName = $firstName . " " . $lastName;
// "John Doe"

// Với .=
$greeting = "Hello";
$greeting .= " World";  // "Hello World"
```

### Interpolation

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

### Template String (heredoc/nowdoc)

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

### Split

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

### Join

```php
$fruits = ['apple', 'banana', 'cherry'];
$str = implode(", ", $fruits);
// "apple, banana, cherry"

// join() là alias của implode
$str = join("-", $fruits);
// "apple-banana-cherry"
```

### Replace

```php
$str = "Hello World";

// String replace
str_replace("World", "PHP", $str);     // "Hello PHP"

// Case insensitive
strireplace("hello", "Hi", $str);      // "Hi World"

// Multiple replacements
str_replace(["hello", "world"], ["Hi", "PHP"], $str);

// Regex replace
preg_replace('/\d+/', '#', "test123");  // "test#"

// Callback replace
preg_replace_callback('/\d+/', fn($m) => (int)$m[0] * 2, "test5"); // "test10"
```

### Trim

```php
$str = "   Hello World   ";

trim($str);      // "Hello World"
ltrim($str);     // "Hello World   "
rtrim($str);     // "   Hello World"

// Trim specific characters
trim($str, " H"); // "ello World"
```

### Upper/Lower Case

```php
$str = "Hello World";

strtoupper($str);    // "HELLO WORLD"
strtolower($str);    // "hello world"
ucfirst($str);       // "Hello world" - viết hoa chữ cái đầu
ucwords($str);       // "Hello World" - viết hoa mỗi từ
```

### Regex Match

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

### Substring

```php
$str = "Hello World";

substr($str, 0, 5);      // "Hello" - từ vị trí 0, length 5
substr($str, 6);         // "World" - từ vị trí 6 đến cuối
substr($str, -5);        // "World" - 5 ký tự cuối

// mb_substr cho multibyte
$str = "Xin chào";
mb_substr($str, 0, 4);  // "Xin "
```

### Length

```php
$str = "Hello";

strlen($str);        // 5 bytes
mb_strlen($str);     // 5 ký tự (cho UTF-8)
```

---

## 2.14. Concurrency/Async

### Threads

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

### Async với ReactPHP / Swoole

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

### Promise/Future

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

### Fibers (PHP 8.1+)

```php
$fiber = new Fiber(function(): void {
    $value = Fiber::suspend("suspended value");
    echo "Resumed with: $value\n";
});

$value = $fiber->start(); // "suspended value"
$fiber->resume("resuming"); // "Resumed with: resuming"
```

### Async/Await (simulated với Fiber)

```php
function fetchUser(int $id): Fiber {
    return new Fiber(function() use ($id) {
        // Simulate async request
        $result = yield asyncHttpGet("/users/$id");
        return $result;
    });
}
```

### Parallel Processing

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

## 2.15. Visibility (Access Modifiers)

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

### Default Visibility

```php
// Trong class - mặc định là public
class MyClass {
    function method() {}  // public
}

// Trong namespace/global - mặc định là public
function globalFunction() {}  // public
```

---

## 2.16. Import/Module

### Require/Include

```php
// Include file
include 'header.php';      // Warning nếu lỗi
require 'header.php';       // Fatal error nếu lỗi

// Include once
include_once 'config.php';
require_once 'config.php';
```

### Namespace

```php
// file: App/Controllers/UserController.php
namespace App\Controllers;

class UserController {
    // ...
}
```

### Import

```php
use App\Models\User;
use App\Models\User as UserModel;
use App\Controllers\{UserController, PostController};

// Import hàm
use function App\Helpers\formatDate;

// Import constant
use const App\Config\MAX_SIZE;
```

### Autoloading (PSR-4)

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

---

## 2.17. Kiểu Dữ Liệu Cơ Bản (Primitive Types)

### Integer

```php
$int = 42;
$hex = 0x1A;       // 26
$binary = 0b1010;  // 10
$octal = 052;      // 42

// PHP 8.0+ numeric string
var_dump(is_numeric("42"));  // true
var_dump(intval("42"));       // 42
```

### Float

```php
$float = 3.14;
$scientific = 1.2e3;  // 1200

// Float precision
var_dump(0.1 + 0.2);   // 0.3 (gần đúng!)
```

### Boolean

```php
$bool = true;
$bool = false;

// Truthy/Falsy values
// Falsy: 0, 0.0, "", "0", null, [], false
// Truthy: "0" (string), -1, etc.
```

### String

```php
$str = "Hello";
$str = 'Hello';

// Single vs Double quotes
$name = "John";
"$name";   // "John" (interpolate)
'$name';   // "$name" (literal)
```

### Array

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

### Object

```php
$obj = new stdClass();
$obj->name = 'John';

// Từ array
$obj = (object)['name' => 'John'];
```

### Callable/Closure

```php
$func = function($x) { return $x * 2; };

// Callable type
function callIt(callable $fn) {
    return $fn(5);
}
```

### Resource

```php
$file = fopen("test.txt", "r");  // Resource
fclose($file);
```

### Never (PHP 8.1+)

```php
function redirect(string $url): never {
    header("Location: $url");
    exit();
}
```

### Void (PHP 7.1+)

```php
function logMessage(string $msg): void {
    echo $msg;
    // Không return gì
}
```

---

## 2.18. Null Safety

### Elvis Operator

```php
$name = $user "Guest";
$value = $data['name'] ??['key'] ?? $default ?? "default";
```

### Null-safe Operator (PHP 8.0+)

```php
$result = $user?->getProfile()?->getAvatar()?->getUrl();
```

### Null Coalescing Assignment (PHP 7.4+)

```php
$user['name'] ??= "Guest";  // Chỉ gán nếu null
```

---

## 2.19. Property & Getter/Setter

### Public Property

```php
class User {
    public string $name = 'Guest';
    public ?string $email = null;
}

$user = new User();
$user->name = "John";  // Direct access
echo $user->name;
```

### Getter/Setter

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

### Readonly Properties (PHP 8.1+)

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

### Lazy Properties (PHP 8.4+)

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

## 2.20. Functional Programming

### Pure Function

```php
function add(int $a, int $b): int {
    return $a + $b;  // Không có side effect
}
```

### First-Class Function

```php
$fn = function($x) { return $x * 2; };

function apply(callable $fn, $value) {
    return $fn($value);
}
```

### Immutability

```php
// Thay vì mutate
$arr = [1, 2, 3];
$newArr = [...$arr, 4];  // [1, 2, 3, 4]

// Array với immutable operations
$newArr = array_map(fn($x) => $x * 2, $arr);
```

### Function Composition

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

### Currying

```php
function curriedAdd(int $a): callable {
    return fn(int $b) => $a + $b;
}

$add5 = curriedAdd(5);
echo $add5(3);  // 8
```

### Partial Application

```php
function partial(callable $fn, ...$args): callable {
    return fn(...$more) => $fn(...$args, ...$more);
}

$mul = fn($a, $b) => $a * $b;
$mulBy2 = partial($mul, 2);
echo $mulBy2(5);  // 10
```

---

## 2.21. Memory Management

### Garbage Collection

PHP sử dụng automatic garbage collection:

```php
// Reference counting
$a = "hello";
$b = $a;  // $a and $b cùng reference
unset($a); // Giảm reference count

// Circular references được GC xử lý tự động
```

### Weak Reference (PHP 7.4+)

```php
$obj = new stdClass();
$weakRef = WeakReference::create($obj);

if ($weakRef->get()) {
    echo "Object still exists";
}

unset($obj);  // Object được giải phóng
var_dump($weakRef->get());  // null
```

### Memory Limit

```php
// Trong php.ini
memory_limit = 256M

// Trong code
ini_set('memory_limit', '512M');
echo memory_get_usage();
echo memory_get_peak_usage();
```

---

## 2.22. Annotation/Attribute

### Attributes (PHP 8.0+)

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

### Built-in Attributes

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

## 2.23. Trait (xem 2.7)

---

## 2.24. Operator Overloading

### PHP không hỗ trợ operator overloading

Nhưng có thể dùng magic methods:

```php
class Money {
    public function __construct(
        public int $amount
    ) {}

    // Khi dùng +
    public function __add(Money $other): Money {
        return new Money($this->amount + $other->amount);
    }

    // Khi convert sang string
    public function __toString(): string {
        return "$" . $this->amount;
    }

    // Clone
    public function __clone() {
        // Custom clone logic
    }
}

$total = new Money(100) + new Money(50);
echo $total; // "$150"
```

---

## 2.25. HTTP & Networking

### Built-in cURL

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

### File Get Contents

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

### Guzzle HTTP (thư viện phổ biến)

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

## 2.26. File I/O

### Read File

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

### Write File

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

### File Path

```php
$path = '/var/www/html/images/photo.jpg';

basename($path);        // "photo.jpg"
dirname($path);         // "/var/www/html/images"
pathinfo($path);        // ['dirname', 'basename', 'extension', 'filename']
pathinfo($path, PATHINFO_EXTENSION);  // "jpg"

// Real path
realpath('relative/path');  // Absolute path
```

### Stream

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

### Async File I/O

```php
// Swoole async file
Swoole\Runtime::enableCoroutine();

Co\run(function() {
    $content = Co\readFile('test.txt');
    Co\writeFile('output.txt', $content);
});
```

---

## 2.27. JSON & Serialization

### JSON Encode/Decode

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

### Serialization

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

## 2.28. Date & Time

### DateTime Class

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

### DateTimeImmutable (PHP 5.5+)

```php
$date = new DateTimeImmutable('2024-01-01');
$newDate = $date->modify('+1 day');  // Tạo instance mới, không thay đổi $date
```

### Timestamp

```php
// Current timestamp
time();           // Unix timestamp (giây)
microtime(true);  // Unix timestamp với microseconds

// Từ timestamp
$date = new DateTime('@' . time());

// Tạo DateTime từ timestamp
$date = DateTime::createFromFormat('U', '1705312800');
```

### DateInterval

```php
$date = new DateTime();
$date->add(new DateInterval('P1D'));      // +1 day
$date->sub(new DateInterval('P1W'));      // -1 week

// Tạo DateInterval
$interval = new DateInterval('P2DT3H4M'); // 2 days, 3 hours, 4 minutes
```

### DateTimeZone

```php
$tz = new DateTimeZone('Asia/Ho_Chi_Minh');
$date = new DateTime('now', $tz);

// Convert timezone
$date = new DateTime('2024-01-15 10:00:00', new DateTimeZone('UTC'));
$date->setTimezone(new DateTimeZone('Asia/Ho_Chi_Minh'));
```

### Carbon Library (thường dùng)

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

## 2.29. Regular Expression

### preg_* functions

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

### Pattern Modifiers

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

### Named Capture Groups

```php
preg_match('/(?<area>\d{3})-(?<number>\d{4})/', '123-4567', $matches);
// $matches['area'] = '123'
// $matches['number'] = '4567'
```

---

## 2.30. Testing

### PHPUnit

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

### Mocking

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

### Assertions

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

## 2.31. Logging

### Native Error Logging

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

### Monolog (thư viện phổ biến)

```php
use Monolog\Logger;
use Monolog\Handler\StreamHandler;
use Monolog\Handler\SlackHandler;

$log = new Logger('app');

// Log to file
$log->pushHandler(new StreamHandler('app.log', Logger::DEBUG));

// Log to Slack
$log->pushHandler(new SlackHandler('token', 'channel'));

$log->debug('Debug message', ['data' => [1, 2, 3]]);
$log->info('User logged in', ['user_id' => 123]);
$log->warning('Low memory');
$log->error('Database connection failed', ['exception' => $e]);
$log->critical('System down!');
```

### Structured Logging

```php
$log->info('User registered', [
    'user_id' => 123,
    'email' => 'user@example.com',
    'ip' => $_SERVER['REMOTE_ADDR'],
    'context' => ['source' => 'web']
]);
```

---

## 2.32. Dependency Injection

### Constructor Injection

```php
class UserService {
    public function __construct(
        private UserRepository $userRepo,
        private Mailer $mailer
    ) {}

    public function createUser(string $email): void {
        $user = new User($email);
        $this->userRepo->save($user);
        $this->mailer->sendWelcome($email);
    }
}

// Manual DI
$repo = new UserRepository();
$mailer = new Mailer();
$service = new UserService($repo, $mailer);
```

### Setter Injection

```php
class CacheService {
    private ?Cache $cache = null;

    public function setCache(Cache $cache): void {
        $this->cache = $cache;
    }

    public function get(string $key): mixed {
        return $this->cache?->get($key);
    }
}
```

### Interface Injection

```php
interface LoggerAwareInterface {
    public function setLogger(Logger $logger): void;
}

class LoggerAwareTrait {
    private Logger $logger;

    public function setLogger(Logger $logger): void {
        $this->logger = $logger;
    }
}

class MyService {
    use LoggerAwareTrait;

    public function doWork(): void {
        $this->logger->info('Work started');
    }
}
```

### Service Container (PSR-11)

```php
use Psr\Container\ContainerInterface;

class Container implements ContainerInterface {
    private array $services = [];

    public function get(string $id): mixed {
        if (!isset($this->services[$id])) {
            $this->services[$id] = $this->create($id);
        }
        return $this->services[$id];
    }

    public function has(string $id): bool {
        return isset($this->services[$id]) || method_exists($this, 'create' . $id);
    }

    private function create(string $id): mixed {
        return match($id) {
            UserRepository::class => new UserRepository(),
            Mailer::class => new Mailer(),
            default => throw new \Exception("Unknown service: $id")
        };
    }
}
```

---

## 2.33. Configuration

### Environment Variables

```php
// $_ENV or getenv()
$dbHost = $_ENV['DB_HOST'] ?? 'localhost';
$dbHost = getenv('DB_HOST') ?: 'localhost';

// Dùng dotenv (vlucas/phpdotenv)
require 'vendor/autoload.php';
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$dbHost = $_ENV['DB_HOST'];
```

### Config File

```php
// config/app.php
return [
    'debug' => true,
    'db' => [
        'host' => 'localhost',
        'name' => 'myapp',
        'user' => 'root',
    ],
    'mail' => [
        'driver' => 'smtp',
        'host' => 'smtp.mailtrap.io',
    ]
];

// Load config
$config = require 'config/app.php';
echo $config['debug'];
```

### Command Line Args

```php
// $argv, $argc
// php script.php arg1 arg2 --option=value

// Dùng Composer console component
use Symfony\Component\Console\Application;

$app = new Application();
$app->register('greet')
    ->addArgument('name')
    ->addOption('yell')
    ->setCode(function($input, $output) {
        $name = $input->getArgument('name');
        $message = "Hello, $name";
        if ($input->getOption('yell')) {
            $message = strtoupper($message);
        }
        $output->writeln($message);
    });
$app->run();
```

---

## 2.34. Build & Package Management

### Composer

```json
// composer.json
{
    "name": "vendor/project",
    "description": "My project",
    "type": "project",
    "require": {
        "php": "^8.1",
        "laravel/framework": "^10.0",
        "guzzlehttp/guzzle": "^7.0"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.0",
        "phpstan/phpstan": "^1.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    },
    "scripts": {
        "test": "phpunit",
        "lint": "phpstan analyse"
    },
    "config": {
        "optimize-autoloader": true
    }
}
```

### Composer Commands

```bash
# Install
composer install

# Update
composer update

# Add package
composer require guzzlehttp/guzzle
composer require --dev phpunit/phpunit

# Autoload
composer dump-autoload

# Scripts
composer test
composer run-script lint
```

### Linter & Formatter

```php
// PHPStan (static analysis)
composer require --dev phpstan/phpstan
// phpstan.neon
includes:
    - vendor/phpstan/phpstan-phpunit/extension.neon
parameters:
    level: 8
    paths:
        - src

// PHP-CS-Fixer (code style)
composer require --dev friendsofphp/php-cs-fixer
// .php-cs-fixer.dist.php
$config = new PhpCsFixer\Config();
return $config->setRules([
    '@PSR12' => true,
    'array_syntax' => ['syntax' => 'short'],
]);

// Run
phpstan analyse src
php-cs-fixer fix src
```

---

## 2.35. Documentation

### Comments

```php
// Single line comment

/*
 * Multi-line
 * comment
 */

/**
 * DocBlock comment for documentation
 *
 * @param string $name User's name
 * @param int $age User's age
 * @return bool Success status
 */
function process(string $name, int $age): bool {
    return true;
}
```

### DocBlock Tags

```php
/**
 * Short description.
 *
 * Long description with multiple lines.
 *
 * @param string $param1 Description of param1
 * @param int|null $param2 Optional param
 * @return bool Return description
 * @throws \InvalidArgumentException When validation fails
 * @see OtherClass::method()
 * @since 1.0.0
 * @deprecated 2.0.0 Use newMethod() instead
 */
```

---

## 2.36. Error Types

### Exception Hierarchy

```php
// Throwable (PHP 7+)
try {
    // code
} catch (\Throwable $e) {
    // Catch all
}

// Error (PHP 7+) - programming errors
catch (\Error $e) {
    // TypeError, ArgumentCountError, etc.
}

// Exception - application errors
catch (\Exception $e) {
    // Custom application errors
}
```

### Custom Error Types

```php
class ValidationException extends \Exception {}
class NotFoundException extends \Exception {}
class UnauthorizedException extends \Exception {}

// Với error codes
class ApiException extends \Exception {
    public function __construct(
        string $message,
        private int $statusCode = 500
    ) {
        parent::__construct($message);
    }

    public function getStatusCode(): int {
        return $this->statusCode;
    }
}
```

### Error Handling

```php
// Set custom handler
set_error_handler(function($errno, $errstr, $errfile, $errline) {
    throw new \ErrorException($errstr, $errno, 1, $errfile, $errline);
});

// Exception handler
set_exception_handler(function($e) {
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
    exit();
});

// Shutdown handler
register_shutdown_function(function() {
    $error = error_get_last();
    if ($error) {
        // Log fatal errors
    }
});
```

---

## 2.37. Advanced Concepts

### Reflection

```php
class User {
    public string $name = 'Guest';
    public function greet(): string {
        return "Hello, $this->name";
    }
}

$class = new ReflectionClass(User::class);

// Get properties
$props = $class->getProperties();
// Get methods
$methods = $class->getMethods();
// Get doc comment
$doc = $class->getDocComment();

// Invoke method
$method = $class->getMethod('greet');
$user = $class->newInstance();
$result = $method->invoke($user);

// Check property type
$prop = $class->getProperty('name');
$type = $prop->getType();
```

### Attributes (xem 2.22)

### Dynamic Properties

```php
class StdClass {
    // PHP 8.2+ - không cần class
}

$obj = new stdClass();
$obj->name = 'John';  // Dynamic property
$obj->{'dynamic-' . $key} = $value;

// PHP 8.2+ - #[AllowDynamicProperties]
#[AllowDynamicProperties]
class Dynamic {}
```

### Magic Methods

```php
class Magic {
    private array $data = [];

    // __get($name) - truy cập property không tồn tại
    public function __get(string $name): mixed {
        return $this->data[$name] ?? null;
    }

    // __set($name, $value) - gán property không tồn tại
    public function __set(string $name, mixed $value): void {
        $this->data[$name] = $value;
    }

    // __isset($name) - kiểm tra property
    public function __isset(string $name): bool {
        return isset($this->data[$name]);
    }

    // __unset($name) - unset property
    public function __unset(string $name): void {
        unset($this->data[$name]);
    }

    // __call($name, $args) - gọi method không tồn tại
    public function __call(string $name, array $args): mixed {
        return "Called $name with: " . implode(', ', $args);
    }

    // __callStatic() - static call
    // __toString() - convert to string
    // __invoke() - gọi object như function
    // __clone() - khi clone
    // __debugInfo() - var_dump
}
```

### FFI (Foreign Function Interface) (PHP 7.4+)

```php
// Cần extension ffi.enable=1 trong php.ini

$ffi = FFI::cdef("
    int printf(const char *format, ...);
", "libc.so.6");

$ffi->printf("Hello %s\n", "World");
```

### Meta-programming

```php
// Dynamic class creation
$className = 'DynamicClass';
eval("class $className { public \$value; }");

// Method missing (via __call)
class API {
    public function __call(string $method, array $args) {
        return "Calling $method with: " . json_encode($args);
    }
}

$api = new API();
echo $api->getUser(123);  // Calling getUser with: [123]
```

### Traits (xem 2.7)

---

## Tổng Kết

PHP là ngôn ngữ:
- **Dynamic typing** với optional type declarations (PHP 7.0+)
- **Weakly typed** nhưng có type hints
- **Server-side** chủ yếu cho web development
- Có nhiều magic methods cho meta-programming
- Không có built-in generics như Java
- Không có true operator overloading
- Hỗ trợ OOP đầy đủ từ PHP 5, với nhiều cải tiến trong PHP 7, 8

### PHP Version History

| Version | Year | Key Features |
|---------|------|--------------|
| PHP 5 | 2004 | OOP improvements, PDO |
| PHP 7 | 2015 | Scalar type hints, return types, null coalescing |
| PHP 7.4 | 2019 | Arrow functions, typed properties |
| PHP 8 | 2020 | Attributes, named arguments, union types, match |
| PHP 8.1 | 2021 | Enums, readonly properties, fibers |
| PHP 8.2 | 2022 | Readonly classes, Disjunctive Normal Form types |
| PHP 8.3 | 2023 | Typed class constants, JSON validation |
| PHP 8.4 | 2024 | Lazy objects, array_find/any/all, property hooks |
