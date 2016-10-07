

# Problem name : Warmup-1 > monkeyTrouble

Reference : [CodoingBat](http://codingbat.com/prob/p181646)

# Problem Details 
We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return true if we are in trouble.

monkeyTrouble(true, true) → true
monkeyTrouble(false, false) → true
monkeyTrouble(true, false) → false

## My Work
```java
public boolean monkeyTrouble(boolean aSmile, boolean bSmile) {
  if (aSmile){ // a smile
    if (bSmile){  // b smile (a,b both smile -> trouble -> true)
      return true;
    }else { //  b don't smile (a smile, b no smile -> false)
    return false; 
    }
  }
  if (bSmile) { // b smile
    if (aSmile) { // a smile (b, a both smile -> trouble -> true)
     return true; 
    } else { // a don't smile, b smile -> false
      return false;
    }
  }
  return true; // a, b no smile 
}



```

## Solution
```java
public boolean monkeyTrouble(boolean aSmile, boolean bSmile) {
  if (aSmile && bSmile) {
    return true;
  }
  if (!aSmile && !bSmile) {
    return true;
  }
  return false;
  // The above can be shortened to:
  //   return ((aSmile && bSmile) || (!aSmile && !bSmile));
  // Or this very short version (think about how this is the same as the above)
  //   return (aSmile == bSmile);
}
```