<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Convert Integer to the Sum of Two No-Zero Integers

**Difficulty:** `Easy`

## Problem

A No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:
- a and b are No-Zero integers.
- a + b = n

The test cases are generated so that there is at least one valid solution.

On LeetCode any valid pair is accepted. On this website the answer must be unique, so print the valid pair with the smallest possible a.

Input format: one line containing n.

Output format: print a and b separated by a space, choosing the valid pair with the smallest a.

## Examples

### Example 1

**Input**
```
n = 2
```
**Output**
```
[1,1]
```

**Explanation:** a = 1 and b = 1. Both are No-Zero integers and 1 + 1 = 2.

### Example 2

**Input**
```
n = 11
```
**Output**
```
[2,9]
```

**Explanation:** a = 1 would give b = 10, which contains a 0. The next choice a = 2, b = 9 is valid.

### Example 3

**Input**
```
n = 1010
```
**Output**
```
[11,999]
```

**Explanation:** Every a from 1 to 10 fails because either a or 1010 - a contains a 0.

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/convert-integer-to-the-sum-of-two-no-zero-integers).