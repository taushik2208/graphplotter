from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
#import tkMessageBox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bisect
root= Tk()
root.title("Graph Plotter")

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
    
frame1 = Frame(root,height=300,width=300)
frame1.pack(side=TOP)
lb1=Label(frame1,font=("ALGERIAN",40),text="GRAPH PLOTTER")
lb1.pack()
def sel():
    global selection
    selection =str(var.get())
    

rowChosen=Combobox(frame1,textvariable=comb,state='readonly',width=12)
rowChosen.bind("<<ComboboxSelected>>",getstrx)
rowChosen.pack()
rowy=Combobox(frame1,textvariable=combval,state='readonly',width=12)
rowy.bind("<<ComboboxSelected>>",getstry)
rowy.pack()

R1 = Radiobutton(frame1, text = "Histogram", variable = var, value = 1,command = sel)
R1.pack( anchor = W )

R2 = Radiobutton(frame1, text = "Piechart", variable = var, value = 2,command = sel)
R2.pack( anchor = W )

R3 = Radiobutton(frame1, text = "Bar Graph", variable = var, value = 3,command = sel)
R3.pack( anchor = W)

R4 = Radiobutton(frame1, text = "Scatter Plot", variable = var, value = 4,command = sel)
R4.pack( anchor = W)

R5 = Radiobutton(frame1, text = "Line Graph", variable = var, value = 5,command = sel)
R5.pack( anchor = W)


    

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
        
    
            
            
    #plt.plot(file.dropna())
    #plt.show()
    


   
    
    
print(var.get())
browsebutton = Button(frame1, text="Browse", command=browsefunc)
browsebutton.pack()
plotbutton = Button(frame1, text="Plot Graph", command=plotfunc)
plotbutton.pack()
 


