<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Shuffle the Array

**Difficulty:** `Easy`

## Problem

Given the array nums consisting of 2n elements in the form [x1, x2, ..., xn, y1, y2, ..., yn].

Return the array in the form [x1, y1, x2, y2, ..., xn, yn].

In other words, the first half of the array holds the x values and the second half holds the y values, and you must interleave them so that each x is immediately followed by the y with the same index.

Input format: the first line is n. The second line has the 2n values of nums.

Output format: print the 2n values of the shuffled array separated by spaces.

## Examples

### Example 1

**Input**
```
nums = [2,5,1,3,4,7], n = 3
```
**Output**
```
[2,3,5,4,1,7]
```

**Explanation:** x1 = 2, x2 = 5, x3 = 1, y1 = 3, y2 = 4, y3 = 7, so the answer is [2,3,5,4,1,7].

### Example 2

**Input**
```
nums = [1,2,3,4,4,3,2,1], n = 4
```
**Output**
```
[1,4,2,3,3,2,4,1]
```

**Explanation:** The first half is [1,2,3,4] and the second half is [4,3,2,1]; they are interleaved one by one.

### Example 3

**Input**
```
nums = [1,1,2,2], n = 2
```
**Output**
```
[1,2,1,2]
```

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/shuffle-the-array).