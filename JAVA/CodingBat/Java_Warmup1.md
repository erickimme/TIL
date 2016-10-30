# [CodoingBat](http://codingbat.com/) _ Java Warmup1
Simple warmup problems to get started (solutions available)

## Problem name : Warmup-1 > parrotTrouble #
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return true if we are in trouble.

parrotTrouble(true, 6) → true

parrotTrouble(true, 7) → false

parrotTrouble(false, 6) → false

## My Work
```java
public boolean parrotTrouble(boolean talking, int hour) {
  return(talking && (hour <7 || hour >20));
}
```
## Solution
```java
public boolean parrotTrouble(boolean talking, int hour) {
  return (talking && (hour < 7 || hour > 20));
  // Need extra parenthesis around the || clause
  // since && binds more tightly than ||
  // && is like arithmetic *, || is like arithmetic +
}
```
=====
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
## Problem : Warmup-1 > front22
Given a string, take the first 2 chars and return the string with the 2 chars added at both the front and back, so "kitten" yields"kikittenki". If the string length is less than 2, use whatever chars are there.

front22("kitten") → "kikittenki"

front22("Ha") → "HaHaHa"

front22("abc") → "ababcab"

### My Work
```java
public String front22(String str) {
 if (str.length() < 2){
   return str+str+str;
 } else {
 String firstTwo = str.substring(0,2);
  return firstTwo + str + firstTwo; 
 }
}
```
### Solution
```java
public String front22(String str) {
  // First figure the number of chars to take
  int take = 2;
  if (take > str.length()) {
    take = str.length();
  }
  
  String front = str.substring(0, take);
  return front + str + front;
}
```
=====
## Problem : Warmup-1 > startHi 
Given a string, return true if the string starts with "hi" and false otherwise.

startHi("hi there") → true

startHi("hi") → true

startHi("hello hi") → false

### My Work
```java
public boolean startHi(String str) {
  if (str.length() <2){
    return false;
  }
  if (str.substring(0,2).equals("hi")){
    return true;  
  } else {
    return false;
  }
}
```
### Solution
```java
public boolean startHi(String str) {
  // First test if the string is not at least length 2
  // (so the substring() below does not go past the end).
  if (str.length() < 2) return false;
  
  // Pull out the string of the first two chars
  String firstTwo = str.substring(0, 2);
  
  // Test if it is equal to "hi"
  if (firstTwo.equals("hi")) {
    return true;
  } else {
    return false;
  }
  // This last part can be shortened to: return(firstTwo.equals("hi"));
}
```
=====
## Problem : Warmup-1 > icyHot
Given two temperatures, return true if one is less than 0 and the other is greater than 100.

icyHot(120, -1) → true

icyHot(-1, 120) → true

icyHot(2, 120) → false

### My Work
```java
public boolean icyHot(int temp1, int temp2) {
  if((temp1 < 0 && temp2 > 100) || (temp1 > 100 && temp2 < 0)){
    return true;
  } else {
    return false;
  }
}
```
### Solution
```java
public boolean icyHot(int temp1, int temp2) {
  if ((temp1 < 0 && temp2 > 100) || (temp1 > 100 && temp2 < 0)) {
    return true;
  } else {
    return false;
  }
  // Could be written as: return ((temp1 < 0 && ...));
}

```
=====
## Problem : Warmup-1 > in1020 
Given 2 int values, return true if either of them is in the range 10..20 inclusive.

in1020(12, 99) → true

in1020(21, 12) → true

in1020(8, 99) → false

### My Work
```java
public boolean in1020(int a, int b) {
  if((a >= 10 && a <= 20) || (b >= 10 && b <= 20)){
    return true;
  } else {
    return false;
  }
}

```
### Solution
```java
public boolean in1020(int a, int b) {
  return ((a >= 10 && a <= 20) || (b >= 10 && b <= 20));
}
```
=====
## Problem : Warmup-1 > hasTeen 
We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 3 int values, return true if 1 or more of them are teen.

hasTeen(13, 20, 10) → true

hasTeen(20, 19, 10) → true

hasTeen(20, 10, 13) → true

### My Work
```java
public boolean hasTeen(int a, int b, int c) {
  if ((a >= 13 && a <= 19) || (b >= 13 && b <= 19) || (c >= 13 && c <= 19)){
    return true;
  } else {
    return false;
  }
}
```
### Solution
```java
public boolean hasTeen(int a, int b, int c) {
  // Here it is written as one big expression,
  // vs. a series of if-statements.
  return (a>=13 && a<=19) ||
         (b>=13 && b<=19) ||
         (c>=13 && c<=19);
}
```
=====
## Problem : Warmup-1 > loneTeen
We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 2 int values, return true if one or the other is teen, but not both.

loneTeen(13, 99) → true

loneTeen(21, 19) → true

loneTeen(13, 13) → false

### My Work
```java
public boolean loneTeen(int a, int b) {
  boolean aTeen = (a >= 13 && a <= 19);
  boolean bTeen = (b >= 13 && b <= 19);
  
  if ((aTeen && !bTeen) || (bTeen && !aTeen)){
    return true;
  } else {
    return false;
  }
}
```
### Solution
```java
public boolean loneTeen(int a, int b) {
  // Store teen-ness in boolean local vars first. Boolean local
  // vars like this are a little rare, but here they work great.
  boolean aTeen = (a >= 13 && a <= 19);
  boolean bTeen = (b >= 13 && b <= 19);
  
  return (aTeen && !bTeen) || (!aTeen && bTeen);
  // Translation: one or the other, but not both.
  // Alternately could use the Java xor operator, but it's obscure.
}
```
=====
## Problem : Warmup-1 > delDel 
Given a string, if the string "del" appears starting at index 1, return a string where that "del" has been deleted. Otherwise, return the string unchanged.

delDel("adelbc") → "abc"

delDel("adelHello") → "aHello"

delDel("adedbc") → "adedbc"
### My Work
```java
public String delDel(String str) {
  if (str.length() >= 4 && str.substring(1,4).equals("del")) {
    //before "del"
    String before = str.substring(0,1);
    //after "del"
    String after = str.substring(4,str.length());
    return before + after;
  } else{
    return str;
  }
}
```
### Solution
```java
public String delDel(String str) {
  if (str.length()>=4 && str.substring(1, 4).equals("del")) {
    // First char + rest of string starting at 4
    return str.substring(0, 1) + str.substring(4);
  }
  // Otherwise return the original string.
  return str;
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







