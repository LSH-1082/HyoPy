import shutil
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import os

def copy():
    try:
        current_directory = directoryPath.get()
        all_items = os.listdir(current_directory)
        folders = [item for item in all_items if os.path.isdir(os.path.join(current_directory, item))]

        split = []
        file = filePath.get().split("} ")
        for i in range(0, len(file)):
            split.append(file[i].translate({ord(letter): None for letter in '{}'}))

        for i in range(0, len(split)):
            destination_folder = current_directory +"/"+ folders[i] +"/"+ yearComboBox.get() +"/"+ monthComboBox.get()
            if not os.path.exists(destination_folder):
                raise FileNotFoundError("목적지 폴더가 존재하지 않습니다.")
        
        for i in range(0, len(folders)):
            for j in range(0, len(split)):
                shutil.copy2(split[j], current_directory +"/"+ folders[i] +"/"+ yearComboBox.get() +"/"+ monthComboBox.get())
        msgbox.showinfo("INFO", yearComboBox.get() + " " + monthComboBox.get() + "에 대한 " + str(len(split)) + "개의 파일을 복사했습니다")
        
    except FileNotFoundError:
        msgbox.showerror("오류", "년/월, 파일/폴더의 경로를 확인하세요!")

def selectFile():
    file_paths = filedialog.askopenfilenames()
    filePath.insert(0, file_paths)
    
def selectDirectory():
    directory_path = filedialog.askdirectory()
    directoryPath.insert(0, directory_path)

def check():
    if yearComboBox.get() not in yearValue or monthComboBox.get() not in monthValue:
        msgbox.showerror("오류", "년도 혹은 월이 잘못되었습니다")
    else:
        copy()



root = Tk()
root.title("효드림노인복지센터")
root.geometry("+700+400")
root.resizable(False, False)

fileFrame = Frame(root)
fileLabel = Label(fileFrame, text="파일 선택")
fileLabel.pack(side="left")
filePath = Entry(fileFrame, width=30)
filePath.pack(side="left")
fileButton = Button(fileFrame, width=1, height=1, text="...", command=selectFile)
fileButton.pack(side="right")


directoryFrame = Frame(root)
directoryLabel = Label(directoryFrame, text="폴더 선택")
directoryLabel.pack(side="left")
directoryPath = Entry(directoryFrame, width=30)
directoryPath.pack(side="left")
directoryButton = Button(directoryFrame, width=1, height=1, text="...", command=selectDirectory)
directoryButton.pack(side="right")


dateFrame = Frame(root)
yearValue = [str(i) + "년" for i in range(2023, 2027)]
yearComboBox = ttk.Combobox(dateFrame, width=10, values = yearValue)
yearComboBox.set("년도 선택")
yearComboBox.pack(side="left")

monthValue = [str(i) + "월" for i in range(1, 13)]
monthComboBox = ttk.Combobox(dateFrame, width=10, values = monthValue)
monthComboBox.set("월 선택")
monthComboBox.pack(side="right")

btn = Button(root, text="실행", command=check)

fileFrame.pack()
directoryFrame.pack()
dateFrame.pack()
btn.pack()
root.mainloop()