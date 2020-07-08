# git intro

0. git cmd 기본 사용 법

   `$ mkdir 폴더명` 폴더 생성하기

   `$ cd ` 경로 이동 	

   `$ ls` 폴더 내 목록 보기 `$ ls -a` 숨겨진 것 까지 모두 보기

   `./` : 현재폴더 `../` : 상위 폴더

   `$ touch 파일명` 새 파일 생성 `$ touch .파일명` 숨김파일 생성됨

   `$ rm 파일명` 파일 삭제 `$ rm *.txt`  모든 txt파일 삭제  `$ rm -r` 폴더 지우기

   `$ pwd` 현재경로 표시

1. 초기화 `$ git int`
   1. 실제로는 `.git/` 폴더가 생성됨
   2. 버전관리가 시작 됨
   3. repo(repository)라고 부름
2. 서명 설정
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





working directory

처음 확인한 파일들 -> untracked 상태

add 하면 stage로 올린다(tracking 시작)

commit 하면 stage전체를 history로 기록, stage에서 사라짐

파일 수정 일어남

add 하면 stage로 올린다(바뀐 부분만 올라감)

commit 하면 history로 기록(바뀐부분 기록)