import fitz  # PyMuPDF

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

# 예제 사용법
pdf_path = '/Users/lsh/Downloads/수급자/상담일지/상담일지(2024.01.).pdf'
keyword = "상담일지"
document = fitz.open(pdf_path)

print(slicePdfPage(searchKeywordInPdf(document, keyword), document))