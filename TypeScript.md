# TypeScript Syntax Reference

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
    - [14.2 TypeScript Compiler](#142-typescript-compiler)
15. [Tầng 15: Linking Model](#tầng-15-linking-model)
    - [15.1 Module Loading](#151-module-loading)
16. [Tầng 16: Runtime](#tầng-16-runtime)
    - [16.1 JavaScript Runtime](#161-javascript-runtime)
    - [16.2 TypeScript Runtime](#162-typescript-runtime)
17. [Tầng 17: Language Design Patterns](#tầng-17-language-design-patterns)
    - [17.1 Duck Typing](#171-duck-typing)
    - [17.2 Structural Typing](#172-structural-typing)
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

### Chạy File TypeScript

```bash
# Cài đặt TypeScript
npm install -g typescript

# Compile
tsc script.ts

# Compile và chạy (với ts-node)
npx ts-node script.ts

# Watch mode
tsc --watch script.ts

# Với tsconfig
tsc
tsc --project tsconfig.json
```

### Đặc điểm TypeScript

- **Typing**: Static typing với type inference, optional typing
- **Paradigm**: Multi-paradigm (Functional, OOP, Procedural)
- **Execution**: Compiled to JavaScript, runs in any JS runtime
- **Use Cases**: Web development, Node.js, Angular, React, Vue

---

## 1. Tầng 1: Syntax & Semantics

### 1.1. Khai Báo Biến (Variable Declaration)

#### Mutable - Biến thường

```typescript
// Khai báo biến
let x = 10;
let name = "TypeScript";
let isActive = true;
let prices = [1.5, 2.0, 3.5];

// Explicit type
let x: number = 10;
let name: string = "TypeScript";
let isActive: boolean = true;

// Type annotation
let x: number = 10;
let y: string = "hello";
let z: boolean = true;

// Multiple assignment
let a = 1, b = 2, c = 3;
```

#### Immutable - Hằng số

```typescript
// const (không thể reassign)
const MAX_SIZE = 100;
const PI = 3.14159;

// const với object
const user = { name: "John" };
user.name = "Jane"; // OK - mutating property
// user = {}; // Error - reassignment

// Readonly (compiler check)
const user: Readonly<User> = { name: "John" };
// user.name = "Jane"; // Error
```

#### Type Inference

```typescript
// TypeScript tự suy luận kiểu
let x = 10;        // number
let y = "hello";   // string
let z = true;      // boolean

// Kiểm tra kiểu
typeof x;          // "number"

// Type assertion
let value: unknown = "hello";
let length = (value as string).length;
```

#### Global Variable

```typescript
// Biến toàn cục (trong browser)
let globalVar = "I am global";

// Trong Node.js
(globalThis as any).globalVar = "value";

// Trong module, dùng export/import thay vì global
```

#### Static Variable (Class-level)

```typescript
class Counter {
    static count = 0;  // Biến class (static)

    constructor() {
        Counter.count++;
    }
}

console.log(Counter.count);  // 0
new Counter();
console.log(Counter.count);  // 1
```

---

### 1.2. Khai Báo Hàm (Function Declaration)

#### Function cơ bản

```typescript
// Function không có return
function greet(): void {
    console.log("Hello!");
}

// Function có return
function add(a: number, b: number): number {
    return a + b;
}

// Function với type hints
function greet(name: string): string {
    return `Hello, ${name}!`;
}

// Function expression
const add = function(a: number, b: number): number {
    return a + b;
};

// Docstring / JSDoc
/**
 * Calculate rectangle area.
 * @param width - Width of rectangle
 * @param height - Height of rectangle
 * @returns Area of rectangle
 */
function calculateArea(width: number, height: number): number {
    return width * height;
}
```

#### Parameters

```typescript
// Default parameters
function greet(name: string, greeting: string = "Hello"): string {
    return `${greeting}, ${name}!`;
}

// Named arguments (dùng object)
function createUser({ name, email, age }: {
    name: string;
    email: string;
    age: number;
}): User {
    return { name, email, age };
}

createUser({ name: "John", email: "john@example.com", age: 30 });

// Rest parameters
function func(...args: number[]): void {
    console.log(args);  // Array
}

func(1, 2, 3, 4, 5);

// Destructuring parameters
function func({ name, age }: { name: string; age: number }): void {
    console.log(name, age);
}
```

#### Arrow Function

```typescript
// Arrow function
const add = (a: number, b: number): number => a + b;

// Với block body
const add = (a: number, b: number): number => {
    return a + b;
};

// Dùng với các hàm higher-order
const numbers = [1, 2, 3, 4, 5];
const squared = numbers.map((x) => x ** 2);
const evens = numbers.filter((x) => x % 2 === 0);

// Arrow với conditional
const max = (a: number, b: number) => a > b ? a : b;

// This binding
class Counter {
    count = 0;

    increment = () => {
        this.count++;
    };
}
```

#### Closure

```typescript
function outer(x: number): (y: number) => number {
    return function inner(y: number): number {
        return x + y;  // Closure: capture biến từ outer
    };
}

const closure = outer(10);
closure(5);  // 15
```

#### Higher-Order Function

```typescript
// Function nhận function khác làm tham số
function applyTwice(func: (x: number) => number, x: number): number {
    return func(func(x));
}

function addFive(x: number): number {
    return x + 5;
}

const result = applyTwice(addFive, 10);  // 20

// Function trả về function
function multiplier(factor: number): (x: number) => number {
    return (x: number) => x * factor;
}

const double = multiplier(2);
double(5);  // 10
```

#### Method trong Class

```typescript
class Calculator {
    // Static method
    static add(a: number, b: number): number {
        return a + b;
    }

    // Instance method
    multiply(a: number, b: number): number {
        return a * b;
    }

    // Arrow function (bound)
    greet = () => {
        return "Hello!";
    };
}
```

#### Constructor & Destructor

```typescript
class Resource {
    name: string;

    constructor(name: string) {
        this.name = name;
        console.log(`Creating ${name}`);
    }

    // Destructor (JavaScript không có, dùng WeakRef hoặc cleanup)
    [Symbol.dispose]?.(): void {
        console.log(`Cleaning up ${this.name}`);
    }
}

// Using với Symbol.dispose
using resource = new Resource("test");
```

---

### 1.3. Vòng Lặp (Loops)

#### For Loop

```typescript
// For cơ bản
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// For với array
const fruits = ["apple", "banana", "cherry"];
for (const fruit of fruits) {
    console.log(fruit);
}

// For với index
for (const [index, fruit] of fruits.entries()) {
    console.log(`${index}: ${fruit}`);
}

// For-in (key)
for (const key in fruits) {
    console.log(`${key}: ${fruits[key]}`);
}

// ForEach
fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`);
});
```

#### While Loop

```typescript
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}

// Do-while
let input: string;
do {
    input = getInput();
} while (input !== "quit");

// While với break/continue
while (true) {
    const userInput = getInput();
    if (userInput === "quit") {
        break;
    }
    console.log(`You entered: ${userInput}`);
}
```

#### Array Comprehension (không có trực tiếp, dùng map/filter)

```typescript
// Map
const squares = [1, 2, 3, 4, 5].map(x => x ** 2);

// Filter
const evens = [1, 2, 3, 4, 5].filter(x => x % 2 === 0);

// Combined
const result = [1, 2, 3, 4, 5]
    .filter(x => x > 2)
    .map(x => x * 2);

// Array.from
const squares = Array.from({ length: 5 }, (_, i) => i ** 2);
```

#### Iterator

```typescript
// Dùng Array iterator
const numbers = [1, 2, 3];
const iterator = numbers[Symbol.iterator]();
iterator.next();  // { value: 1, done: false }
iterator.next();  // { value: 2, done: false }
iterator.next();  // { value: 3, done: false }
iterator.next();  // { value: undefined, done: true }

// Custom iterator
class RangeIterator {
    private current: number;
    constructor(private max: number) {
        this.current = 0;
    }

    [Symbol.iterator]() {
        return this;
    }

    next(): IteratorResult<number> {
        if (this.current < this.max) {
            return { value: this.current++, done: false };
        }
        return { value: undefined, done: true };
    }
}

for (const i of new RangeIterator(5)) {
    console.log(i);  // 0, 1, 2, 3, 4
}
```

#### Loop Control

```typescript
// Break - thoát vòng lặp
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break;
    }
    console.log(i);  // 0, 1, 2, 3, 4
}

// Continue - bỏ qua lần lặp hiện tại
for (let i = 0; i < 5; i++) {
    if (i === 2) {
        continue;
    }
    console.log(i);  // 0, 1, 3, 4
}

// Label
outer: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        if (j === 1) {
            break outer;
        }
    }
}
```

---

### 1.4. Điều Kiện (Conditionals)

#### If-Else

```typescript
// If-else cơ bản
const age = 18;
if (age >= 18) {
    console.log("Adult");
} else {
    console.log("Minor");
}

// Else if
const score = 85;
let grade: string;
if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else if (score >= 70) {
    grade = "C";
} else {
    grade = "F";
}

// Ternary operator
const status = age >= 18 ? "adult" : "minor";

// Nested ternary
const grade2 = score >= 90 ? "A" : score >= 80 ? "B" : "C";
```

#### Switch

```typescript
// Switch
function httpStatus(status: number): string {
    switch (status) {
        case 200:
            return "OK";
        case 404:
            return "Not Found";
        case 500:
            return "Server Error";
        default:
            return "Unknown";
    }
}

// Switch với multiple values
function httpStatusMulti(status: number): string {
    switch (status) {
        case 200:
        case 201:
        case 202:
            return "Success";
        case 400:
        case 401:
        case 403:
            return "Client Error";
        default:
            return "Unknown";
    }
}
```

#### Match Expression (TypeScript 4.7+)

```typescript
// Dùng switch như expression
const result = (() => {
    switch (value) {
        case 1:
            return "one";
        case 2:
            return "two";
        default:
            return "other";
    }
})();

// Pattern matching với discriminated union
type Shape =
    | { kind: "circle"; radius: number }
    | { kind: "square"; side: number };

function area(shape: Shape): number {
    switch (shape.kind) {
        case "circle":
            return Math.PI * shape.radius ** 2;
        case "square":
            return shape.side ** 2;
    }
}
```

---

## 2. Tầng 2: Type System

### 2.1. Kiểu Dữ Liệu Cơ Bản (Primitive Types)

#### Number

```typescript
// Number (JavaScript: 64-bit floating point)
let x: number = 10;
let negative = -5;
let hex = 0xff;       // 255
let binary = 0b1010;  // 10
let octal = 0o777;     // 511

// Special values
let inf = Infinity;
let negInf = -Infinity;
let nan = NaN;

// Operations
5 + 3;    // 8
5 - 3;    // 2
5 * 3;    // 15
5 / 3;    // 1.666...
5 % 3;    // 2
5 ** 3;   // 125

// Number methods
Math.floor(3.14);   // 3
Math.ceil(3.14);    // 4
Math.round(3.5);    // 4
Math.abs(-5);       // 5
Math.max(1, 2, 3);  // 3
Math.min(1, 2, 3);  // 1
```

#### String

```typescript
// String
let s1 = "Hello";
let s2 = 'World';
let s3 = `Multi
line
string`;

// Template literal
const name = "TypeScript";
const version = 5.0;
const msg = `Welcome to ${name} ${version}`;  // "Welcome to TypeScript 5.0"

// String methods
const s = "Hello World";
s.length;                    // 11
s.toUpperCase();             // "HELLO WORLD"
s.toLowerCase();             // "hello world"
s.trim();                    // "Hello World"
s.split(" ");                // ["Hello", "World"]
s.replace("World", "TypeScript");  // "Hello TypeScript"
s.includes("World");         // true
s.startsWith("Hello");       // true
s.endsWith("World");         // true
s.indexOf("World");          // 6
s.substring(0, 5);           // "Hello"
s.slice(0, 5);              // "Hello"
```

#### Boolean

```typescript
let isActive = true;
let isDeleted = false;

// Operations
true && false;  // false
true || false;   // true
!true;           // false

// Truthy/Falsy
// Falsy: false, 0, "", null, undefined, NaN
// Truthy: mọi giá trị khác

Boolean(0);     // false
Boolean(1);     // true
Boolean("");     // false
Boolean("hello"); // true
```

#### Array

```typescript
// Array
const numbers: number[] = [1, 2, 3, 4, 5];
const mixed = [1, "hello", 3.14, true];

// Generic array
const nums: Array<number> = [1, 2, 3];

// Array methods
numbers.push(6);        // Thêm vào cuối
numbers.pop();           // Xóa từ cuối
numbers.shift();         // Xóa từ đầu
numbers.unshift(0);      // Thêm vào đầu
numbers.splice(1, 1);    // Xóa tại vị trí

// Slicing
const arr = [0, 1, 2, 3, 4];
arr.slice(1, 3);    // [1, 2]
arr.slice(0, 3);    // [0, 1, 2]
arr.slice(3);       // [3, 4]
arr.slice(-2);      // [3, 4]

// Spread
const arr2 = [...arr, 5, 6];
```

#### Tuple

```typescript
// Tuple
const point: [number, number] = [10, 20];
const coords: [number, number, number] = [1, 2, 3];
const single: [number] = [1];  // Tuple với 1 element

// Destructuring
const [x, y] = point;  // x=10, y=20

// Optional elements
const optional: [number, number?] = [1];
optional[1];  // undefined

// Rest elements
const rest: [number, ...number[]] = [1, 2, 3, 4, 5];
```

#### Object

```typescript
// Object
const user = {
    name: "John",
    age: 30,
    email: "john@example.com"
};

// Object methods
Object.keys(user);      // ["name", "age", "email"]
Object.values(user);    // ["John", 30, "john@example.com"]
Object.entries(user);   // [["name", "John"], ["age", 30], ...]

// Spread
const user2 = { ...user, age: 31 };
```

#### Symbol

```typescript
const sym = Symbol("description");
const sym2 = Symbol("description");
sym === sym2;  // false

// Well-known symbols
Symbol.iterator;
Symbol.toStringTag;
Symbol.hasInstance;
```

#### null & undefined

```typescript
let value: null = null;
let undefined: undefined = undefined;

// Optional
let name: string | undefined = undefined;
```

---

### 2.2. Enum

```typescript
// Numeric Enum
enum Color {
    Red,     // 0
    Green,   // 1
    Blue     // 2
}

Color.Red;           // 0
Color[0];            // "Red"

// Enum với giá trị tùy chỉnh
enum Status {
    Pending = "PENDING",
    Approved = "APPROVED",
    Rejected = "REJECTED"
}

// String Enum
enum Direction {
    Up = "UP",
    Down = "DOWN",
    Left = "LEFT",
    Right = "RIGHT"
}

// Const Enum
const enum Color {
    Red = "RED",
    Green = "GREEN"
}

// Enum với methods
enum Color {
    Red = "RED",
    Green = "GREEN",

    description() {
        return `Color ${this.valueOf()}`;
    }
}

// Reverse mapping (chỉ với numeric enum)
enum Color {
    Red,
    Green,
    Blue
}
Color.Red;      // 0
Color[0];       // "Red"
```

---

### 2.3. Nullable Types

```typescript
// Union type với null/undefined
let name: string | null = null;
let age: number | undefined;

// Optional type
type Optional<T> = T | null | undefined;

// Optional parameter
function greet(name?: string): string {
    if (name === undefined) {
        return "Hello, World!";
    }
    return `Hello, ${name}!`;
}

// Optional property
interface User {
    name: string;
    email?: string;  // Optional
}

const user: User = { name: "John" };  // OK - email is optional
```

---

### 2.4. Null Safety

```typescript
// Optional chaining (?.)
const user = {
    address: {
        city: {
            name: "NYC"
        }
    }
};

const city = user?.address?.city?.name;  // "NYC"
const zip = user?.address?.zipCode ?? "Unknown";  // "Unknown" if null

// Nullish coalescing (??)
const value = null ?? "default";  // "default"
const value2 = 0 ?? "default";    // 0 (vì 0 không phải null/undefined)

// Optional parameters
function greet(name?: string): string {
    return name ?? "World";
}

// Type guard
function printLength(str: string | null): void {
    if (str !== null) {
        console.log(str.length);  // OK - narrowed to string
    }
}

// Non-null assertion
const name = user!.name;  // Assert not null
```

---

### 2.5. Generics

```typescript
// Generic interface
interface Container<T> {
    value: T;
    get(): T;
}

const intContainer: Container<number> = {
    value: 42,
    get() { return this.value; }
};

// Generic class
class Box<T> {
    constructor(private value: T) {}

    get(): T {
        return this.value;
    }

    set(value: T): void {
        this.value = value;
    }
}

const box = new Box<number>(42);

// Generic function
function first<T>(arr: T[]): T | undefined {
    return arr[0];
}

first([1, 2, 3]);       // number
first(["a", "b", "c"]); // string

// Generic constraints
interface Lengthwise {
    length: number;
}

function logLength<T extends Lengthwise>(arg: T): number {
    return arg.length;
}

logLength("hello");  // OK
logLength([1, 2, 3]); // OK
// logLength(123);    // Error - number không có length

// Multiple type parameters
function pair<K, V>(key: K, value: V): [K, V] {
    return [key, value];
}

// Default type parameters
interface ApiResponse<T = string> {
    data: T;
    status: number;
}
```

---

### 2.6. Collection Operations

#### Map/Transform

```typescript
const numbers = [1, 2, 3, 4, 5];

// map()
const squared = numbers.map(x => x ** 2);

// with index
const indexed = numbers.map((x, i) => ({ value: x, index: i }));
```

#### Filter

```typescript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// filter()
const evens = numbers.filter(x => x % 2 === 0);
```

#### Reduce/Fold

```typescript
const numbers = [1, 2, 3, 4, 5];

// reduce()
const total = numbers.reduce((acc, x) => acc + x, 0);  // 15
const product = numbers.reduce((acc, x) => acc * x, 1);  // 120

// sum() - dùng reduce
const sum = numbers.reduce((a, b) => a + b, 0);
```

#### FlatMap

```typescript
const nested = [[1, 2], [3, 4], [5, 6]];

// flat()
const flattened = nested.flat();  // [1, 2, 3, 4, 5, 6]

// flatMap()
const words = ["hello", "world"];
const chars = words.flatMap(word => word.split(""));  // ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d"]
```

#### Sort

```typescript
const numbers = [3, 1, 4, 1, 5, 9, 2, 6];

// sort() - sắp xếp in-place
const sorted = [...numbers].sort((a, b) => a - b);           // Tăng dần
const sortedDesc = [...numbers].sort((a, b) => b - a);       // Giảm dần

// Sort với key
const users = [
    { name: "John", age: 30 },
    { name: "Jane", age: 25 }
];
const sortedByAge = [...users].sort((a, b) => a.age - b.age);
```

#### Find/First/Last

```typescript
const numbers = [1, 2, 3, 4, 5];

// Find first
const result = numbers.find(x => x > 3);  // 4

// Find index
const index = numbers.findIndex(x => x === 3);  // 2

// Last
const last = numbers[numbers.length - 1];  // 5
const last2 = numbers.at(-1);  // 5 (ES2022)
```

#### Any/All/Some/Every

```typescript
const numbers = [1, 2, 3, 4, 5];

numbers.some(x => x > 3);   // true (có ít nhất 1)
numbers.every(x => x > 0);  // true (tất cả đều > 0)
numbers.every(x => x > 10); // false
numbers.includes(3);        // true
```

#### GroupBy

```typescript
const data = [
    { name: "a", value: 1 },
    { name: "a", value: 2 },
    { name: "b", value: 3 }
];

// Manual groupBy
const grouped = data.reduce((acc, item) => {
    if (!acc[item.name]) {
        acc[item.name] = [];
    }
    acc[item.name].push(item);
    return acc;
}, {} as Record<string, typeof data>);
```

#### Chunk

```typescript
function chunk<T>(arr: T[], size: number): T[][] {
    const result: T[][] = [];
    for (let i = 0; i < arr.length; i += size) {
        result.push(arr.slice(i, i + size));
    }
    return result;
}

chunk([1, 2, 3, 4, 5, 6, 7], 3);  // [[1,2,3], [4,5,6], [7]]
```

#### Zip

```typescript
const names = ["Alice", "Bob", "Charlie"];
const ages = [25, 30, 35];

// Zip
const combined = names.map((name, i) => ({ name, age: ages[i] }));
// [{ name: "Alice", age: 25 }, ...]

// Enumerate
names.map((name, i) => ({ index: i, name }));
```

---

### 2.7. String Operations

#### Concatenation

```typescript
// Template literal
const s = `Hello ${"World"}`;

// String.concat()
"Hello ".concat("World");

// +
"Hello " + "World";
```

#### Interpolation

```typescript
const name = "TypeScript";
const version = 5.0;

// Template literal
`Welcome to ${name} ${version}`;

// replace
"Hello {name}".replace("{name}", "World");
```

#### Regex

```typescript
const text = "My email is john@example.com";

// Match
const match = text.match(/[\w.-]+@[\w.-]+/);
if (match) {
    console.log(match[0]);  // "john@example.com"
}

// Find all
const emails = text.match(/[\w.-]+@[\w.-]+/g);

// Pattern với named groups
const pattern = /(?<user>[\w.-]+)@(?<domain>[\w.-]+)/;
const result = pattern.exec(text);
if (result?.groups) {
    console.log(result.groups.user);   // "john"
    console.log(result.groups.domain); // "example.com"
}

// Replace
text.replace(/\d+/g, "#");

// Split
text.split(/\s+/);
```

---

## 3. Tầng 3: OOP & Type Relationships

### 3.1. Class/Object

#### Class Definition

```typescript
class User {
    // Properties
    name: string;
    email: string;
    private _age: number;  // Private (TypeScript)
    protected role: string = "user";  // Protected

    // Constructor
    constructor(name: string, email: string, age: number) {
        this.name = name;
        this.email = email;
        this._age = age;
    }

    // Method
    greet(): string {
        return `Hello, I'm ${this.name}`;
    }

    // Getter
    get age(): number {
        return this._age;
    }

    // Setter
    set age(value: number) {
        if (value >= 0) {
            this._age = value;
        }
    }

    // Static method
    static createGuest(): User {
        return new User("Guest", "guest@example.com", 0);
    }
}

// Create instance
const user = new User("John", "john@example.com", 30);
user.greet();  // "Hello, I'm John"
```

#### Shorthand (Parameter Properties)

```typescript
class User {
    constructor(
        public name: string,
        public email: string,
        private _age: number
    ) {}
}
```

#### Singleton

```typescript
class Singleton {
    private static instance: Singleton;
    public value: string;

    private constructor() {
        this.value = "Singleton instance";
    }

    static getInstance(): Singleton {
        if (!Singleton.instance) {
            Singleton.instance = new Singleton();
        }
        return Singleton.instance;
    }
}

const s1 = Singleton.getInstance();
const s2 = Singleton.getInstance();
s1 === s2;  // true
```

#### Factory Method

```typescript
class User {
    constructor(
        public name: string,
        public email: string
    ) {}

    static fromDict(data: Record<string, unknown>): User {
        return new User(
            data["name"] as string,
            data["email"] as string
        );
    }

    static fromJson(json: string): User {
        const data = JSON.parse(json);
        return User.fromDict(data);
    }
}

const user = User.fromDict({ name: "John", email: "john@example.com" });
```

#### Abstract Class

```typescript
abstract class Animal {
    constructor(public name: string) {}

    // Abstract method - phải implement
    abstract speak(): string;

    // Concrete method
    describe(): string {
        return `${this.name} says ${this.speak()}`;
    }
}

class Dog extends Animal {
    speak(): string {
        return "Woof!";
    }
}

// const animal = new Animal("Test");  // Error: Cannot create instance of abstract class
const dog = new Dog("Buddy");  // OK
```

---

### 3.2. Kế Thừa & Đa Hình (Inheritance & Polymorphism)

#### Inheritance

```typescript
class Animal {
    constructor(public name: string) {}

    speak(): string {
        return "...";
    }
}

class Dog extends Animal {
    speak(): string {
        return "Woof!";
    }

    fetch(): string {
        return "Fetching!";
    }
}

class Cat extends Animal {
    speak(): string {
        return "Meow!";
    }
}

const dog = new Dog("Buddy");
dog.speak();  // "Woof!"
dog.fetch();  // "Fetching!"
```

#### Super

```typescript
class Animal {
    constructor(public name: string) {}

    speak(): string {
        return "...";
    }
}

class Dog extends Animal {
    constructor(name: string, public breed: string) {
        super(name);  // Gọi parent constructor
    }

    speak(): string {
        return `${super.speak()} Woof!`;  // Gọi parent method
    }
}
```

#### Polymorphism

```typescript
function makeSpeak(animal: Animal): string {
    return animal.speak();
}

const animals: Animal[] = [new Dog("Buddy"), new Cat("Whiskers")];
animals.forEach(animal => {
    console.log(animal.speak());  // Polymorphism
});
```

#### Multiple Inheritance (không có - dùng Interface)

```typescript
// TypeScript không có multiple inheritance
// Dùng interface

interface Flyable {
    fly(): string;
}

interface Swimmable {
    swim(): string;
}

class Duck implements Flyable, Swimmable {
    fly(): string {
        return "Flying!";
    }

    swim(): string {
        return "Swimming!";
    }
}
```

---

### 3.3. Interface/Trait/Protocol

#### Interface

```typescript
interface Drawable {
    draw(): void;
}

interface Colorable {
    color: string;
}

class Circle implements Drawable, Colorable {
    color: string;
    radius: number;

    constructor(radius: number, color: string) {
        this.radius = radius;
        this.color = color;
    }

    draw(): void {
        console.log(`Drawing circle with radius ${this.radius}`);
    }
}

class Square implements Drawable {
    side: number;

    constructor(side: number) {
        this.side = side;
    }

    draw(): void {
        console.log(`Drawing square with side ${this.side}`);
    }
}

// Type checking
function render(shape: Drawable): void {
    shape.draw();
}

render(new Circle(5, "red"));  // OK
render(new Square(10));       // OK
```

#### Interface với methods

```typescript
interface Calculator {
    add(a: number, b: number): number;
    subtract(a: number, b: number): number;
}

const calculator: Calculator = {
    add: (a, b) => a + b,
    subtract: (a, b) => a - b
};
```

#### Extending Interface

```typescript
interface Person {
    name: string;
    age: number;
}

interface Employee extends Person {
    employeeId: string;
    department: string;
}

const employee: Employee = {
    name: "John",
    age: 30,
    employeeId: "E001",
    department: "Engineering"
};
```

#### Interface với optional properties

```typescript
interface Config {
    host?: string;
    port?: number;
    ssl?: boolean;
    [key: string]: unknown;  // Index signature
}
```

---

### 3.4. Visibility/Access Modifiers

```typescript
class Example {
    public publicVar = "I am public";       // Public (default)
    protected protectedVar = "I am protected"; // Protected
    private privateVar = "I am private";     // Private (TypeScript)
    readonly readOnly = "Cannot change";      // Readonly

    public publicMethod(): void {}
    protected protectedMethod(): void {}
    private privateMethod(): void {}
}

// Subclass
class SubExample extends Example {
    method(): void {
        this.protectedVar;  // OK
        // this.privateVar;  // Error
    }
}

const ex = new Example();
ex.publicVar;        // OK
// ex.privateVar;    // Error
// ex.protectedVar;  // Error
```

---

## 4. Tầng 4: Memory Model

### 4.1. Memory Management

```typescript
// JavaScript: Automatic garbage collection
// Reference counting, Mark and sweep

// Weak references
let obj = { name: "test" };
const weakRef = new WeakRef(obj);

// Check if still alive
if (weakRef.deref()) {
    console.log(weakRef.deref()?.name);
}

// WeakMap/WeakSet (keys are garbage collected)
const weakMap = new WeakMap();
weakMap.set(obj, "value");
weakMap.get(obj);  // "value"

// Memory info (limited in JS)
const used = (performance as any).memory?.usedJSHeapSize;
```

### 4.2. Property & Getter/Setter

```typescript
class Temperature {
    private _celsius = 0;

    // Getter
    get celsius(): number {
        return this._celsius;
    }

    // Setter
    set celsius(value: number) {
        this._celsius = value;
    }

    // Read-only
    get fahrenheit(): number {
        return this._celsius * 9/5 + 32;
    }

    // Computed property
    get kelvin(): number {
        return this._celsius + 273.15;
    }
}

const temp = new Temperature();
temp.celsius = 25;
console.log(temp.fahrenheit);  // 77
```

---

## 5. Tầng 5: Concurrency Model

### 5.1. Concurrency/Async

#### Callbacks

```typescript
function fetchData(callback: (error: Error | null, data?: string) => void): void {
    setTimeout(() => {
        callback(null, "data");
    }, 1000);
}

fetchData((error, data) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

#### Promise

```typescript
function fetchData(): Promise<string> {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("data");
        }, 1000);
    });
}

fetchData()
    .then(data => console.log(data))
    .catch(error => console.error(error));

// Promise.all
Promise.all([promise1, promise2, promise3])
    .then(([result1, result2, result3]) => {});

// Promise.race
Promise.race([promise1, promise2])
    .then(result => {});

// Promise.allSettled
Promise.allSettled([promise1, promise2])
    .then(results => {
        results.forEach(result => {
            if (result.status === "fulfilled") {
                console.log(result.value);
            } else {
                console.error(result.reason);
            }
        });
    });
```

#### Async/Await

```typescript
async function fetchData(): Promise<string> {
    return "data";
}

async function main(): Promise<void> {
    // Single task
    const result = await fetchData();

    // Multiple tasks
    const [result1, result2] = await Promise.all([
        fetchData(),
        fetchData()
    ]);

    // Error handling
    try {
        const data = await fetchData();
    } catch (error) {
        console.error(error);
    }

    // With timeout
    const withTimeout = await Promise.race([
        fetchData(),
        new Promise((_, reject) =>
            setTimeout(() => reject(new Error("Timeout")), 3000)
        )
    ]);
}
```

#### Worker

```typescript
// Web Worker
const worker = new Worker("worker.js");

worker.onmessage = (event) => {
    console.log(event.data);
};

worker.postMessage({ type: "compute", data: 42 });
worker.terminate();
```

---

## 6. Tầng 6: Paradigm

### 6.1. Functional Programming

#### Pure Function

```typescript
// Pure function
function add(a: number, b: number): number {
    return a + b;
}

// Impure function
let counter = 0;
function impureAdd(a: number, b: number): number {
    counter++;
    return a + b;
}
```

#### Immutability

```typescript
// Dùng const và spread
const user = { name: "John", age: 30 };
const updatedUser = { ...user, age: 31 };

// Dùng Object.freeze
const frozen = Object.freeze({ name: "John" });
// frozen.name = "Jane";  // Error

// Dùng libraries như Immer hoặc Immutable.js
```

#### First-Class Function

```typescript
// Function là first-class citizens
function apply(func: (x: number) => number, x: number): number {
    return func(x);
}

function double(x: number): number {
    return x * 2;
}

apply(double, 5);  // 10
apply(x => x ** 2, 5);  // 25
```

#### Function Composition

```typescript
const compose = <T, U, V>(f: (x: U) => V, g: (x: T) => U) =>
    (x: T): V => f(g(x));

const f = compose(
    (x: number) => x + 1,
    (x: number) => x * 2
);
f(3);  // (3 * 2) + 1 = 7

// Pipe
const pipe = <T,>(...fns: Array<(x: unknown) => unknown>) =>
    (x: T): unknown => fns.reduce((acc, fn) => fn(acc), x);
```

#### Currying

```typescript
const curry =
    <T extends unknown[], R>(fn: (...args: T) => R) =>
    (...args: T): R | ((...args: T) => R) =>
        args.length === fn.length
            ? fn(...args)
            : (...rest: T) => fn(...args, ...rest);

const add = curry((a: number, b: number, c: number) => a + b + c);
add(1)(2)(3);   // 6
add(1, 2)(3);   // 6
add(1)(2, 3);  // 6
```

#### Partial Application

```typescript
const partial =
    <T extends unknown[], U extends unknown[], R>(
        fn: (...args: [...T, ...U]) => R,
        ...args: T
    ) =>
    (...rest: U): R =>
        fn(...args, ...rest);

const power = (base: number, exp: number): number => base ** exp;
const square = partial(power, 2);
square(5);  // 25

const cube = partial(power, 3);
cube(5);    // 125
```

---

## 7. Tầng 7: Error Handling

### 7.1. Xử Lý Lỗi (Error Handling)

#### Try-Catch

```typescript
try {
    const result = riskyOperation();
} catch (error) {
    console.error("Error:", error);
    if (error instanceof TypeError) {
        console.error("Type error:", error.message);
    }
}

// Finally
try {
    const result = riskyOperation();
} finally {
    console.log("Cleanup");  // Always executed
}
```

#### Throw Exception

```typescript
function validateAge(age: number): number {
    if (age < 0) {
        throw new Error("Age cannot be negative");
    }
    if (age > 150) {
        throw new RangeError("Age is unrealistic");
    }
    return age;
}

try {
    validateAge(-5);
} catch (error) {
    if (error instanceof Error) {
        console.log(error.message);
    }
}
```

#### Custom Exception

```typescript
class ValidationError extends Error {
    constructor(
        public field: string,
        message: string
    ) {
        super(message);
        this.name = "ValidationError";
    }
}

function validateEmail(email: string): void {
    if (!email.includes("@")) {
        throw new ValidationError("email", "Invalid email format");
    }
}
```

### 7.2. Error Types

```typescript
// Built-in errors
Error;
TypeError;
RangeError;
SyntaxError;
ReferenceError;
URIError;
EvalError;

// Custom error hierarchy
class AppError extends Error {
    constructor(message: string, public code: string) {
        super(message);
        this.name = "AppError";
    }
}

class ValidationError extends AppError {
    constructor(message: string) {
        super(message, "VALIDATION_ERROR");
        this.name = "ValidationError";
    }
}
```

---

## 8. Tầng 8: Module & Organization

### 8.1. Import/Module

#### ES Modules

```typescript
// Import
import { add, multiply } from "./math";
import * as Math from "./math";

// Import với alias
import { add as sum } from "./math";

// Default import
import myFunction from "./math";

// Re-export
export { add, multiply };
export default function defaultExport() {}

// Dynamic import
const module = await import("./math");
```

#### Namespace (deprecated - dùng module)

```typescript
namespace Math {
    export function add(a: number, b: number): number {
        return a + b;
    }
}

Math.add(1, 2);
```

---

### 8.2. Extension Methods

#### Module Augmentation

```typescript
// extend-array.ts
declare global {
    interface Array<T> {
        chunk(size: number): T[][];
    }
}

Array.prototype.chunk = function<T>(this: T[], size: number): T[][] {
    const result: T[][] = [];
    for (let i = 0; i < this.length; i += size) {
        result.push(this.slice(i, i + size));
    }
    return result;
};

// Usage
[1, 2, 3, 4, 5, 6].chunk(3);  // [[1,2,3], [4,5,6]]
```

---

## 9. Tầng 9: I/O & Networking

### 9.1. HTTP & Networking

#### Fetch API

```typescript
// GET
const response = await fetch("https://api.example.com/users");
const data = await response.json();

// POST
const response = await fetch("https://api.example.com/users", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer token"
    },
    body: JSON.stringify({
        name: "John",
        email: "john@example.com"
    })
});

// Error handling
if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
}

// With timeout
const controller = new AbortController();
const timeout = setTimeout(() => controller.abort(), 5000);

try {
    const response = await fetch(url, { signal: controller.signal });
} catch (error) {
    if (error instanceof Error && error.name === "AbortError") {
        console.log("Request timed out");
    }
} finally {
    clearTimeout(timeout);
}
```

#### Axios

```typescript
import axios from "axios";

// GET
const response = await axios.get("https://api.example.com/users");
const users = response.data;

// POST
const response = await axios.post("https://api.example.com/users", {
    name: "John",
    email: "john@example.com"
});

// With headers
const response = await axios.get(url, {
    headers: { Authorization: "Bearer token" }
});

// Error handling
try {
    await axios.get(url);
} catch (error) {
    if (axios.isAxiosError(error)) {
        console.log(error.message);
    }
}
```

### 9.2. File I/O

#### Node.js File I/O

```typescript
import fs from "fs/promises";

// Read file
const content = await fs.readFile("file.txt", "utf-8");

// Write file
await fs.writeFile("output.txt", "Hello World");

// Append file
await fs.appendFile("log.txt", "New log entry\n");

// Check existence
try {
    await fs.access("file.txt");
} catch {
    console.log("File does not exist");
}

// Read directory
const files = await fs.readdir(".");
```

#### Browser File I/O

```typescript
// File input
const input = document.querySelector('input[type="file"]');
input?.addEventListener("change", async (e) => {
    const file = (e.target as HTMLInputElement).files?.[0];
    const text = await file?.text();
});

// Download file
const blob = new Blob(["Hello World"], { type: "text/plain" });
const url = URL.createObjectURL(blob);
const a = document.createElement("a");
a.href = url;
a.download = "file.txt";
a.click();
URL.revokeObjectURL(url);
```

---

## 10. Tầng 10: Data & Serialization

### 10.1. JSON & Serialization

```typescript
// JSON
const data = { name: "John", age: 30, active: true };

// Serialize
const jsonStr = JSON.stringify(data);
const prettyJson = JSON.stringify(data, null, 2);

// Deserialize
const parsed = JSON.parse(jsonStr);

// With reviver
const parsed = JSON.parse(jsonStr, (key, value) => {
    if (key === "date") {
        return new Date(value);
    }
    return value;
});

// JSON with classes
// Dùng serialization libraries: class-transformer, serializr
```

### 10.2. Date & Time

```typescript
// Date
const now = new Date();
const date = new Date("2024-01-15T10:30:00Z");

// Create
const date2 = new Date(2024, 0, 15, 10, 30, 0);

// Format
date.toISOString();          // "2024-01-15T10:30:00.000Z"
date.toLocaleDateString();   // "1/15/2024"
date.toLocaleTimeString();   // "10:30:00 AM"

// Parse
Date.parse("2024-01-15");

// Arithmetic
const tomorrow = new Date(now);
tomorrow.setDate(tomorrow.getDate() + 1);

const diff = date2.getTime() - date.getTime();
const days = diff / (1000 * 60 * 60 * 24);

// Libraries: date-fns, moment, luxon
```

### 10.3. Regular Expression

```typescript
const text = "My email is john@example.com";

// Match
const match = text.match(/[\w.-]+@[\w.-]+/);
if (match) {
    console.log(match[0]);
}

// Find all
const matches = text.match(/[\w.-]+@[\w.-]+/g);

// Groups
const pattern = /(?<user>[\w.-]+)@(?<domain>[\w.-]+)/;
const result = pattern.exec(text);
if (result?.groups) {
    console.log(result.groups.user);
    console.log(result.groups.domain);
}

// Replace
text.replace(/\d+/g, "#");

// Split
text.split(/\s+/);

// Compile for reuse
const emailPattern = new RegExp(/[\w.-]+@[\w.-]+/);
```

---

## 11. Tầng 11: Development Practices

### 11.1. Testing

#### Jest

```typescript
// test.spec.ts

test("adds 1 + 2 to equal 3", () => {
    expect(1 + 2).toBe(3);
});

test("object assignment", () => {
    const data = { one: 1 };
    expect(data).toEqual({ one: 1 });
});

test("async", async () => {
    const data = await fetchData();
    expect(data).toBe("data");
});

describe("Math", () => {
    beforeAll(() => {
        // Setup
    });

    afterEach(() => {
        // Cleanup
    });

    test("add", () => {
        expect(1 + 2).toBe(3);
    });
});

// Mock
jest.fn(() => "mocked");
jest.spyOn(obj, "method");
jest.mock("./module");
```

#### Vitest

```typescript
import { describe, it, expect, vi } from "vitest";

describe("Math", () => {
    it("adds", () => {
        expect(1 + 2).toBe(3);
    });

    it("mocks", () => {
        const fn = vi.fn(() => "mocked");
        expect(fn()).toBe("mocked");
    });
});
```

### 11.2. Logging

```typescript
// Console
console.log("Info");
console.info("Info");
console.warn("Warning");
console.error("Error");
console.debug("Debug");

// Styled console
console.log("%cStyled text", "color: red; font-size: 20px");

// Table
console.table([{ a: 1 }, { a: 2 }]);

// Timing
console.time("label");
console.timeEnd("label");

// Libraries: winston, pino, loglevel
```

### 11.3. Dependency Injection

```typescript
// Constructor injection
class UserService {
    constructor(private repository: UserRepository) {}

    getUser(id: string) {
        return this.repository.find(id);
    }
}

// Usage
const userService = new UserService(new UserRepository());

// Interface
interface IStorage {
    save(data: unknown): Promise<void>;
    load(): Promise<unknown>;
}

class FileStorage implements IStorage {
    async save(data: unknown): Promise<void> {}
    async load(): Promise<unknown> { return {}; }
}
```

### 11.4. Configuration

#### Environment Variables

```typescript
// Vite/Webpack
import.meta.env.VITE_API_URL;

// Node.js
import dotenv from "dotenv";
dotenv.config();

const apiKey = process.env.API_KEY;

// Dùng zod cho type-safe config
import { z } from "zod";

const configSchema = z.object({
    API_URL: z.string().url(),
    PORT: z.coerce.number().default(3000),
    DEBUG: z.coerce.boolean().default(false),
});

const config = configSchema.parse(process.env);
```

---

### 11.5. Build & Package Management

```bash
# npm/yarn/pnpm
npm install package
npm install -D dev_package
npm install package@version

# package.json
npm init
npm publish

# tsconfig.json
npx tsc --init
```

### 11.6. Documentation

#### JSDoc

```typescript
/**
 * Adds two numbers.
 * @param a - The first number
 * @param b - The second number
 * @returns The sum of a and b
 * @example
 * add(1, 2) // returns 3
 */
function add(a: number, b: number): number {
    return a + b;
}

// Type documentation
/** @type {string} */
const name = "John";

/** @interface */
interface User {
    /** @property */
    name: string;
}
```

---

## 12. Tầng 12: Advanced Concepts

### 12.1. Advanced Concepts

#### Reflection/Introspection

```typescript
// Type guard
function isString(value: unknown): value is string {
    return typeof value === "string";
}

// Instanceof
if (value instanceof Date) {
    // value is Date
}

// typeof
typeof "hello";  // "string"
typeof 123;     // "number"

// Constructor check
function isInstanceOf<T>(value: unknown, constructor: new (...args: unknown[]) => T): value is T {
    return value instanceof constructor;
}
```

#### Decorator (Experimental)

```typescript
// Cần enable "experimentalDecorators" trong tsconfig.json

function logged(target: unknown, propertyKey: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function (...args: unknown[]) {
        console.log(`Calling ${propertyKey} with`, args);
        return original.apply(this, args);
    };
    return descriptor;
}

class Calculator {
    @logged
    add(a: number, b: number): number {
        return a + b;
    }
}

// Class decorator
function sealed(constructor: new (...args: unknown[]) => unknown) {
    Object.seal(constructor);
    Object.seal(constructor.prototype);
}
```

#### Symbol

```typescript
const sym = Symbol("description");

// Well-known symbols
Symbol.iterator;
Symbol.toStringTag;
Symbol.hasInstance;

// Custom Symbol.for
const sym2 = Symbol.for("key");
const sym3 = Symbol.for("key");
sym2 === sym3;  // true
```

---

## 13. Tầng 13: Memory Layout

### 13.1. Object Layout

```typescript
// JavaScript objects:
// - Hidden class (shapes in V8)
// - Inline cache
// - Properties stored in property store

// V8 optimization
class Point {
    constructor(public x: number, public y: number) {}
}

// Use objects with consistent shape for optimization
const points: Point[] = [];
for (let i = 0; i < 1000; i++) {
    points.push(new Point(i, i));
}
```

### 13.2. Array/String Layout

```typescript
// Arrays:
// - Elements stored in contiguous memory
// - Sparse arrays use dictionary

// Strings:
// - Immutable
// - Stored as UTF-16 (mostly)

// ArrayBuffer
const buffer = new ArrayBuffer(8);
const view = new DataView(buffer);
view.setInt32(0, 42, true);
```

---

## 14. Tầng 14: Compilation Model

### 14.1. TypeScript Compiler

```bash
# Compile
tsc script.ts

# Compile với watch
tsc --watch

# Compile với config
tsc --project tsconfig.json

# Compile to different targets
tsc --target es2020

# Generate declaration files
tsc --declaration
```

### 14.2. tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020", "DOM"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

---

## 15. Tầng 15: Linking Model

### 15.1. Module Loading

```typescript
// ES Modules (default)
import { add } from "./math";

// CommonJS (Node.js)
const { add } = require("./math");

// Dynamic import
const module = await import("./math");
```

---

## 16. Tầng 16: Runtime

### 16.1. JavaScript Runtime

```typescript
// V8 (Chrome, Node.js)
// SpiderMonkey (Firefox)
// JavaScriptCore (Safari)

// Event loop
console.log("1");
setTimeout(() => console.log("2"), 0);
Promise.resolve().then(() => console.log("3"));
console.log("4");
// Output: 1, 4, 3, 2
```

### 16.2. TypeScript Runtime

```typescript
// TypeScript removed at compile time
// Runtime chỉ thấy JavaScript

// Type annotations không runtime
let x: number = 5;  // Runtime: let x = 5;

// Generic không runtime
function identity<T>(arg: T): T {
    return arg;
}
identity<string>("hello");  // Runtime: identity("hello");
```

---

## 17. Tầng 17: Language Design Patterns

### 17.1. Duck Typing

```typescript
// "If it walks like a duck and quacks like a duck, it's a duck"
interface Duck {
    walk(): void;
    quack(): void;
}

class RealDuck implements Duck {
    walk(): void { console.log("Walking like a duck"); }
    quack(): void { console.log("Quack!"); }
}

class Person {
    walk(): void { console.log("Person walking"); }
    quack(): void { console.log("Person quacking"); }
}

function makeItWalk(duck: Duck): void {
    duck.walk();
}

makeItWalk(new RealDuck()); // OK
makeItWalk(new Person());   // OK - structural typing
```

### 17.2. Structural Typing

```typescript
interface Point {
    x: number;
    y: number;
}

function distance(p1: Point, p2: Point): number {
    return Math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2);
}

const point = { x: 1, y: 2, z: 3 }; // Extra properties OK
distance(point, { x: 4, y: 5 });    // OK - structural typing

// Type compatibility
type A = { x: number };
type B = { x: number; y: number };
// B extends A (B has all A's properties)
```

---

## 18. Tầng 18: Standard Library

### 18.1. Collections

```typescript
// Array
const arr: number[] = [1, 2, 3];
arr.push(4);
arr.pop();

// Set
const set = new Set([1, 2, 3, 3, 3]);  // {1, 2, 3}
set.add(4);
set.has(1);
set.delete(1);

// Map
const map = new Map<string, number>();
map.set("one", 1);
map.get("one");
map.has("one");
map.delete("one");

// WeakMap/WeakSet
const weakMap = new WeakMap();
const weakSet = new WeakSet();
```

### 18.2. Utilities

#### Object

```typescript
Object.keys({ a: 1, b: 2 });    // ["a", "b"]
Object.values({ a: 1, b: 2 });   // [1, 2]
Object.entries({ a: 1, b: 2 });  // [["a", 1], ["b", 2]]
Object.assign({}, { a: 1 });
Object.freeze({});
Object.seal({});
```

#### Array

```typescript
[1, 2, 3].find(x => x > 2);
[1, 2, 3].findIndex(x => x === 2);
[1, 2, 3].includes(2);
[1, 2, 3].indexOf(2);
[1, 2, 3].join(",");
[1, 2, 3].reverse();
[1, 2, 3].slice(1, 2);
[1, 2, 3].splice(1, 1);
```

### 18.3. I/O & System

```typescript
// Console
console.log();
console.error();

// Process (Node.js)
import process from "process";
process.argv;
process.env;
process.exit();

// File (Node.js)
import fs from "fs/promises";
await fs.readFile("file.txt", "utf-8");
```

---

## 19. Tầng 19: Ecosystem

### 19.1. Web Frameworks

#### React

```tsx
import React, { useState, useEffect } from "react";

interface User {
    id: number;
    name: string;
}

function UserList() {
    const [users, setUsers] = useState<User[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch("/api/users")
            .then(res => res.json())
            .then(data => {
                setUsers(data);
                setLoading(false);
            });
    }, []);

    if (loading) return <div>Loading...</div>;

    return (
        <ul>
            {users.map(user => (
                <li key={user.id}>{user.name}</li>
            ))}
        </ul>
    );
}
```

#### Vue

```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface User {
  id: number
  name: string
}

const users = ref<User[]>([])

onMounted(async () => {
  const res = await fetch('/api/users')
  users.value = await res.json()
})
</script>

<template>
  <ul>
    <li v-for="user in users" :key="user.id">
      {{ user.name }}
    </li>
  </ul>
</template>
```

#### Angular

```typescript
import { Component, OnInit, Service } from "@angular/core";
import { HttpClient } from "@angular/common/http";

interface User {
    id: number;
    name: string;
}

@Component({
    selector: "app-user-list",
    template: `
        <ul>
            <li *ngFor="let user of users">
                {{ user.name }}
            </li>
        </ul>
    `
})
export class UserListComponent implements OnInit {
    users: User[] = [];

    constructor(private http: HttpClient) {}

    ngOnInit() {
        this.http.get<User[]>("/api/users")
            .subscribe(users => this.users = users);
    }
}
```

### 19.2. Database & ORM

#### TypeORM

```typescript
import { Entity, PrimaryGeneratedColumn, Column, DataSource } from "typeorm";

@Entity()
class User {
    @PrimaryGeneratedColumn()
    id!: number;

    @Column()
    name!: string;

    @Column()
    email!: string;
}

const dataSource = new DataSource({
    type: "mysql",
    host: "localhost",
    entities: [User],
    synchronize: true
});

const user = new User();
user.name = "John";
user.email = "john@example.com";
await dataSource.manager.save(user);
```

#### Prisma

```prisma
// schema.prisma
model User {
    id    Int     @id @default(autoincrement())
    name  String
    email String  @unique
}
```

```typescript
import { PrismaClient } from "@prisma/client";
const prisma = new PrismaClient();

const user = await prisma.user.create({
    data: {
        name: "John",
        email: "john@example.com"
    }
});
```

### 19.3. Testing

```typescript
// Vitest / Jest
import { describe, it, expect, vi } from "vitest";

describe("Math", () => {
    it("adds", () => {
        expect(1 + 2).toBe(3);
    });

    it("async", async () => {
        const fn = vi.fn(() => Promise.resolve("data"));
        expect(await fn()).toBe("data");
    });

    it("mock", () => {
        const mock = vi.fn(() => "mocked");
        expect(mock()).toBe("mocked");
    });
});
```

---

## 20. Tầng 20: Toolchain

### 20.1. Build & Package Management

```bash
# npm/yarn/pnpm
npm init -y
npm install typescript -D
npm install express
npm run build

# npx
npx tsc --init

# Vite
npm create vite@latest my-app -- --template react-ts

# Next.js
npx create-next-app@latest my-app --typescript
```

### 20.2. Code Quality

```bash
# ESLint
npm install eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
npx eslint src/

# Prettier
npm install -D prettier
npx prettier --write src/

# husky + lint-staged
npm install -D husky lint-staged
```

### 20.3. IDE & Debugging

```typescript
// VS Code debugger
// Set breakpoints in IDE

// Console debugging
console.log("Debug:", value);

// Debugger
debugger;

// Chrome DevTools
// debugger; in code, then use Chrome
```

---

## Tổng Kết

TypeScript là ngôn ngữ:

- **Static typing** với type inference mạnh mẽ
- **Structural typing** thay vì nominal typing
- **Compiled** sang JavaScript, chạy trên mọi JS runtime
- **Modern features**: Generics, Decorators, Async/Await
- **Rich ecosystem**: React, Vue, Angular, Node.js, Deno

### TypeScript Version History

| Version  | Release Date | Key Features                                           |
|----------|-------------|-------------------------------------------------------|
| TypeScript 1.0 | 2012-10-01 | Initial release                                        |
| TypeScript 2.0 | 2016-09-22 | Non-nullable types, Control flow analysis             |
| TypeScript 2.1 | 2016-11-08 | Keyof, Mapped types                                   |
| TypeScript 2.8 | 2018-03-27 | Conditional types, Improved type inference            |
| TypeScript 3.0 | 2018-07-30 | Project references, Tuples in rest parameters         |
| TypeScript 3.8 | 2020-02-20 | Top-level await, Export * as ns                       |
| TypeScript 4.0 | 2020-08-20 | Variadic tuple types, Labeled tuple elements         |
| TypeScript 4.5 | 2021-11-17 | ES2021 lib, Template string type                     |
| TypeScript 4.7 | 2022-05-24 | Instantiation expressions, Control flow analysis     |
| TypeScript 4.9 | 2023-03-16 | satisfies operator, Auto-import                       |
| TypeScript 5.0 | 2023-03-16 | Decorators, const type parameters, ES decorators    |
| TypeScript 5.3 | 2023-11-20 | Import attributes, Narrowing in switch statements    |
| TypeScript 5.4 | 2024-02-22 | NoInfer, Preserved narrowing in closures             |
