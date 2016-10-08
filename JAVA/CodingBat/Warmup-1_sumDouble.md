

# Problem name : Warmup-1 > SumDouble 
Reference : [CodoingBat](http://codingbat.com/prob/p154485)

# Problem Details 
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sumDouble(1, 2) → 3 

sumDouble(3, 2) → 5 

sumDouble(2, 2) → 8 

## My Work
```java
public int sumDouble(int a, int b) {
    int sum = a + b;
    if (a == b){
      sum = 2*sum;
    }
    return sum;
}
```

## Solution
```java
public int sumDouble(int a, int b) {
  // Store the sum in a local variable
  int sum = a + b;
  
  // Double it if a and b are the same
  if (a == b) {
    sum = sum * 2;
  }
  
  return sum;
}

```


