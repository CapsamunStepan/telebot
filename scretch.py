from tkinter import *
from tkinter.ttk import *
from BoyerMoore import boyer_moore, time_of_method1
from RabinCarp import rabin_carp, time_of_method2
from FiniteAutomata import finite_automata, time_of_method3
from KnuthMorrisPratta import knuth_morris_pratt, time_of_method4

global i


def click(method):
    global i
    if method == 1:
        spisok = boyer_moore(e1, e2)
        for i in range(len(spisok)):
            print(spisok[i])
            lab = Label(master, text=spisok[i])
            lab.grid(row=i, column=0, sticky=W, pady=2, padx=4)
        lab = Label(master, text=time_of_method1())
        lab.grid(row=i+1, column=0, sticky=W, pady=2, padx=4)
    elif method == 2:
        spisok = rabin_carp(e1, e2)
        for i in range(len(spisok)):
            lab = Label(master, text=spisok[i])
            lab.grid(row=i, column=0, sticky=W, pady=2, padx=4)
        lab = Label(master, text=time_of_method2())
        lab.grid(row=i + 1, column=0, sticky=W, pady=2, padx=4)
    elif method == 3:
        spisok = finite_automata(e1, e2)
        for i in range(len(spisok)):
            lab = Label(master, text=spisok[i])
            lab.grid(row=i, column=0, sticky=W, pady=2, padx=4)
        lab = Label(master, text=time_of_method3())
        lab.grid(row=i + 1, column=0, sticky=W, pady=2, padx=4)
    elif method == 4:
        spisok = knuth_morris_pratt(e1, e2)
        for i in range(len(spisok)):
            lab = Label(master, text=spisok[i])
            lab.grid(row=i, column=0, sticky=W, pady=2, padx=4)
        lab = Label(master, text=time_of_method4())
        lab.grid(row=i + 1, column=0, sticky=W, pady=2, padx=4)


master = Tk()
master.geometry("1200x500")

l1 = Label(master, text="Подстрока:")
l2 = Label(master, text="Строка:")

l1.grid(row=0, column=0, sticky=W, pady=2, padx=4)
l2.grid(row=1, column=0, sticky=W, pady=2, padx=4)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1, pady=2, ipadx=400, ipady=5)
e2.grid(row=1, column=1, pady=2, ipadx=400, ipady=5)

text1 = Label(master, text="Выберите алгоритм:\n"
                           "1. Алгоритм Бойера-Мура\n"
                           "2. Алгоритм Рабина-Карпа\n"
                           "3. Алгоритм конечных автоматов\n"
                           "4. Алгоритм Кнута-Морриса-Пратта")
text1.grid(row=3, column=0)

method = Entry(master)
method.grid(row=4, column=0, padx=4, pady=2, ipadx=50)

call = Button(master, text="Выбрать", command=click(method))
call.grid(row=4, column=1, pady=2, ipadx=200)
mainloop()
