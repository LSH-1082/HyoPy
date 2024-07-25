from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import time
import os

option = Options()
option.add_experimental_option('detach', True)
option.add_argument("headless"), True     #브라우저 표시 옵션

def loginCmd():
    try:
        if yearComboBox.get() not in yearValue or monthComboBox.get() not in monthValue:
            msgbox.showerror("오류", "년도 혹은 월이 잘못되었습니다")

        else:
            driver = webdriver.Chrome(options = option)
            driver.get("https://www.carefor.co.kr/login.php")
            drvNum = driver.find_element(By.XPATH, "//*[@id=\"login_outline\"]/div[1]/div/form/ul/li[1]/input")
            drvID = driver.find_element(By.XPATH, "//*[@id=\"login_outline\"]/div[1]/div/form/ul/li[2]/input")
            drvPass = driver.find_element(By.XPATH, "//*[@id=\"login_outline\"]/div[1]/div/form/ul/li[3]/input")
            drvNum.send_keys(centNum.get())
            drvID.send_keys(id.get())
            drvPass.send_keys(passwd.get(), Keys.ENTER)
            result = driver.switch_to.alert
            msgbox.showwarning("경고", result.text)
            result.accept()
            driver.quit()
    except NoAlertPresentException:
        try:
            time.sleep(0.5)
            appNotice = driver.find_element(By.XPATH, "//*[@id=\"layerModal\"]/div/div[6]/span[2]")
            appNotice.click()
        except NoSuchElementException:
            pass

        try:
            time.sleep(0.5)
            appNotice2 = driver.find_element(By.XPATH, "//*[@id=\"layerModal\"]/section/section/section[3]/div")
            appNotice2.click()
        except NoSuchElementException:
            pass
        
        nameList = []
        totalNum = int(driver.find_element(By.XPATH, '//*[@id="div_patient_list"]/div/div[3]/span[1]/span').text)
        for i in range(1, totalNum + 1):
            name = driver.find_element(By.XPATH, '//*[@id="patient_list_table"]/tbody/tr['+ str(i) +']/td[3]').text
            nameList.append(name)
        current_path = directoryPath.get()
        cnt = 0
        for i in nameList:
            try:
                os.makedirs(current_path + "/수급자/" + i + "/"  + yearComboBox.get() + "/" + monthComboBox.get())
            except FileExistsError:
                cnt +=1
        for i in nameList:
            try:
                os.makedirs(current_path + "/수급자/" + i + "/" + yearComboBox.get() + "/연간서류")
                os.makedirs(current_path + "/수급자/" + i + "/" + yearComboBox.get() + "/분기서류")
            except FileExistsError:
                pass

        if(totalNum == cnt):
            msgbox.showerror("INFO", "모든 폴더가 존재합니다!")
            driver.quit()

        if(totalNum != cnt):
            msgbox.showinfo("INFO", str(int(totalNum)-int(cnt)) + "명에 대한 폴더를 생성하였습니다")
            driver.quit()

def selectDirectory():
    directory_path = filedialog.askdirectory()
    directoryPath.insert(0, directory_path)

root = Tk()
root.title("효드림노인복지센터")
root.geometry("+700+400")
root.resizable(False, False)

numFrame = Frame(root)
numLabel = Label(numFrame, text="기관번호:")
centNum = Entry(numFrame)


idFrame = Frame(root)
id = Entry(idFrame, width=20)
idLabel = Label(idFrame, width=7, text="아이디: ")

passwdFrame = Frame(root)
passwd = Entry(passwdFrame, show="*")
passwdLabel = Label(passwdFrame, text="비밀번호:")

dateFrame = Frame(root)
yearValue = [str(i) + "년" for i in range(2023, 2027)]
yearComboBox = ttk.Combobox(dateFrame, width=10, values = yearValue)
yearComboBox.set("년도 선택")

monthValue = [str(i) + "월" for i in range(1, 13)]
monthComboBox = ttk.Combobox(dateFrame, width=10, values = monthValue)
monthComboBox.set("월 선택")

directoryFrame = Frame(root)
directoryLabel = Label(directoryFrame, text="폴더 선택")
directoryPath = Entry(directoryFrame, width=30)
directoryButton = Button(directoryFrame, width=1, height=1, text="...", command=selectDirectory)



directoryButton.pack(side="right")
directoryPath.pack(side="left")
directoryLabel.pack(side="left")
centNum.pack(side="right")
numLabel.pack(side="left")
id.pack(side="right")
idLabel.pack(side="left")
passwd.pack(side="right")
passwdLabel.pack(side="left")
yearComboBox.pack(side="left")
monthComboBox.pack(side="right")

numFrame.pack()
idFrame.pack()
passwdFrame.pack()
directoryFrame.pack()
dateFrame.pack()


btn = Button(root, text="실행", command=loginCmd)
btn.pack()
root.mainloop()
