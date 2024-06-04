# oss_personal_project_phase1_2021312381
# Reference
[1] <https://github.com/pygame/pygame> "pygame"
# 지원 Operating Systems 및 실행 방법
+ ## MacOS
#### 1. Python 설치
  Pygame을 설치하기 전에 Python이 설치되어 있는지 확인해야 합니다. macOS에는 기본적으로 Python이 설치되어 있지만, 최신 버전을 사용하기 위해 Python 설치를 권장합니다.
  
   a. [Python 공식 웹사이트](https://www.python.org/)로 이동하여 최신 Python 버전을 다운로드합니다.
  
   b. 다운로드한 설치 파일을 실행하고 지시에 따라 Python을 설치합니다.
  
   c. 설치가 완료되면 터미널을 열어 다음 명령어를 입력하여 Python이 정상적으로 설치되었는지 확인합니다:
```
python3 --version
```
   pip는 Python 패키지 관리자입니다. Python을 설치하면 자동으로 pip도 설치됩니다. pip가 정상적으로 설치되었는지 확인하려면 터미널에 다음 명령어를 입력합니다:
```
pip3 --version
```
#### 2. 가상환경 설정
   가상환경을 만들고자 하는 디렉토리로 이동합니다.
```
mkdir ~/Projects/my_pygame_project
cd ~/Projects/my_pygame_project
```
   venv 모듈을 사용하여 가상환경을 생성합니다.
```
python3 -m venv venv
```
#### 3. 가상환경 활성화
   가상환경을 활성화하려면 다음 명령어를 입력합니다.
```
source venv/bin/activate
```
#### 4. Pygame 설치
   가상환경이 활성화된 상태에서 Pygame을 설치합니다.
```
pip install pygame
```
#### 5. 실행
   가상환경 경로에서 stackgame.py를 실행합니다.
```
~/Projects/my_pygame_project/myenv/bin/python stackgame.py
```

# 실행 예시
![화면-기록-2024-06-04-오후-3 56 52](https://github.com/DongGyunLeeeee/oss_personal_project_phase1_2021312381/assets/83210475/8acedd20-a9f7-46fb-8919-38783336dfec)

# 코드 설명
## stackgame.py
### class Block
+ description: stackgame에서 stack될 block의 정보가 담긴 클래스

    i. Def init: block의 x좌표, y좌표, 너비, 높이, 색, 속도를 초기화함.
  
    ii. Def draw: block을 화면에 표시함.
  
    iii. Def move: 움직이는 block이 왼쪽, 오른쪽 양쪽 화면에 닿으면 반대로 움직이게 함.
  
### class Stack
+ description: stackgame을 수행하는 메인 클래스
  
    i. Def init: 게임 실행 시 기본으로 깔려 있는 block을 stack 배열 안에 초기화함.
  
    ii. Def show: 범위 내 block을 draw함.
  
    iii. Def move: 범위 내 block의 move를 관리함.
  
    iv. Def adding: block을 추가함.

    v. Def stacking: 움직이는 block과 바로 아래에 있는 마지막 block을 비교하여 게임을 이어가거나 종료함.
### def scoreboard
+ description: 현재 점수를 나타냄.
### def highestboard
+ description: 최고 점수를 나타냄.
### def ending
+ description: stackgame이 종료되었을 때, 최고점 갱신 기능을 수행하고 스페이바를 눌러 재시작하거나 'Q'를 눌러 pygame을 종료함.
### def close
+ description: pygame을 종료함.
### def explain
+ description: pygame 실행 시 나오는 화면으로 조작키를 설명함.
### def game
+ description: stackgame이 실행되는 loop임.
