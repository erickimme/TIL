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
## Problem : Warmup-1 > frontBack
Given a string, return a new string where the first and last chars have been exchanged.

frontBack("code") → "eodc"

frontBack("a") → "a"

frontBack("ab") → "ba"

### My Work
```java
public String frontBack(String str) {
  if (str.length() <=1) {
  return str;
  }
  int len = str.length();
  char first = str.charAt(0);
  char last = str.charAt(len-1);
  String mid = str.substring(1, len-1);
  //code -> c + od + e ----> first and last needed to be swapped
  // last + mid + first
  return last + mid + first;
}
```
### Solution
```java
public String frontBack(String str) {
  if (str.length() <= 1) return str;
  
  String mid = str.substring(1, str.length()-1);
  
  // last + mid + first
  return str.charAt(str.length()-1) + mid + str.charAt(0);
}
```
=====
## Problem : Warmup-1 > front3 
Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.

front3("Java") → "JavJavJav"

front3("Chocolate") → "ChoChoCho"

front3("abc") → "abcabcabc"

### My Work
```java
public String front3(String str) {
  int len = str.length();
  if (len <3){
    String front3 = str + str + str;
    return front3;
  } else {
    String frontMore3 = str.substring(0,3) + str.substring(0,3) + str.substring(0,3);
    return frontMore3;
  }
}
```
### Solution
```java
public String front3(String str) {
  String front;
  
  if (str.length() >= 3) {
    front = str.substring(0, 3);
  }
  else {
    front = str;
  }

  return front + front + front;
}
```
=====
## Problem : Warmup-1 > backAround 
Given a string, take the last char and return a new string with the last char added at the front and back, so "cat" yields "tcatt". The original string will be length 1 or more.

backAround("cat") → "tcatt"

backAround("Hello") → "oHelloo"

backAround("a") → "aaa"

### My Work
```java
public String backAround(String str) {
  int len = str.length();
  char last;
  last = str.charAt(len-1);
  
  return last + str.substring(0,len) + last;
}
```
### Solution
```java
public String backAround(String str) {
  // Get the last char
  String last = str.substring(str.length() - 1);
  return last + str + last;
}
```
=====
## Problem : Warmup-1 > or35 
Return true if the given non-negative number is a multiple of 3 or a multiple of 5. Use the % "mod" operator -- see Introduction to Mod

or35(3) → true

or35(10) → true

or35(8) → false

### My Work
```java
public boolean or35(int n) {
  if (n%3 == 0 || n%5 == 0) {
  return true;
  } else {
    return false;
  }
}
```
### Solution
```java
public boolean or35(int n) {
  return (n % 3 == 0) || (n % 5 == 0);
}
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
## Problem : 

### My Work
```java
```
### Solution
```java
```
=====



