import PySimpleGUI as s
import math
import string
size=(7,3)
font=('helvetica',10)
CONSTANTS = ("pi", "e")
CONST_VAL = {i:f"math.{i}" for i in CONSTANTS}
WAVE = ("sin", "cos", "tan")
WAVE_FUNC = {i:f"math.{i}" for i in WAVE}
ARITHMETIC = {"+":"+", "-":"-", "x":"*", "/":"/", ".":".","(":"(", ")":")"}
DIGITS = dict(zip(string.digits, string.digits))
ALL_ALPHA = {**DIGITS, **ARITHMETIC}
figures=[]
for index, i in enumerate(range(1, len(DIGITS), 3)):
    x = [s.ReadButton(j, size=size) for j in range(i, i+3)]
    x+=[s.ReadButton(tuple(ARITHMETIC)[index], size=size)]
    figures.append(x)

gui=[
    [s.InputText('',key='inval', font=('helvetica',22))],
    figures,
    [s.ReadButton('0', size=size),
     s.ReadButton('.', size=size),
     s.ReadButton('sqrt', size=size),
     s.ReadButton('/', size=size)],
    [s.ReadButton('tan', size=size),s.ReadButton('cos', size=size),
     s.ReadButton('sin', size=size),
     s.ReadButton('(', size=size)],
    [s.ReadButton('log', size=size),s.ReadButton('e', size=size),
     s.ReadButton('pi', size=size),s.ReadButton(')', size=size)],
    [s.ReadButton('ANS', size=(24,3)),s.ReadButton('C', size=size)],
   
    [s.Text('IBM Abdulsalam - For Educational Purpose')]
    ]
win=s.Window('Calx v2.1',size=(320,540)).Layout(gui)

key_entered=''
while True:
    button, val=win.Read()
    try:
        if button is None:
            break
        elif button == 'C':
            key_entered=''
        elif button in ALL_ALPHA:
            key_entered=val['inval']
            key_entered+=button
        elif button in CONST_VAL:
            key_entered+=str(eval(CONST_VAL[button]))
        elif button in ['sin','cos','tan','log', 'sqrt']:
            key_entered=val['inval']
            key_entered+=button
        elif button == 'ANS':
            TOTAL = list(ARITHMETIC)+list(WAVE_FUNC)
            try:
                for k in TOTAL:
                    if k in key_entered.keys():
                        key_entered.replace(k, ARITHMETIC.get(k)).replace(k, WAVE_FUNC.get(k))
                    key_entered = key_entered 
            except:
                print(key_entered)
            finally:
                key_entered = eval(key_entered)
                
        elif key_entered == NameError:
            key_entered=''
        else:
            key_entered=''
    except AttributeError:
        key_entered='Error'
        
    except SyntaxError:
        key_entered='Error'
        
    win.find_element('inval').Update(key_entered)
