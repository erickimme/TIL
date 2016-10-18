# CodingBatadsfasdfkj
# Java Warmup Collection
=====
## Problem : Warmup-1 > posNeg [CodoingBat](http://codingbat.com/prob/p140449)
//Given 2 int values, return true if one is negative and one is positive. Except if the parameter "negative" is true, then return true only if both are negative.
//posNeg(1, -1, false) → true
//posNeg(-1, 1, false) → true
//posNeg(-4, -5, true) → true
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
public boolean parrotTrouble(boolean talking, int hour) {
  return (talking && (hour < 7 || hour > 20));
  // Need extra parenthesis around the || clause
  // since && binds more tightly than ||
  // && is like arithmetic *, || is like arithmetic +
}
```
=====
dd



