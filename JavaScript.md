# JavaScript Syntax Reference

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
   - [3.3 Prototype/Prototype Chain](#33-prototypeprototype-chain)
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
    - [14.2 JIT](#142-jit)
15. [Tầng 15: Linking Model](#tầng-15-linking-model)
    - [15.1 Module Loading](#151-module-loading)
16. [Tầng 16: Runtime](#tầng-16-runtime)
    - [16.1 JavaScript Runtime](#161-javascript-runtime)
    - [16.2 Event Loop](#162-event-loop)
17. [Tầng 17: Language Design Patterns](#tầng-17-language-design-patterns)
    - [17.1 Duck Typing](#171-duck-typing)
    - [17.2 Prototype-based OOP](#172-prototype-based-oop)
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

### Chạy File JavaScript

```bash
# Node.js
node script.js

# Interactive mode
node

# Browser (Console)
# Open DevTools (F12) -> Console tab

# Bun
bun run script.js

# Deno
deno run script.js
```

### Đặc điểm JavaScript

- **Typing**: Dynamic, Weak typing với optional static typing (TypeScript)
- **Paradigm**: Multi-paradigm (Functional, OOP, Prototype-based)
- **Execution**: Interpreted/JIT compiled
- **Use Cases**: Web development, Server (Node.js), Mobile (React Native), Desktop (Electron)

---

## 1. Tầng 1: Syntax & Semantics

### 1.1. Khai Báo Biến (Variable Declaration)

#### Mutable - Biến thường

```javascript
// Khai báo biến (dynamic typing)
let x = 10;
let name = "JavaScript";
let isActive = true;
let prices = [1.5, 2.0, 3.5];

// const (không thể reassign)
const MAX_SIZE = 100;

// var (legacy - avoid)
var oldStyle = "don't use";
```

#### Immutable - Hằng số

```javascript
// const (reference không đổi)
const PI = 3.14159;
const APP_NAME = "MyApp";

// Object.freeze (deep immutability)
const frozen = Object.freeze({ name: "John" });
// frozen.name = "Jane"; // Error in strict mode

// Spread tạo bản sao
const original = { name: "John" };
const copy = { ...original };
```

#### Type Inference

```javascript
// JavaScript tự suy luận kiểu
let x = 10;        // number
let y = "hello";   // string
let z = true;      // boolean

// Kiểm tra kiểu
typeof x;          // "number"

// instanceof
x instanceof Number;
```

#### Global Variable

```javascript
// Global object
// Browser: window
// Node.js: global (hoặc globalThis)

globalThis.globalVar = "I am global";

// Trong module, dùng export/import
```

---

### 1.2. Khai Báo Hàm (Function Declaration)

#### Function cơ bản

```javascript
// Function declaration
function greet() {
    console.log("Hello!");
}

// Function expression
const greet = function() {
    console.log("Hello!");
};

// Function có return
function add(a, b) {
    return a + b;
}

// Arrow function
const add = (a, b) => a + b;

// JSDoc
/**
 * Calculate rectangle area.
 * @param {number} width - Width of rectangle
 * @param {number} height - Height of rectangle
 * @returns {number} Area of rectangle
 */
function calculateArea(width, height) {
    return width * height;
}
```

#### Parameters

```javascript
// Default parameters
function greet(name = "World") {
    return `Hello, ${name}!`;
}

// Rest parameters
function sum(...numbers) {
    return numbers.reduce((a, b) => a + b, 0);
}

sum(1, 2, 3, 4, 5); // 15

// Destructuring parameters
function func({ name, age }) {
    console.log(name, age);
}

func({ name: "John", age: 30 });

// Named arguments (dùng object)
function createUser({ name, email, age }) {
    return { name, email, age };
}

createUser({ name: "John", email: "john@example.com", age: 30 });
```

#### Arrow Function

```javascript
// Arrow function
const add = (a, b) => a + b;

// Với block body
const add = (a, b) => {
    return a + b;
};

// Dùng với higher-order functions
const numbers = [1, 2, 3, 4, 5];
const squared = numbers.map(x => x ** 2);
const evens = numbers.filter(x => x % 2 === 0);

// Arrow với conditional
const max = (a, b) => a > b ? a : b;

// This binding (arrow không có this riêng)
class Counter {
    count = 0;

    increment = () => {
        this.count++;
    };
}
```

#### Closure

```javascript
function outer(x) {
    return function inner(y) {
        return x + y; // Closure: capture biến từ outer
    };
}

const closure = outer(10);
closure(5); // 15
```

#### Higher-Order Function

```javascript
// Function nhận function khác làm tham số
function applyTwice(func, x) {
    return func(func(x));
}

function addFive(x) {
    return x + 5;
}

applyTwice(addFive, 10); // 20

// Function trả về function
function multiplier(factor) {
    return function(x) {
        return x * factor;
    };
}

const double = multiplier(2);
double(5); // 10
```

#### Method trong Class

```javascript
class Calculator {
    // Static method
    static add(a, b) {
        return a + b;
    }

    // Instance method
    multiply(a, b) {
        return a * b;
    }

    // Arrow (bound)
    greet = () => {
        return "Hello!";
    };
}
```

---

### 1.3. Vòng Lặp (Loops)

#### For Loop

```javascript
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

// forEach
fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`);
});
```

#### While Loop

```javascript
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}

// Do-while
let input;
do {
    input = getInput();
} while (input !== "quit");

// While với break/continue
while (true) {
    const userInput = getInput();
    if (userInput === "quit") break;
    console.log(`You entered: ${userInput}`);
}
```

#### Array Comprehension (không có, dùng map/filter)

```javascript
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

```javascript
// Dùng Array iterator
const numbers = [1, 2, 3];
const iterator = numbers[Symbol.iterator]();
iterator.next(); // { value: 1, done: false }
iterator.next(); // { value: 2, done: false }
iterator.next(); // { value: 3, done: false }
iterator.next(); // { value: undefined, done: true }

// Custom iterator
class RangeIterator {
    constructor(max) {
        this.current = 0;
        this.max = max;
    }

    [Symbol.iterator]() {
        return this;
    }

    next() {
        if (this.current < this.max) {
            return { value: this.current++, done: false };
        }
        return { value: undefined, done: true };
    }
}

for (const i of new RangeIterator(5)) {
    console.log(i); // 0, 1, 2, 3, 4
}
```

#### Loop Control

```javascript
// Break
for (let i = 0; i < 10; i++) {
    if (i === 5) break;
    console.log(i); // 0, 1, 2, 3, 4
}

// Continue
for (let i = 0; i < 5; i++) {
    if (i === 2) continue;
    console.log(i); // 0, 1, 3, 4
}

// Label
outer:
for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        if (j === 1) break outer;
    }
}
```

---

### 1.4. Điều Kiện (Conditionals)

#### If-Else

```javascript
// If-else cơ bản
const age = 18;
if (age >= 18) {
    console.log("Adult");
} else {
    console.log("Minor");
}

// Else if
const score = 85;
let grade;
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

```javascript
function httpStatus(status) {
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
function httpStatusMulti(status) {
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

#### Match Expression (không có native switch)

```javascript
// Dùng object/Map cho pattern matching
const httpStatusMap = {
    200: "OK",
    404: "Not Found",
    500: "Server Error"
};

function httpStatus(status) {
    return httpStatusMap[status] ?? "Unknown";
}

// Với discriminated union
const shape = { type: "circle", radius: 5 };

function area(shape) {
    switch (shape.type) {
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

```javascript
// Number (JavaScript: 64-bit floating point)
let x = 10;
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
Number.isInteger(x);
Number.isNaN(x);
Number.isFinite(x);
```

#### BigInt

```javascript
// BigInt (arbitrary precision)
const big = 9007199254740991n;
const big2 = BigInt(9007199254740991);
big + 1n; // 9007199254740992n
```

#### String

```javascript
// String
let s1 = "Hello";
let s2 = 'World';
let s3 = `Multi
line
string`;

// Template literal
const name = "JavaScript";
const version = "ES2024";
const msg = `Welcome to ${name} ${version}`; // "Welcome to JavaScript ES2024"

// String methods
const s = "Hello World";
s.length;                    // 11
s.toUpperCase();             // "HELLO WORLD"
s.toLowerCase();             // "hello world"
s.trim();                    // "Hello World"
s.split(" ");                // ["Hello", "World"]
s.replace("World", "JS");    // "Hello JS"
s.replaceAll("o", "0");     // "Hell0 W0rld"
s.includes("World");         // true
s.startsWith("Hello");       // true
s.endsWith("World");         // true
s.indexOf("World // 6
");         s.substring(0, 5);          // "Hello"
s.slice(0, 5);              // "Hello"
```

#### Boolean

```javascript
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

```javascript
// Array
const numbers = [1, 2, 3, 4, 5];
const mixed = [1, "hello", 3.14, true];

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
arr.slice(-2);       // [3, 4]

// Spread
const arr2 = [...arr, 5, 6];
```

#### Object

```javascript
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

// Destructuring
const { name, age } = user;
const { name: userName } = user;
```

#### null & undefined

```javascript
let value = null;
let undefined = undefined;

// Optional chaining
const user = { address: { city: { name: "NYC" } } };
const city = user?.address?.city?.name; // "NYC"

// Nullish coalescing
const value = null ?? "default"; // "default"
const value2 = 0 ?? "default";   // 0 (vì 0 không phải null/undefined)
```

---

### 2.2. Enum

```javascript
// JavaScript không có enum native
// Dùng const object
const Color = Object.freeze({
    RED: "RED",
    GREEN: "GREEN",
    BLUE: "BLUE"
});

// Với values
const Status = Object.freeze({
    PENDING: "PENDING",
    APPROVED: "APPROVED",
    REJECTED: "REJECTED"
});

// Enum với methods
const Color = Object.freeze({
    RED: "RED",
    GREEN: "GREEN",
    BLUE: "BLUE",
    describe(color) {
        return `Color ${color}`;
    }
});

// TypeScript enum (khi compile to JS)
// enum Color { Red, Green, Blue }
// -> const Color = { Red: 0, Green: 1, Blue: 2, 0: "Red", 1: "Green", 2: "Blue" }
```

---

### 2.3. Nullable Types

```javascript
// Union type với null/undefined
let name = null;
let age = undefined;

// Optional parameter
function greet(name) {
    if (name === undefined) {
        return "Hello, World!";
    }
    return `Hello, ${name}!`;
}

// Optional property
const user = {
    name: "John"
    // email is optional
};
```

---

### 2.4. Null Safety

```javascript
// Optional chaining (?.)
const user = {
    address: {
        city: {
            name: "NYC"
        }
    }
};

const city = user?.address?.city?.name; // "NYC"
const zip = user?.address?.zipCode ?? "Unknown"; // "Unknown"

// Nullish coalescing (??)
const value = null ?? "default"; // "default"
const value2 = 0 ?? "default"; // 0

// Type guard
function printLength(str) {
    if (str !== null && str !== undefined) {
        console.log(str.length); // OK
    }
}
```

---

### 2.5. Generics (TypeScript only)

```typescript
// JavaScript không có generics
// Dùng TypeScript cho generics

interface Container<T> {
    value: T;
    get(): T;
}

const intContainer: Container<number> = {
    value: 42,
    get() { return this.value; }
};
```

---

### 2.6. Collection Operations

#### Map/Transform

```javascript
const numbers = [1, 2, 3, 4, 5];

// map()
const squared = numbers.map(x => x ** 2);

// with index
const indexed = numbers.map((x, i) => ({ value: x, index: i }));
```

#### Filter

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// filter()
const evens = numbers.filter(x => x % 2 === 0);
```

#### Reduce/Fold

```javascript
const numbers = [1, 2, 3, 4, 5];

// reduce()
const total = numbers.reduce((acc, x) => acc + x, 0); // 15
const product = numbers.reduce((acc, x) => acc * x, 1); // 120
```

#### FlatMap

```javascript
const nested = [[1, 2], [3, 4], [5, 6]];

// flat()
const flattened = nested.flat(); // [1, 2, 3, 4, 5, 6]

// flatMap()
const words = ["hello", "world"];
const chars = words.flatMap(word => word.split("")); // ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d"]
```

#### Sort

```javascript
const numbers = [3, 1, 4, 1, 5, 9, 2, 6];

// sort()
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

```javascript
const numbers = [1, 2, 3, 4, 5];

// Find first
const result = numbers.find(x => x > 3); // 4

// Find index
const index = numbers.findIndex(x => x === 3); // 2

// Last
const last = numbers[numbers.length - 1]; // 5
const last2 = numbers.at(-1); // 5 (ES2022)
```

#### Any/All/Some/Every

```javascript
const numbers = [1, 2, 3, 4, 5];

numbers.some(x => x > 3);   // true
numbers.every(x => x > 0);  // true
numbers.every(x => x > 10); // false
numbers.includes(3);         // true

// none
numbers.every(x => x < 3); // false
```

#### GroupBy

```javascript
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
}, {});
```

#### Chunk

```javascript
function chunk(arr, size) {
    const result = [];
    for (let i = 0; i < arr.length; i += size) {
        result.push(arr.slice(i, i + size));
    }
    return result;
}

chunk([1, 2, 3, 4, 5, 6, 7], 3); // [[1,2,3], [4,5,6], [7]]
```

#### Zip

```javascript
const names = ["Alice", "Bob", "Charlie"];
const ages = [25, 30, 35];

// Zip
const combined = names.map((name, i) => ({ name, age: ages[i] }));
// [{ name: "Alice", age: 25 }, ...]
```

---

### 2.7. String Operations

#### Concatenation

```javascript
// Template literal
const s = `Hello ${"World"}`;

// String.concat()
"Hello ".concat("World");

// +
"Hello " + "World";

// Array.join
["Hello", "World"].join(" ");
```

#### Interpolation

```javascript
const name = "JavaScript";
const version = "ES2024";

// Template literal
`Welcome to ${name} ${version}`;

// replace
"Hello {name}".replace("{name}", "World");
```

#### Regex

```javascript
const text = "My email is john@example.com";

// Match
const match = text.match(/[\w.-]+@[\w.-]+/);
if (match) {
    console.log(match[0]); // "john@example.com"
}

// Find all
const emails = text.match(/[\w.-]+@[\w.-]+/g);

// Pattern với named groups (ES2024)
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

```javascript
class User {
    // Properties
    name;
    email;
    #age; // Private field (ES2022)

    // Constructor
    constructor(name, email, age) {
        this.name = name;
        this.email = email;
        this.#age = age;
    }

    // Method
    greet() {
        return `Hello, I'm ${this.name}`;
    }

    // Getter
    get age() {
        return this.#age;
    }

    // Setter
    set age(value) {
        if (value >= 0) {
            this.#age = value;
        }
    }

    // Static method
    static createGuest() {
        return new User("Guest", "guest@example.com", 0);
    }
}

// Create instance
const user = new User("John", "john@example.com", 30);
user.greet(); // "Hello, I'm John"
```

#### Shorthand (Object)

```javascript
// Object literal
const user = {
    name: "John",
    email: "john@example.com",
    age: 30,

    // Method shorthand
    greet() {
        return `Hello, I'm ${this.name}`;
    }
};
```

#### Singleton

```javascript
// Object.create
const singleton = Object.create(null);

// Singleton pattern
class Singleton {
    static #instance;

    constructor() {
        if (Singleton.#instance) {
            return Singleton.#instance;
        }
        Singleton.#instance = this;
        this.value = "Singleton instance";
    }
}

const s1 = new Singleton();
const s2 = new Singleton();
s1 === s2; // true
```

#### Factory Method

```javascript
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    static fromDict(data) {
        return new User(data.name, data.email);
    }

    static fromJson(json) {
        const data = JSON.parse(json);
        return User.fromDict(data);
    }
}

const user = User.fromDict({ name: "John", email: "john@example.com" });
```

#### Abstract Class

```javascript
// JavaScript không có abstract class native
// Dùng Error để simulate

class Animal {
    constructor(name) {
        if (this.constructor === Animal) {
            throw new Error("Cannot instantiate abstract class");
        }
        this.name = name;
    }

    speak() {
        throw new Error("Method 'speak' must be implemented");
    }
}

class Dog extends Animal {
    speak() {
        return "Woof!";
    }
}

const dog = new Dog("Buddy"); // OK
// const animal = new Animal("Test"); // Error
```

---

### 3.2. Kế Thừa & Đa Hình (Inheritance & Polymorphism)

#### Inheritance

```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        return "...";
    }
}

class Dog extends Animal {
    speak() {
        return "Woof!";
    }

    fetch() {
        return "Fetching!";
    }
}

class Cat extends Animal {
    speak() {
        return "Meow!";
    }
}

const dog = new Dog("Buddy");
dog.speak(); // "Woof!"
dog.fetch(); // "Fetching!"
```

#### Super

```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        return "...";
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name); // Gọi parent constructor
        this.breed = breed;
    }

    speak() {
        return `${super.speak()} Woof!`; // Gọi parent method
    }
}
```

#### Polymorphism

```javascript
function makeSpeak(animal) {
    return animal.speak();
}

const animals = [new Dog("Buddy"), new Cat("Whiskers")];
animals.forEach(animal => {
    console.log(animal.speak()); // Polymorphism
});
```

#### Multiple Inheritance (không có - dùng Mixin)

```javascript
// Mixin
const Flyable = {
    fly() {
        return "Flying!";
    }
};

const Swimmable = {
    swim() {
        return "Swimming!";
    }
};

class Duck {
    quack() {
        return "Quack!";
    }
}

// Apply mixins
Object.assign(Duck.prototype, Flyable, Swimmable);

const duck = new Duck();
duck.fly();    // "Flying!"
duck.swim();  // "Swimming!"
duck.quack(); // "Quack!"
```

---

### 3.3. Prototype/Prototype Chain

```javascript
// Prototype
class Animal {
    speak() {
        return "...";
    }
}

Animal.prototype.speak; // method

// Prototype chain
const dog = new Dog("Buddy");
dog.__proto__ === Dog.prototype;
dog.__proto__.__proto__ === Animal.prototype;

// Object.create
const animalProto = {
    speak() { return "..."; }
};

const dog = Object.create(animalProto);
dog.speak(); // "..."

// hasOwnProperty
dog.hasOwnProperty("name"); // true
dog.hasOwnProperty("speak"); // false (inherited)
```

---

### 3.4. Visibility/Access Modifiers

```javascript
class Example {
    publicVar = "I am public";      // Public (default)
    #privateVar = "I am private";   // Private (ES2022)

    publicMethod() {}
    #privateMethod() {} // Private method
}

const ex = new Example();
ex.publicVar;      // OK
// ex.#privateVar; // Error
```

---

## 4. Tầng 4: Memory Model

### 4.1. Memory Management

```javascript
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
weakMap.get(obj); // "value"

// Memory info (limited in JS)
const used = performance?.memory?.usedJSHeapSize;
```

### 4.2. Property & Getter/Setter

```javascript
class Temperature {
    #celsius = 0;

    // Getter
    get celsius() {
        return this.#celsius;
    }

    // Setter
    set celsius(value) {
        this.#celsius = value;
    }

    // Read-only
    get fahrenheit() {
        return this.#celsius * 9/5 + 32;
    }

    // Computed property
    get kelvin() {
        return this.#celsius + 273.15;
    }
}

const temp = new Temperature();
temp.celsius = 25;
console.log(temp.fahrenheit); // 77
```

---

## 5. Tầng 5: Concurrency Model

### 5.1. Concurrency/Async

#### Callbacks

```javascript
function fetchData(callback) {
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

```javascript
function fetchData() {
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

```javascript
async function fetchData() {
    return "data";
}

async function main() {
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

```javascript
// Web Worker
const worker = new Worker("worker.js");

worker.onmessage = (event) => {
    console.log(event.data);
};

worker.postMessage({ type: "compute", data: 42 });
worker.terminate();

// SharedWorker
const shared = new SharedWorker("sharedWorker.js");
```

---

## 6. Tầng 6: Paradigm

### 6.1. Functional Programming

#### Pure Function

```javascript
// Pure function
function add(a, b) {
    return a + b;
}

// Impure function
let counter = 0;
function impureAdd(a, b) {
    counter++;
    return a + b;
}
```

#### Immutability

```javascript
// Dùng const và spread
const user = { name: "John", age: 30 };
const updatedUser = { ...user, age: 31 };

// Dùng Object.freeze
const frozen = Object.freeze({ name: "John" });
// frozen.name = "Jane"; // Error (strict mode)

// Dùng libraries: Immer, Immutable.js
```

#### First-Class Function

```javascript
// Function là first-class citizens
function apply(func, x) {
    return func(x);
}

function double(x) {
    return x * 2;
}

apply(double, 5); // 10
apply(x => x ** 2, 5); // 25
```

#### Function Composition

```javascript
const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);
const pipe = (...fns) => x => fns.reduce((acc, fn) => fn(acc), x);

const f = compose(
    x => x + 1,
    x => x * 2
);
f(3); // (3 * 2) + 1 = 7
```

#### Currying

```javascript
const curry =
    (...args) =>
    (...rest) =>
        args.length === 0
            ? rest[0]
            : curry(...args.slice(0, -1))(...[...args.slice(-1), ...rest]);

const add = curry((a, b, c) => a + b + c);
add(1)(2)(3);   // 6
add(1, 2)(3);   // 6
add(1)(2, 3);  // 6
```

#### Partial Application

```javascript
const partial = (fn, ...args) => (...rest) => fn(...args, ...rest);

const power = (base, exp) => base ** exp;
const square = partial(power, 2);
square(5); // 25

const cube = partial(power, 3);
cube(5); // 125
```

---

## 7. Tầng 7: Error Handling

### 7.1. Xử Lý Lỗi (Error Handling)

#### Try-Catch

```javascript
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
    console.log("Cleanup"); // Always executed
}
```

#### Throw Exception

```javascript
function validateAge(age) {
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

```javascript
class ValidationError extends Error {
    constructor(field, message) {
        super(message);
        this.name = "ValidationError";
        this.field = field;
    }
}

function validateEmail(email) {
    if (!email.includes("@")) {
        throw new ValidationError("email", "Invalid email format");
    }
}
```

### 7.2. Error Types

```javascript
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
    constructor(message, code) {
        super(message);
        this.name = "AppError";
        this.code = code;
    }
}

class ValidationError extends AppError {
    constructor(message) {
        super(message, "VALIDATION_ERROR");
        this.name = "ValidationError";
    }
}
```

---

## 8. Tầng 8: Module & Organization

### 8.1. Import/Module

#### ES Modules

```javascript
// Import
import { add, multiply } from "./math.js";
import * as Math from "./math.js";

// Import với alias
import { add as sum } from "./math.js";

// Default import
import myFunction from "./math.js";

// Re-export
export { add, multiply };
export default function defaultExport() {}

// Dynamic import
const module = await import("./math.js");
```

#### CommonJS

```javascript
// Require
const { add, multiply } = require("./math.js");
const math = require("./math.js");
```

---

### 8.2. Extension Methods

#### Monkey Patching

```javascript
// Thêm method vào prototype có sẵn
Array.prototype.chunk = function(size) {
    const result = [];
    for (let i = 0; i < this.length; i += size) {
        result.push(this.slice(i, i + size));
    }
    return result;
};

// Usage
[1, 2, 3, 4, 5, 6].chunk(3); // [[1,2,3], [4,5,6]]
```

---

## 9. Tầng 9: I/O & Networking

### 9.1. HTTP & Networking

#### Fetch API

```javascript
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

```javascript
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

```javascript
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

```javascript
// File input
const input = document.querySelector('input[type="file"]');
input?.addEventListener("change", async (e) => {
    const file = e.target.files?.[0];
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

```javascript
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
```

### 10.2. Date & Time

```javascript
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

```javascript
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

```javascript
// test.spec.js

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

```javascript
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

```javascript
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

// Trace
console.trace("trace");

// Assert
console.assert(true, "This will not log");
console.assert(false, "This will log");

// Libraries: winston, pino, loglevel
```

### 11.3. Dependency Injection

```javascript
// Constructor injection
class UserService {
    constructor(repository) {
        this.repository = repository;
    }

    getUser(id) {
        return this.repository.find(id);
    }
}

// Usage
class UserRepository {
    find(id) {
        return { id, name: "John" };
    }
}

const userService = new UserService(new UserRepository());

// Interface
// JavaScript không có interface, dùng JSDoc hoặc convention
```

### 11.4. Configuration

#### Environment Variables

```javascript
// Vite/Webpack
import.meta.env.VITE_API_URL;

// Node.js
require("dotenv").config();
const apiKey = process.env.API_KEY;

// Browser
const apiKey = import.meta.env.VITE_API_KEY;
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

# npx
npx create-react-app my-app
npx vite build
```

### 11.6. Documentation

#### JSDoc

```javascript
/**
 * Adds two numbers.
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The sum of a and b
 * @example
 * add(1, 2) // returns 3
 */
function add(a, b) {
    return a + b;
}
```

---

## 12. Tầng 12: Advanced Concepts

### 12.1. Advanced Concepts

#### Reflection/Introspection

```javascript
// typeof
typeof "hello"; // "string"
typeof 123;    // "number"

// instanceof
"hello" instanceof String; // false (primitive)

// constructor
"hello".constructor === String; // true

// Object.getPrototypeOf
Object.getPrototypeOf({}) === Object.prototype; // true

// Object.keys, Object.getOwnPropertyNames
Object.keys({ a: 1 }); // ["a"]
Object.getOwnPropertyNames({ a: 1 }); // ["a"]
```

#### Symbol

```javascript
const sym = Symbol("description");
const sym2 = Symbol("description");
sym === sym2; // false

// Well-known symbols
Symbol.iterator;
Symbol.toStringTag;
Symbol.hasInstance;

// Symbol.for
const sym3 = Symbol.for("key");
const sym4 = Symbol.for("key");
sym3 === sym4; // true
```

#### Proxy

```javascript
const handler = {
    get(target, prop) {
        console.log(`Getting ${prop}`);
        return target[prop];
    },
    set(target, prop, value) {
        console.log(`Setting ${prop} to ${value}`);
        target[prop] = value;
    }
};

const proxy = new Proxy({}, handler);
proxy.name = "John"; // "Setting name to John"
console.log(proxy.name); // "Getting name" -> "John"
```

#### Reflect

```javascript
Reflect.get({ a: 1 }, "a"); // 1
Reflect.set({ a: 1 }, "a", 2); // true
Reflect.has({ a: 1 }, "a"); // true
Reflect.ownKeys({ a: 1, b: 2 }); // ["a", "b"]
```

---

## 13. Tầng 13: Memory Layout

### 13.1. Object Layout

```javascript
// JavaScript objects:
// - Hidden class (shapes in V8)
// - Inline cache
// - Properties stored in property store

// V8 optimization
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

// Use objects with consistent shape for optimization
const points = [];
for (let i = 0; i < 1000; i++) {
    points.push(new Point(i, i));
}
```

### 13.2. Array/String Layout

```javascript
// Arrays:
// - Elements stored in contiguous memory
// - Sparse arrays use dictionary

// Strings:
// - Immutable
// - Stored as UTF-16

// ArrayBuffer
const buffer = new ArrayBuffer(8);
const view = new DataView(buffer);
view.setInt32(0, 42, true);
```

---

## 14. Tầng 14: Compilation Model

### 14.1. Interpreter

```javascript
// JavaScript engine:
// 1. Parser -> AST
// 2. Interpreter (Ignition) -> Bytecode
// 3. Optimizer (TurboFan) -> Machine code

// eval
const code = "console.log('hello')";
eval(code);

// Function constructor
const fn = new Function("a", "b", "return a + b");
fn(1, 2); // 3
```

### 14.2. JIT

```javascript
// Just-In-Time Compilation:
// - Baseline compiler: quick machine code
// - Optimizing compiler: profiled, optimized machine code
// - Deoptimization: fallback when assumptions fail

// V8 (Chrome, Node.js)
// SpiderMonkey (Firefox)
// JavaScriptCore (Safari)
```

---

## 15. Tầng 15: Linking Model

### 15.1. Module Loading

```javascript
// ES Modules (default)
import { add } from "./math.js";

// CommonJS (Node.js)
const { add } = require("./math.js");

// Dynamic import
const module = await import("./math.js");

// AMD (legacy)
require(["module"], function(module) { });
```

---

## 16. Tầng 16: Runtime

### 16.1. JavaScript Runtime

```javascript
// V8 (Chrome, Node.js)
// SpiderMonkey (Firefox)
// JavaScriptCore (Safari)

// Components:
// - Call Stack
// - Heap (memory allocation)
// - Task Queue (macro tasks)
// - Microtask Queue (promises)
// - Event Loop

// Execution order
console.log("1");
setTimeout(() => console.log("2"), 0);
Promise.resolve().then(() => console.log("3"));
console.log("4");
// Output: 1, 4, 3, 2
```

### 16.2. Event Loop

```javascript
// Event Loop
// 1. Execute current call stack
// 2. Execute all microtasks (promises)
// 3. Render (if needed)
// 4. Execute next macrotask (setTimeout, I/O)

// Microtasks
Promise.resolve().then(() => console.log("microtask"));

// Macrotasks
setTimeout(() => console.log("macrotask"), 0);

// requestAnimationFrame
requestAnimationFrame(() => console.log("animation frame"));
```

---

## 17. Tầng 17: Language Design Patterns

### 17.1. Duck Typing

```javascript
// "If it walks like a duck and quacks like a duck, it's a duck"
function makeItWalk(duck) {
    return duck.walk();
}

makeItWalk({ walk: () => "Walking like a duck" }); // OK
makeItWalk({ walk: () => "Person walking" }); // OK
```

### 17.2. Prototype-based OOP

```javascript
// Prototype-based inheritance
function Animal(name) {
    this.name = name;
}

Animal.prototype.speak = function() {
    return "...";
};

function Dog(name, breed) {
    Animal.call(this, name);
    this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.speak = function() {
    return "Woof!";
};

const dog = new Dog("Buddy", "Golden");
dog.speak(); // "Woof!"
dog.name;    // "Buddy"
```

---

## 18. Tầng 18: Standard Library

### 18.1. Collections

```javascript
// Array
const arr = [1, 2, 3];
arr.push(4);
arr.pop();

// Set
const set = new Set([1, 2, 3, 3, 3]); // {1, 2, 3}
set.add(4);
set.has(1);
set.delete(1);

// Map
const map = new Map();
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

```javascript
Object.keys({ a: 1, b: 2 });    // ["a", "b"]
Object.values({ a: 1, b: 2 });   // [1, 2]
Object.entries({ a: 1, b: 2 });  // [["a", 1], ["b", 2]]
Object.assign({}, { a: 1 });
Object.freeze({});
Object.seal({});
Object.create(null);
```

#### Array

```javascript
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

```javascript
// Console
console.log();

// Process (Node.js)
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

```javascript
import React, { useState, useEffect } from "react";

function UserList() {
    const [users, setUsers] = useState([]);
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

```javascript
import { ref, onMounted } from "vue";

export default {
    setup() {
        const users = ref([]);

        onMounted(async () => {
            const res = await fetch("/api/users");
            users.value = await res.json();
        });

        return { users };
    },
    template: `
        <ul>
            <li v-for="user in users" :key="user.id">
                {{ user.name }}
            </li>
        </ul>
    `
};
```

#### Svelte

```javascript
<script>
    import { onMount } from "svelte";

    let users = [];

    onMount(async () => {
        const res = await fetch("/api/users");
        users = await res.json();
    });
</script>

<ul>
    {#each users as user}
        <li>{user.name}</li>
    {/each}
</ul>
```

### 19.2. Database & ORM

#### Prisma

```javascript
// schema.prisma
// model User {
//     id    Int     @id @default(autoincrement())
//     name  String
//     email String  @unique
// }

import { PrismaClient } from "@prisma/client";
const prisma = new PrismaClient();

const user = await prisma.user.create({
    data: {
        name: "John",
        email: "john@example.com"
    }
});
```

#### Mongoose

```javascript
import mongoose from "mongoose";

const userSchema = new mongoose.Schema({
    name: String,
    email: { type: String, unique: true },
    age: Number
});

const User = mongoose.model("User", userSchema);

const user = await User.create({
    name: "John",
    email: "john@example.com",
    age: 30
});
```

### 19.3. Testing

```javascript
// Jest / Vitest
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
npm install express
npm run build

# npx
npx create-react-app my-app
npx vite build

# Bun
bun install
bun run build

# Deno
deno run --allow-net server.ts
```

### 20.2. Code Quality

```bash
# ESLint
npm install eslint
npx eslint src/

# Prettier
npm install -D prettier
npx prettier --write src/

# husky + lint-staged
npm install -D husky lint-staged

# TypeScript (optional)
npm install -D typescript
npx tsc --init
```

### 20.3. IDE & Debugging

```javascript
// VS Code debugger
// Set breakpoints in IDE

// Console debugging
console.log("Debug:", value);

// debugger
debugger;

// Chrome DevTools
// debugger; in code, then use Chrome
```

---

## Tổng Kết

JavaScript là ngôn ngữ:

- **Dynamic typing** với weak typing
- **Prototype-based** OOP (không có class inheritance truyền thống)
- **Event-driven** với non-blocking I/O
- **Multi-platform**: Browser, Node.js, Mobile, Desktop
- **Rich ecosystem**: React, Vue, Angular, Node.js

### JavaScript/ECMAScript Version History

| Version | Release Date | Key Features                                           |
|---------|-------------|-------------------------------------------------------|
| ES1     | 1997-06-01  | First edition                                         |
| ES3     | 1999-12-03  | try/catch, regex, string methods                       |
| ES5     | 2009-12-03  | Strict mode, JSON, getters/setters                     |
| ES6/ES2015 | 2015-06-17 | Classes, Promises, let/const, arrow functions, modules |
| ES7/ES2016 | 2016-06-01 | ** operator, Array.includes                          |
| ES8/ES2017 | 2017-06-01 | async/await, Object.entries/values                    |
| ES9/ES2018 | 2018-06-01 | Async iteration, spread in objects                   |
| ES10/ES2019 | 2019-06-01 | Array.flat, Object.fromEntries, optional catch       |
| ES11/ES2020 | 2020-06-01 | BigInt, nullish coalescing, optional chaining          |
| ES12/ES2021 | 2021-06-01 | String.replaceAll, logical assignment                 |
| ES13/ES2022 | 2022-06-01 | Class fields, at() method, Error cause                |
| ES14/ES2023 | 2023-06-01 | Array findLast, toReversed, toSorted                  |
| ES15/ES2024 | 2024-06-01 | Promise any, RegExp v flag, Structured Clone          |
