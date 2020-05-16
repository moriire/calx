import PySimpleGUI as s
import math
size=(6,3)
font=('helvetica',10)
gui=[
    [s.InputText('',key='inval', font=('helvetica',22))],
    [s.ReadButton('1', size=size),s.ReadButton('2', size=size), s.ReadButton('3', size=size),s.ReadButton('+', size=size)],
    [s.ReadButton('4', size=size), s.ReadButton('5', size=size), s.ReadButton('6', size=size), s.ReadButton('-', size=size)],
    [s.ReadButton('7', size=size), s.ReadButton('8', size=size), s.ReadButton('9', size=size), s.ReadButton('*', size=size)],
    [s.ReadButton('0', size=size), s.ReadButton('.', size=size), s.ReadButton('sqrt', size=size), s.ReadButton('/', size=size)],
    [s.ReadButton('tan', size=size),s.ReadButton('cos', size=size),s.ReadButton('sin', size=size),
     s.ReadButton('(', size=size)],
    [s.ReadButton('log', size=size),s.ReadButton('e', size=size),s.ReadButton('pi', size=size),s.ReadButton(')', size=size)],
    [s.ReadButton('ANS', size=(22,3)),s.ReadButton('C', size=size)],
   
    [s.Text('Created For Educational Purpose by:\nAgesXpat(agesxpat@gmail.com)')]
    ]
win=s.Window('Calx v2.1',size=(300,540)).Layout(gui)
#s.Window(
key_entered=''
while True:
    button, val=win.Read()
    try:
        if button is None:
            break
        elif button == 'C':
            key_entered=''
        elif button in '0123456789+-*/().':
            key_entered=val['inval']
            key_entered+=button
        elif button in ['sin','cos','tan','log','e','pi', 'sqrt']:
            key_entered=val['inval']
            key_entered+=button
        elif button == 'ANS':
            try:
                key_entered = eval(val['inval'])  
            except NameError:
                key_entered = eval('math.'+val['inval'])
            #else:
                #key_entered='Error'
        elif key_entered == NameError and button =='C':
            key_entered=''
        else:
            key_entered=''
    except AttributeError:
        key_entered='Error'
        
    except SyntaxError:
        key_entered='Error'
        
    win.FindElement('inval').Update(key_entered)
