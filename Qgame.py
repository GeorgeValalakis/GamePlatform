from tkinter import*
import random
from tkinter import messagebox


def quizgame():

    global label3,list1,x,label2,label1,entry,j,score,wan,score1
    window = Tk()
    window.geometry("1800x840")
    window.title("QuizGame")
    score=0
    wan=0
    list1=["Δίνεται μια μεταβλητή b=19. Τι θα εμφανίζει η εντολή print(b//5);\n1) b//5\n2) 3\n3) 3.8\n4) 19//5","2"],\
    ["Δίνεται μια μεταβλητή a=3. Τι θα εμφανίζει η εντολή print(a**5);\n1) 243\n2) a**5\n3) 15\n4) 3**5","1"],\
    ["Τι επιστρέφει μια συνάρτηση η οποία δεν περιέχει την εντολή return;\n1) nothing\n2) none\n3) return\n4) -","2"],\
    ["Με ποια εντολή η python μετατρέπει κείμενο σε ακέραιο;\n1) str\n2) float\n3) int\n4) num","3"],\
    ["Τι θα εμφανίσει η εντολή print( 10%3);\n1) 3.3\n2) 3\n3) 10%3\n4) 1","4"],\
    ["Τι θα εμφανίσει η εντολή print((4 + 8) / 2);\n1) (4 + 8) / 2 \n2) 6\n3) 6.0\n4) Τίποτα. Περιέχει λάθος","3"],\
    ["this_is_a_list=[7,'yoda',3,'error'],\n Τι εκτυπώνει η εντολή print(this_is_a_list[3]);\n1) yoda \n2) 3\n3) 7\n4)error","4"]

    j=0
    score1 = score



    def start(event):
        global label3, list1, score, wan, j,entry,x,score1
        x = 1

        if x==1:

            entry = Entry(window, font=('Times', 40, 'bold'), width=16)
            entry.grid(column=0, row=2, pady=3, padx=40)
            entry.delete(0, "end")
            label2.destroy()
            label3.configure(text=list1[j][0])

            if entry.get() == list1[j][1]:
                score1 = score1 +1
                yordle()
            else:
                wan=wan+1
                yordle()



            print(j)


    def yordle():

        global j,x,label3,score,wan,btnex,btnre

        if j <= 5:
            j = j + 1
        elif j == 6:
            x = 0
            messagebox.showinfo("Your Score", "Correct Answers: " + str(score1) + "\nFalse Answers: " + str(wan))
            print(score1)
            btnre = Button(window, text="Return", font=('Times', 40, 'bold'),command= window.destroy,bg="Light green")
            btnre.grid(column=0, row=4, pady=4, padx=40)




    label1 = Label(window, text="Python Test!", font=('Times', 40, 'bold'))
    label1.grid(column=0, row=0, pady=3, padx=40)
    label2 = Label(window, text="Press Enter to Start!", font=('Times', 40, 'bold'))
    label2.grid(column=0, row=1, pady=3, padx=40)
    label3 = Label(window,font=('Times', 40, 'bold'))
    label3.grid(column=0, row=1, pady=3, padx=40)




    window.bind("<Return>",start)















    window.mainloop()
