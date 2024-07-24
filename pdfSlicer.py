import fitz  # PyMuPDF
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox as msgbox
import os




def execute():
    document = fitz.open(pdfPath.get())
    pages = searchKeywordInPdf(document)
    slicedPages = slicePdfPage(pages, document)
    errorPeople = []
    for i in range(len(slicedPages)):
        text = extractTextFromRegion(document, slicedPages[i][0])
        slicedPages[i].insert(0, text)
        ret = extractPages(document, slicedPages[i][0], slicedPages[i][1], slicedPages[i][-1])
        if ret:
            errorPeople.append(ret)
            
    if errorPeople:
        msgbox.showerror("오류", str(errorPeople) + "님에 대한 폴더가 존재하지 않습니다 확인해주세요")
    else:
        msgbox.showinfo("완료", "파일이 모두 저장되었습니다")

def selectPdfFile():
    filePath = filedialog.askopenfilename()
    pdfPath.insert(0, filePath)
    

def selectDirectory():
    directory_path = filedialog.askdirectory()
    directoryPath.insert(0, directory_path) 


def searchKeywordInPdf(document):
    keyword = '제공기록지'
    pagesWithKeyword = []

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text(keyword)

        if keyword.lower() in text.lower():
            pagesWithKeyword.append(page_num)
    return pagesWithKeyword


def slicePdfPage(pages, document):
    tempPage = []
    resultPage = []
    cnt = 0
    num = 0
    flag = False
    while(num <= pages[-1]):
        if(flag):
            if(pages[cnt] == num):
                resultPage.append(tempPage)
                tempPage = []
                tempPage.append(num)
                cnt += 1
                flag = False
            else:
                tempPage.append(num)
        else:
            if(pages[cnt] == num):
                tempPage.append(num)
                cnt += 1
            else:
                tempPage.append(num)
                flag = True
        num += 1

    totalPage = len(document)
    remain = totalPage - (pages[-1] + 1)
    if(remain != 0):
        for i in range(1, remain + 1):
            tempPage.append(pages[-1] + i) 

    if tempPage:
        resultPage.append(tempPage)

    return resultPage
        

def extractTextFromRegion(document, pageNum):
    rect = [97.51000213623047, 68.2528076171875, 121.0999984741211, 76.2528076171875]
    page = document.load_page(pageNum)
    text = page.get_text("text", clip=fitz.Rect(rect))
    return text.strip()


def extractPages(document, name, startPage, endPage):
    outputDocument = fitz.open()

    errorPeople = ''

    for page_num in range(startPage, endPage + 1):
        page = document.load_page(page_num)
        outputDocument.insert_pdf(document, from_page=page_num, to_page=page_num)

    fileName = pdfPath.get().split("/")[-1]
    yearMonth = fileName.split("(")[1].split(")")[0]
    year = yearMonth.split(".")[0]
    month = yearMonth.split(".")[1].replace("0", "")


    outputPath = directoryPath.get() + "/수급자/" + year + "년/" + name + "/" + month + "월/"
    if os.path.exists(outputPath):
        outputPath += name + " 장기요양급여 제공기록지.pdf"
        outputDocument.save(outputPath)
    else:
        errorPeople = name
    
    return errorPeople







root = Tk()
root.title("효드림노인복지센터")
root.geometry("+700+400")
root.resizable(False, False)

fileFrame = Frame(root)
fileLabel = Label(fileFrame, text="파일 선택")
fileLabel.pack(side="left")
pdfPath = Entry(fileFrame, width=30)
pdfPath.pack(side="left")
fileButton = Button(fileFrame, width=1, height=1, text="...", command=selectPdfFile)
fileButton.pack(side="right")

directoryFrame = Frame(root)
directoryLabel = Label(directoryFrame, text="폴더 선택")
directoryLabel.pack(side="left")
directoryPath = Entry(directoryFrame, width=30)
directoryPath.pack(side="left")
directoryButton = Button(directoryFrame, width=1, height=1, text="...", command=selectDirectory)
directoryButton.pack(side="right")

btn = Button(root, text="실행", command=execute)

fileFrame.pack()
directoryFrame.pack()
btn.pack()
root.mainloop()
