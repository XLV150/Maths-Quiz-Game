from tkinter import *
import random

root = Tk()
root.title("Math")

def mainfunc():
    labelMenu = Label(root, text="Main Menu")
    labelMenu.grid(row=0, column=0)

    button_TimesTable = Button(root, text="Start Times Table Quiz.", padx=24, pady=5, command=lambda :TimesTable())
    button_TimesTable.grid(row=1, column=0)

    button_Addition = Button(root, text="Start Addition Quiz.", padx=32, pady=5, command=lambda :Addition())
    button_Addition.grid(row=2, column=0)

    button_Subtraction = Button(root, text="Start Subtraction Quiz.", padx=24, pady=5, command=lambda :Subtraction())
    button_Subtraction.grid(row=3, column=0)

    button_Exit = Button(root, text="Exit the program.", padx=39, pady=5, command=lambda :Exit())
    button_Exit.grid(row=4, column=0)


    def TimesTable():
            entry1 = Entry(root, width=35, borderwidth=5)
            entry1.grid(row=1, column=2, columnspan=3, padx=10, pady=10)

            button_1 = Button(root, text="Start", padx=10, pady=5, command=lambda: button_click())
            button_1.grid(row=1, column=5)

            labelstart = Label(root, text="Click The start Button to begin your new quiz.")
            labelstart.grid(row=4, column=2)

            def button_click():
                button_1 = Button(root, text="Next", padx=10, pady=5, command=lambda: button_click())
                button_1.grid(row=1, column=5)
                labelstart.destroy()
                if entry1.get() == "":
                    x = random.randint(1, 12)
                    y = random.randint(1, 12)
                    global answer_times
                    answer_times = x * y
                    times_question = "What is {} X {}?".format(x, y)
                    label_question = Label(root, text=times_question)
                    label_question.grid(row=1, column=1, )
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


    def Addition():
        entry1 = Entry(root, width=35, borderwidth=5)
        entry1.grid(row=1, column=2, columnspan=3, padx=10, pady=10)

        button_1 = Button(root, text="Start", padx=10, pady=5, command=lambda: button_click_Addition())
        button_1.grid(row=1, column=5)

        labelstart = Label(root, text="Click The start Button to begin your new quiz.")
        labelstart.grid(row=4, column=2)

        def button_click_Addition():
            button_1 = Button(root, text="Next", padx=10, pady=5, command=lambda: button_click_Addition())
            button_1.grid(row=1, column=5)
            labelstart.destroy()
            if entry1.get() == "":
                x = random.randint(1, 100)
                y = random.randint(1, 100)
                global answer_Addition
                answer_Addition = x + y
                addition_question = "What is {} + {}?".format(x, y)
                label_question = Label(root, text=addition_question)
                label_question.grid(row=1, column=1, )
            else:
                answer2 = str(answer_Addition)
                stringentry = str(entry1.get())
                if stringentry == answer2:
                    label1 = Label(root, text="Correct")
                    label1.grid(row=2, column=2)
                    entry1.delete(0, 'end')
                    button_click_Addition()
                else:
                    label2 = Label(root, text="Wrong")
                    label2.grid(row=2, column=2)
                    entry1.delete(0, 'end')
                    button_click_Addition()


    def Subtraction():
        entry1 = Entry(root, width=35, borderwidth=5)
        entry1.grid(row=1, column=2, columnspan=3, padx=10, pady=10)

        button_1 = Button(root, text="Start", padx=10, pady=5, command=lambda: button_click_Subtraction())
        button_1.grid(row=1, column=5)

        labelstart = Label(root, text="Click The start Button to begin your new quiz.")
        labelstart.grid(row=4, column=2)

        def button_click_Subtraction():
            button_1 = Button(root, text="Next", padx=10, pady=5, command=lambda: button_click_Subtraction())
            button_1.grid(row=1, column=5)
            labelstart.destroy()
            if entry1.get() == "":
                x = random.randint(50, 100)
                y = random.randint(1, 50)
                global answer_Subtraction
                answer_Subtraction = x + y
                addition_question = "What is {} - {}?".format(x, y)
                label_question = Label(root, text=addition_question)
                label_question.grid(row=1, column=1, )
            else:
                answer3 = str(answer_Subtraction)
                stringentry = str(entry1.get())
                if stringentry == answer3:
                    label1 = Label(root, text="Correct")
                    label1.grid(row=2, column=2)
                    entry1.delete(0, 'end')
                    button_click_Subtraction()
                else:
                    label2 = Label(root, text="Wrong")
                    label2.grid(row=2, column=2)
                    entry1.delete(0, 'end')
                    button_click_Subtraction()

    def Exit():
        exit()

mainfunc()

root.mainloop()
