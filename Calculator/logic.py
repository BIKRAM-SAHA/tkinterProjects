from tkinter import StringVar
from decimal import Decimal

def keydown(key,textVar):
    try: 
        handleNumClick(int(key.char),textVar)
    except ValueError as e: 
        if(key.keysym=='Return'):
            handleEqual(textVar)
        elif(key.keysym=='Delete'):
            handleClear(textVar)
        elif(key.keysym=='BackSpace'):
            handleBack(textVar)
        else:
            handleOperator(key.char,textVar)
    
def remove_exponent(num):
    return num.to_integral() if num == num.to_integral() else num.normalize()

def handleNumClick(num,textVar):
    if(textVar.get()=='Invalid Expression'):
        textVar.set('')
    if(textVar.get()=='0'):
        textVar.set('')
    number=textVar.get()
    number+=str(num)
    textVar.set(number)

def handleEqual(textVar):
    if(textVar.get()=='Invalid Expression'):
        textVar.set('')
    try:
        result=remove_exponent(Decimal('%.13f'%eval(textVar.get())))
        textVar.set(result)
    except:
        textVar.set("Invalid Expression")

def handleOperator(op,textVar):
    if(textVar.get()=='Invalid Expression'):
        textVar.set('')
    if(op=='+'):
        textVar.set(textVar.get()+'+')
    elif(op=='-'):
        textVar.set(textVar.get()+'-')
    elif(op=='*'):
        textVar.set(textVar.get()+'*')
    elif(op=='/'):
        textVar.set(textVar.get()+'/')

def handleBack(textVar):
    if(textVar.get()!='Invalid Expression'):
        val=textVar.get()
        val=val[:-1]
        textVar.set(val)

def handleClear(textVar):
    textVar.set("")