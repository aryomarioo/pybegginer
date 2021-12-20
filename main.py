from tkinter import *
import webbrowser
root = Tk()
root.configure(bg='black')
def click1():
    webbrowser.open('https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=23s&ab_channel=ProgrammingwithMosh')
def click2():
    webbrowser.open('https://www.youtube.com/watch?v=BDi3SD7E6no&t=283s&ab_channel=TechWithTim')
def click3():
    webbrowser.open('www.codingbat.com')
def click4():
    webbrowser.open('https://www.youtube.com/watch?v=I9st-DgQoWc&ab_channel=PhilsBeginnerCode')
def click5():
    webbrowser.open('https://www.youtube.com/watch?v=YXPyB4XeYLA&ab_channel=freeCodeCamp.org')
def click6():
    webbrowser.open('https://www.techbeamers.com/top-10-python-coding-tips-for-beginners/')
    
but1 = Button(root,text="Full python course(Youtube)",command=click1,fg="black",bg="white")
but1.pack()

but2 = Button(root,text="Good first project(video tutorial)",command=click2,fg="black",bg="white")
but2.pack()

but3 = Button(text="Coding problems begginer/intermediate",fg="black",bg="white",command=click3)
but3.pack()

but4 = Button(root,text="module error fix",command=click4,fg="black",bg="white")
but4.pack()

but5 = Button(root,text="Full Tkniter tutorial",command=click5,bg="white")
but5.pack()

but6 = Button(root,text="10 python tips and tricks for begginers",bg="white",command=click6)
but6.pack()


root.mainloop()