# Java Syntax Reference

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
   - [3.1 Class & Object](#31-class--object)
   - [3.2 Kế Thừa & Đa Hình](#32-kế-thừa--đa-hình)
   - [3.3 Interface](#33-interface)
   - [3.4 Visibility](#34-visibility)
4. [Tầng 4: Memory Model](#tầng-4-memory-model)
   - [4.1 Memory Management](#41-memory-management)
   - [4.2 Garbage Collection](#42-garbage-collection)
   - [4.3 Reference Types](#43-reference-types)
5. [Tầng 5: Concurrency Model](#tầng-5-concurrency-model)
   - [5.1 Thread](#51-thread)
   - [5.2 Executor Service](#52-executor-service)
   - [5.3 Synchronization](#53-synchronization)
   - [5.4 CompletableFuture](#54-completablefuture)
6. [Tầng 6: Paradigm](#tầng-6-paradigm)
   - [6.1 Functional Programming](#61-functional-programming)
   - [6.2 Lambda Expressions](#62-lambda-expressions)
   - [6.3 Stream API](#63-stream-api)
7. [Tầng 7: Error Handling](#tầng-7-error-handling)
   - [7.1 Exception](#71-exception)
   - [7.2 Try-with-Resources](#72-try-with-resources)
   - [7.3 Optional](#73-optional)
8. [Tầng 8: Module & Organization](#tầng-8-module--organization)
   - [8.1 Package](#81-package)
   - [8.2 Import](#82-import)
   - [8.3 Module System](#83-module-system-jdk-9)
9. [Tầng 9: I/O & Networking](#tầng-9-io--networking)
   - [9.1 HTTP & Networking](#91-http--networking)
   - [9.2 File I/O](#92-file-io)
   - [9.3 Stream I/O](#93-stream-io)
10. [Tầng 10: Data & Serialization](#tầng-10-data--serialization)
    - [10.1 JSON](#101-json)
    - [10.2 Date & Time](#102-date--time)
    - [10.3 Regular Expression](#103-regular-expression)
11. [Tầng 11: Development Practices](#tầng-11-development-practices)
    - [11.1 Testing](#111-testing)
    - [11.2 Logging](#112-logging)
    - [11.3 Build & Package Management](#113-build--package-management)
12. [Tầng 12: Advanced Concepts](#tầng-12-advanced-concepts)
    - [12.1 Records (JDK 14+)](#121-records-jdk-14)
    - [12.2 Sealed Classes (JDK 17+)](#122-sealed-classes-jdk-17)
    - [12.3 Pattern Matching](#123-pattern-matching)
13. [Tầng 13: Memory Layout](#tầng-13-memory-layout)
    - [13.1 Object Layout](#131-object-layout)
    - [13.2 Memory Alignment](#132-memory-alignment)
14. [Tầng 14: Compilation Model](#tầng-14-compilation-model)
    - [14.1 Compilation](#141-compilation)
    - [14.2 Bytecode](#142-bytecode)
    - [14.3 JIT Compiler](#143-jit-compiler)
15. [Tầng 15: Linking Model](#tầng-15-linking-model)
    - [15.1 Class Loading](#151-class-loading)
    - [15.2 Dynamic Loading](#152-dynamic-loading)
16. [Tầng 16: Runtime](#tầng-16-runtime)
    - [16.1 JVM](#161-jvm)
    - [16.2 Stack & Heap](#162-stack--heap)
    - [16.3 Virtual Method Dispatch](#163-virtual-method-dispatch)
17. [Tầng 17: Language Design Patterns](#tầng-17-language-design-patterns)
    - [17.1 Builder Pattern](#171-builder-pattern)
    - [17.2 Factory Pattern](#172-factory-pattern)
    - [17.3 Singleton](#173-singleton)
18. [Tầng 18: Standard Library](#tầng-18-standard-library)
    - [18.1 Collections](#181-collections)
    - [18.2 Utilities](#182-utilities)
    - [18.3 I/O & System](#183-io--system)
19. [Tầng 19: Ecosystem](#tầng-19-ecosystem)
    - [19.1 Frameworks](#191-frameworks)
    - [19.2 Libraries](#192-libraries)
    - [19.3 Build Tools](#193-build-tools)
20. [Tầng 20: Toolchain](#tầng-20-toolchain)
    - [20.1 Compiler](#201-compiler)
    - [20.2 Debugging](#202-debugging)
    - [20.3 Code Quality](#203-code-quality)

---

## 0. Phân Loại Ngôn Ngữ

### Chạy File Java

```bash
# Compile và chạy
javac Main.java && java Main

# Với Maven
mvn clean compile
mvn exec:java -Dexec.mainClass="com.example.Main"

# Với Gradle
gradle run

# Java versions
java -version           # Kiểm tra phiên bản
javac --source 17      # Compile với Java 17
java --enable-preview   # Preview features
```

### Đặc điểm Java

- **Typing**: Static typing, Strong typing
- **Paradigm**: Object-Oriented, (Functional từ Java 8)
- **Execution**: Compiled to Bytecode, Interpreted/JIT by JVM
- **Memory Safety**: Automatic với Garbage Collection
- **Use Cases**: Enterprise applications, Android, Web backends, Big data

---

## 1. Tầng 1: Syntax & Semantics

### 1.1. Khai Báo Biến (Variable Declaration)

#### Mutable - Biến thường

```java
// Khai báo biến với type inference (Java 10+)
var x = 10;
var name = "Java";
var isActive = true;
var prices = new ArrayList<Double>();

// Explicit type
int x = 10;
String name = "Java";
boolean isActive = true;
List<Double> prices = Arrays.asList(1.5, 2.0, 3.5);

// Mutable
int counter = 0;
counter += 1;

// Reference
int[] arr = {1, 2, 3};
int[] arrRef = arr;  // arrRef trỏ đến cùng array
```

#### Immutable - Hằng số

```java
// final (compile-time constant cho primitives và String)
final int MAX_SIZE = 100;
final double PI = 3.14159;
final String APP_NAME = "MyApp";

// static final (class-level constant)
public static final int DEFAULT_PORT = 8080;

// enum
enum Priority {
    LOW, MEDIUM, HIGH
}
```

#### Global Variable

```java
// Static field (class-level)
public class Config {
    public static final String VERSION = "1.0.0";
    private static int instanceCount = 0;
}

// Instance field
public class Person {
    private String name;  // Instance variable
}
```

---

### 1.2. Khai Báo Hàm (Method Declaration)

#### Method cơ bản

```java
// Method không có return
public void greet() {
    System.out.println("Hello!");
}

// Method có return
public int add(int a, int b) {
    return a + b;
}

// Method với varargs
public int sum(int... numbers) {
    int total = 0;
    for (int n : numbers) {
        total += n;
    }
    return total;
}

// Method overloading
public int add(int a, int b) { return a + b; }
public double add(double a, double b) { return a + b; }
public String add(String a, String b) { return a + b; }
```

#### Parameters

```java
// Pass by value (primitives) / Pass by value of reference (objects)
public void setValue(int x) {
    x = 10;  // Chỉ thay đổi bản sao cục bộ
}

public void setName(Person p, String name) {
    p.setName(name);  // Thay đổi object được tham chiếu
    p = new Person("new");  // Không ảnh hưởng đến caller
}

// Default parameters - Java không có
// Dùng method overloading
public void configure() {
    configure(8080, false);
}

public void configure(int port) {
    configure(port, false);
}

public void configure(int port, boolean ssl) {
    // implementation
}
```

---

### 1.3. Vòng Lặp (Loops)

#### For loop

```java
// C-style for
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}

// Enhanced for (for-each)
int[] nums = {1, 2, 3, 4, 5};
for (int n : nums) {
    System.out.println(n);
}

// For với List
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
for (String name : names) {
    System.out.println(name);
}

// For với iterator
for (Iterator<String> it = names.iterator(); it.hasNext(); ) {
    String name = it.next();
}
```

#### While loop

```java
int count = 0;
while (count < 5) {
    System.out.println(count++);
}

// Do-while
do {
    System.out.println(count--);
} while (count > 0);

// Infinite loop
while (true) {
    // ...
}

// Stream-based (Java 8+)
names.forEach(System.out::println);
```

---

### 1.4. Điều Kiện (Conditionals)

#### If-else

```java
int x = 10;

if (x > 0) {
    System.out.println("Positive");
} else if (x < 0) {
    System.out.println("Negative");
} else {
    System.out.println("Zero");
}

// Ternary operator
String result = (x > 0) ? "Positive" : "Non-positive";
```

#### Switch-case

```java
int day = 3;
switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    case 3:
        System.out.println("Wednesday");
        break;
    default:
        System.out.println("Unknown");
}

// Switch expression (Java 14+)
String dayName = switch (day) {
    case 1 -> "Monday";
    case 2 -> "Tuesday";
    case 3 -> "Wednesday";
    default -> "Unknown";
};

// Switch với multiple values
switch (month) {
    case JANUARY, FEBRUARY, MARCH -> System.out.println("Q1");
    case APRIL, MAY, JUNE -> System.out.println("Q2");
    default -> System.out.println("Other");
}
```

---

## 2. Tầng 2: Type System

### 2.1. Kiểu Dữ Liệu Cơ Bản (Primitive Types)

```java
// Integer
int i = 42;
long l = 9223372036854775807L;
short s = 32767;
byte b = 127;

// Floating point
float f = 3.14f;
double d = 3.14159;

// Character
char c = 'A';

// Boolean
boolean flag = true;

// String (object, không phải primitive)
String str = "Hello";

// Wrapper classes (boxed types)
Integer boxedInt = 42;  // Auto-boxing
int unboxed = boxedInt; // Auto-unboxing

// Type inference (Java 10+)
var number = 42;  // int
var text = "Hello";  // String
```

#### Size & Limits

```java
System.out.println(Integer.MAX_VALUE);  // 2147483647
System.out.println(Integer.MIN_VALUE);   // -2147483648
System.out.println(Integer.SIZE);        // 32 bits
System.out.println(Double.MAX_VALUE);    // 1.7976931348623157E308
```

---

### 2.2. Enum

```java
// Enum cơ bản
enum Color {
    RED, GREEN, BLUE
}

Color c = Color.RED;

// Enum với giá trị
enum Priority {
    LOW(1), MEDIUM(2), HIGH(3);

    private final int value;
    Priority(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}

// Enum với methods
enum Status {
    PENDING("Pending"),
    APPROVED("Approved"),
    REJECTED("Rejected");

    private final String description;

    Status(String description) {
        this.description = description;
    }

    public String getDescription() {
        return description;
    }
}

// Enum with abstract method
enum Operation {
    PLUS {
        public int apply(int a, int b) { return a + b; }
    },
    MINUS {
        public int apply(int a, int b) { return a - b; }
    };

    public abstract int apply(int a, int b);
}
```

---

### 2.3. Nullable Types

```java
// Reference types có thể null
String name = null;

// Wrapper classes có thể null
Integer value = null;

// Primitive không thể null (dùng wrapper nếu cần)
int num = 0;
Integer numWrapper = null;

// Optional (Java 8+)
import java.util.Optional;

Optional<String> optional = Optional.of("value");
Optional<String> empty = Optional.empty();
Optional<String> fromNullable = Optional.ofNullable(getValue());

// Sử dụng Optional
if (optional.isPresent()) {
    System.out.println(optional.get());
}

// Hoặc
String result = optional.orElse("default");
String result2 = optional.orElseGet(() -> computeDefault());
```

---

### 2.4. Null Safety

```java
// Null check thủ công
String name = getName();
if (name != null) {
    System.out.println(name.length());
}

// Null-safe operators (Java 14+)
String name = getName();
int len = name != null ? name.length() : 0;

// Optional (Java 8+)
Optional<String> name = Optional.ofNullable(getName());
int len = name.map(String::length).orElse(0);

// Objects.requireNonNull
public void setName(String name) {
    this.name = Objects.requireNonNull(name, "Name cannot be null");
}

// @NonNull annotations (static analysis)
import javax.annotation.Nonnull;

public void process(@Nonnull String input) {
    // IDE sẽ cảnh báo nếu null được truyền vào
}

// NullPointerException với message (Java 15+)
throw new NullPointerException("name is null");
```

---

### 2.5. Generics

```java
// Generic class
public class Box<T> {
    private T content;

    public void set(T content) {
        this.content = content;
    }

    public T get() {
        return content;
    }
}

Box<String> stringBox = new Box<>();
stringBox.set("Hello");
String value = stringBox.get();

// Generic method
public <T> T identity(T value) {
    return value;
}

String s = identity("Hello");
Integer i = identity(42);

// Bounded type parameters
public <T extends Number> T max(T a, T b) {
    return a.doubleValue() > b.doubleValue() ? a : b;
}

// Multiple bounds
public <T extends Comparable<T> & Serializable> void process(T item) {
    // ...
}

// Wildcards
public void printList(List<?> list) {
    for (Object item : list) {
        System.out.println(item);
    }
}

public void addNumbers(List<? super Integer> list) {
    list.add(42);  // OK với super
}

public void printIntegers(List<? extends Number> list) {
    // Chỉ đọc, không thêm
    Number n = list.get(0);
}
```

---

### 2.6. Collection Operations

```java
import java.util.*;
import java.util.stream.*;

List<Integer> nums = Arrays.asList(5, 2, 8, 1, 9);

// Map/Transform
List<Integer> doubled = nums.stream()
    .map(n -> n * 2)
    .collect(Collectors.toList());

// Filter
List<Integer> evens = nums.stream()
    .filter(n -> n % 2 == 0)
    .collect(Collectors.toList());

// Reduce
int sum = nums.stream()
    .reduce(0, Integer::sum);

// Reduce với identity
Optional<Integer> max = nums.stream()
    .reduce(Integer::max);

// Sort
List<Integer> sorted = nums.stream()
    .sorted()
    .collect(Collectors.toList());

// Find
Optional<Integer> first = nums.stream()
    .filter(n -> n > 5)
    .findFirst();

boolean anyMatch = nums.stream().anyMatch(n -> n > 5);
boolean allMatch = nums.stream().allMatch(n -> n > 0);
boolean noneMatch = nums.stream().noneMatch(n -> n < 0);

// Collect
Set<Integer> set = nums.stream().collect(Collectors.toSet());
Map<String, Integer> map = nums.stream()
    .collect(Collectors.toMap(n -> "num" + n, n -> n));

// Chaining
String result = nums.stream()
    .filter(n -> n > 0)
    .map(n -> n * 2)
    .limit(5)
    .map(String::valueOf)
    .collect(Collectors.joining(", "));
```

---

### 2.7. String Operations

```java
// Khởi tạo
String s1 = "Hello";
String s2 = new String("World");
String s3 = String.join(" ", "Hello", "World");

// Concatenation
String full = s1 + " " + s2;
full += "!";

// String.format
String msg = String.format("Name: %s, Age: %d", name, age);

// StringBuilder (mutable, hiệu quả cho nhiều concatenation)
StringBuilder sb = new StringBuilder();
sb.append("Hello");
sb.append(" ");
sb.append("World");
String result = sb.toString();

// Formatted string (Java 15+)
String formatted = """
    Name: %s
    Age: %d
    """.formatted(name, age);

// String comparison
if (s1.equals(s2)) {  // Không dùng ==
    // Equal
}
if (s1.equalsIgnoreCase(s2)) {  // Case-insensitive
    // Equal
}

// Substring
String sub = s1.substring(0, 3);  // "Hel"

// Split
String[] parts = "one,two,three".split(",");

// Replace
String s = "Hello World";
s = s.replace("World", "Java");
s = s.replaceAll("\\d", "#");

// Trim
String trimmed = "   hello   ".trim();

// Case conversion
String lower = "HELLO".toLowerCase();
String upper = "hello".toUpperCase();

// Index operations
int idx = s1.indexOf("lo");       // 3
int lastIdx = s1.lastIndexOf("l"); // 3
boolean contains = s1.contains("lo");
boolean startsWith = s1.startsWith("He");
boolean endsWith = s1.endsWith("lo");

// isEmpty / isBlank (Java 11+)
boolean empty = s1.isEmpty();
boolean blank = s1.isBlank();  // whitespace cũng tính

// String to number
int i = Integer.parseInt("42");
double d = Double.parseDouble("3.14");
Integer boxed = Integer.valueOf("42");

// Number to String
String si = String.valueOf(42);
String sd = Double.toString(3.14);

// String to/from bytes
byte[] bytes = "Hello".getBytes(StandardCharsets.UTF_8);
String decoded = new String(bytes, StandardCharsets.UTF_8);
```

---

## 3. Tầng 3: OOP & Type Relationships

### 3.1. Class & Object

```java
// Class declaration
public class Person {
    // Fields
    private String name;
    private int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Default constructor
    public Person() {
        this("Unknown", 0);
    }

    // Copy constructor
    public Person(Person other) {
        this(other.name, other.age);
    }

    // Getter/Setter
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    // Method
    public void introduce() {
        System.out.println("I'm " + name + ", " + age + " years old");
    }

    // toString
    @Override
    public String toString() {
        return "Person{name='" + name + "', age=" + age + "}";
    }

    // equals and hashCode
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return age == person.age && Objects.equals(name, person.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }
}

// Sử dụng
Person p1 = new Person("John", 30);
Person p2 = new Person("John", 30);
System.out.println(p1.equals(p2));  // true

// Record (Java 14+)
public record PersonRecord(String name, int age) {
    // Automatic: constructor, getters, equals, hashCode, toString
}

// Sử dụng record
PersonRecord pr = new PersonRecord("John", 30);
System.out.println(pr.name());  // "John" (getter là name())
System.out.println(pr);  // PersonRecord[name=John, age=30]
```

#### Singleton

```java
// Singleton - Eager initialization
public class Singleton {
    private static final Singleton INSTANCE = new Singleton();

    private Singleton() {}

    public static Singleton getInstance() {
        return INSTANCE;
    }
}

// Singleton - Lazy initialization (thread-safe)
public class SingletonLazy {
    private static volatile SingletonLazy instance;

    private SingletonLazy() {}

    public static SingletonLazy getInstance() {
        if (instance == null) {
            synchronized (SingletonLazy.class) {
                if (instance == null) {
                    instance = new SingletonLazy();
                }
            }
        }
        return instance;
    }
}

// Singleton - Bill Pugh (Java 5+)
public class SingletonBillPugh {
    private SingletonBillPugh() {}

    private static class SingletonHelper {
        private static final SingletonBillPugh INSTANCE = new SingletonBillPugh();
    }

    public static SingletonBillPugh getInstance() {
        return SingletonHelper.INSTANCE;
    }
}

// Enum Singleton (recommended)
public enum SingletonEnum {
    INSTANCE;

    public void doSomething() {
        // ...
    }
}
```

---

### 3.2. Kế Thừa & Đa Hình (Inheritance & Polymorphism)

```java
// Base class
public class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    // Virtual method - có thể override
    public void speak() {
        System.out.println("...");
    }

    public String getName() {
        return name;
    }
}

// Derived class
public class Dog extends Animal {
    public Dog(String name) {
        super(name);  // Gọi constructor của parent
    }

    @Override
    public void speak() {
        System.out.println(name + " says: Woof!");
    }
}

public class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.println(name + " says: Meow!");
    }
}

// Sử dụng polymorphism
Animal animal = new Dog("Buddy");
animal.speak();  // Output: Buddy says: Woof!

// instanceof (Java 16+ có pattern matching)
if (animal instanceof Dog dog) {
    dog.bark();  // Smart cast
}

// Method reference với super
public class Labrador extends Dog {
    @Override
    public void speak() {
        super.speak();
        System.out.println("Labrador woof!");
    }
}
```

#### Multiple Inheritance

```java
// Java không có multiple inheritance cho classes
// Nhưng có thể implements nhiều interfaces

public interface Printable {
    void print();
}

public interface Loggable {
    void log(String message);
}

public class Document implements Printable, Loggable {
    @Override
    public void print() {
        System.out.println("Printing document");
    }

    @Override
    public void log(String message) {
        System.out.println("[LOG] " + message);
    }
}
```

---

### 3.3. Interface

```java
// Interface (Java 8+ có default và static methods)
public interface Drawable {
    // Abstract method
    void draw();

    // Default method (Java 8+)
    default void drawWithBorder() {
        System.out.println("Drawing with border");
        draw();
    }

    // Static method (Java 8+)
    static Drawable createDefault() {
        return () -> System.out.println("Default drawable");
    }

    // Private method (Java 9+)
    private void helper() {
        // Private helper
    }
}

// Functional interface (Single Abstract Method)
@FunctionalInterface
public interface Comparator<T> {
    int compare(T o1, T o2);
    // Có thể có default methods nhưng chỉ 1 abstract method
}

// Interface với static fields
public interface Constants {
    int MAX_SIZE = 100;
    String APP_NAME = "MyApp";
}

// Implementation
public class Circle implements Drawable {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public void draw() {
        System.out.println("Drawing circle with radius " + radius);
    }
}

// Sử dụng
Drawable d = new Circle(5.0);
d.draw();
d.drawWithBorder();  // Default method

Drawable defaultDrawable = Drawable.createDefault();
```

#### Functional Interface

```java
// Built-in functional interfaces
import java.util.function.*;

// Predicate - boolean test
Predicate<String> isEmpty = String::isEmpty;
Predicate<String> notEmpty = isEmpty.negate();

// Function - transform
Function<Integer, String> intToString = Object::toString;
Function<String, Integer> parseInt = Integer::parseInt;

// Supplier - no input
Supplier<LocalDateTime> now = LocalDateTime::now;

// Consumer - no output
Consumer<String> printer = System.out::println;

// Bi-function
BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;

// UnaryOperator, BinaryOperator
UnaryOperator<Integer> doubleIt = x -> x * 2;
BinaryOperator<Integer> max = Integer::max;
```

---

### 3.4. Visibility

```java
public class MyClass {
    // public - accessible everywhere
    public int publicField;

    // protected - accessible trong package và subclasses
    protected int protectedField;

    // package-private (default) - accessible trong cùng package
    int packagePrivateField;

    // private - chỉ accessible trong class này
    private int privateField;

    // public method
    public void publicMethod() {}

    // protected method
    protected void protectedMethod() {}

    // private method
    private void privateMethod() {}

    // package-private method
    void packagePrivateMethod() {}
}

// Static nested class - có thể access static members của outer
public class Outer {
    public static class StaticNested {
    }
}

// Inner class - có thể access instance members của outer
public class Outer {
    public class Inner {
    }
}
```

---

## 4. Tầng 4: Memory Model

### 4.1. Memory Management

```java
// Java automatic memory management
// Object được allocate trên heap
Person p = new Person("John", 30);  // Heap

// Primitive locals trên stack
int x = 10;  // Stack

// Object references trên stack, objects trên heap
int[] arr = new int[10];  // arr trên stack, array object trên heap
```

---

### 4.2. Garbage Collection

```java
// Reference counting - Java KHÔNG dùng

// GC roots: static fields, stack variables, active threads, JNI references

// Explicit nullify
Object obj = new Object();
obj = null;  // Object có thể được GC

// try-with-resources (auto-close)
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    // Reader được auto-closed
}

// System.gc() - Gợi ý JVM chạy GC (không guarantee)
System.gc();

// Runtime memory info
Runtime runtime = Runtime.getRuntime();
long maxMemory = runtime.maxMemory();
long totalMemory = runtime.totalMemory();
long freeMemory = runtime.freeMemory();
```

---

### 4.3. Reference Types

```java
import java.lang.ref.*;

// Strong reference (default)
Object obj = new Object();  // Sẽ không bị GC

// WeakReference - GC bất cứ khi nào không có strong reference khác
WeakReference<Object> weakRef = new WeakReference<>(new Object());
System.out.println(weakRef.get());  // Có thể null

// SoftReference - GC khi memory đầy
SoftReference<byte[]> softRef = new SoftReference<>(new byte[1024]);

// PhantomReference - Track khi object bị finalize
ReferenceQueue<Object> queue = new ReferenceQueue<>();
PhantomReference<Object> phantomRef = new PhantomReference<>(new Object(), queue);

// WeakHashMap - Keys có thể bị GC
WeakHashMap<Key, Value> cache = new WeakHashMap<>();
```

---

## 5. Tầng 5: Concurrency Model

### 5.1. Thread

```java
// Extends Thread
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread running");
    }
}

MyThread t = new MyThread();
t.start();

// Implements Runnable
Runnable task = () -> System.out.println("Runnable running");
Thread t2 = new Thread(task);
t2.start();

// Với thread pool
ExecutorService executor = Executors.newFixedThreadPool(4);
executor.submit(() -> doWork());
executor.shutdown();

// Thread local
ThreadLocal<Integer> counter = ThreadLocal.withInitial(() -> 0);
counter.set(42);
int value = counter.get();
counter.remove();
```

---

### 5.2. Executor Service

```java
import java.util.concurrent.*;

// Fixed thread pool
ExecutorService executor = Executors.newFixedThreadPool(4);

// Single thread executor
ExecutorService single = Executors.newSingleThreadExecutor();

// Cached thread pool
ExecutorService cached = Executors.newCachedThreadPool();

// Submit tasks
Future<String> future = executor.submit(() -> "result");
String result = future.get();  // Blocking

// Submit nhiều tasks
List<Callable<Integer>> tasks = Arrays.asList(
    () -> 1,
    () -> 2,
    () -> 3
);

List<Future<Integer>> results = executor.invokeAll(tasks);

// Invoke any (first to complete)
Integer first = executor.invokeAny(tasks);

// Scheduled executor
ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(2);
scheduler.schedule(() -> System.out.println("Delayed"), 5, TimeUnit.SECONDS);
scheduler.scheduleAtFixedRate(() -> System.out.println("Rate"), 1, 1, TimeUnit.SECONDS);
scheduler.scheduleWithFixedDelay(() -> System.out.println("Delay"), 1, 1, TimeUnit.SECONDS);
```

---

### 5.3. Synchronization

```java
// synchronized method
public synchronized void increment() {
    count++;
}

// synchronized block
public void increment() {
    synchronized (this) {
        count++;
    }
}

// Lock interface
import java.util.concurrent.locks.*;

ReentrantLock lock = new ReentrantLock();
lock.lock();
try {
    // Critical section
} finally {
    lock.unlock();
}

// ReadWriteLock
ReadWriteLock rwLock = new ReentrantReadWriteLock();
Lock readLock = rwLock.readLock();
Lock writeLock = rwLock.writeLock();

// Condition
Condition condition = lock.newCondition();
condition.await();
condition.signal();
condition.signalAll();

// Atomic classes
import java.util.concurrent.atomic.*;

AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();
counter.getAndIncrement();
```

---

### 5.4. CompletableFuture

```java
import java.util.concurrent.CompletableFuture;

// Async computation
CompletableFuture<String> future = CompletableFuture
    .supplyAsync(() -> "Hello")
    .thenApply(s -> s + " World")
    .thenApply(String::toUpperCase);

String result = future.get();

// Combine futures
CompletableFuture<Integer> f1 = CompletableFuture.supplyAsync(() -> 10);
CompletableFuture<Integer> f2 = CompletableFuture.supplyAsync(() -> 20);

CompletableFuture<Integer> combined = f1.thenCombine(f2, Integer::sum);

// Exception handling
CompletableFuture<String> safe = CompletableFuture
    .supplyAsync(() -> riskyOperation())
    .exceptionally(ex -> "Default value");

// AllOf / AnyOf
CompletableFuture<Void> all = CompletableFuture.allOf(f1, f2, f3);
CompletableFuture<Object> any = CompletableFuture.anyOf(f1, f2, f3);
```

---

## 6. Tầng 6: Paradigm

### 6.1. Functional Programming

```java
// Pure function
public int add(int a, int b) {
    return a + b;  // No side effects
}

// Higher-order function
@FunctionalInterface
interface Function<T, R> {
    R apply(T t);
}

Function<Integer, Integer> square = x -> x * x;

// Immutability
public final class ImmutablePerson {
    private final String name;
    private final int age;

    // No setters, constructor với all fields
}

// Function composition
Function<Integer, Integer> f1 = x -> x * 2;
Function<Integer, Integer> f2 = x -> x + 1;
Function<Integer, Integer> composed = f1.andThen(f2);  // f1 then f2
```

---

### 6.2. Lambda Expressions

```java
// Lambda cơ bản
Runnable r = () -> System.out.println("Hello");
Supplier<Integer> s = () -> 42;

// Lambda với parameters
Consumer<String> c = (String name) -> System.out.println(name);
Consumer<String> c2 = name -> System.out.println(name);  // Type inference
BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;

// Block body
Comparator<Integer> comp = (a, b) -> {
    if (a > b) return 1;
    if (a < b) return -1;
    return 0;
};

// Method reference
Function<String, Integer> parser = Integer::parseInt;
Consumer<String> printer = System.out::println;
Supplier<LocalDateTime> now = LocalDateTime::now;

// Constructor reference
Supplier<ArrayList<String>> listSupplier = ArrayList::new;
Function<Integer, ArrayList<String>> listWithSize = ArrayList::new;
```

---

### 6.3. Stream API

```java
import java.util.stream.*;

// Tạo Stream
Stream<String> stream1 = Stream.of("a", "b", "c");
Stream<Integer> stream2 = Arrays.asList(1, 2, 3).stream();
Stream<Integer> stream3 = IntStream.range(1, 10).boxed();
Stream<String> stream4 = Files.lines(Paths.get("file.txt"));

// Intermediate operations
Stream<T> filter(Predicate<T>)
Stream<T> map(Function<T,R>)
Stream<R> flatMap(Function<T, Stream<R>>)
Stream<T> distinct()
Stream<T> sorted()
Stream<T> limit(long n)
Stream<T> skip(long n)

// Terminal operations
void forEach(Consumer<T>)
R collect(Collector<T,A,R>)
T reduce(T identity, BinaryOperator<T>)
Optional<T> min(Comparator<T>)
Optional<T> max(Comparator<T>)
boolean allMatch(Predicate<T>)
boolean anyMatch(Predicate<T>)
boolean noneMatch(Predicate<T>)
Object[] toArray()

// Collectors
List<T> toList()
Set<T> toSet()
Map<K,V> toMap(Function<T,K>, Function<T,V>)
groupingBy(Function<T,K>)
partitioningBy(Predicate<T>)
joining(CharSequence delimiter)
```

---

## 7. Tầng 7: Error Handling

### 7.1. Exception

```java
// Throw exception
public int divide(int a, int b) throws ArithmeticException {
    if (b == 0) {
        throw new ArithmeticException("Division by zero");
    }
    return a / b;
}

// Try-catch
try {
    int result = divide(10, 0);
} catch (ArithmeticException e) {
    System.err.println("Error: " + e.getMessage());
} catch (NullPointerException e) {
    // Handle NPE
} finally {
    // Always executed
}

// Multi-catch (Java 7+)
try {
    // ...
} catch (IOException | SQLException e) {
    System.err.println("Error: " + e.getMessage());
}

// Custom exception
public class MyException extends Exception {
    public MyException() { super(); }
    public MyException(String message) { super(message); }
    public MyException(String message, Throwable cause) { super(message, cause); }
}

// Runtime exception (unchecked)
public class ValidationException extends RuntimeException {
    public ValidationException(String message) { super(message); }
}
```

---

### 7.2. Try-with-Resources

```java
// Auto-closeable resources
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}

// Multiple resources
try (
    FileInputStream fis = new FileInputStream("in.txt");
    FileOutputStream fos = new FileOutputStream("out.txt")
) {
    // Use resources
}

// Custom resource implements AutoCloseable
public class Resource implements AutoCloseable {
    @Override
    public void close() {
        System.out.println("Closed");
    }
}
```

---

### 7.3. Optional

```java
import java.util.Optional;

// Tạo Optional
Optional<String> empty = Optional.empty();
Optional<String> of = Optional.of("value");
Optional<String> ofNullable = Optional.ofNullable(getValue());

// Check và get
if (optional.isPresent()) {
    String value = optional.get();
}

// Safe get với default
String value = optional.orElse("default");
String value2 = optional.orElseGet(() -> computeDefault());
String value3 = optional.orElseThrow();

// Transform
Optional<Integer> length = optional.map(String::length);
Optional<String> upper = optional.map(String::toUpperCase);

// FlatMap
Optional<String> result = optional.flatMap(this::findRelated);

// Filter
Optional<String> filtered = optional.filter(s -> s.length() > 5);

// Optional trong method return
public Optional<Person> findPerson(String id) {
    return persons.stream()
        .filter(p -> p.getId().equals(id))
        .findFirst();
}
```

---

## 8. Tầng 8: Module & Organization

### 8.1. Package

```java
// Package declaration (phải là dòng đầu tiên)
package com.example.myapp.models;

// Package structure
// com/example/myapp/models/Person.java

// Default package (không nên dùng)
class MyClass { }  // Default package
```

---

### 8.2. Import

```java
// Single type import
import java.util.List;
import java.util.ArrayList;

// Static import
import static java.lang.System.out;
import static java.util.Collections.sort;

// On-demand import
import java.util.*;

// Type-import-on-demand (không import subpackages)
import java.sql.*;  // SQL types

// Conflict resolution
import java.util.Date;
import java.sql.Date;
import java.sql.Date sqlDate = new java.sql.Date(0);
```

---

### 8.3. Module System (JDK 9+)

```java
// module-info.java
module com.example.myapp {
    // Requires other modules
    requires com.example.utils;
    requires java.sql;

    // Requires statically
    requires static com.example.annotation;

    // Exports
    exports com.example.myapp.models;
    exports com.example.myapp.api;

    // Exports to specific modules
    exports com.example.internal to com.example.client;

    // Provides service
    provides MyService with MyServiceImpl;

    // Opens for reflection
    opens com.example.myapp.models;
    opens com.example.myapp.models to com.example.serialization;
}
```

---

## 9. Tầng 9: I/O & Networking

### 9.1. HTTP & Networking

```java
// Java 11+ HttpClient
import java.net.URI;
import java.net.http.*;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/data"))
    .header("Content-Type", "application/json")
    .GET()
    .build();

HttpResponse<String> response = client.send(request,
    HttpResponse.BodyHandlers.ofString());

System.out.println(response.statusCode());
System.out.println(response.body());

// Async request
CompletableFuture<HttpResponse<String>> future = client.sendAsync(request,
    HttpResponse.BodyHandlers.ofString());

// POST request
HttpRequest postRequest = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/create"))
    .POST(HttpRequest.BodyPublishers.ofString("{\"name\":\"test\"}"))
    .header("Content-Type", "application/json")
    .build();

// URL Connection (legacy)
URL url = new URL("https://api.example.com/data");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setRequestMethod("GET");
BufferedReader reader = new BufferedReader(
    new InputStreamReader(conn.getInputStream()));
```

---

### 9.2. File I/O

```java
import java.nio.file.*;

// Đọc file
String content = Files.readString(Paths.get("file.txt"));  // Java 11+
List<String> lines = Files.readAllLines(Paths.get("file.txt"));

// Ghi file
Files.writeString(Paths.get("output.txt"), "Hello");  // Java 11+
Files.write(Paths.get("output.txt"), Arrays.asList("line1", "line2"));

// Binary I/O
byte[] bytes = Files.readAllBytes(Paths.get("data.bin"));
Files.write(Paths.get("data.bin"), bytes);

// Stream-based
Files.lines(Paths.get("file.txt")).forEach(System.out::println);

// File operations
boolean exists = Files.exists(path);
boolean isDirectory = Files.isDirectory(path);
Files.createDirectory(Paths.get("newdir"));
Files.copy(source, target);
Files.move(source, target);
Files.delete(path);

// Watch service (file changes)
WatchService watcher = FileSystems.getDefault().newWatchService();
path.register(watcher, StandardWatchEventKinds.ENTRY_MODIFY);
```

---

### 9.3. Stream I/O

```java
import java.io.*;

// Input/Output streams
InputStream in = new FileInputStream("file.txt");
OutputStream out = new FileOutputStream("output.txt");

// Buffered streams
BufferedReader reader = new BufferedReader(new FileReader("file.txt"));
BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"));

// Print stream
PrintWriter pw = new PrintWriter(System.out);

// Data streams
DataInputStream dis = new DataInputStream(new FileInputStream("data.bin"));
DataOutputStream dos = new DataOutputStream(new FileOutputStream("data.bin"));

// Object serialization
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("obj.dat"));
oos.writeObject(object);
ObjectInputStream ois = new ObjectInputStream(new FileInputStream("obj.dat"));
Object obj = ois.readObject();

// StringReader/Writer
StringReader sr = new StringReader("text");
StringWriter sw = new StringWriter();
```

---

## 10. Tầng 10: Data & Serialization

### 10.1. JSON

```java
// Thư viện phổ biến: Jackson, Gson

// Jackson
import com.fasterxml.jackson.databind.*;

ObjectMapper mapper = new ObjectMapper();

// Serialize
Person p = new Person("John", 30);
String json = mapper.writeValueAsString(p);

// Deserialize
Person p2 = mapper.readValue(json, Person.class);

// Parse JSON string
JsonNode node = mapper.readTree(json);
String name = node.get("name").asText();

// JSON Array
ArrayNode arr = mapper.createArrayNode();
arr.add(1).add(2).add(3);

// Pretty print
String pretty = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(p);

// Gson
import com.google.gson.*;

Gson gson = new Gson();
String json2 = gson.toJson(p);
Person p3 = gson.fromJson(json2, Person.class);
```

---

### 10.2. Date & Time

```java
import java.time.*;

// LocalDate
LocalDate today = LocalDate.now();
LocalDate date = LocalDate.of(2024, 1, 15);

// LocalTime
LocalTime time = LocalTime.now();
LocalTime noon = LocalTime.of(12, 0, 0);

// LocalDateTime
LocalDateTime dt = LocalDateTime.now();
LocalDateTime dt2 = LocalDateTime.of(2024, 1, 15, 10, 30);

// ZonedDateTime
ZonedDateTime zdt = ZonedDateTime.now(ZoneId.of("Asia/Ho_Chi_Minh"));

// Instant (timestamp)
Instant instant = Instant.now();

// Duration & Period
Duration duration = Duration.ofHours(2);
Period period = Period.ofDays(7);

// Parsing & Formatting
LocalDate parsed = LocalDate.parse("2024-01-15");
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");
String formatted = dt.format(fmt);

// Arithmetic
LocalDate tomorrow = today.plusDays(1);
LocalDate lastMonth = today.minusMonths(1);

// Between
long days = ChronoUnit.DAYS.between(start, end);

// Legacy Date/Calendar (tránh dùng)
Date date = new Date();
Calendar cal = Calendar.getInstance();
```

---

### 10.3. Regular Expression

```java
import java.util.regex.*;

// Pattern
Pattern pattern = Pattern.compile("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");

// Match
Matcher matcher = pattern.matcher("test@example.com");
if (matcher.matches()) {
    System.out.println("Valid email");
}

// Find
String text = "Email: test@example.com, Phone: 123-456-7890";
Matcher findMatcher = pattern.matcher(text);
while (findMatcher.find()) {
    System.out.println("Found: " + findMatcher.group());
}

// Groups
Pattern p = Pattern.compile("(\\w+)@(\\w+\\.\\w+)");
Matcher m = p.matcher("test@example.com");
if (m.find()) {
    String full = m.group(0);   // "test@example.com"
    String user = m.group(1);  // "test"
    String domain = m.group(2); // "example.com"
}

// Replace
String result = text.replaceAll("\\d{3}-\\d{3}-\\d{4}", "[PHONE]");

// Split
String[] parts = "one,two,three".split(",");

// String.matches (convenience)
boolean valid = "test@example.com".matches("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");
```

---

## 11. Tầng 11: Development Practices

### 11.1. Testing

```java
// JUnit 5
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Calculator Tests")
class CalculatorTest {

    @BeforeEach
    void setUp() {
        // Setup
    }

    @Test
    @DisplayName("Addition should return correct sum")
    void testAdd() {
        assertEquals(5, 2 + 3);
    }

    @Test
    void testExceptions() {
        assertThrows(ArithmeticException.class, () -> {
            int x = 1 / 0;
        });
    }

    @ParameterizedTest
    @CsvSource({"1,1,2", "2,3,5", "10,20,30"})
    void testAddParameterized(int a, int b, int expected) {
        assertEquals(expected, a + b);
    }

    @Test
    void testGroupAssertions() {
        assertAll("Math tests",
            () -> assertEquals(4, 2 + 2),
            () -> assertEquals(6, 3 * 2)
        );
    }
}

// Mockito
import org.mockito.Mockito.*;

List mockedList = mock(List.class);
when(mockedList.get(0)).thenReturn("first");
assertEquals("first", mockedList.get(0));
verify(mockedList).get(0);
```

---

### 11.2. Logging

```java
// SLF4J API
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MyClass {
    private static final Logger logger = LoggerFactory.getLogger(MyClass.class);

    public void doSomething() {
        logger.info("Starting process");
        logger.debug("Debug info: {}", value);
        logger.warn("Warning: {}", message);
        logger.error("Error: {}", exception);

        // With parameters
        logger.info("User {} logged in from {}", username, ip);
    }
}

// Logback configuration (logback.xml)
<configuration>
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>app.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>app.%d{yyyy-MM-dd}.log</fileNamePattern>
        </rollingPolicy>
    </appender>
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
    </root>
</configuration>
```

---

### 11.3. Build & Package Management

```bash
# Maven
mvn clean compile
mvn test
mvn package
mvn exec:java -Dexec.mainClass="com.example.Main"

# Gradle
gradle clean build
gradle test
gradle run

# Dependencies (Maven pom.xml)
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-lang3</artifactId>
        <version>3.12.0</version>
    </dependency>
    <dependency>
        <groupId>com.google.code.gson</groupId>
        <artifactId>gson</artifactId>
        <version>2.10.1</version>
    </dependency>
    <!-- Test -->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>5.9.2</version>
        <scope>test</scope>
    </dependency>
</dependencies>

# Gradle build.gradle
plugins {
    id 'java'
    id 'application'
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.apache.commons:commons-lang3:3.12.0'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.9.2'
}

application {
    mainClass = 'com.example.Main'
}
```

---

## 12. Tầng 12: Advanced Concepts

### 12.1. Records (JDK 14+)

```java
// Record - immutable data carrier
public record Person(String name, int age) {
    // Automatic: constructor, getters, equals, hashCode, toString
}

// Compact constructor
public record Person(String name, int age) {
    public Person {
        Objects.requireNonNull(name);
    }
}

// Static methods và nested types allowed
public record Range(int start, int end) {
    public static Range of(int start, int end) {
        return new Range(start, end);
    }

    public boolean contains(int value) {
        return value >= start && value <= end;
    }
}

// Sử dụng
Person p = new Person("John", 30);
String name = p.name();  // Getter
System.out.println(p);   // Person[name=John, age=30]
```

---

### 12.2. Sealed Classes (JDK 17+)

```java
// Sealed class - giới hạn inheritance
public sealed class Shape
    permits Circle, Rectangle, Square {

    private final String color;

    public Shape(String color) {
        this.color = color;
    }
}

// Non-sealed subclass
non-sealed class Circle extends Shape {
    private double radius;
    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }
}

// Final subclass
final class Square extends Shape {
    private double side;
    public Square(String color, double side) {
        super(color);
        this.side = side;
    }
}

// Pattern matching với sealed
String getArea(Shape s) {
    return switch (s) {
        case Circle c -> "Circle area: " + Math.PI * c.radius() * c.radius();
        case Rectangle r -> "Rectangle area: " + r.width() * r.height();
        case Square sq -> "Square area: " + sq.side() * sq.side();
    };
}

// Interface cũng có thể sealed
public sealed interface Readable permits InputStreamReader, BufferedReader {
    String readLine();
}
```

---

### 12.3. Pattern Matching

```java
// Pattern matching for instanceof (JDK 16+)
if (obj instanceof String s) {
    System.out.println(s.toUpperCase());  // Smart cast
}

// With additional condition
if (obj instanceof Integer i && i > 0) {
    System.out.println(i * 2);
}

// Switch patterns (JDK 21+)
String getDescription(Object obj) {
    return switch (obj) {
        case Integer i -> "Integer: " + i;
        case String s -> "String: " + s;
        case null -> "Null value";
        default -> "Unknown type";
    };
}

// Record patterns
record Point(int x, int y) {}

void processPoint(Object obj) {
    if (obj instanceof Point(int x, int y)) {
        System.out.println(x + y);
    }
}

// Nested patterns
record Pair<T, U>(T first, U second) {}
record Entry(Pair<String, Integer> pair) {}

if (obj instanceof Entry(Pair(String s, Integer i))) {
    System.out.println(s + i);
}
```

---

## 13. Tầng 13: Memory Layout

### 13.1. Object Layout

```java
// Object header (mark word + class pointer)
// Instance data: fields
// Padding

// Array header: object header + length + elements

// Compressed Class Pointers (4 bytes thay vì 8 trong 64-bit với heap < 32GB)
-XX:+UseCompressedClassPointers

// Object padding - alignment 8 bytes mặc định
// -XX:ObjectAlignmentInBytes=16
```

---

### 13.2. Memory Alignment

```java
// JVM aligns objects to 8-byte boundary by default
// Arrays of primitives are aligned to element size

// -XX:ObjectAlignmentInBytes=16
// -XX:ArrayCopyMaxInlineBits=64
```

---

## 14. Tầng 14: Compilation Model

### 14.1. Compilation

```bash
# Compile
javac Main.java

# Compile với module
javac -d out --module-source-path src src/module-info.java src/com/example/Main.java

# Compile với classpath
javac -cp "lib/*:." -d out src/Main.java

# Decompile
javap -c ClassName
javap -p ClassName  // Private members
```

---

### 14.2. Bytecode

```java
// Generated .class files chứa bytecode
// JVM interprets/JIT compiles bytecode

// View bytecode
javap -c MyClass

// Verbose
javap -verbose MyClass
```

---

### 14.3. JIT Compiler

```bash
# JIT compilation options
-XX:+PrintCompilation    // Print JIT compilation
-XX:+TieredCompilation   // Use tiered compilation
-XX:CompileThreshold=10000

# C1 (client) vs C2 (server) compiler
// C1: Fast compilation, less optimization
// C2: Slower compilation, aggressive optimization
```

---

## 15. Tầng 15: Linking Model

### 15.1. Class Loading

```java
// ClassLoader hierarchy
// Bootstrap ClassLoader (null) - loads java.*
// Platform ClassLoader - loads JDK modules
// Application ClassLoader - loads classpath

// Custom ClassLoader
public class MyClassLoader extends ClassLoader {
    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {
        byte[] b = loadClassData(name);
        return defineClass(name, b, 0, b.length);
    }
}
```

---

### 15.2. Dynamic Loading

```java
// Load class by name
Class<?> clazz = Class.forName("com.example.MyClass");

// Load với classpath
URL[] urls = {new File("lib").toURI().toURL()};
ClassLoader loader = new URLClassLoader(urls);
Class<?> clazz = loader.loadClass("com.example.MyClass");

// ServiceLoader
ServiceLoader<MyService> loader = ServiceLoader.load(MyService.class);
for (MyService service : loader) {
    service.doSomething();
}
```

---

## 16. Tầng 16: Runtime

### 16.1. JVM

```bash
# Run
java -Xms512m -Xmx2g MyClass

# GC options
java -XX:+UseG1GC MyClass
java -XX:+UseZGC MyClass
java -XX:+UseShenandoahGC MyClass
```

---

### 16.2. Stack & Heap

```java
// Stack: method frames, local variables
// Heap: objects, arrays
// Metaspace: class metadata
// Native: native method stacks

// -Xss stack size
// -Xms initial heap
// -Xmx max heap
// -XX:MetaspaceSize
```

---

### 16.3. Virtual Method Dispatch

```java
// Dynamic dispatch - runtime quyết định method nào gọi
Animal animal = new Dog("Buddy");
animal.speak();  // Dog.speak() được gọi

// Invokevirtual: standard method dispatch
// Invokestatic: Invokespecial: constructors, private, super static methods
//
// Invokedynamic: lambda, method references (Java 8+)
```

---

## 17. Tầng 17: Language Design Patterns

### 17.1. Builder Pattern

```java
// Builder
public class Person {
    private String name;
    private int age;
    private String address;

    private Person(Builder builder) {
        this.name = builder.name;
        this.age = builder.age;
        this.address = builder.address;
    }

    public static class Builder {
        private String name;
        private int age = 0;
        private String address;

        public Builder name(String name) {
            this.name = name;
            return this;
        }

        public Builder age(int age) {
            this.age = age;
            return this;
        }

        public Builder address(String address) {
            this.address = address;
            return this;
        }

        public Person build() {
            return new Person(this);
        }
    }
}

// Sử dụng
Person p = new Person.Builder()
    .name("John")
    .age(30)
    .address("NYC")
    .build();
```

---

### 17.2. Factory Pattern

```java
// Factory method
public interface Shape {
    void draw();
}

public class Circle implements Shape {
    public void draw() { System.out.println("Circle"); }
}

public class ShapeFactory {
    public Shape create(String type) {
        return switch (type) {
            case "circle" -> new Circle();
            case "square" -> new Square();
            default -> throw new IllegalArgumentException();
        };
    }
}

// Abstract factory
public interface AbstractFactory<T> {
    T create(String type);
}
```

---

### 17.3. Singleton

```java
// Enum (recommended)
public enum Singleton {
    INSTANCE;

    public void doSomething() { }
}

// Bill Pugh (thread-safe, lazy)
public class Singleton {
    private Singleton() {}

    private static class Holder {
        private static final Singleton INSTANCE = new Singleton();
    }

    public static Singleton getInstance() {
        return Holder.INSTANCE;
    }
}
```

---

## 18. Tầng 18: Standard Library

### 18.1. Collections

```java
import java.util.*;

// List
List<String> list = new ArrayList<>();
List<String> linked = new LinkedList<>();
List<String> fixed = Arrays.asList("a", "b", "c");

// Set
Set<String> hashSet = new HashSet<>();
Set<String> linkedHashSet = new LinkedHashSet<>();
Set<String> treeSet = new TreeSet<>();

// Map
Map<String, Integer> hashMap = new HashMap<>();
Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
Map<String, Integer> treeMap = new TreeMap<>();

// Queue
Queue<String> queue = new LinkedList<>();
Deque<String> deque = new ArrayDeque<>();
PriorityQueue<Integer> pq = new PriorityQueue<>();

// Collections utility
Collections.sort(list);
Collections.reverse(list);
Collections.shuffle(list);
Collections.max(collection);
Collections.min(collection);
```

---

### 18.2. Utilities

```java
import java.util.*;

// Objects
Objects.equals(a, b);
Objects.hash(a, b, c);
Objects.requireNonNull(obj);
Objects.toString(obj);

// Arrays
Arrays.sort(arr);
Arrays.fill(arr, value);
Arrays.toString(arr);
Arrays.asList(arr);

// Collections
List<String> unmodifiable = Collections.unmodifiableList(list);
List<String> synchronized = Collections.synchronizedList(list);

// Optional
Optional.of("value");

// CompletableFuture
CompletableFuture.supplyAsync(() -> "result");

// Number
Integer.parseInt("42");
Integer.valueOf("42");
String.valueOf(42);

// Random
new Random().nextInt(100);
ThreadLocalRandom.current().nextInt(100);
```

---

### 18.3. I/O & System

```java
import java.io.*;
import java.nio.file.*;
import java.util.*;

// Console
Console console = System.console();
String input = console.readLine("Name: ");
console.printf("Hello %s%n", input);

// Properties
Properties props = new Properties();
props.load(new FileInputStream("config.properties"));
String value = props.getProperty("key");

// Environment variables
String path = System.getenv("PATH");
Map<String, String> env = System.getenv();

// System properties
String javaVersion = System.getProperty("java.version");
System.setProperty("myprop", "myvalue");
```

---

## 19. Tầng 19: Ecosystem

### 19.1. Frameworks

```java
// Spring Framework
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

// Jakarta EE / Java EE
import jakarta.ws.rs.*;
import jakarta.ejb.*;

 // Android
 // Android SDK, Jetpack Compose
```

---

### 19.2. Libraries

```java
// Popular libraries:
// - Spring Boot: Web, REST APIs
// - Hibernate: ORM
// - Jackson/Gson: JSON
// - Lombok: Boilerplate reduction
// - Apache Commons: Utilities
// - Guava: Google utilities
// - JUnit/Mockito: Testing

// Lombok
@Data  // @Getter @Setter @ToString @EqualsAndHashCode
@NoArgsConstructor @AllArgsConstructor
public class Person {
    private String name;
    private int age;
}
```

---

### 19.3. Build Tools

```bash
# Maven
mvn clean package -DskipTests

# Gradle
gradle clean build -x test

# Build image (jlink)
jlink --add-modules java.sql --output jre-minimal

# Create jar
jar cf myapp.jar -C out .
jar cfe myapp.jar com.example.Main -C out .
```

---

## 20. Tầng 20: Toolchain

### 20.1. Compiler

```bash
# javac
javac -d out -cp "lib/*" Main.java
javac --release 17 -d out Main.java

# jshell (REPL)
jshell

# jdeps (dependency analysis)
jdeps myapp.jar

# jlink (custom runtime)
jlink --add-modules java.sql,java.base --output myjre

# jpackage (native installer)
jpackage --input target --main-jar myapp.jar --name MyApp --type dmg
```

---

### 20.2. Debugging

```bash
# jdb
jdb MyClass

# jstack (thread dump)
jstack -l <pid>

# jmap (heap dump)
jmap -heap <pid>
jmap -dump:format=b,file=heap.hprof <pid>

# jconsole / VisualVM
jconsole
visualvm

# Heap dump analysis
jhat heap.hprof
```

---

### 20.3. Code Quality

```bash
# Checkstyle
mvn checkstyle:check

# Spotbugs
mvn spotbugs:check

# JaCoCo (coverage)
mvn jacoco:report

# Formatting
google-java-format -i MyFile.java
```

---

## Tóm Tắt

### Ưu Điểm Java
- **Portability**: Write Once, Run Anywhere (JVM)
- **Automatic Memory Management**: Garbage Collection
- **Rich Ecosystem**: Enterprise frameworks, libraries
- **Strong Typing**: Early error detection
- **Multi-paradigm**: OOP + Functional (Java 8+)
- **Security**: Sandboxed execution

### Nhược Điểm Java
- **Performance**: Không bằng C/C++ (nhưng vẫn rất nhanh)
- **Startup time**: JVM cần thời gian khởi động
- **Memory usage**: Heap lớn hơn native languages
- **Verbosity**: Boilerplate code (dùng Lombok/Records giảm thiểu)

### Java Versions Timeline
- **Java 8 (2014)**: Lambda, Stream, Optional, default methods
- **Java 9 (2017)**: Modules, JShell, private methods in interfaces
- **Java 10 (2018)**: Local-Variable Type Inference (var)
- **Java 11 (2018)**: HTTP Client (final), String methods
- **Java 12-13**: Switch expressions
- **Java 14 (2020)**: Records, Pattern Matching instanceof
- **Java 16 (2021)**: Pattern Matching for instanceof (final)
- **Java 17 (2021)**: Sealed Classes, Switch patterns
- **Java 18-21**: Continued improvements, Virtual threads
- **Java 22-23**: Further enhancements
