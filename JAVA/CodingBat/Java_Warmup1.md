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
## Problem : Warmup-1 > notString 
Given a string, return a new string where "not " has been added to the front. 

However, if the string already begins with "not", return the string unchanged. Note: use .equals() to compare 2 strings.

notString("candy") → "not candy"

notString("x") → "not x"

notString("not bad") → "not bad"

### My Work
1. using "equals()"
```java
public String notString(String str) {
 if (str.length() >=3 && str.substring(0,3).equals("not")){ 
  return str;
 }
 else {
   return "not " +str;
 }
}
```
2. using "startsWtih()"
```java
public String notString(String str) {
 if (str.startsWith("not")){ 
  return str;
 }
 else {
   return "not " +str;
 }
}
```
### Solution
```java
public String notString(String str) {
  if (str.length() >= 3 && str.substring(0, 3).equals("not")) {
    return str;
  }
  
  return "not " + str;
}
```
=====
## Problem : Warmup-1 > missingChar 
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..str.length()-1 inclusive).

missingChar("kitten", 1) → "ktten"
missingChar("kitten", 0) → "itten"
missingChar("kitten", 4) → "kittn"

### My Work
```java
public String missingChar(String str, int n) {
  String before = str.substring(0,n);
  String after = str.substring(n+1, str.length());
  String conc = before + after;
  return conc;
}
```
### Solution
```java
public String missingChar(String str, int n) {
  String front = str.substring(0, n);
  
  // Start this substring at n+1 to omit the char.
  // Can also be shortened to just str.substring(n+1)
  // which goes through the end of the string.
  String back = str.substring(n+1, str.length());
  
  return front + back;
}
```
=====






