# C Syntax Reference

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
   - [2.3 Typedef](#23-typedef)
   - [2.4 Pointers](#24-pointers)
   - [2.5 Arrays](#25-arrays)
   - [2.6 String Operations](#26-string-operations)
3. [Tầng 3: OOP & Type Relationships](#tầng-3-oop--type-relationships)
   - [3.1 Struct](#31-struct)
   - [3.2 Union](#32-union)
   - [3.3 Bit Fields](#33-bit-fields)
   - [3.4 Function Pointers](#34-function-pointers)
4. [Tầng 4: Memory Model](#tầng-4-memory-model)
   - [4.1 Memory Allocation](#41-memory-allocation)
   - [4.2 Pointer Arithmetic](#42-pointer-arithmetic)
   - [4.3 Volatile & Const](#43-volatile--const)
5. [Tầng 5: Concurrency Model](#tầng-5-concurrency-model)
   - [5.1 POSIX Threads](#51-posix-threads)
   - [5.2 Mutex](#52-mutex)
   - [5.3 Atomics](#53-atomics)
6. [Tầng 6: Paradigm](#tầng-6-paradigm)
   - [6.1 Procedural Programming](#61-procedural-programming)
   - [6.2 Function Pointers as Callbacks](#62-function-pointers-as-callbacks)
7. [Tầng 7: Error Handling](#tầng-7-error-handling)
   - [7.1 Error Return Codes](#71-error-return-codes)
   - [7.2 setjmp/longjmp](#72-setjmplongjmp)
   - [7.3 Signal Handling](#73-signal-handling)
8. [Tầng 8: Module & Organization](#tầng-8-module--organization)
   - [8.1 Include](#81-include)
   - [8.2 Header Files](#82-header-files)
   - [8.3 Static/Extern](#83-staticextern)
9. [Tầng 9: I/O & Networking](#tầng-9-io--networking)
   - [9.1 Standard I/O](#91-standard-io)
   - [9.2 File I/O](#92-file-io)
   - [9.3 Socket Programming](#93-socket-programming)
10. [Tầng 10: Data & Serialization](#tầng-10-data--serialization)
    - [10.1 JSON](#101-json)
    - [10.2 Date & Time](#102-date--time)
    - [10.3 Regular Expression](#103-regular-expression)
11. [Tầng 11: Development Practices](#tầng-11-development-practices)
    - [11.1 Testing](#111-testing)
    - [11.2 Logging](#112-logging)
    - [11.3 Build Systems](#113-build-systems)
12. [Tầng 12: Advanced Concepts](#tầng-12-advanced-concepts)
    - [12.1 Preprocessor](#121-preprocessor)
    - [12.2 Variadic Functions](#122-variadic-functions)
    - [12.3 Inline Assembly](#123-inline-assembly)
13. [Tầng 13: Memory Layout](#tầng-13-memory-layout)
    - [13.1 Struct Layout](#131-struct-layout)
    - [13.2 Memory Alignment](#132-memory-alignment)
    - [13.3 Padding & Packing](#133-padding--packing)
14. [Tầng 14: Compilation Model](#tầng-14-compilation-model)
    - [14.1 Compilation Pipeline](#141-compilation-pipeline)
    - [14.2 Object Files](#142-object-files)
15. [Tầng 15: Linking Model](#tầng-15-linking-model)
    - [15.1 Static Linking](#151-static-linking)
    - [15.2 Dynamic Linking](#152-dynamic-linking)
    - [15.3 Symbol Resolution](#153-symbol-resolution)
16. [Tầng 16: Runtime](#tầng-16-runtime)
    - [16.1 Stack Frame](#161-stack-frame)
    - [16.2 Call Stack](#162-call-stack)
    - [16.3 Memory Model](#163-memory-model)
17. [Tầng 17: Language Design Patterns](#tầng-17-language-design-patterns)
    - [17.1 Opaque Pointers](#17-opaque-pointers)
    - [17.2 Handler Pattern](#172-handler-pattern)
18. [Tầng 18: Standard Library](#tầng-18-standard-library)
    - [18.1 Standard Headers](#181-standard-headers)
    - [18.2 libc Functions](#182-libc-functions)
19. [Tầng 19: Ecosystem](#tầng-19-ecosystem)
    - [19.1 Libraries](#191-libraries)
    - [19.2 Tools](#192-tools)
20. [Tầng 20: Toolchain](#tầng-20-toolchain)
    - [20.1 Compiler](#201-compiler)
    - [20.2 Debugger](#202-debugger)
    - [20.3 Static Analysis](#203-static-analysis)

---

## 0. Phân Loại Ngôn Ngữ

### Chạy File C

```bash
# Compile và chạy
gcc -o main main.c && ./main

# Với make
make

# Các cờ compiler phổ biến
gcc -std=c11 -Wall -Wextra -O2 -g main.c -o main

# C11 (2011), C17 (2018), C23 (2023)
# -Wall -Wextra: Cảnh báo đầy đủ
# -O0/-O1/-O2/-O3: Tối ưu hóa
# -g: Debug symbols
# -l: Link library
```

### Đặc điểm C

- **Typing**: Static typing, weak typing
- **Paradigm**: Procedural, Imperative
- **Execution**: Compiled (AOT), Native code
- **Memory Safety**: Manual memory management (malloc/free)
- **Use Cases**: Systems programming, Embedded, OS, Drivers, High-performance applications

---

## 1. Tầng 1: Syntax & Semantics

### 1.1. Khai Báo Biến (Variable Declaration)

#### Mutable - Biến thường

```c
// Khai báo biến với type inference (C99+)
int x = 10;
char name[] = "C";
_Bool is_active = 1;

// Explicit type
int x = 10;
float pi = 3.14f;
double e = 2.718;

// Mutable
int counter = 0;
counter += 1;

// Global variable
int global_counter = 0;

void increment(void) {
    global_counter++;
}
```

#### Immutable - Hằng số

```c
// const (read-only, nhưng không phải compile-time constant)
const int MAX_SIZE = 100;
const double PI = 3.14159;

// constexpr (C23+)
constexpr int MAX_SIZE = 100;

// #define macro (preprocessor)
#define MAX_SIZE 100
#define PI 3.14159
#define HELLO "Hello"

// enum (compile-time constant)
enum { MAX_SIZE = 100 };

// static (file scope)
static int file_counter = 0;
```

#### Global Variable

```c
// Global variable
int global_var = 42;

// Static global (chỉ available trong file này)
static int internal_var = 10;

// extern (declaration, định nghĩa ở file khác)
extern int external_var;
```

---

### 1.2. Khai Báo Hàm (Function Declaration)

#### Function cơ bản

```c
// Function không có return
void greet(void) {
    printf("Hello!\n");
}

// Function có return
int add(int a, int b) {
    return a + b;
}

// Function với pointer return
int* create_array(int size) {
    int* arr = malloc(size * sizeof(int));
    return arr;
}

// Function với void pointer
void* generic_alloc(size_t size) {
    return malloc(size);
}

// Function prototype (declaration)
int calculate(int x, int y);
```

#### Parameters

```c
// Pass by value
void set_value(int x) {
    x = 10;  // Chỉ thay đổi bản sao
}

// Pass by pointer
void set_value(int* x) {
    if (x != NULL) {
        *x = 10;  // Thay đổi giá trị gốc
    }
}

// Pass by const pointer (không sửa đổi)
void print_array(const int* arr, size_t n) {
    for (size_t i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
}

// Variable-length array (C99+)
void process_array(int n, int arr[n]) {
    // ...
}

// Default parameters - C không có, dùng macro
#define SET_DEFAULT(x, default_val) ((x) == 0 ? (default_val) : (x))
```

---

### 1.3. Vòng Lặp (Loops)

#### For loop

```c
// C-style for
for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}

// For với multiple variables
for (int i = 0, j = 10; i < 10 && j > 0; i++, j--) {
    // ...
}

// For without body (C99+)
int arr[5] = {1, 2, 3, 4, 5};
int sum = 0;
for (int i = 0; i < 5; sum += arr[i++]);
```

#### While loop

```c
int count = 0;
while (count < 5) {
    printf("%d ", count++);
}

// Do-while
do {
    printf("%d ", count--);
} while (count > 0);

// Infinite loop
while (1) {
    // ...
}

for (;;) {
    // ...
}
```

#### Break/Continue

```c
// Break - thoát khỏi loop
for (int i = 0; i < 10; i++) {
    if (i == 5) break;
    printf("%d ", i);
}

// Continue - bỏ qua iteration hiện tại
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) continue;
    printf("%d ", i);  // Chỉ in số lẻ
}

// goto (tránh dùng trừ khi cần thiết)
for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
        if (condition) goto found;
    }
}
found:
    // ...
```

---

### 1.4. Điều Kiện (Conditionals)

#### If-else

```c
int x = 10;

if (x > 0) {
    printf("Positive");
} else if (x < 0) {
    printf("Negative");
} else {
    printf("Zero");
}

// Assignment in condition (C99+)
if (int result = get_value()) {
    // result != 0
}

// Ternary operator
int x = 10;
const char* result = (x > 0) ? "Positive" : "Non-positive";
```

#### Switch-case

```c
int day = 3;
switch (day) {
    case 1:
        printf("Monday");
        break;
    case 2:
        printf("Tuesday");
        break;
    case 3:
        printf("Wednesday");
        break;
    default:
        printf("Unknown");
}

// Switch without break (fall-through)
switch (x) {
    case 1:
    case 2:
        printf("Small");
        break;
    case 3:
        printf("Medium");
        break;
}

// Expression switch (C23+)
int result = switch (x) {
    case 1 => 10;
    case 2 => 20;
    default => 0;
};
```

---

## 2. Tầng 2: Type System

### 2.1. Kiểu Dữ Liệu Cơ Bản (Primitive Types)

```c
// Integer
int i = 42;
long long ll = 9223372036854775807LL;
short s = 32767;
unsigned int ui = 42;

// Character
char c = 'A';
signed char sc = -1;
unsigned char uc = 255;

// Floating point
float f = 3.14f;
double d = 3.14159;
long double ld = 3.14159L;

// Boolean (C99+)
_BBool bb = 1;  // Boolean (true/false)

// Void
void* ptr = NULL;

// Pointer
int* p = NULL;
int** pp = NULL;

// Array
int arr[10];
int arr2[] = {1, 2, 3};
```

#### Size & Limits

```c
#include <limits.h>
#include <stdint.h>

printf("%zu bytes\n", sizeof(int));
printf("INT_MAX: %d\n", INT_MAX);
printf("UINT_MAX: %u\n", UINT_MAX);

int64_t large_number = 9223372036854775807LL;
int32_t small_number = 2147483647;
uint8_t byte = 255;
```

---

### 2.2. Enum

```c
// Enum cơ bản
enum Color {
    RED,
    GREEN,
    BLUE
};

enum Color c = RED;

// Enum với giá trị cụ thể
enum Priority {
    LOW = 1,
    MEDIUM = 2,
    HIGH = 3
};

// Enum với type (C11+)
enum Color : unsigned char {
    RED = 0,
    GREEN = 1,
    BLUE = 2
};

// Anonymous enum
enum { MAX_CONNECTIONS = 100 };
```

---

### 2.3. Typedef

```c
// Typedef cho kiểu đơn giản
typedef unsigned int uint;
typedef char* string;

// Typedef cho pointer
typedef void* Handle;
typedef int (*Callback)(int, int);

// Typedef cho function pointer
typedef int (*CompareFunc)(const void*, const void*);
typedef void (*CleanupFunc)(void*);

// Typedef cho struct
typedef struct {
    int x;
    int y;
} Point;

// Anonymous struct với typedef
typedef struct {
    int id;
    char name[64];
} Employee;
```

---

### 2.4. Pointers

```c
int x = 10;
int* p = &x;      // Address of x
int value = *p;   // Dereference

// Pointer to pointer
int** pp = &p;

// Constant pointer
int* const p_const = &x;  // Cannot change pointer
const int* p_const2 = &x;  // Cannot change value through this
const int* const p_const3 = &x;  // Cannot change either

// void pointer
void* vp = &x;
int* pi = (int*)vp;

// NULL pointer
int* p = NULL;
if (p != NULL) {
    // Safe to use
}

// Function pointer
int (*func_ptr)(int, int) = &add;
int result = (*func_ptr)(1, 2);
```

---

### 2.5. Arrays

```c
// Array declaration
int arr[10];
int arr2[5] = {1, 2, 3, 4, 5};
int arr3[5] = {1, 2};  // Rest = 0

// Multi-dimensional array
int matrix[3][4];
int matrix2[2][3] = {{1, 2, 3}, {4, 5, 6}};

// Variable-length array (C99+)
int n = 10;
int arr[n];  // Runtime-sized

// Array as pointer
int* arr = malloc(10 * sizeof(int));
free(arr);

// sizeof với array
int arr[] = {1, 2, 3, 4, 5};
size_t n = sizeof(arr) / sizeof(arr[0]);

// Flexible array member (C99+)
struct buffer {
    size_t size;
    char data[];  // Must be last member
};
```

---

### 2.6. String Operations

```c
#include <string.h>
#include <stdio.h>

// String literals
char* s1 = "Hello";
char s2[] = "World";

// String concatenation
char dest[100];
strcpy(dest, "Hello");
strcat(dest, " World");

// String comparison
if (strcmp(s1, s2) == 0) {  // Equal }
if (strcmp(s1, s2) > 0) {    // s1 > s2 }

// String length
size_t len = strlen(s1);

// String copy
strcpy(dest, source);
strncpy(dest, source, n);  // Copy n characters

// String search
char* found = strchr(s1, 'o');
char* found2 = strstr(s1, "lo");

// Tokenize
char str[] = "one,two,three";
char* token = strtok(str, ",");
while (token != NULL) {
    printf("%s\n", token);
    token = strtok(NULL, ",");
}

// Formatted string
char buf[100];
sprintf(buf, "Value: %d", 42);
snprintf(buf, sizeof(buf), "Value: %d", 42);

// String to number
int i = atoi("42");
double d = atof("3.14");
long l = atol("123456");

// Better alternatives (C99+)
int i2 = (int)strtol("42", NULL, 10);
double d2 = strtod("3.14", NULL);
```

---

## 3. Tầng 3: OOP & Type Relationships

### 3.1. Struct

```c
// Struct cơ bản
struct Point {
    double x;
    double y;
};

struct Point p1 = {1.0, 2.0};
struct Point p2 = {.x = 1.0, .y = 2.0};  // C99+

// Typedef cho struct
typedef struct {
    int id;
    char name[64];
    double salary;
} Employee;

// Nested struct
struct Rectangle {
    struct Point top_left;
    struct Point bottom_right;
};

// Struct với function pointer
struct Callback {
    void (*on_event)(void*);
    void* data;
};

// Struct methods simulation
struct Counter {
    int value;
};

void counter_init(struct Counter* c) {
    c->value = 0;
}

void counter_inc(struct Counter* c) {
    c->value++;
}
```

---

### 3.2. Union

```c
// Union - share memory
union Data {
    int i;
    float f;
    char c;
};

union Data d;
d.i = 42;
printf("%f\n", d.f);  // Undefined behavior!

// Tagged union (discriminated union)
enum Type { TYPE_INT, TYPE_FLOAT, TYPE_STRING };

union Value {
    int i;
    float f;
    char* s;
};

struct Variant {
    enum Type type;
    union Value value;
};

// Function to access variant
int get_int(struct Variant* v) {
    if (v->type != TYPE_INT) {
        // Handle error
    }
    return v->value.i;
}
```

---

### 3.3. Bit Fields

```c
// Bit fields
struct Flags {
    unsigned int enabled : 1;
    unsigned int visible : 1;
    unsigned int mode : 4;  // 0-15
};

struct Flags f;
f.enabled = 1;
f.mode = 7;

// Bit operations thay thế
#define FLAG_ENABLED (1 << 0)
#define FLAG_VISIBLE (1 << 1)
#define FLAG_MODE_MASK (0xF << 2)

unsigned int flags = 0;
flags |= FLAG_ENABLED;
if (flags & FLAG_ENABLED) {
    // ...
}
```

---

### 3.4. Function Pointers

```c
// Function pointer type
typedef int (*CompareFunc)(const void*, const void*);

// Function pointer as parameter
void qsort(void* base, size_t nmemb, size_t size, CompareFunc comp);

// Implementation
int compare_int(const void* a, const void* b) {
    int ai = *(const int*)a;
    int bi = *(const int*)b;
    return ai - bi;
}

// Usage
int arr[] = {5, 2, 8, 1, 9};
qsort(arr, 5, sizeof(int), compare_int);

// Callback pattern
typedef void (*EventHandler)(int event_code, void* data);

struct EventEmitter {
    EventHandler handlers[10];
    void* user_data;
};

void emit_event(struct EventEmitter* emitter, int code) {
    if (emitter->handlers[code]) {
        emitter->handlers[code](code, emitter->user_data);
    }
}
```

---

## 4. Tầng 4: Memory Model

### 4.1. Memory Allocation

```c
#include <stdlib.h>

// malloc - allocate memory
int* arr = (int*)malloc(10 * sizeof(int));
if (arr == NULL) {
    // Handle allocation failure
}

// calloc - allocate and zero-initialize
int* arr2 = (int*)calloc(10, sizeof(int));  // All zeros

// realloc - resize allocation
int* arr3 = (int*)realloc(arr, 20 * sizeof(int));
if (arr3 == NULL) {
    free(arr);  // Keep old pointer
    arr = NULL;
}

// free - deallocate
free(arr);
arr = NULL;  // Good practice

// aligned_alloc (C17+)
#include <stdlib.h>
void* aligned = aligned_alloc(16, 64);  // 16-byte aligned, 64 bytes
free(aligned);

// Alloca (stack allocation - avoid in production)
#include <alloca.h>
int* temp = (int*)alloca(n * sizeof(int));
```

---

### 4.2. Pointer Arithmetic

```c
int arr[] = {10, 20, 30, 40, 50};
int* p = arr;

// Pointer arithmetic
p = p + 2;       // Move 2 * sizeof(int) bytes
int val = *p;    // 30

// Array indexing via pointer
for (int* q = arr; q < arr + 5; q++) {
    printf("%d ", *q);
}

// Pointer difference
ptrdiff_t diff = p - arr;  // Index difference

// void pointer arithmetic (need cast)
void* vp = arr;
int* ip = (int*)vp + 1;  // Move 4 bytes

// Comparing pointers
if (p < arr + 5) {
    // Within array bounds
}
```

---

### 4.3. Volatile & Const

```c
// volatile - may change unexpectedly (hardware registers)
volatile uint32_t* reg = (volatile uint32_t*)0x40021000;
*reg = 0xFF;  // Write to hardware register

// const - read-only
const int MAX = 100;
int const* p1 = &MAX;    // Cannot modify through p1
int* const p2 = &x;      // Cannot change p2
const int* const p3 = &MAX;  // Cannot change either

// const trong function parameters
void process_string(const char* str) {
    // str is read-only
}

// restrict (C99+) - no aliasing
void process_array(int* restrict a, int* restrict b, size_t n) {
    // a and b don't overlap
}
```

---

## 5. Tầng 5: Concurrency Model

### 5.1. POSIX Threads

```c
#include <pthread.h>
#include <stdio.h>

void* worker(void* arg) {
    int id = *(int*)arg;
    printf("Worker %d running\n", id);
    return NULL;
}

int main() {
    pthread_t threads[3];
    int ids[] = {0, 1, 2};

    for (int i = 0; i < 3; i++) {
        pthread_create(&threads[i], NULL, worker, &ids[i]);
    }

    for (int i = 0; i < 3; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}

// Compile: gcc -pthread main.c -o main
```

---

### 5.2. Mutex

```c
#include <pthread.h>

typedef struct {
    pthread_mutex_t mutex;
    int counter;
} Counter;

void counter_init(Counter* c) {
    pthread_mutex_init(&c->mutex, NULL);
    c->counter = 0;
}

void counter_inc(Counter* c) {
    pthread_mutex_lock(&c->mutex);
    c->counter++;
    pthread_mutex_unlock(&c->mutex);
}

void counter_destroy(Counter* c) {
    pthread_mutex_destroy(&c->mutex);
}

// Try lock
if (pthread_mutex_trylock(&c->mutex) == 0) {
    // Lock acquired
    pthread_mutex_unlock(&c->mutex);
}
```

---

### 5.3. Atomics

```c
#include <stdatomic.h>

// Atomic types (C11+)
atomic_int counter = ATOMIC_VAR_INIT(0);
_Atomic int flag = 0;

// Atomic operations
atomic_store(&counter, 10);
int val = atomic_load(&counter);
atomic_fetch_add(&counter, 1);
int old = atomic_fetch_sub(&counter, 1);

// Compare-and-swap
int expected = 10;
if (atomic_compare_exchange_strong(&counter, &expected, 20)) {
    // Successfully changed from 10 to 20
}

// Memory ordering
atomic_store_explicit(&flag, 1, memory_order_release);
atomic_load_explicit(&flag, memory_order_acquire);
```

---

## 6. Tầng 6: Paradigm

### 6.1. Procedural Programming

```c
// C là procedural language
// Functions operate on data

// Procedure không có return
void print_hello(void) {
    printf("Hello!\n");
}

// Procedure với output parameter
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```

---

### 6.2. Function Pointers as Callbacks

```c
// Callback pattern
typedef void (*Callback)(int);

void for_each(int* arr, size_t n, Callback cb) {
    for (size_t i = 0; i < n; i++) {
        cb(arr[i]);
    }
}

void print_num(int n) {
    printf("%d ", n);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    for_each(arr, 5, print_num);
}

// qsort callback
int compare_ints(const void* a, const void* b) {
    int ai = *(const int*)a;
    int bi = *(const int*)b;
    return (ai > bi) - (ai < bi);  // Avoid overflow
}

qsort(arr, n, sizeof(int), compare_ints);
```

---

## 7. Tầng 7: Error Handling

### 7.1. Error Return Codes

```c
#include <errno.h>

// Return error code
int divide(int a, int b, int* result) {
    if (b == 0) {
        errno = EINVAL;
        return -1;
    }
    *result = a / b;
    return 0;
}

// Sử dụng
int result;
if (divide(10, 0, &result) != 0) {
    perror("divide failed");
}

// Custom error codes
enum ErrorCode {
    SUCCESS = 0,
    ERR_INVALID_INPUT = 1,
    ERR_OUT_OF_MEMORY = 2,
    ERR_NOT_FOUND = 3
};
```

---

### 7.2. setjmp/longjmp

```c
#include <setjmp.h>

static jmp_buf jump_buffer;

void nested_function(void) {
    // Jump back to setjmp location
    longjmp(jump_buffer, 1);
}

void function_with_error(void) {
    if (setjmp(jump_buffer) == 0) {
        // Normal execution
        nested_function();
    } else {
        // Returned via longjmp
        printf("Caught error!\n");
    }
}
```

---

### 7.3. Signal Handling

```c
#include <signal.h>
#include <stdio.h>

void signal_handler(int signum) {
    printf("Received signal %d\n", signum);
}

int main() {
    struct sigaction sa;
    sa.sa_handler = signal_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;

    sigaction(SIGINT, &sa, NULL);

    // Wait for signal
    pause();
}
```

---

## 8. Tầng 8: Module & Organization

### 8.1. Include

```c
// System header
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Local header
#include "myheader.h"
#include "subdir/header.h"

// Macro include guard
#ifndef MYHEADER_H
#define MYHEADER_H
// ... declarations
#endif

// #pragma once (supported by most compilers)
```

---

### 8.2. Header Files

```c
// myheader.h

#ifndef MYHEADER_H
#define MYHEADER_H

// Function declarations
int calculate(int x, int y);
void process_array(int* arr, size_t n);

// Struct declaration (incomplete)
struct Config;
struct Config* config_create(void);
void config_destroy(struct Config* cfg);

// Inline function (C99+)
static inline int max(int a, int b) {
    return a > b ? a : b;
}

#endif
```

---

### 8.3. Static/Extern

```c
// Static - internal linkage
static int internal_counter = 0;
static void internal_function(void) { }

// Extern - external linkage (default for functions)
extern int external_var;
extern void external_function(void);

// Definition
int external_var = 42;
void external_function(void) { }

// Static trong function - persistent
void counter(void) {
    static int count = 0;
    printf("Count: %d\n", ++count);
}
```

---

## 9. Tầng 9: I/O & Networking

### 9.1. Standard I/O

```c
#include <stdio.h>

// printf/scanf
printf("Hello %s, age: %d\n", name, age);
scanf("%d", &age);

// Format specifiers
// %d - int, %u - unsigned
// %ld - long, %lld - long long
// %f - float, %lf - double
// %s - string, %c - char
// %p - pointer, %x - hex

// File streams
FILE* fp = fopen("file.txt", "r");
if (fp == NULL) {
    perror("fopen failed");
    return 1;
}

char buffer[256];
while (fgets(buffer, sizeof(buffer), fp) != NULL) {
    fputs(buffer, stdout);
}

fclose(fp);

// String I/O
char buf[100];
sprintf(buf, "Value: %d", 42);
sscanf(buf, "Value: %d", &value);
```

---

### 9.2. File I/O

```c
#include <stdio.h>

// Binary I/O
struct Data {
    int id;
    char name[32];
};

struct Data d = {1, "test"};
FILE* fp = fopen("data.bin", "wb");
fwrite(&d, sizeof(d), 1, fp);
fclose(fp);

FILE* fp2 = fopen("data.bin", "rb");
fread(&d, sizeof(d), 1, fp2);
fclose(fp2);

// Position
fseek(fp, 0, SEEK_SET);   // Beginning
fseek(fp, 0, SEEK_END);   // End
fseek(fp, offset, SEEK_CUR);  // Current
long pos = ftell(fp);

// Low-level I/O (POSIX)
#include <fcntl.h>
#include <unistd.h>

int fd = open("file.txt", O_RDONLY);
char buf[256];
read(fd, buf, sizeof(buf));
close(fd);
```

---

### 9.3. Socket Programming

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

// TCP Server
int server_fd = socket(AF_INET, SOCK_STREAM, 0);
struct sockaddr_in addr = {
    .sin_family = AF_INET,
    .sin_port = htons(8080),
    .sin_addr.s_addr = INADDR_ANY
};

bind(server_fd, (struct sockaddr*)&addr, sizeof(addr));
listen(server_fd, 10);

int client_fd = accept(server_fd, NULL, NULL);
// Read/write...

// TCP Client
int client_fd = socket(AF_INET, SOCK_STREAM, 0);
struct sockaddr_in server_addr = {
    .sin_family = AF_INET,
    .sin_port = htons(8080)
};
inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr);

connect(client_fd, (struct sockaddr*)&server_addr, sizeof(server_addr));
// Read/write...
```

---

## 10. Tầng 10: Data & Serialization

### 10.1. JSON

```c
// C không có built-in JSON
// Thường dùng: cJSON, Jansson, json-c

// cJSON example
#include "cJSON.h"

cJSON* root = cJSON_CreateObject();
cJSON_AddStringToObject(root, "name", "John");
cJSON_AddNumberToObject(root, "age", 30);
cJSON_AddBoolToObject(root, "active", 1);

char* json_str = cJSON_Print(root);
printf("%s\n", json_str);

cJSON_Delete(root);

// Parse JSON
cJSON* parsed = cJSON_Parse(json_str);
cJSON* name = cJSON_GetObjectItem(parsed, "name");
printf("Name: %s\n", name->valuestring);
cJSON_Delete(parsed);
```

---

### 10.2. Date & Time

```c
#include <time.h>
#include <stdio.h>

// time_t
time_t now = time(NULL);
printf("Seconds since epoch: %ld\n", now);

// struct tm
struct tm* tm_info = localtime(&now);
printf("%04d-%02d-%02d %02d:%02d:%02d\n",
    tm_info->tm_year + 1900,
    tm_info->tm_mon + 1,
    tm_info->tm_mday,
    tm_info->tm_hour,
    tm_info->tm_min,
    tm_info->tm_sec);

// Parse time
struct tm tm_parsed = {0};
strptime("2024-01-15 10:30:00", "%Y-%m-%d %H:%M:%S", &tm_parsed);
time_t parsed = mktime(&tm_parsed);

// Format time
char buf[100];
strftime(buf, sizeof(buf), "%Y-%m-%d %H:%M:%S", tm_info);

// Measure time
clock_t start = clock();
// ... do work
clock_t end = clock();
printf("Time: %f seconds\n", (double)(end - start) / CLOCKS_PER_SEC);
```

---

### 10.3. Regular Expression

```c
#include <regex.h>
#include <stdio.h>

regex_t regex;
int ret;

// Compile regex
ret = regcomp(&regex, "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", 0);
if (ret) {
    char errbuf[100];
    regerror(ret, &regex, errbuf, sizeof(errbuf));
    fprintf(stderr, "Regex error: %s\n", errbuf);
}

// Match
const char* test = "test@example.com";
ret = regexec(&regex, test, 0, NULL, 0);
if (!ret) {
    printf("Match found!\n");
} else if (ret == REG_NOMATCH) {
    printf("No match\n");
}

regfree(&regex);

// Match with groups
regmatch_t matches[2];
ret = regexec(&regex, test, 2, matches, 0);
if (!ret) {
    printf("Match: %.*s\n", matches[0].rm_eo - matches[0].rm_so, test + matches[0].rm_so);
}
```

---

## 11. Tầng 11: Development Practices

### 11.1. Testing

```c
// Unity Test Framework
#include "unity.h"

void setUp(void) {
    // Run before each test
}

void tearDown(void) {
    // Run after each test
}

void test_calculator_add(void) {
    TEST_ASSERT_EQUAL(5, add(2, 3));
}

void test_array_sort(void) {
    int arr[] = {3, 1, 2};
    sort(arr, 3);
    TEST_ASSERT_EQUAL_INT_ARRAY((int[]){1, 2, 3}, arr, 3);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_calculator_add);
    RUN_TEST(test_array_sort);
    return UNITY_END();
}

// Check library
#include <assert.h>
assert(x > 0);
```

---

### 11.2. Logging

```c
// Simple logging macros
#include <stdio.h>
#include <time.h>

#define LOG_LEVEL 2
#define LOG_DEBUG 0
#define LOG_INFO  1
#define LOG_ERROR 2

#define LOG(fmt, ...) \
    do { \
        if (LOG_LEVEL <= LOG_INFO) \
            printf("[INFO] " fmt "\n", ##__VA_ARGS__); \
    } while(0)

#define LOG_ERROR(fmt, ...) \
    do { \
        fprintf(stderr, "[ERROR] " fmt "\n", ##__VA_ARGS__); \
    } while(0)

// syslog (POSIX)
#include <syslog.h>

openlog("myapp", LOG_PID, LOG_USER);
syslog(LOG_INFO, "Application started");
syslog(LOG_ERROR, "Error: %m");
closelog();
```

---

### 11.3. Build Systems

```bash
# Makefile
CC = gcc
CFLAGS = -Wall -Wextra -O2
TARGET = main
SRCS = main.c foo.c bar.c
OBJS = $(SRCS:.c=.o)

$(TARGET): $(OBJS)
    $(CC) $(OBJS) -o $(TARGET)

%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $>

clean:
    rm -f $(OBJS) $(TARGET)

# CMake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.10)
project(MyApp C)

set(CMAKE_C_STANDARD 11)

add_executable(myapp main.c foo.c)

target_include_directories(myapp PRIVATE ${CMAKE_SOURCE_DIR}/include)

# Autotools
# configure.ac, Makefile.am
autoreconf -i
./configure
make
```

---

## 12. Tầng 12: Advanced Concepts

### 12.1. Preprocessor

```c
// Macro với arguments
#define MAX(a, b) ((a) > (b) ? (a) : (b))

// Macro với statements
#define SWAP(a, b) do { \
    typeof(a) _tmp = a; \
    a = b; \
    b = _tmp; \
} while(0)

// Variadic macro
#define LOG(fmt, ...) fprintf(stderr, "[LOG] " fmt "\n", ##__VA_ARGS__)

// Stringification
#define STRINGIFY(x) #x
#define TOSTRING(x) STRINGIFY(x)

// Token concatenation
#define CONCAT(a, b) a##b

// Conditional compilation
#ifdef DEBUG
#define DEBUG_PRINT(fmt, ...) fprintf(stderr, "DEBUG: " fmt "\n", ##__VA_ARGS__)
#else
#define DEBUG_PRINT(...)
#endif

// __FILE__, __LINE__, __func__
printf("Error at %s:%d in %s\n", __FILE__, __LINE__, __func__);
```

---

### 12.2. Variadic Functions

```c
#include <stdarg.h>

// Variadic function
int sum(int count, ...) {
    va_list args;
    va_start(args, count);

    int total = 0;
    for (int i = 0; i < count; i++) {
        total += va_arg(args, int);
    }

    va_end(args);
    return total;
}

// Sử dụng
int result = sum(4, 1, 2, 3, 4);

// printf implementation pattern
int my_printf(const char* fmt, ...) {
    va_list args;
    va_start(args, fmt);
    // Parse format string and process args
    va_end(args);
}
```

---

### 12.3. Inline Assembly

```c
// GCC inline assembly
#include <stdio.h>

int main() {
    int result;

    // Simple inline asm
    __asm__ ("movl $5, %eax" : "=r"(result));
    printf("Result: %d\n", result);

    // With inputs
    int a = 10, b = 20, sum;
    __asm__ ("addl %1, %0" : "=r"(sum) : "r"(a), "0"(b));
    printf("Sum: %d\n", sum);

    return 0;
}
```

---

## 13. Tầng 13: Memory Layout

### 13.1. Struct Layout

```c
struct Simple {
    char a;      // Offset 0
                 // Padding 1-2
    short b;     // Offset 2
                 // Padding 4
    int c;       // Offset 4
    char d;      // Offset 8
                 // Padding 9-11
};
// Total: 12 bytes, alignof = 4

// Reordered (better)
struct Optimized {
    int c;       // Offset 0
    short b;     // Offset 4
    char a;      // Offset 6
    char d;      // Offset 7
};
// Total: 8 bytes
```

---

### 13.2. Memory Alignment

```c
#include <stdalign.h>

// alignas (C11+)
struct alignas(16) Aligned {
    int a;
    double b;
};

// alignof
static_assert(alignof(double) == 8);

// alignas với struct members
struct Packed {
    int a;
    int b __attribute__((aligned(16)));
};

// Manual alignment
#include <stdalign.h>
void* aligned_alloc(size_t alignment, size_t size);
void* ptr = aligned_alloc(16, 64);
free(ptr);
```

---

### 13.3. Padding & Packing

```c
// #pragma pack
#pragma pack(push, 1)
struct Packed {
    char a;      // Offset 0
    int b;      // Offset 1
    short c;    // Offset 5
};
#pragma pack(pop)
// Total: 7 bytes

// __attribute__((packed)) (GCC/Clang)
struct Packed2 {
    char a;
    int b __attribute__((packed));
    short c;
};

// Bit fields alignment
struct Flags {
    unsigned int a : 3;  // 3 bits
    unsigned int b : 5;  // 5 bits
};
```

---

## 14. Tầng 14: Compilation Model

### 14.1. Compilation Pipeline

```bash
# Preprocess
gcc -E main.c -o main.i

# Compile to assembly
gcc -S main.c -o main.s
gcc -S main.c -o main.o

# Compile to object
gcc -c main.c -o main.o

# Link
gcc main.o other.o -o executable

# Full pipeline
gcc -std=c11 -Wall -Wextra -g -O2 main.c -o main
```

---

### 14.2. Object Files

```bash
# View symbols
nm main.o
nm -D lib.so

# View sections
readelf -S main.o
objdump -h main.o

# Disassemble
objdump -d main.o
```

---

## 15. Tầng 15: Linking Model

### 15.1. Static Linking

```bash
# Create static library
ar rcs libmylib.a obj1.o obj2.o

# Link
gcc main.o -L. -lmylib -o main

# Link order matters!
gcc main.o liba.a libb.a
```

---

### 15.2. Dynamic Linking

```bash
# Create shared library
gcc -fPIC -shared mylib.c -o libmylib.so

# Compile with shared library
gcc main.c -L. -lmylib -o main

# Runtime library path
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.

# ldd - check dependencies
ldd ./main
```

---

### 15.3. Symbol Resolution

```c
// dlopen API
#include <dlfcn.h>

void* handle = dlopen("./libmylib.so", RTLD_LAZY);
if (!handle) {
    fprintf(stderr, "dlopen error: %s\n", dlerror());
    return;
}

typedef int (*AddFunc)(int, int);
AddFunc add = (AddFunc)dlsym(handle, "add");

int result = add(1, 2);
dlclose(handle);
```

---

## 16. Tầng 16: Runtime

### 16.1. Stack Frame

```c
// Stack grows down, heap grows up
// Stack frame: return address, saved registers, local variables

// Alloca - stack allocation
#include <alloca.h>
void* ptr = alloca(size);  // Freed automatically
```

---

### 16.2. Call Stack

```c
// Backtrace (GLIBC)
#include <execinfo.h>

void* buffer[100];
int n = backtrace(buffer, 100);
char** strings = backtrace_symbols(buffer, n);

for (int i = 0; i < n; i++) {
    printf("%s\n", strings[i]);
}
free(strings);

// Print to stderr
backtrace_symbols_fd(buffer, n, 2);
```

---

### 16.3. Memory Model

```c
// .text - code
// .data - initialized global/static
// .bss - uninitialized global/static (zero)
// .heap - dynamic allocation
// .stack - local variables
// .rodata - read-only data (string literals, const)

// Segfault handler
#include <signal.h>

void segfault_handler(int sig) {
    printf("Segmentation fault!\n");
    exit(1);
}

signal(SIGSEGV, segfault_handler);
```

---

## 17. Tầng 17: Language Design Patterns

### 17.1. Opaque Pointers

```c
// header.h
typedef struct MyContext MyContext;  // Incomplete type

MyContext* context_create(void);
void context_destroy(MyContext* ctx);
int context_process(MyContext* ctx, int data);

// implementation.c
struct MyContext {
    int state;
    void* internal;
};

MyContext* context_create(void) {
    MyContext* ctx = malloc(sizeof(MyContext));
    ctx->state = 0;
    return ctx;
}
```

---

### 17.2. Handler Pattern

```c
// Resource handle pattern
typedef struct {
    int fd;
    void* buffer;
    size_t size;
} FileHandle;

FileHandle* open_file(const char* path) {
    FileHandle* h = malloc(sizeof(FileHandle));
    h->fd = open(path, O_RDONLY);
    // ...
    return h;
}

void close_file(FileHandle* h) {
    if (h) {
        close(h->fd);
        free(h->buffer);
        free(h);
    }
}
```

---

## 18. Tầng 18: Standard Library

### 18.1. Standard Headers

```c
// C Standard Library
#include <stdio.h>      // I/O
#include <stdlib.h>     // Memory, process
#include <string.h>     // String functions
#include <ctype.h>      // Character functions
#include <math.h>       // Math functions
#include <time.h>       // Time/date
#include <limits.h>     // Type limits
#include <stdint.h>     // Fixed-width integers
#include <stdbool.h>    // bool (C99)
#include <stdarg.h>     // Variadic functions
#include <stddef.h>     // Common definitions

// POSIX
#include <pthread.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
```

---

### 18.2. libc Functions

```c
// Memory
void* malloc(size_t);
void* calloc(size_t, size_t);
void* realloc(void*, size_t);
void free(void*);

// String
size_t strlen(const char*);
char* strcpy(char*, const char*);
char* strcat(char*, const char*);
int strcmp(const char*, const char*);
char* strchr(const char*, int);
char* strstr(const char*, const char*);

// I/O
int printf(const char*, ...);
int scanf(const char*, ...);
FILE* fopen(const char*, const char*);
size_t fread(void*, size_t, size_t, FILE*);
size_t fwrite(const void*, size_t, size_t, FILE*);
int fclose(FILE*);
```

---

## 19. Tầng 19: Ecosystem

### 19.1. Libraries

```c
// Popular C libraries:
// - GLib: Data structures, utilities
// - cURL: HTTP/FTP
// - OpenSSL: Cryptography
// - SQLite: Database
// - Jansson/cJSON: JSON
// - Zlib: Compression
// - ncurses: Terminal UI
// - SDL2: Graphics/Games
// - Boost (C++): nhiều utilities

// GLib example
#include <glib.h>

GHashTable* hash = g_hash_table_new(g_str_hash, g_str_equal);
g_hash_table_insert(hash, "key", "value");
gchar* val = g_hash_table_lookup(hash, "key");
g_hash_table_destroy(hash);
```

---

### 19.2. Tools

```bash
# Build
gcc, clang, make, cmake, meson, ninja

# Debug
gdb, lldb, valgrind, address sanitizer

# Static analysis
gcc -fanalyzer
clang --analyze
cppcheck
splint

# Format
clang-format

# Dependencies
pkg-config --cflags --libs glib-2.0
```

---

## 20. Tầng 20: Toolchain

### 20.1. Compiler

```bash
# GCC
gcc -std=c11 -Wall -Wextra -O2 -g -o main main.c

# Clang
clang -std=c11 -Wall -Wextra -O2 -g -o main main.c

# MSVC
cl /std:c11 /W4 /O2 main.c

# Flags
# -std=c89/c99/c11/c17/c23
# -Wall -Wextra -Werror -Wpedantic
# -O0/-O1/-O2/-O3/-Os/-Ofast
# -g -ggdb
# -fPIC
# -fsanitize=address
```

---

### 20.2. Debugger

```bash
# GDB
gdb ./main
# Commands: run, break, next, step, print, bt, info locals, continue

# Valgrind
valgrind --leak-check=full ./main
valgrind --tool=callgrind ./main

# AddressSanitizer
gcc -fsanitize=address -g main.c -o main
./main

# GDB with TUI
gdb -tui ./main
```

---

### 20.3. Static Analysis

```bash
# GCC analyzer (GCC 13+)
gcc -fanalyzer main.c

# Clang static analyzer
scan-build gcc -c main.c

# cppcheck
cppcheck --enable=all --std=c11 main.c

# splint
splint +bounds main.c
```

---

## Tóm Tắt

### Ưu Điểm C
- **Hiệu năng cao**: Native code, tối ưu hóa sát phần cứng
- **Kiểm soát bộ nhớ**: Manual memory management
- **Portability**: ISO standard, compile anywhere
- **Simple**: Ít abstractions, dễ hiểu underlying behavior
- **Wide support**: Embedded systems, OS, drivers

### Nhược Điểm C
- **No safety**: Buffer overflow, memory leaks dễ xảy ra
- **No OOP**: Không có class, inheritance
- **No built-in concurrency**: Phải dùng pthreads manually
- **Weak type checking**: Có thể cast bất kỳ đâu
- **Manual memory management**: malloc/free dễ gây leak

### C Standards Timeline
- **C89/C90**: ANSI/ISO standard đầu tiên
- **C99**: Variable-length arrays, designated initializers, // comments
- **C11**: Threads, Unicode, generic selections, atomic operations
- **C17**: Bug fixes, no new features
- **C23**: stdckdint.h, constexpr, improved Unicode, attributes
