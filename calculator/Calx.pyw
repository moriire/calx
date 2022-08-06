import PySimpleGUI as s
import math
import sys
import webbrowser as wb
size=(7,3)
from . import settings

def change(field, new_val):
    with open('settings.py') as f:
        tok = field
        data = f.read()
        print(data)
        new_data = data.replace(str(tok), str(new_val))
        print(new_data)
        with open('settings.py', "w+") as fw:
            fw.write(new_data)
            return 1

MENU_COLOR = s.LOOK_AND_FEEL_TABLE[settings.THEME]
FIELD_LENGTH = len(settings.FIELDS)
WAVE=settings.WAVE
WAVE_FUNC=settings.WAVE_FUNC
ARITHMETIC=settings.ARITHMETIC
CONST_VAL=settings.CONST_VAL
DEVELOPER=settings.DEVELOPER
VERSIONS = settings.VERSIONS
FIELDS = settings.FIELDS
LOOKS = settings.LOOKS
THEME=settings.THEME
change_look=THEME

s.change_look_and_feel(change_look)
figures=[]
for index, i in enumerate(range(0, FIELD_LENGTH, 3)):
    x = [s.ReadButton(FIELDS[j], size=size) for j in range(i, i+3)]
    x+=[s.ReadButton(tuple(ARITHMETIC)[index], size=size)]
    figures.append(x)

gui=[
    [s.Menu([["Settings", ["theme",[LOOKS], "Exit"]],
             ["About",["Developer", "Versions"]]
            ], background_color=MENU_COLOR['BACKGROUND'], text_color=MENU_COLOR['TEXT'])
            ],
    [s.InputText('',key='inval', font=settings.FONT, size=(27, 3), pad=(5,15))],
    figures,
    [
        s.ReadButton(w, size=size) for w in WAVE
    ],
    [s.ReadButton('ANS', size=(16,3)),s.ReadButton('C', size=size),
    s.ReadButton('CE', size=size)],
   
    [s.Text('IBM Abdulsalam - For Educational Purpose', enable_events=True, key="redirect", tooltip="Click to view my profile")]
    ]
win=s.Window('Calx v3.1',size=(320,540)).Layout(gui)
key_entered=''
while True:
    button, val=win.Read()
    try:
        if button == "redirect":
            wb.open("https://www.linkedin.com/in/ibmabdulsalam/")
        if button == "Exit":
            sys.exit()
        if button == "Developer":
            s.Popup(DEVELOPER)
        if button == "Versions":
            s.Popup(VERSIONS)
        if button is None:
            break
        if button == 'C':
            key_entered=''
        if button in LOOKS:
            if change(THEME, button):
                sys.exit()
        if button == 'CE':
            key_entered=str(key_entered)[:-1]
        elif button in settings.ALL_ALPHA:
            key_entered=val['inval']
            key_entered+=button
        elif button in CONST_VAL:
            key_entered+=str(eval(CONST_VAL[button]))
        elif button in WAVE_FUNC:
            key_entered=val['inval']
            key_entered+=button
        elif button == 'ANS':
            try:
                key_entered = key_entered.replace("x", "*")
                key_entered = key_entered.replace("^", "**")
                for k in WAVE_FUNC:
                    if k in key_entered:
                        key_entered = key_entered.replace(k, WAVE_FUNC.get(k))
                        key_entered = key_entered
            except Exception as e:
                print(e)
            finally:
                key_entered = eval(key_entered)
            
        elif key_entered == NameError:
            key_entered=''
        else:
            key_entered=''
    except [AttributeError, SyntaxError]:
        key_entered='Error'

    except TypeError:
        key_entered=''
        key_entered=val['inval']
        
    else:
        key_entered='Error'
        
    win.find_element('inval').Update(key_entered)
