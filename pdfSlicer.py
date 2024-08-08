import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox as msgbox
import os

def option1():
    keyword = "목욕도움 제공 기록지"
    document = fitz.open(pdfPath.get())
    pages = searchKeywordInPdf(document, keyword.split(" ")[0])
    slicedPages = slicePdfPage(pages, document)
    rect = [111.12000274658203, 114.57763671875, 143.66000366210938, 125.57763671875]
    for i in range(len(slicedPages)):
        text = extractTextFromRegion(document, slicedPages[i][0], rect)
        slicedPages[i].insert(0, text)
        extractPages(document, slicedPages[i][0], slicedPages[i][1], slicedPages[i][-1], keyword)
    msgbox.showinfo("완료", "파일이 모두 저장되었습니다")


def option2():
    keyword = "상태변화 기록지"
    document = fitz.open(pdfPath.get())
    pages = searchKeywordInPdf(document, keyword.split(" ")[1])
    slicedPages = slicePdfPage(pages, document)
    rect = [111.12000274658203, 86.23760986328125, 143.66000366210938, 97.23760986328125]
    for i in range(len(slicedPages)):
        text = extractTextFromRegion(document, slicedPages[i][0], rect)
        slicedPages[i].insert(0, text)
        extractPages(document, slicedPages[i][0], slicedPages[i][1], slicedPages[i][-1], keyword)
    msgbox.showinfo("완료", "파일이 모두 저장되었습니다")


def option3():
    keyword = "프로그램관리자 업무수행일지"
    document = fitz.open(pdfPath.get())
    pages = searchKeywordInPdf(document, keyword.split(" ")[0])
    slicedPages = slicePdfPage(pages, document)
    rect = [94.11000061035156, 113.1676025390625, 126.6500015258789, 124.1676025390625]
    for i in range(len(slicedPages)):
        text = extractTextFromRegion(document, slicedPages[i][0], rect)
        slicedPages[i].insert(0, text)
        extractPages(document, slicedPages[i][0], slicedPages[i][1], slicedPages[i][-1], keyword)
    msgbox.showinfo("완료", "파일이 모두 저장되었습니다")


def option4():
    keyword = "상담일지"
    document = fitz.open(pdfPath.get())
    pages = searchKeywordInPdf(document, keyword)
    slicedPages = slicePdfPage(pages, document)
    rect = [111.12000274658203, 86.23760986328125, 143.66000366210938, 97.23760986328125]
    for i in range(len(slicedPages)):
        text = extractTextFromRegion(document, slicedPages[i][0], rect)
        slicedPages[i].insert(0, text)
        extractPages(document, slicedPages[i][0], slicedPages[i][1], slicedPages[i][-1], keyword)
    msgbox.showinfo("완료", "파일이 모두 저장되었습니다")


def option5():
    keyword = "장기요양급여 제공기록지"
    document = fitz.open(pdfPath.get())
    pages = searchKeywordInPdf(document, keyword.split(" ")[0])
    slicedPages = option5SlicePdfPage(pages, document)
    rect = [97.51000213623047, 68.2528076171875, 121.0999984741211, 76.2528076171875]
    for i in range(len(slicedPages)):
        text = extractTextFromRegion(document, slicedPages[i][0], rect)
        slicedPages[i].insert(0, text)
        extractPages(document, slicedPages[i][0], slicedPages[i][1], slicedPages[i][-1], keyword)
    msgbox.showinfo("완료", "파일이 모두 저장되었습니다")


def unknown():
    msgbox.showerror("오류", "옵션을 선택하세요!")
    return


def executeAction(actionName):
    return actions.get(actionName, unknown)()


actions = {
    "목욕도움 제공 기록지": option1,
    "상태변화 기록지": option2,
    "프로그램관리자 업무수행일지": option3,
    "상담일지": option4,
    "장기요양급여 제공기록지": option5,
}


def execute(): 
    actionName = radioVar.get()
    executeAction(actionName)


def selectPdfFile():
    filePath = filedialog.askopenfilename()
    pdfPath.delete(0, tk.END)
    pdfPath.insert(0, filePath)
    

def selectDirectory():
    directory_path = filedialog.askdirectory()
    directoryPath.delete(0, tk.END)
    directoryPath.insert(0, directory_path) 


def searchKeywordInPdf(document, keyword):
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
    flag = True
    while(num <= pages[-1]):
        if(flag):
            if(pages[cnt] == num):
                resultPage.append(tempPage)
                tempPage = []
                tempPage.append(num)
                cnt += 1
            else:
                tempPage.append(num)
                flag = False
        else:
            if(pages[cnt] == num):
                resultPage.append(tempPage)
                tempPage = []
                tempPage.append(num)
                cnt += 1
                flag = True
            else:
                tempPage.append(num)
        num += 1

    totalPage = len(document)
    remain = totalPage - (pages[-1] + 1)
    if(remain != 0):
        for i in range(1, remain + 1):
            tempPage.append(pages[-1] + i) 

    if tempPage:
        resultPage.append(tempPage)
    
    resultPage.pop(0)

    return resultPage


def option5SlicePdfPage(pages, document):
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
        

def extractTextFromRegion(document, pageNum, rect):
    page = document.load_page(pageNum)
    text = page.get_text("text", clip=fitz.Rect(rect))
    return text.strip()


def extractPages(document, name, startPage, endPage, keyword):
    outputDocument = fitz.open()


    for page_num in range(startPage, endPage + 1):
        page = document.load_page(page_num)
        outputDocument.insert_pdf(document, from_page=page_num, to_page=page_num)

    fileName = pdfPath.get().split("/")[-1]
    yearMonth = fileName.split("(")[1].split(")")[0]
    year = yearMonth.split(".")[0]
    month = yearMonth.split(".")[1].replace("0", "")

    outputPath = directoryPath.get() + "/수급자/" + name + "/" + year + "년/" + month + "월/"

    os.makedirs(outputPath, exist_ok=True)
    outputPath += name + " " + keyword + ".pdf"
    if keyword == '상담일지' and os.path.exists(outputPath):
        file = fitz.open(outputPath)
        outputDocument.insert_pdf(file, start_at=0)
    outputDocument.save(outputPath)







root = Tk()
root.title("효드림노인복지센터")
root.geometry("+700+400")
root.resizable(False, False)




# 위젯 배치

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

radioVar = tk.StringVar(value="")

radioFrame = Frame(root)

radio1 = tk.Radiobutton(radioFrame, text="목욕도움 제공 기록지", variable = radioVar, value="목욕도움 제공 기록지")
radio1.pack(side="left")
radio2 = tk.Radiobutton(radioFrame, text="상담일지", variable = radioVar, value="상담일지")
radio2.pack(side="left")
radio3 = tk.Radiobutton(radioFrame, text="프로그램관리자 업무수행일지", variable = radioVar, value="프로그램관리자 업무수행일지")
radio3.pack(side="left")
radio4 = tk.Radiobutton(radioFrame, text="상태변화 기록지", variable = radioVar, value="상태변화 기록지")
radio4.pack(side="left")
radio5 = tk.Radiobutton(radioFrame, text="장기요양급여 제공기록지", variable = radioVar, value="장기요양급여 제공기록지")
radio5.pack(side="left")


btn = Button(root, text="실행", command=execute)
fileFrame.pack()
directoryFrame.pack()
radioFrame.pack()
btn.pack()
root.mainloop()
