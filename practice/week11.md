# Week 11 실습 기록

## 목표
PyInstaller 사용하여 게임 빌드

## 오늘 한 것
- PyInstaller 설치 및 빌드
- resource_path() 함수로 경로 조정
- .exe 실행 확인 (성공)

## resource_path() 를 써야 하는 이유
게임을 빌드한 후에는 asset폴더를 압축 해제한 후 임시 폴더에서 사용하는데, 이는 .exe 파일의 위치와 다르기 때문에 빌드 전, 후의 asset폴더 경로를 자동으로 설정하기 위해서 필요하다.

## 빌드 명령어
- pyinstaller main.py
- 결과: 에셋이 적용되지 않음

- pyinstaller --onefile --windowed --add-data "assets;assets" --name=GAME main.py
- 에셋 적용에 파일 이름까지 설정할 수 있었음


**Q1: 빌드 후 pygame 모듈을 찾을 수 없대**

- AI 답변: pygame 설치
- 결과: 컴퓨터 콘솔 대신 Thonny 콘솔 써서 해결

**Q2: pygame이 안 깔려**

- AI 답변: python 3.14.0버전은 너무 최신이라 호환되지 않을 수 있다.
- 적용 결과: 컴퓨터 콘솔 대신 Thonny 콘솔 써서 해결
