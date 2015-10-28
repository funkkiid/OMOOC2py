# -*- coding: utf-8 -*-
import Tkinter as tk
import time
from Tkinter import *

TITLE_FONT = ("Helvetica", 18, "bold")
READING_FONT=('sans-serif', 16)


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Diary", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="写日记",
                            command=lambda: controller.show_frame(PageOne))
        button2 = tk.Button(self, text="读日记",
                            command=lambda: controller.show_frame(PageTwo))

        self.photo1=tk.PhotoImage(file="images/write_200.gif")
        canvas1=tk.Canvas(self, width=self.photo1.width(), height=self.photo1.height())
        canvas1.create_image(100,70,image=self.photo1)


        self.photo2=tk.PhotoImage(file="images/read_200.gif")
        canvas2=tk.Canvas(self, width=self.photo2.width(), height=self.photo1.height())
        canvas2.create_image(100,80,image=self.photo2)

        canvas1.pack()
        button1.pack()
        canvas2.pack()
        button2.pack()

        canvas=tk.Canvas(self,width=400,height=10)
        canvas.pack()
        # 让界面宽一点，同时给底部添加一个pady，因为还不知道具体用法，先用weight和height来占位

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="写日记", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()

        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="保存", command=self.save)
        self.entry.pack(ipadx=100,ipady=10)
        self.button.pack()

    def save(self):
        diaryFile = open('diary.txt','a')

        diary=self.entry.get().encode('utf-8')
        diaryFile.write('\n' + time.strftime('%Y/%m/%d')+ ' ' +diary)
        
        self.entry.delete(0,tk.END)
        diaryFile.close()





class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="读日记", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()
        
        # 尝试添加scrollbar
        scrollbar = tk.Scrollbar(self)
        text = tk.Text(self,height=10, width=40,font=READING_FONT)

        scrollbar.pack(side=RIGHT,fill=Y)
        text.pack(side=LEFT, fill=Y)

        scrollbar.config(command=text.yview)
        text.config(yscrollcommand=scrollbar.set)

        # 是想实现 如果不存在diary.txt，创建它。 看有更好的方法来判断这个吗。
        diaryFile = open('diary.txt','a')
        diaryFile.close()

        diaryFile = open('diary.txt')

        diary = diaryFile.read()
        text.insert(tk.END, diary)
        
        diaryFile.close()
        

        


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

