# [CodoingBat](http://codingbat.com/) _ Java Array-1
## Problem : Array-1 > firstLast6 
Given an array of ints, return true if 6 appears as either the first or last element in the array. The array will be length 1 or more.

firstLast6([1, 2, 6]) → true

firstLast6([6, 1, 2, 3]) → true

firstLast6([13, 6, 1, 2, 3]) → false

### My Work
```java
public boolean firstLast6(int[] nums) {
  if (nums[0] == 6 || nums[nums.length-1] == 6){
    return true;
  } else {
    return false;
  }
}
```
### Solution
```java
public boolean firstLast6(int[] nums) {
  if (nums[0] == 6) {
    return true;
  }
  if (nums[nums.length - 1] == 6) {
    return true;
  }
  return false;
  
  // Solution notes: check the first and last elements, returning true
  // if they are == 6. we are given that the array is at least length 1,
  // so we don't need to check the length before using [].
  // A solution can be written very compactly with || as just
  // return(nums[0] == 6 || nums[nums.length - 1] == 6);
}
```
=====
## Problem : Array-1 > sameFirstLast
Given an array of ints, return true if the array is length 1 or more, and the first element and the last element are equal.

sameFirstLast([1, 2, 3]) → false

sameFirstLast([1, 2, 3, 1]) → true

sameFirstLast([1, 2, 1]) → true
### My Work
```java
```
### Solution
```java
```
=====
## Problem : 

### My Work
```java
```
### Solution
```java
```
=====
## Problem : 

### My Work
```java
```
### Solution
```java
```
=====
