# Problem name : #Warmup-1 > nearHundred
Reference : [CodoingBat](http://codingbat.com/prob/p184004)

# Problem Details 
Given an int n, return true if it is within 10 of 100 or 200. Note: Math.abs(num) computes the absolute value of a number.

nearHundred(93) → true
nearHundred(90) → true
nearHundred(89) → false

## My Work
```java
public boolean nearHundred(int n) {
  return((Math.abs(100-n) < 11) || (Math.abs(200-n)<11));
}

```

## Solution
```java
public boolean nearHundred(int n) {
  return ((Math.abs(100 - n) <= 10) ||
    (Math.abs(200 - n) <= 10));
}
```

