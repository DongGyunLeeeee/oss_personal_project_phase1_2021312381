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

# 코드 설명
