
# subprocess

os.system은 보안상 문제가 발생할수 있고, 보다 더 많은 기능을 수행할 수 있다.

```python
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None)
```

> window shell command
> https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands




| 인자                  | 설명                                                         |
| --------------------- | ------------------------------------------------------------ |
| args                  | 이곳에 써있는 명령어를 실행한다.                             |
| stdin, stdout, stderr | 표준 입력, 출력, 오류를 설정한다. (데이터를 중간에 가로채서 다른 곳으로 보낼 수 있다) |
| input                 | 입력데이터를 설정한다.                                       |
| capture_output        | True면 run 메소드에 의해 실행된 결과값을 변수에 저장할 수 있다. |
| shell                 | 쉘 화면에 출력을 할 것인가 (윈도우 쉘 명령어를 쓰려면 True해야됨) |
| cwd                   | Current Working Directory(현재 실행중인 디렉토리 반환)       |
| timeout               | 지적시간이후 해당 프로세스 정지, 삭제                        |
| check                 | True라면 Called ProcessError 예외가 발생한다. run()으로 해당 프로세스가 정상 종료되면 CompletedProcess가 선언되서 0으로 리턴되어야하는데, 이를 다른값으로 만들겠다는 뜻. 선언된 예외처리에 run()의 입력값과 데이터가 보관된다. |
| encoding              | 결과값이 기본 바이너리 형태인데 다른 방식으로 바꿀수 있음 'utf-8 등' |
| text                  | 결과값 string으로 출력                                       |
| errors                | encoding과 마찬가지                                          |
| evn                   | None 이 아니라면 지정한 새로운 환경에서 실행                 |



```python

#단순 명령실행
subprocess.run('dir', shell=True)
# dir명령은 shell에 내장되어 있으므로 true 인수 전달
subprocess.run(['ls', '-la'])


 
```



shell 실행 결과를 파일로 저장하고 싶을 때

```python
out=subprocess.check_output(['test.py'], shell=True, encoding='utf-8')
f.write(out)
```



자세한 내용 (http://blog.naver.com/PostView.nhn?blogId=sagala_soske&logNo=221280201722&parentCategoryNo=&categoryNo=118&viewDate=&isShowPopularPosts=true&from=search)