from tkinter import *
def button_1():
    l['text']=int(a.get())*2
root=Tk()
root.title("Приложение")
root.geometry('500x300')
a=Entry(root, width=15, bg='gray', fg="cyan", font="consolas")
a.pack()
Button(root, text="умножить на 2", width=15, height=2, bg= 'white' , command=button_1).pack()
l = Label(root, width=15, bg='gray', fg= 'cyan', font= "consolas")
l.pack()
root.mainloop()