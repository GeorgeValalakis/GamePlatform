from tkinter import*
from Qgame import quizgame
from ColorGame import colorgame
def secwindow():
    global entry2, win
    win=Tk()
    win.geometry("490x700")
    win.title("Main Menu")
    labelw = Label(win, text="Welcome, "+str(entry2.get())+"!", font=('Times', 40, 'bold'))

    labelw.grid(column=0, row=0, pady=10, padx=50)
    labele = Label(win, text="Available Games:", font=('Times', 40, 'bold'))

    labele.grid(column=0, row=1, pady=5, padx=40)
    buttocg= Button(win, text="Color Game", font=('Times', 40, 'bold'),bg="orange", command=colorgame)

    buttocg.grid(column=0, row=2, pady=3, padx=40)
    buttoqg = Button(win, text="Quiz Game", font=('Times', 40, 'bold'),bg="light blue", command=quizgame)
    buttoqg.grid(column=0, row=3, pady=3, padx=40)

    buttonex = Button(win, text="Exit", font=('Times', 40, 'bold'),bg="Red", command=win.destroy)
    buttonex.grid(column=0, row=5, pady=3, padx=70)
    buttopre = Button(win, text="Return", font=('Times', 40, 'bold'),bg="light yellow", command=start11)
    buttopre.grid(column=0, row=4, pady=3, padx=70)

    window1.destroy()



def start11():
    global win
    win.destroy()
    start1()
def start1():
    global entry2, window1

    window1 = Tk()
    window1.geometry("460x390")
    window1.title("Information")

    label11=Label(window1, text="Your Name:", font=('Times', 40, 'bold'))


    label11.grid(column=0,row=0, pady=3, padx=40)
    entry2= Entry(window1, font=('Times', 40, 'bold'), width=16)
    entry2.grid(column=0,row=1,padx=10)
    button11=Button(window1, text="Submit", font=('Times', 40, 'bold'),bg="light green",command=secwindow)
    button11.grid(column=0,row=3, pady=3, padx=40)




start1()
window1.mainloop()