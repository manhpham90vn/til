# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal "TIL" (Today I Learned) knowledge base written in Vietnamese. It contains syntax comparisons across multiple programming languages organized as a reference document.

## Project Type

**Documentation-only repository** - No build system, tests, or executable code. This is a markdown reference document, not a software project.

## Content Structure

The main content is in `README.md`, which serves as a comprehensive syntax comparison organized in **12 conceptual layers**:

### Layer 1: Syntax & Semantics
- Variable declarations (mutable, immutable, constants)
- Function declarations (parameters, return types, arrow functions)
- Loops (for, while, foreach, iterators)
- Conditionals (if-else, switch/match, ternary)

### Layer 2: Type System
- Primitive types (int, float, bool, string, array)
- Enum (basic, with values, with methods)
- Nullable/Option types
- Null Safety (Elvis, safe call, null coalescing)
- Generics
- Collection Operations (map, filter, reduce, sort)
- String Operations (concatenation, interpolation, regex)

### Layer 3: OOP & Type Relationships
- Class/Object (struct, data class, singleton, factory)
- Inheritance & Polymorphism
- Interface/Trait/Protocol
- Visibility/Access Modifiers

### Layer 4: Memory Model
- Memory Management (GC, weak reference)
- Property & Getter/Setter

### Layer 5: Concurrency Model
- Async/Await, Thread, Coroutine
- Goroutine (Go-specific)
- Future/Promise, Channel

### Layer 6: Paradigm
- Functional Programming (pure function, immutability, currying)
- Function Composition

### Layer 7: Error Handling
- Try-Catch, Throw Exception
- Custom Exception, Finally Block
- Result/Option pattern

### Layer 8: Module & Organization
- Import/Export, Namespace
- Extension Methods, Operator Overloading

### Layer 9: I/O & Networking
- HTTP Request/Response
- File I/O, Stream, Buffer

### Layer 10: Data & Serialization
- JSON & Serialization
- Date & Time
- Regular Expression

### Layer 11: Development Practices
- Testing (Unit, Integration, E2E, Mock)
- Logging
- Dependency Injection
- Configuration
- Build & Package Management
- Documentation

### Layer 12: Advanced Concepts
- Reflection, Metadata
- Pointer/Reference
- Unsafe Code, FFI
- Coroutine/Fiber
- Actor Model
- Type Classes, Lazy Evaluation
- TCO, Continuations

### Layer 13: Memory Layout
- Struct Layout (packing, field order, alignment)
- Object Layout (header, array, string)
- VTable (virtual method table)
- Cache Locality (spatial/temporal, cache line, prefetching)
- Padding (struct padding, alignment, packed struct)

### Layer 14: Compilation Model
- Interpreter (AST, bytecode, threaded code)
- Bytecode (VM, instruction set, optimization)
- JIT (baseline, optimizing, inline caching, deoptimization)
- AOT (native compilation, LTO, code generation)

### Layer 15: Linking Model
- Static Linking (static library, linker, relocation)
- Dynamic Linking (shared library, loader, lazy binding, PLT/GOT)
- Symbol Resolution (visibility, collision, name mangling)

### Layer 16: Runtime
- Stack Frame (layout, return address, frame pointer)
- Call Stack (unwinding, tail call, recursion)
- Exception Unwinding (unwind tables, cleanup, catch blocks)
- Garbage Collector Internals (mark & sweep, generational, compaction)

### Layer 17: Language Design Patterns
- Zero-Cost Abstractions (inlining, monomorphization)
- RAII (resource management, scope-based)
- Ownership (move semantics, borrowing, lifetimes)
- Algebraic Data Type (sum type, product type, pattern matching)

### Layer 18: Standard Library
- Collections & Data Structures (Vector, HashMap, Queue, etc.)
- Utilities (Option, Result, Iterator, Range)
- Concurrency Primitives (Thread, Mutex, Channel, Atomic)
- I/O & System (File, Process, Environment)
- String & Text (String, Regex, Formatter)

### Layer 19: Ecosystem
- Web Frameworks (Backend, Frontend, API, GraphQL)
- Database & ORM (ORM, Query Builder, Migration)
- Testing (Unit Test, Mock, Property Testing, Benchmark)
- DevOps & Infrastructure (Docker, Kubernetes, CI/CD)
- Networking & Communication (HTTP, WebSocket, gRPC)
- Security & Cryptography (Auth, Encryption, JWT)
- Data Science & ML (NumPy-like, Pandas-like, ML Frameworks)

### Layer 20: Toolchain
- Compiler & Build (Compiler, Linker, Build System, Package Manager)
- Code Quality (Linter, Formatter, Static Analyzer)
- IDE & Editor (Language Server, Debug Adapter)
- Version Control (Git Hooks, Merge Tool)
- Documentation & Publishing (Doc Generator, Package Registry)
- Runtime & Environment (VM, Interpreter, JIT, REPL)
- Profiling & Debugging (Profiler, Debugger, Memory Profiler)

## Usage

Since this is a documentation project:

- No build commands needed
- No test commands needed
- No linting required
- Edit `README.md` directly for content updates
- Language-specific files (e.g., `PHP.md`) follow the same 12-layer structure
- Content is written in Vietnamese with programming terminology

## Language Coverage

The reference covers: Rust, Go, Python, TypeScript, JavaScript, Swift, Kotlin, Dart, PHP
