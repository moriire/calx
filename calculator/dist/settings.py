import string
THEME="DarkTeal10"
LOOKS=(
    "DarkTeal10",
    "DarkTeal10",
    "DarkGrey2",
    "DarkPurple4",
    "LightGreen6",
    "DarkTeal10",
    "DarkBlack1"
    )
FONT=('helvetica',15)
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
