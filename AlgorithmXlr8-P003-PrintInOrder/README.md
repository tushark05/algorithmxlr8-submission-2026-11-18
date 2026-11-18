<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Print in Order

**Difficulty:** `Easy`

## Problem

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}

The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

The threads may be started in any order, and the operating system can switch between them at any moment. Your synchronisation must make the output correct for every possible schedule.

On this website the threads are simulated: the input tells you the order in which the threads are started, and your program must print what the correctly synchronised program prints.

Input format: one line with three integers, a permutation of 1, 2 and 3. Value 1 is the thread that calls first(), 2 calls second() and 3 calls third(), listed in the order the threads start.

Output format: the single line printed by the synchronised program.

## Examples

### Example 1

**Input**
```
nums = [1,2,3]
```
**Output**
```
"firstsecondthird"
```

**Explanation:** Thread A calls first(), thread B calls second() and thread C calls third(). The output is "firstsecondthird".

### Example 2

**Input**
```
nums = [1,3,2]
```
**Output**
```
"firstsecondthird"
```

**Explanation:** Thread C starts before thread B, but third() must wait until second() has run, so the output is still "firstsecondthird".

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/print-in-order).