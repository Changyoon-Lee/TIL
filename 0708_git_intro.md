# git intro

0. git cmd 기본 사용 법

   `$ mkdir 폴더명` 폴더 생성하기

   `$ cd ` 경로 이동 	

   `$ ls` 폴더 내 목록 보기 `$ ls -a` 숨겨진 것 까지 모두 보기

   `./` : 현재폴더 `../` : 상위 폴더

   `$ touch 파일명` 새 파일 생성 `$ touch .파일명` 숨김파일 생성됨

   `$ rm 파일명` 파일 삭제 `$ rm *.txt`  모든 txt파일 삭제  `$ rm -r` 폴더 지우기

   `$ pwd` 현재경로 표시



## local git

1. git 다운로드 및 설치 
2. 초기화 `$ git int`
   1. 실제로는 `.git/` 폴더가 생성됨
   2. 버전관리가 시작 됨
   3. repo(repository)라고 부름
3. 서명 설정
   1. `$ git config --global user.name 'name'`
   2. `$ git config --global user.email 'email@mail'`

3. 리포의 상태 보기(stage의 상태) `$ git status`

4. stage에 올리기 `$ git add`

   - 특정파일만 올리기 `$ git add 파일명1 파일명2` 

   - 내 위치 폴더 내 수정된 것 다올리기 `$ git add .`

5. snapshot 찍기 `$ git commit`

6. 로그 보기 `$ git log`

7. 상태 보기 `$ git status`

8. git diff : 변경된부분 나타냄

9. git reset : 수정하기 전으로 되돌아가기

### 집 컴퓨터 세팅

1. git 다운 및 설치
2. `$ git config --global ....` 
3. `$ git clone <URL>` : `$ git removt -v`로 경로 알 수 있음, github에서 Clone with https
4. 



working directory

처음 확인한 파일들 -> untracked 상태

add 하면 stage로 올린다(tracking 시작)

commit 하면 stage전체를 history로 기록, stage에서 사라짐

파일 수정 일어남

add 하면 stage로 올린다(바뀐 부분만 올라감)

commit 하면 history로 기록(바뀐부분 기록)

삭제할떄도 add commit작업 수행해야 한다.

## github

1. 원격 저장소(remote repository) 생성

2. local repo => remote repo  연결 `$ git remote add origin <URL>`

3. local commit 들을 remote로 보내기 `$ git push origin master`

4. `$ git push` == `$ git push origin master`로 단축 명령하기

   `$ git push -u origin master`

5. 다른 컴퓨터에서 remote repo 받아오기(**최초 1회**)

   `$ git clone <URL>`

6. 이후 remote repo 변경사항을 local repo에서 반영하기

   `$ git pull`



## TIL 관리 시나리오

1. 멀캠에 온다.
2. `$ git pull`
3. 열공
4. `$ git add` & `$git commit` 으로  중간중간 저장
5. 퇴근 전 `$ git push`
6. 집에서 켜서 동기화를 위해 ` $ git pull`
7. 수정 후 `$ git add와 commit`, `$ git push`