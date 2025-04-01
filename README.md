# 셀레니움으로 넷플릭스를 제어할 수 있는가?에 대한 테스트

## Set Up

```
python -m venv selenium
```

위의 명령어를 terminal에서 실행 후 selenium 가상환경을 구축한다.

```
cd selenium
activate
```

activate명령어를 입력해서 가상 환경을 가동한다.

```
pip install selenium
```

1. 이후 본인의 크롬 버젼과 일치하는 [크롬 드라이버](https://googlechromelabs.github.io/chrome-for-testing/#stable)를 설치한다.
2. 설치된 크롬 브라우저를 selenium 폴더에 넣는다.
3. main.py를 생성 후 본인의 크롬 데이터 경로(--user-data-dir=C:/Users/{사용자 이름}/AppData/Local/Google/Chrome/User Data)와 프로필(--profile-directory=Default)을 options.add_argument()함수를 이용해서 추가한다. (example.py를 참고하라)
