pyinstaller -w -F fileFolderSelector.py
pyinstaller -w -F elder.py

pyinstaller
-w -> 실행파일을 실행했을 때 콘솔창이 안뜨게 해주는 옵션
-F -> 실행파일을 만들었을 때 다른 잡다한 파일없이 실행파일만 생성해주는 옵션

pyinstaller -w -F elder.py --hidden-import selenium
-> 모듈 포함 패키징 '--hidden-import 모듈명'
