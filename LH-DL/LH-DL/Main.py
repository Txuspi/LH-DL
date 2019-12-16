'''
Created on 25 nov. 2019

@author: jesusalvaro.alonso
'''

if __name__ == '__main__':
    pass
import _tkinter
import tkinter
Course = ""
def get_URLS(urls):
       url = Course
       print(EntryCourse.get()) 
def press_button():
    urls = []
    get_URLS(urls)
    
top = tkinter.Tk()
top.title("Obtener cursos en pdf")
LabelCourse = tkinter.Label(top, text="Course Name:")
LabelCourse.grid(pady=5, row=0, column=0)
EntryCourse = tkinter.Entry(top, width=40, text=Course)
EntryCourse.grid(padx=5, row=0, column=1)
LabelPageCount = tkinter.Label(top, text="Page Count:")
LabelPageCount.grid(pady=5, row=1, column=0)
EntryPageCount = tkinter.Entry(top, width=40)
EntryPageCount.grid(padx=5, row=1, column=1)

ButtonGetUrls = tkinter.Button(top, text="Extraer" ,width=50 ,command=press_button, bd =5)
ButtonGetUrls.grid(padx=10, pady=10, row=2, column=0, columnspan=2)
# Code to add widgets will go here...
top.mainloop()


    