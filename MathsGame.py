from tkinter import *
import random

root = Tk()
root.title("Math")

entry1 = Entry(root, width=35, borderwidth=5)
entry1.grid(row=1, column=2, columnspan=3, padx=10, pady=10)


def button_click():
    if entry1.get() == "":
        x = random.randint(1, 12)
        y = random.randint(1, 12)
        global answer_times
        answer_times = x * y
        addition_question = "What is {} X {}?".format(x, y)
        label_question = Label(root, text=addition_question)
        label_question.grid(row=0, column=0, rowspan=2, columnspan=2)
    else:
        answer1 = str(answer_times)
        stringentry = str(entry1.get())
        if stringentry == answer1:
            label1 = Label(root, text="Correct")
            label1.grid(row=2, column=2)
            entry1.delete(0, 'end')
            button_click()
        else:
            label2 = Label(root, text="Wrong")
            label2.grid(row=2, column=2)
            entry1.delete(0, 'end')
            button_click()


button_1 = Button(root, text="Continue", padx=10, pady=10, command=lambda: button_click())
button_1.grid(row=2, column=4)


root.mainloop()
