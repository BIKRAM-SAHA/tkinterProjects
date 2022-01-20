from tkinter import Tk, PhotoImage, StringVar
from tkinter import ttk
from logic import *

#code to enable corect path on using pyinstaller to create .exe
import sys, os #
def resource_path(relative_path): #
    """ Get absolute path to resource, works for dev and for PyInstaller """ #
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))) #
    return os.path.join(base_path, relative_path) #

root=Tk()
root.title("Calc")
root.resizable(False,False)
root.iconphoto(False,PhotoImage(file=resource_path("icon.png")))

root.tk.call("source", resource_path("sun-valley.tcl"))
root.tk.call("set_theme", "dark")

ttk.Style().configure("TButton", width=3, padding=10, font=(None, 20))
ttk.Style().configure("TLabel", padding=5)

DisplayText=StringVar()
Display=ttk.Label(root, textvariable=DisplayText, anchor='e')
Display.grid(row=0,column=0,columnspan=4,sticky='nswe', padx=2, pady=2, ipady=5)

Button0 =ttk.Button(root, text="0", command=lambda: handleNumClick(0,DisplayText))
Button0.grid(row=5,column=0,columnspan=2,sticky='we',padx=2,pady=2)
Button1 =ttk.Button(root, text="1", command=lambda: handleNumClick(1,DisplayText))
Button1.grid(row=4,column=0,padx=2,pady=2)
Button2 =ttk.Button(root, text="2", command=lambda: handleNumClick(2,DisplayText))
Button2.grid(row=4,column=1,padx=2,pady=2)
Button3 =ttk.Button(root, text="3", command=lambda: handleNumClick(3,DisplayText))
Button3.grid(row=4,column=2,padx=2,pady=2)
Button4 =ttk.Button(root, text="4", command=lambda: handleNumClick(4,DisplayText))
Button4.grid(row=3,column=0,padx=2,pady=2)
Button5 =ttk.Button(root, text="5", command=lambda: handleNumClick(5,DisplayText))
Button5.grid(row=3,column=1,padx=2,pady=2)
Button6 =ttk.Button(root, text="6", command=lambda: handleNumClick(6,DisplayText))
Button6.grid(row=3,column=2,padx=2,pady=2)
Button7 =ttk.Button(root, text="7", command=lambda: handleNumClick(7,DisplayText))
Button7.grid(row=2,column=0,padx=2,pady=2)
Button8 =ttk.Button(root, text="8", command=lambda: handleNumClick(8,DisplayText))
Button8.grid(row=2,column=1,padx=2,pady=2)
Button9 =ttk.Button(root, text="9", command=lambda: handleNumClick(9,DisplayText))
Button9.grid(row=2,column=2,padx=2,pady=2)

ButtonEqual =ttk.Button(root, text="=", command=lambda: handleEqual(DisplayText),style="Accent.TButton")
ButtonEqual.grid(row=4,column=3,rowspan=2,sticky='ns',padx=2,pady=2)
ButtonDivide =ttk.Button(root, text="/", command=lambda: handleOperator('/',DisplayText))
ButtonDivide.grid(row=1,column=0,padx=2,pady=2)
ButtonMultiply =ttk.Button(root, text="*", command=lambda: handleOperator('*',DisplayText))
ButtonMultiply.grid(row=1,column=1,padx=2,pady=2)
ButtonSubtract =ttk.Button(root, text="-", command=lambda: handleOperator('-',DisplayText))
ButtonSubtract.grid(row=1,column=2,padx=2,pady=2)
ButtonAdd =ttk.Button(root, text="+", command=lambda: handleOperator('+',DisplayText))
ButtonAdd.grid(row=2,column=3,rowspan=2,sticky="ns",padx=2,pady=2)
ButtonClear =ttk.Button(root, text="C", command=lambda: handleClear(DisplayText))
ButtonClear.grid(row=5,column=2,padx=2,pady=2)
ButtonBack = ttk.Button(root, text=u"\u232B", command=lambda: handleBack(DisplayText))
ButtonBack.grid(row=1,column=3,padx=2,pady=2)

root.bind("<KeyPress>", lambda key:keydown(key,DisplayText))
root.mainloop()