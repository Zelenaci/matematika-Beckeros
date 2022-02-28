import random
import tkinter as tk
from xml.dom.minidom import Entity
from os.path import basename, splitext
from tkinter.constants import END


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "MAT GAME"



    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="")
        self.generuj()
        self.vysledek_vstup = tk.Entry(self)
        self.vysledek_vstup.grid(row=3, column=1)
        self.lbl_hodnoceni = tk.Label(self, text="")
        self.lbl_hodnoceni.grid(row=4,column=1)
        self.btn3 = tk.Button(self, text="CHECK", command=self.kontrola)
        self.btn3.grid(row=5, column=1)



    def plus(self):
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,100-self.cisloA)#aby vysledek nebyl větší než 100
        self.vysledek = self.cisloA + self.cisloB
        return str(self.cisloA)+"+"+str(self.cisloB)


    def minus(self):
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,self.cisloA)
        self.vysledek = self.cisloA - self.cisloB
        return str(self.cisloA)+"-"+str(self.cisloB)





    def krat(self):
        self.cisloA = random.randint(1,10)
        self.cisloB = random.randint(1,10)
        self.vysledek = self.cisloA * self.cisloB
        return str(self.cisloA)+"*"+str(self.cisloB)

        


    def deleno(self):
        self.vysledek = random.randint(1,10)
        self.cisloB = random.randint(1,10)
        self.cisloA = self.vysledek * self.cisloB
        return str(self.cisloA)+ "/" +str(self.cisloB)



    def generuj(self):
        self.funkce = random.choice([self.plus,self.minus,self.krat,self.deleno])
        self.priklad = self.funkce()
        self.lbl.config(text= self.priklad)
        self.lbl.grid(row=1,column=1)
        



    def kontrola(self):
        if int(self.vysledek_vstup.get()) == int(self.vysledek):
            self.lbl_hodnoceni.config(text="CORRECT")
        else:
            self.lbl_hodnoceni.config(text="WRONG")
        self.generuj()
        self.vysledek_vstup.delete(0,END)
        








app = Application()
app.mainloop()