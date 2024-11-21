<div align='center'>
   
   # ⚙️ HyoPy
  파이썬을 이용한 크롤링 및 업무 자동화 프로그램
   
  <img src="https://img.shields.io/badge/status-active-brightgreen" alt="Project Status">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
  <img src="https://img.shields.io/github/languages/top/LSH-1082/HyoPy" alt="Top Language">

   
</div>


## 📖 목차
1. [📋 프로젝트 소개](#-프로젝트-소개)
2. [✨ 주요 기능](#-주요-기능)
3. [🛠️ 기술 스택](#%EF%B8%8F-기술-스택)
4. [🧱 실행파일 생성 방법](#-실행파일-생성-방법)
5. [🤝 기여 방법](#-기여-방법)


## 📋 프로젝트 소개

이 프로젝트는 웹 크롤링을 사용해 사람 이름을 자동으로 추출하고, 그에 맞는 PDF 파일 페이지를 분리하여 저장하는 기능을 제공합니다. 사용자에게 편리한 GUI를 제공하여 직관적으로 작업을 수행할 수 있도록 구현되었습니다.

## ✨ 주요 기능

1. **웹 크롤링**  
   - 웹 크롤링을 사용하여 특정 웹사이트에서 사람 이름을 자동으로 추출후 폴더 생성 
2. **PDF Slice**  
   - 크롤링한 사람의 이름을 PDF 파일에서 찾은 후, 그 사람과 관련된 페이지를 찾아 잘라내어 해당 사람에게 맞는 PDF 페이지를 분리하여 저장
3. **GUI 프로그램**  
   - GUI를 제공하여 누구나 쉽게 사용할 수 있도록 구현

## 🛠️ 기술 스택


**개발언어**
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)



**사용 도구**
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

**사용 모듈**
- ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white)
- tkinter
- PyMuPDF-fitz
- -pyinstaller
- os

## 🧱 실행파일 생성 방법 ##
```
   pyinstaller -w -F fileFolderSelector.py pyinstaller -w -F elder.py
   -w -> 실행파일을 실행했을 때 콘솔창이 안뜨게 해주는 옵션
   -F -> 실행파일을 만들었을 때 다른 잡다한 파일없이 실행파일만 생성해주는 옵션
   pyinstaller -w -F elder.py --hidden-import selenium
   모듈 포함 패키징 '--hidden-import 모듈명'
```

## 🤝 기여 방법

1. 이 레포지토리를 포크합니다.
2. 새로운 브랜치를 생성합니다. (git checkout -b feature/기능명)
3. 변경사항을 커밋합니다. (git commit -m '기능 추가 내용')
4. 브랜치를 푸시합니다. (git push origin feature/기능명)
5. 풀 리퀘스트를 생성합니다.


<div align="center">
   
  🌟 **Team MintCoding** 🌟  
  
</div>

