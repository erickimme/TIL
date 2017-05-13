// # Author: eric kim
// # Date : 2017-05-12

// # Elice 코딩 유치원 - 자바 주말반 
// # 강의 소개 
// # 유재영 강사, 김창현, 유준배 조교 @일 20:00~22:40 (20:00-21:15) (21:30-22:40)
// # 2017/4/23 ~ 6/11
// # 주차별 커리큘럼
// # 	1주차 : 언어소개 & 키워드와 식별자 (4/23)
// #	2주차 : 데이터 타입 (4/30)
// # 	3주차 : 제어구조 (5/7)
// # 	4주차 : 연산자와 제어구조 (5/14)
// # 	5주차 : 제어구조와 배열 (5/21)
// # 	6주차 : 객체지향 프로그래밍 개요 (5/28)
// # 	7주차 : 클래스와 객체 (6/4)
// # 	8주차 : 생성자와 객체 생성 (6/11)
// # 
// # 화면 세팅 : 와이드 모드 로 강의 와 코드 작성을 동시에 진행 (개이득)
// # 도움 요청 : 막히면 질문 (개이득) -> 추후 질문은 헬프 센터로 이동
// # 샌드박스 : 온라인 코딩 에디터 main.py (실습) + note.txt (필기)
// # main.py : 단축키 (ctrl + shift + enter)

/******* 1주차 : 코스 및 자바 언어 소개********************************************
* 1. 자바의 역사 : 다양한 소형 가전기기에서 실행 간으한 호환성 있는 언어를 위한 Green Project에서 시작
* 	Sun Microsystem : Debut in 1995
* 	"Write Once, Run Anywhere (WORA)"
* 	최신 버전 : JAVA SE 8.0 (3.18.2014)
* 2. JAVA의 강점 : 1) Platform Independent 2) Object-oriented Programming
* 3. Java Application Running Process
* 	: Source code (HelloWorld.java) -> (compile) -> byte code (HelloWorld.class) -> (excute) -> JVM (Java Virtual Machine) -> Platform (OS, HW, Resrouces)
* 	소스파일, 실행파일, JVM, Platform이라는 4단계가 존재하는데 단계가 복잡한 만큼 flexibility 가 높아진다.
* 4. Java Program 구조
*		package korea.seoul; 			-> 패키지 선언문
*		pulbic class HellowWorld {  	-> 클래스 선언문
*			int age = 30; 				-> 필드 선언
*			public void go(){			-> 메소드 선언
*				System.out.println(++age); 
*			}
*		}
* 5. Java Program 실행해보기
*	패키지, 클래스, 메소드 
*
* 6. 키워드(keyword)와 식별자
* 	1) keyword : 자바에서 이미 사용하고 있는 값 (abstract, goto, public 등등)
*		유사키워드 : true, false, null
* 
*	2) Identifier (식별자) : 프로그램 작성 시 사용자가 정의한 후 사용하는 개체들
*		a. 식별자의 종류 : 변수, 상수 | 메소드 | 클래스, 인터페이스, 패키지
*		b. 식별자의 특징
*			i. 글자 길이 제한 없음
*			ii. 시작은 문자나 특수문자($, _)로 함
*			iii. 시작문자 뒤 문자,숫자, 특수문자 *혼합 사용 가능
*			iv. 대소문자 구분, 키워드 사용x, 공백 사용x
*		c. 식별자의 예
*			1) class Hello{}  			(o)
*			2) class hello{}  			(o)
*			3) class Name$3{} 			(o)
*			4) class Imported_Car{} 	(o)
*			5) class 3D_Movie{} 		(x : 숫자로 시작)
*			6) class *Buck{} 			(x : _, $로만 시작 가능)
*			7) class this{} 			(x : keyword 사용한 이름)
*			8) class This{}				(o)
*			9) class star wars{}		(x : 공백 안됨)			
*
* 7. 변수 (Variable)
*	1) 변수의 정의 : 어떤 값을 저장하는 공간 
*				: ex) 문자열, 숫자(정수, 실수), 논리값
*				: String name -> "tommy"
*	2) 변수 예 	: 변수타입 + 변수 이름 + 변수값
*				: String    company =  "Orange Company";
*				: int 		age 	= 30;
****************************************************************************/

/******* 2주차 : 키워드와 식별자 & 데이터 타입 (4/30)*********************************
* 1. 키워드 (Keyword)
*	: 미리 예약된 단어 (abstract, assert, boolean ...)
* 	: 모두 소문자
*	: goto, const는 사용하지 말아라
*
* 2. 식별자 (Identifier)
*	:  사용자가 정의한 후 사용하는 개체들
*		1. 변수,상수 2. 메소드, 3. 클래스,인터페이스,패키지
*	: 길이 제한x
*	: 시작은 문자, 특수문자($_)로만함 + 아무거나 가능
*	: 대소문자 구분, 키워드 사용불가, 공백 사용 불가
*
* 3. 변수 	(Variable)
	: 값을 저장하는 공간 (그릇)
	: 문자열, 숫자(정수, 실수), 논리값
	: name = "tommy";

* 4. 리터럴	(Literal)
	1) 정의: 어떤 값 자체 -> 변수값에 들어간다. 
			String name = "Tommy"
			변수타입 변수명   변수값  --------> 리터럴!
	2) 예 : 7, 156, 3.2, '아', "TOM", true
		: int age = 30; -> 30을 literal이라고함
	3) 종류
		a. 정수 리터럴 : -141
		b. 실수 리터럴 : -1.2, 13.5 
		c. 문자(캐릭터) 리터럴 :'c'
		d. 문자열 리터럴 : "Seoul"
		e. 논리 리터럴 : true, false

* 5. 데이터타입	(Data Type)
	1) 정의 : 데이터들의 종류
	2) 종류 *자바 데이터 타입은 2종류가 있으며 무조건 둘 중 하나이다.
		a. 기본형 (primitive type)
			i. 논리형 (boolean) : true (참), false (거짓)
			ii. 숫자형
				가. 정수형
					a) byte(1)  = 8*bits
					b) short(2)
					c) int(4)
					d) long(8)
					e) char(2) : 한 글자를 저장할 수 있는 데이터 타입
				나. 실수형
					a) float(4) -> float f = 9.23f 
						*JVM에서 데이터 저장 크기를 정할 때 double(8)과 float(4)의 혼란을 막기위해 
						 float타입 변수의 뒤에 f를 입혁한다.
					b) double(8)
			*데이터타입 기본형 정리*
			-------------------------------------------------------------
			|종류		|값 	       |크기(bit)|값의범위					|기본값	|
			-------------------------------------------------------------
			|boolean|논리값      |1		|true,false				|false	|*
			|byte	|정수       |8		|-128~127				|0		|
			|short	|정수       |16		|-32768~32767			|0		|
			|int 	|정수       |32		|-2147483648~2147483647	|0		|*
			|long	|정수       |64		|-2^63~2^63-1			|0		|
			|char	|Unicode문자|16		|0~65535				|0		|*
			|float	|실수       |32		|-3.4e^38~3.4e^38		|0.0	|
			|double	|실수       |64		|-1.7e^308~1.7e^308		|0.0	|*
			-------------------------------------------------------------

		b. 참조형 (reference type)
			i. 클래스, 인터페이스, 배열, 열거형
	3) 사용 : 변수, 상수 선언 시 사용
		a. 상수 : 값이 한번 정해지면 값을 바꿀 수 없다. 
			ex) final double pi = 3.141592;
				final int speed = 200;
* 
*
****************************************************************************/


