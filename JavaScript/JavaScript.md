#JavaScript


[생활코딩_비교(3/4)](http://opentutorials.org/module/532/4722) : ===를 사용하자

[강의영상](https://youtu.be/rN0045zf-y4?list=PLuHgQVnccGMA4uSig3hCjl7wTDeyIeZVU)


== : 동등연산자

=== : 일치연산자


###DataType

`undefined` : 값이 없다. 프로그래머가 의도하지 않은 상황

`null` : 값이 없다. 프로그래머가 의도하여 값이 없는 상태를 의도적으로 부여한것값이 없다.

예) undefined
```undifned 
var a;
alert(a);
```

예) null
```null
var a = null;
alert(a);
```

비교)
```
alert(undefined == null);   //true
alert(undefined === null);  //false
alert(true == 1);           //true
alert(true == 2);          //false : 숫자 1이 아닌 것들은 false로 간
alert(true === 1);          //false
alert(true == '1');         //true
alert(true === '1');        //false

alert(0 === -0);            //true
alert(NaN === NaN);         //false
                            // **Note : NaN은 0/0과 같은 연산의 결과로 만들어지는 특수 데이텨형으로 '계산할 수 없음' 혹은'숫자가 아님'을 뜻함.
```

## **DataType**

+ Boolean
: true/false

+ Number
: -1, 0, 1, 2, 3

+ String
:"a" "b" "c"

+ Undefined
: undefined

+ null
: null

---

생활코딩_비교(4/4)](http://opentutorials.org/module/532/4722) : 부정과 부등호

[강의영상](https://youtu.be/rN0045zf-y4?list=PLuHgQVnccGMA4uSig3hCjl7wTDeyIeZVU)

`<`
`>`




