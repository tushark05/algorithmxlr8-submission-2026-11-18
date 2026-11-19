<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Add Binary

**Difficulty:** `Easy`

## Problem

Given two binary strings a and b, return their sum as a binary string.

Each string represents a non-negative integer written in base 2 with the most significant bit first. The strings can be up to 10^4 characters long, so the numbers can be far larger than any built-in integer type. Add them column by column from the right end, exactly like adding decimal numbers by hand: a column whose bits (plus the incoming carry) sum to 2 or 3 writes 0 or 1 and carries 1 into the next column. If a carry is left after the leftmost column, it becomes a new leading 1.

The two strings may have different lengths. The result must not contain leading zeros, except for the number zero itself, which is written as "0".

Input format: the first line contains the string a and the second line contains the string b.

Output format: print the binary sum of a and b on a single line.

## Examples

### Example 1

**Input**
```
a = "11", b = "1"
```
**Output**
```
"100"
```

**Explanation:** 11 in binary is 3 and 1 is 1. 3 + 1 = 4, which is 100 in binary.

### Example 2

**Input**
```
a = "1010", b = "1011"
```
**Output**
```
"10101"
```

**Explanation:** 1010 is 10 and 1011 is 11. 10 + 11 = 21, which is 10101 in binary.

### Example 3

**Input**
```
a = "1111", b = "1111"
```
**Output**
```
"11110"
```

**Explanation:** 1111 is 15, and 15 + 15 = 30, which is 11110 in binary. The final carry adds a fifth digit.

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/add-binary).