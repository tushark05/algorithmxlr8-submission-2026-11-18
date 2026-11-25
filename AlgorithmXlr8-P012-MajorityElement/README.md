<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Majority Element

**Difficulty:** `Easy`

## Problem

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than floor(n / 2) times. You may assume that the majority element always exists in the array. Because it fills more than half of the positions, there can be only one such element, so the answer is unique.

Elements can be negative, and other values may also repeat, as long as none of them reaches the majority. For example, in [2,2,1,1,1,2,2] the value 1 appears three times but 2 appears four times out of seven, so 2 is the majority element.

Follow-up: Could you solve the problem in linear time and in O(1) space?

Input format: The first line contains the integer n. The second line contains the n integers of nums separated by spaces.

Output format: Print a single integer, the majority element.

## Examples

### Example 1

**Input**
```
nums = [3,2,3]
```
**Output**
```
3
```

**Explanation:** n = 3, so the majority element must appear more than 1 time. The value 3 appears 2 times.

### Example 2

**Input**
```
nums = [2,2,1,1,1,2,2]
```
**Output**
```
2
```

**Explanation:** n = 7, so the majority element must appear more than 3 times. The value 2 appears 4 times, while 1 appears only 3 times.

### Example 3

**Input**
```
nums = [5,5,5,5,1,2,3]
```
**Output**
```
5
```

**Explanation:** The value 5 appears 4 times out of 7, which is more than 3.

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/majority-element).