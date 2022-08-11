import PySimpleGUI as s
import math
import sys
import webbrowser as wb
import os
env = os.environ
import string
import subprocess as sp
size=(7,3)

LOOKS=(
    "LightGreen6",
    "DarkPurple4",
    "DarkBlack1"
    )
FONT=('Helvetica', 25)#env.get("FONT")
CONSTANTS = ("pi", "e")
BASIC = ["+", "-", "x"]
SYMB = (".","(", ")")
SYMBOLS = {i: f"math.{i}" for i in SYMB}
CONST_VAL = {i:f"math.{i}" for i in CONSTANTS}
WAVE = ("sin", "cos", "tan", 'log', 'sqrt')
WAVE_FUNC = {i: f"math.{i}" for i in WAVE}
ARITHMETIC = {"+":"+", "-":"-", "x":"*", "/":"/","^":"**"}
DIGITS = dict(zip(string.digits, string.digits))
FIELDS = (*string.digits, *CONSTANTS, *SYMB)
ALL_ALPHA = {**DIGITS, **ARITHMETIC, **SYMBOLS}
DEVELOPER = """
IBM Abdulsalam.
linkedin: https://www.linkedin.com/in/ibmabdulsalam/
facebook: https://www.facebook.com/ibmabdulsalam
github: https://www.github.com/moriire
"""
VERSIONS = """
IBM Abdulsalam.
v3.2.0
"""
try:
    THEME=env["THEME"]
except KeyError:
    THEME = "DarkPurple4"
    env["THEME"] = THEME


def change(field, new_val):
    sp.run(['set',f"{field}={new_val}"], shell=True)
    #os.putenv(field, new_val)
    #env[field] = new_val
    return 1

MENU_COLOR = s.LOOK_AND_FEEL_TABLE[env["THEME"]]
FIELD_LENGTH = len(FIELDS)
change_look=env["THEME"]

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
    [s.InputText('',key='inval', font=FONT, size=(27, 3), pad=(5,15))],
    figures,
    [
        s.ReadButton(w, size=size) for w in WAVE
    ],
    [s.ReadButton('ANS', size=(16,3)),s.ReadButton('C', size=size),
    s.ReadButton('CE', size=size)],
   
    [s.Text('IBM Abdulsalam - For Educational Purpose', enable_events=True, key="redirect", tooltip="Click to view my profile")]
    ]
win=s.Window('Calx v3.1.0',size=(320,560)).Layout(gui)
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
            if change("THEME", button):
                print(button)
                sys.exit()
        if button == 'CE':
            key_entered=str(key_entered)[:-1]
        elif button in ALL_ALPHA:
            key_entered=val['inval']
            key_entered+=str(button)
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
    except (AttributeError, SyntaxError) as err:
        print(err)
        key_entered='Error'

    except TypeError:
        key_entered=''
        key_entered=val['inval']
        
    except Exception:
        key_entered=''
        continue
        
    win.find_element('inval').Update(key_entered)
