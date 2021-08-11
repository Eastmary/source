'''
from tkinter import *

window = Tk()
window.title("윈도창 연습")
window.geometry("400x100")
window.resizable(width=FALSE, height=FALSE)
#이 부분에서 화면을 구성하고 처리

window.mainloop()
'''

from tkinter import *
window = Tk()

label1 = Label(window, text="This is MySQL을")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text="공부 중입니다", bg="magenta", width=20, height=5, anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()