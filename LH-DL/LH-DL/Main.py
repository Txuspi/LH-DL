'''
Created on 25 nov. 2019

@author: jesusalvaro.alonso
'''

if __name__ == '__main__':
    pass
import _tkinter
import tkinter
  
    
top = tkinter.Tk()
LabelCourse = tkinter.Label(top, text="Course Name:")
LabelCourse.pack( side = tkinter.LEFT)
EntryCourse = tkinter.Entry(top, bd =5)
EntryCourse.pack(side = tkinter.RIGHT)
LabelPageCount = tkinter.Label(top, text="Page Count:")
LabelPageCount.pack( side = tkinter.LEFT)
EntryPageCount = tkinter.Entry(top, bd =5)
EntryPageCount.pack(side = tkinter.RIGHT)

class get_URLS():
    url = EntryCourse.get()
    print('%s:' % (url)) 
class LH:
    urls = []
    get_URLS()
ButtonGetUrls = tkinter.Button(top,  command = LH, bd =5)
ButtonGetUrls.pack(side = tkinter.RIGHT)
# Code to add widgets will go here...
top.mainloop()



#class getURLS:
    