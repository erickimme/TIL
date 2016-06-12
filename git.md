# Git, git-flow 
Git의 정의, 설정, 기본 명령어 정리, 절차,


<<<<<<< HEAD
-[Git 정의](#Git 정의)
	- Version Control, 혼자 개발이 아닌 여러명이 함께 작업을 하는 환경에서 코드의 변화를 추적하는 목적이 있다.


-[Git 설정](#Git 설정)
	+ 추후 공부 후 정리 예정


-[Git 기본 명령어 정리](#Git 기본 명령어 정리)


+ `git init` : 버전 관리할 폴더에 처음에 딱 한 번만 해준다. 이 디렉토리를 git으로 버전관리하겠다는 의미.
+ 가장 많이 사용하는 명령어는 다음 세 가지다. `status`, `add`, `commit`.
=======

### 1. Git 정의
	- Version Control, 혼자 개발이 아닌 여러명이 함께 작업을 하는 환경에서 코드의 변화를 추적하는 목적이 있다.

### Git 설정
	- 추후 공부 후 정리 예정


### Git 기본 명령어 정리
	+ `git init` : 버전 관리할 폴더에 처음에 딱 한 번만 해준다. 이 디렉토리를 git으로 버전관리하겠다는 의미.
	+ 가장 많이 사용하는 명령어는 다음 세 가지다. `status`, `add`, `commit`.
>>>>>>> db2a82439fcf61a6d7e341e40a538594dd996dc9


	```sh
	git status      # 현재 파일들의 상태를 본다.
	git add file_name   # 특정 파일의
	현재 상태를 stage 상태로 만들기.
<<<<<<< HEAD
    git commit -m "commit message"  # 짧은 메시지와 함께 커밋	    

    ```
=======
    	git commit -m "commit message"  # 짧은 메시지와 함께 커밋	    
	git pull upstream master # 호스트의 새로 업데이트된 파일 끌어오기
	``` 


### GitHub 작업 절차
	1. 호스트가 Repository (저장소) 폴더를 만듬

	2. Fork해서 뜯어옴 (온라인 상에 복사됨)
	   : 개인 깃헙 계정으로 가져감
	   : Copy Only (사본은 마음대로 수정해도됨)

	3. Desktop>Local로 복사해오기 
		-git init (git과 내 계정과 컴퓨터 상에서 
		-git clone “클립보드에 복사된 것 붙여넣기"
		-cd  “폴더명”
		-Sublime 등의 text editor에서 작업하기
		-ls - a (관리하는 파일 항목들 보기)
 		-ls -al  (관리하는 파일 좀 더 자세하게 보기)

	4. 본격적인 Git 하기  (Local 에서 작업)
		: git add "파일명(예 : firstReverse.js)"
		: git add -A  (모든 파일 업데이트하기)
 		: git add .  (모든 파일 업데이트하기)
		: git status
		: git commit -m “이유를 여기에 적는다” (ex) git commit -m “firstReverse update”)

	5. Web상에 작업한 것을 업로드하기
		: git remote origin
		: git push origin
		: commit된 내용이 최종으로 업로드 됨됨 (fork해서 내 계정으로 뜯어온 내 작업 업데이트 됨)
			**git pull 타작업자가 자료 끌어올 때 쓰는 명령어

	-6. 호스트에게 작업한 것 반영해달라고 요청 (쪼르기)
		+ 호스트의 개인 repository 페이지로 이동
		+ “Pull request” 클릭
		+ “New pull request” 클릭
		
	**절차 정리**
	Fork -> Clone -> Local (ADD -> Commit) -> PUSH -> pull request 
>>>>>>> db2a82439fcf61a6d7e341e40a538594dd996dc9


### 또 다른 개념
	+ Branch
		-협력하는 과정에서 따로 작업을 해놓고 완성이 되면 합치기도 한다. 
		-같은 파일을 두 사람이 수정하는 경우
		-충돌...이 나는 경우도있는데 이런 경우는 어떤 코드를 쓸지 정해야함
		-토이프러블럼 모범답안 보는 법법
