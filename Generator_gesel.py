from tkinter import *
import random

class Generiraj:
    def __init__(self, okno):
        Label(okno, text='Vnesite dolžino gesla').grid(row=0, column=0,sticky=W)
        self.vnos = Entry(okno, text='0,0')
        self.vnos.grid(row=1, column=0)

        self.izpis1 = DoubleVar(okno)
        izpis = Entry(okno, textvariable=self.izpis1).grid(row=4, column=0, sticky=W)

        Button(okno, text='Generiraj', command=self.generiraj).grid(row=4, column=1, sticky=W)
        
        self.var1 = IntVar()
        Checkbutton(okno, text="velike črke", var=self.var1).grid(row=1, column=1, sticky=W)
        self.var2 = IntVar()
        Checkbutton(okno, text="male črke", variable=self.var2).grid(row=2, column=1, sticky=W)
        self.var3 = IntVar()
        Checkbutton(okno, text="znaki", variable=self.var3).grid(row=3, column=1, sticky=W)
        
        
    def generiraj(self):
        print(self.var1.get())
        print(self.var2.get())
        print(self.var3.get())
        with open('sestavni_deli_gesla.txt', 'r') as dat:
            x = float(self.vnos.get())
            geslo = []
            sez = []
            for line in dat:
                sez += [line[:-1]]
            while x:
                x -= 1
                vrstica = random.randint(0,3)
                if vrstica < 3:
                    znak = random.randint(0,25)
                if vrstica == 2:
                    znak = random.randint(0,9)
                if vrstica == 3:
                    znak = random.randint(0,8)
                geslo += sez[vrstica][znak]
            self.izpis1.set(''.join(geslo))
            
        



okno = Tk()
app = Generiraj(okno)
okno.mainloop()
