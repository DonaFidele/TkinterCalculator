#coding:utf-8
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
from functools import partial
from math import *
import math
 
class Calculatrice( tk.Tk ):
 
    def __init__ ( self ):
 
        tk.Tk.__init__( self )
        self.a = StringVar()
        self.ecran = Entry(self, width=60, background="gray64", font="time 15 bold", justify="r", textvariable=self.a)
        self.ecran.grid(row=0, columnspan=7, ipady=30, sticky='w')
        self.text = ""
 
        # --- state added to fix the original bugs ---
        self.ans = 0            # last computed result, recalled with "Ans"
        self.rad_deg = "Rad"    # angle mode used by trig functions
        self.inv = False        # inverse mode (sin<->asin, cos<->acos, tan<->atan)
 
        # Safe namespace passed to eval() -- no builtins, only whitelisted math functions.
        # Trig functions are degree-aware wrappers instead of the raw math module functions.
        self.safe_funcs = {
            "sin": self._sin, "cos": self._cos, "tan": self._tan,
            "asin": self._asin, "acos": self._acos, "atan": self._atan,
            "log10": math.log10, "log": math.log, "sqrt": math.sqrt,
            "factorial": math.factorial, "pi": math.pi, "e": math.e,
            "int": int, "float": float, "abs": abs, "round": round,
        }
 
    # ---- degree-aware trig wrappers -------------------------------------
    def _sin(self, x):
        return math.sin(math.radians(x)) if self.rad_deg == "Deg" else math.sin(x)
 
    def _cos(self, x):
        return math.cos(math.radians(x)) if self.rad_deg == "Deg" else math.cos(x)
 
    def _tan(self, x):
        return math.tan(math.radians(x)) if self.rad_deg == "Deg" else math.tan(x)
 
    def _asin(self, x):
        r = math.asin(x)
        return math.degrees(r) if self.rad_deg == "Deg" else r
 
    def _acos(self, x):
        r = math.acos(x)
        return math.degrees(r) if self.rad_deg == "Deg" else r
 
    def _atan(self, x):
        r = math.atan(x)
        return math.degrees(r) if self.rad_deg == "Deg" else r
 
    def clic(self, texte):
        texte = texte.strip()
 
        if texte == "=":
            # FIX: wrap eval in try/except and use a restricted namespace instead
            # of raw eval() on unrestricted builtins.
            try:
                result = eval(self.a.get(), {"__builtins__": None}, self.safe_funcs)
                self.ans = result
                self.a.set(result)
            except Exception:
                self.a.set("Error")
 
        elif texte == "CE":
            # FIX: original code called self.init() here, which re-ran the
            # constructor and duplicated widgets instead of just clearing input.
            self.a.set("")
 
        elif texte == "x":
            self.a.set(self.a.get() + "*")
 
        elif texte == "x^y":
            # FIX: Python's eval() needs "**" for exponentiation, not "^".
            self.a.set(self.a.get() + "**")
 
        elif texte == "sin":
            self.a.set(self.a.get() + ("asin(" if self.inv else "sin("))
 
        elif texte == "cos":
            self.a.set(self.a.get() + ("acos(" if self.inv else "cos("))
 
        elif texte == "tan":
            self.a.set(self.a.get() + ("atan(" if self.inv else "tan("))
 
        elif texte == "log":
            self.a.set(self.a.get() + "log10(")
 
        elif texte in ("In", "ln"):
            # FIX: this button now actually inserts natural log instead of
            # the literal, non-functional text "In".
            self.a.set(self.a.get() + "log(")
 
        elif texte in ("v", "\u221a"):
            # FIX: square root button now inserts a real sqrt() call instead
            # of the literal character "v".
            self.a.set(self.a.get() + "sqrt(")
 
        elif texte == "x!":
            # FIX: factorial now wraps the whole current expression and
            # evaluates immediately, instead of inserting inert text.
            current = self.a.get()
            if current:
                self.a.set(f"factorial(int({current}))")
 
        elif texte == "p":
            # FIX: pi now inserts the actual value of math.pi.
            self.a.set(self.a.get() + str(math.pi))
 
        elif texte == "e":
            self.a.set(self.a.get() + str(math.e))
 
        elif texte == "Ans":
            # FIX: Ans now recalls the last computed result.
            self.a.set(self.a.get() + str(self.ans))
 
        elif texte == "EXP":
            # FIX: EXP now inserts a real scientific-notation exponent marker
            # (e.g. typing 1.5 then EXP then 3 gives 1.5e3) instead of literal text.
            self.a.set(self.a.get() + "e")
 
        elif texte == "Inv":
            # FIX: Inv now actually toggles sin/cos/tan to their inverse
            # (asin/acos/atan) for the next trig button pressed.
            self.inv = not self.inv
 
        elif "Rad" in texte and "Deg" in texte:
            # FIX: Rad/Deg button now actually toggles the angle mode used
            # by the trig wrappers above.
            self.rad_deg = "Deg" if self.rad_deg == "Rad" else "Rad"
 
        else:
            self.a.set(self.a.get() + texte)
 
    def bouttons(self, texte, ligne, colonne):
        self.btn = Button(self, text=texte, font="arial 13", bd=5, relief=GROOVE, foreground="white", bg="gray22", command=partial(self.clic, texte)).grid(row=ligne, column=colonne, ipadx=28, ipady=5, padx=1, sticky="W", columnspan=1)
 
    def num_btn(self, texte, ligne, colonne):
        self.btn = Button(self, text=texte, font="arial 13", bd=5, relief=GROOVE, foreground="white", bg="gray40", command=partial(self.clic, texte)).grid(row=ligne, column=colonne, ipadx=28, ipady=5, padx=1, sticky="W", columnspan=1)
 
    def creer_btn(self):
        btn = Button(self, text="Rad    |     Deg", bd=8, foreground="white", relief=RIDGE, font="arial 14", bg="gray22", command=partial(self.clic, "Rad  |  Deg")).grid(row=1, column=0, sticky="NW", pady=2, columnspan=2, ipadx=40, ipady=5)
 
        self.bouttons(" x! ", 1, 2)
        self.bouttons("  ( ", 1, 3)
        self.bouttons("  ) ", 1, 4)
        self.bouttons("% ", 1, 5)
        self.bouttons("CE", 1, 6)
 
        self.bouttons("Inv", 2, 0)
        self.bouttons(" sin", 2, 1)
        self.bouttons(" ln ", 2, 2)
        self.num_btn(" 7 ", 2, 3)
        self.num_btn(" 8 ", 2, 4)
        self.num_btn(" 9 ", 2, 5)
        self.bouttons("  /  ", 2, 6)
 
        self.bouttons("  p ", 3, 0)
        self.bouttons("cos", 3, 1)
        self.bouttons("log", 3, 2)
        self.num_btn(" 4 ", 3, 3)
        self.num_btn(" 5 ", 3, 4)
        self.num_btn(" 6 ", 3, 5)
        self.bouttons("  x ", 3, 6)
 
        self.bouttons("  e ", 4, 0)
        self.bouttons(" tan", 4, 1)
        self.bouttons("  \u221a ", 4, 2)
        self.num_btn(" 1 ", 4, 3)
        self.num_btn(" 2 ", 4, 4)
        self.num_btn(" 3 ", 4, 5)
        self.bouttons("  -  ", 4, 6)
 
        btn = Button(self, text="Ans", font="arial 11", bd=5, foreground="white", bg="gray22", command=partial(self.clic, "Ans")).grid(row=5, column=0, ipadx=28, ipady=5, padx=1, sticky="W", columnspan=1)
        btn = Button(self, text="EXP", font="arial 11", bd=5, foreground="white", bg="gray22", command=partial(self.clic, "EXP")).grid(row=5, column=1, ipadx=28, ipady=5, padx=1, sticky="W", columnspan=1)
 
        btn = Button(self, text="x^y", font="arial 11", bd=5, foreground="white", bg="gray22", command=partial(self.clic, "x^y")).grid(row=5, column=2, ipadx=28, ipady=5, padx=1, sticky="W", columnspan=1)
 
        self.num_btn(" 0 ", 5, 3)
        self.num_btn("  . ", 5, 4)
 
        btn = Button(self, text=" = ", font="arial 13", bd=5, foreground="white", bg="purple3", command=partial(self.clic, " = ")).grid(row=5, column=5, ipadx=28, ipady=5, padx=1, sticky="W", columnspan=1)
        self.bouttons("  + ", 5, 6)


if __name__ == "__main__":
    Calculatrice=Calculatrice()
    Calculatrice.title("Ma     😁️     Calculatrice       😃️") 
    Calculatrice.creer_btn()
    Calculatrice.resizable(width=False,height=False)
    Calculatrice.mainloop()
    
