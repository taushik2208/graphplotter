from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


root = Tk()
root.title('Graph Plotter')
root.geometry('{}x{}'.format(850, 400))
root.config(bg = "#828481")
# create all of the main containers
top_frame = Frame(root, bg='yellow', pady=3, highlightthickness=2, highlightbackground="blue")
center = Frame(root, bg='yellow', width=80, height=80, padx=3, pady=3,highlightthickness=2, highlightbackground="#111")
btm_frame = Frame(root, bg='yellow', width=450, height=45, pady=3,highlightthickness=2, highlightbackground="#111")


# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, columnspan=3)
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")

model_label = Label(top_frame, text='GRAPH PLOTER',font=("Helvetica", 24),bg="blue", fg="yellow", justify=CENTER)
model_label.grid(row=0, columnspan=10)

center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='blue', width=100, height=190)
ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3, highlightthickness=2, highlightbackground="#111")
ctr_right = Frame(center, bg='blue', width=100, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")


fileName =""
var= IntVar()
comb=StringVar()
combval=StringVar()
def getstrx(event):
    global stringx
    stringx = rowChosen.get()
def getstry(event):
    global stringy
    stringy = rowy.get()
def sel():
    global selection
    selection =str(var.get())

label_1 = Label(ctr_mid, text="Coordinate X",font=("Helvetica", 16),  bg="yellow", anchor=W, justify=LEFT)
rowChosen=ttk.Combobox(ctr_mid,textvariable=comb,state='readonly',width=12)
rowChosen.bind("<<ComboboxSelected>>",getstrx)
label_2 = Label(ctr_mid, text="Coordinate Y",font=("Helvetica", 16),  bg="yellow", anchor=W, justify=LEFT)
rowy=ttk.Combobox(ctr_mid,textvariable=combval,state='readonly',width=12)
rowy.bind("<<ComboboxSelected>>",getstry)

label_3 = Label(ctr_mid, text="Choose one of the Graph Type",font=("Helvetica", 16),bg="yellow")
R1 = Radiobutton(ctr_mid, text = "Histogram",font=("Helvetica", 16), bg="yellow", borderwidth=2, variable = var, value = 1,command = sel)
R2 = Radiobutton(ctr_mid, text = "Piechart",font=("Helvetica", 16), bg="yellow", borderwidth=2, variable = var, value = 2,command = sel)
R3 = Radiobutton(ctr_mid, text = "Bar Graph",font=("Helvetica", 16), bg="yellow", borderwidth=2, variable = var, value = 3,command = sel)
R4 = Radiobutton(ctr_mid, text = "Scatter Plot",font=("Helvetica", 16), bg="yellow", borderwidth=2, variable = var, value = 4,command = sel)
R5 = Radiobutton(ctr_mid, text = "Line Chart",font=("Helvetica", 16), bg="yellow", borderwidth=2, variable = var, value = 5,command = sel)

label_1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
rowChosen.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
label_2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
rowy.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
label_3.grid(row=3, column=0, sticky="nsew")
R1.grid(row=4, column=1, padx=5, pady=5)
R2.grid(row=4, column=2, padx=5, pady=5)
R3.grid(row=5, column=1, padx=5, pady=5)
R4.grid(row=5, column=2, padx=5, pady=5)
R5.grid(row=6, column=1, padx=5, pady=5)

def browsefunc():
    global file
    global fileName
    fileName = str(filedialog.askopenfilename(filetypes = ( ("excel files","*.xls"),("excel files","*.xlsx"),("csv","*.csv") )))
    if fileName.endswith('.csv'):
        file=pd.read_csv(fileName)
    elif fileName.endswith('.xlsx'):
        file=pd.read_excel(fileName)
    elif fileName.endswith('.xls'):
        file=pd.read_excel(fileName)
    val=list(file.columns.values)
    rowChosen['values']=val
    rowy['values']=val

def plotfunc():
    global file
    global fileName
    global stringx,stringy,selection
    
    #pathlabel = Label(root,text=fileName)
    #pathlabel.pack()
    if (len(rowChosen.get()) == 0):
        messagebox.showwarning("Error"," Browse a file and Select Value of X and Y !!!!!!")
        browsebutton.focus_set()
    else:
        if selection == '1':
            dupp=np.arange(len(file[stringx]))
            plt.hist(file[stringx])
            plt.show()
            #plt.xticks(dupp,file[stringy], fontsize=5)
        elif selection == '2':
            plt.pie(file[stringx],labels=file[stringx],startangle=90, autopct='%.1f%%')
            plt.show()
        elif selection == '3':
            if len(rowy.get()) == 0:
                messagebox.showwarning("Error","Select Value of y")
                rowy.focus_set()
            else:
                dup=stringy
                dup=np.arange(len(file[stringx]))
                plt.bar(dup,file[stringx],align='center',alpha=0.5)
                plt.xlabel(stringy, fontsize=5)
                plt.ylabel(stringx, fontsize=5)
                plt.xticks(dup,file[stringy], fontsize=5)
                plt.title(stringx)
                plt.show()
        elif selection == '4':
             if len(rowy.get()) == 0:
                messagebox.showwarning("Error","Select Value of y")
                rowy.focus_set()
             else:
                plt.scatter(file[stringy],file[stringx])
                plt.xlabel(stringy)
                plt.ylabel(stringx)
                plt.show()
            
            
        elif selection == '5':
            if len(rowy.get()) == 0:
                rowy.current(0)
                plt.plot(file[rowy.get()],file[stringx])
                plt.show()
            elif len(rowy.get()) != 0 and len(rowChosen.get()) != 0:
                plt.plot(file[stringy],file[stringx])
                plt.show()
            else:
                plt.plot(file.dropna())
                plt.show()

browsebutton = Button(btm_frame, text="Browse",font=("Helvetica", 12), width=22,fg="red", command=browsefunc, bg="Aqua")
plotbutton = Button(btm_frame, text="Plot Graph",font=("Helvetica", 12), width=22, fg="green", command=plotfunc, bg="Aqua")

browsebutton.grid(row=0, column=0, padx=135, pady=5)
plotbutton.grid(row=0, column=1, padx=10, pady=5)

root.mainloop()
