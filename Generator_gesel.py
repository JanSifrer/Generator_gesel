from tkinter import *
import secrets
from tkinter import messagebox

class Generiraj:
    def __init__(self, okno):
        self.menubar = Menu(okno)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='New')
        self.filemenu.add_separator()
        okno.config(menu=self.menubar)
        okno.title('Generator')
        self.okno = okno
##        
##        
##        Label(okno, text='Vnesite dolžino gesla').grid(row=0, column=0, sticky=W)
##
##        Label(okno, text='Izberite katere simbole\nnaj vsebuje geslo.').grid(row=0, column=1)
##
##        self.vnos = Entry(okno, text='0', font = '1')
##        self.vnos.grid(row=1, column=0)
##        
##        self.izpis1 = DoubleVar(okno)
##        izpis = Entry(okno, textvariable=self.izpis1, font = '2', width=25).grid(row=5, column=0, sticky=W)
##
##        Button(okno, text='Generiraj', command=self.generiraj, height=5, width=10).grid(row=5, column=1, sticky=W)
##
##        
##        self.var1 = IntVar()
##        Checkbutton(okno, text="velike črke", variable=self.var1).grid(row=1, column=1, sticky=W)
##        self.var2 = IntVar()
##        Checkbutton(okno, text="male črke", variable=self.var2).grid(row=2, column=1, sticky=W)
##        self.var3 = IntVar()
##        Checkbutton(okno, text="številke", variable=self.var3).grid(row=3, column=1, sticky=W)
##        self.var4 = IntVar()
##        Checkbutton(okno, text="znaki", variable=self.var4).grid(row=4, column=1, sticky=W)
##
##
##            
##    def generiraj(self):
##        a = float(self.var1.get())
##        b = float(self.var2.get())
##        c = float(self.var3.get())
##        d = float(self.var4.get())
##        with open('sestavni_deli_gesla.txt', 'r') as dat:
##            x = (self.vnos.get())
##            try:
##                x = int(x)
##            except ValueError:
##                return messagebox.showerror('NAPAKA', 'vnesite veljavno stevilko')
##            geslo = []
##            sez = []
##            sez_gesla = []
##            for line in dat:
##                sez += [line[:-1]]
##            if a == 1:
##                sez_gesla += sez[0]
##            if b == 1:
##                sez_gesla += sez[1]
##            if c == 1:
##                sez_gesla += sez[2]
##            if d == 1:
##                sez_gesla += sez[3]
##            if a == b == c == d == 0:
##                sez_gesla = ''.join(sez)
##                
##            while x:
##                x -= 1
##                znak = secrets.randbelow(len(sez_gesla)-1)
##                geslo += sez_gesla[znak]
##            self.izpis1.set(''.join(geslo))
##
##
##

okno = Tk()
app = Generiraj(okno)
okno.mainloop()
