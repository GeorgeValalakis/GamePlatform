from tkinter import*
import random
from tkinter import messagebox
def colorgame():
    global time,score,clbl,label1,label2,label3,label4,entry
    window = Tk()
    window.geometry("720x640")
    window.title("ColorGame")
    clbl=["Red","Blue","Green","Orange","Purple","Yellow","Light blue","Pink","Black","White","Magenta","Gold","Silver"]
    time=10
    score=0
    def randomcolor():
        global score
        if time>0:
            if entry.get().lower() == clbl[1].lower():
                score=score+1
            entry.delete(0,"end")
            random.shuffle(clbl)
            label4.configure(text=str(clbl[0]),fg=str(clbl[1]))
            label2.configure(text="Score: "+str(score))
    def countdown():
        global time

        if time>0:
            time=time-1
            label3.configure(text="Time left: "+str(time))
            label3.after(1000,countdown)
        else:
            end()


    def start(event):
        global x
        x=0
        if time==10:
            countdown()
        randomcolor()
        if time==0:
            x = 1

    def end():
        if score>=7:
            messagebox.showinfo("Your Score", "Your score was:"+str(score)+"   "+"You are a Cheetah!    ")
        elif score<7 and score>=3:
            messagebox.showinfo("Your Score", "Your score was: "+str(score)+ "  "+ "You are a Camel!       ")
        elif score<3 and score>0:
            messagebox.showinfo("Your Score", "Your score was: " + str(score) + "  " + "You are a Turtle!     ")
        else:
            messagebox.showinfo("Your Score", "Game Over!       ")
        global btnex, btnres
        btnex = Button(window, text="Exit",width=9, command=window.destroy,bg="Red",font=('Times', 40, 'bold'))
        btnex.grid(column=0, row=6, pady=3, padx=40)
        btnres = Button(window, text="Play Again",command=yordle,bg="light green",font=('Times', 40, 'bold'))
        btnres.grid(column=0, row=5, pady=3, padx=40)




    def yordle():
        global time,score
        time=10
        score=0
        window.bind("<Return>", start)
        btnex.destroy()
        btnres.destroy()
        countdown()
        randomcolor()








    label1= Label(window,text="Type the color of the words!",font=('Times', 40, 'bold'))
    label1.grid(column=0,row=0, pady=3, padx=40)
    label2=Label(window,text="Press Enter to start!",font=('Times', 40, 'bold'))
    label2.grid(column=0,row=1, pady=3, padx=40)
    label3=Label(window,text="Time left: "+str(time),font=('Times', 40, 'bold'))
    label3.grid(column=0,row=2, pady=3, padx=40)
    label4=Label(window,font=('Times', 60, 'bold'))
    label4.grid(column=0,row=3, pady=3, padx=40)

    entry=Entry(window,font=('Times', 40, 'bold'),width=16)
    entry.grid(column=0,row=4, pady=3, padx=40)
    window.bind("<Return>",start)




    window.mainloop()