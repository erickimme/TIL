# [CodoingBat](http://codingbat.com/) _ Java Warmup1
## Problem : Warmup-1 > posNeg
Given 2 int values, return true if one is negative and one is positive. 

Except if the parameter "negative" is true, then return true only if both are negative.

posNeg(1, -1, false) → true

posNeg(-1, 1, false) → true

posNeg(-4, -5, true) → true

### My Work
```java
public boolean posNeg(int a, int b, boolean negative) {
  if (negative && a<0 && b<0){
    return true;
  }
  else if ( !negative && ((a<0 && b>0) || (a>0 && b<0))) {
    return true;
  }
  else 
  return false;
}
```
### Solution
```java
public boolean posNeg(int a, int b, boolean negative) {
  if (negative) {
    return (a < 0 && b < 0);
  }
  else {
    return ((a < 0 && b > 0) || (a > 0 && b < 0));
  }
}
```
=====




