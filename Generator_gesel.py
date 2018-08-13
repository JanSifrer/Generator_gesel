from tkinter import *
from tkinter import messagebox
import secrets

class Geslo:
    def __init__(self):
        self.geslo = []

    def novo(self):
        izpis1.set(0.0)

    def navodila(self):
        messagebox.showinfo("Navodila", """V prvo vrstico vnesite dolžino željenega gesla. Nato na desni strani izberite iz katerih znakov naj bo sestavljeno geslo. V nasprotnem primeru, bo geslo vsebovalo vse simbole. """)

    def pomoc(self):
        messagebox.showinfo("Pomoč", "Za  dodatna pojasnila nas kontaktirajte na: jan.sifrer@student.fmf.uni-lj.si")

    def shrani(self):
        with open("gesla.txt", "a") as gesla:
                gesla.write("{}\n".format(self.geslo))
        messagebox.showinfo("Shranjeno", "Vaše geslo je shranjeno v datoteko, ki se nahaja v isti mapi kot program.")



    def generiraj(self):
        a = int(velike_crke.get())
        b = int(male_crke.get())
        c = int(stevilke.get())
        d = int(znaki.get())
        with open("sestavni_deli_gesla.txt", "r") as dat:
            x = vnos.get()
            try:
                x = int(x)
            except ValueError:
                return messagebox.showerror("NAPAKA", "Vnesite veljavno dolžino!")
            self.geslo = []
            sez = []
            sez_gesla = []
            for line in dat:
                sez += [line[:-1]]
            if a == 1:
                sez_gesla += sez[0]
            if b == 1:
                sez_gesla += sez[1]
            if c == 1:
                sez_gesla += sez[2]
            if d == 1:
                sez_gesla += sez[3]
            if a == b == c == d == 0:
                sez_gesla = ''.join(sez)

            while x:
                x -= 1
                znak = secrets.randbelow(len(sez_gesla)-1)
                self.geslo += sez_gesla[znak]
            self.geslo = ''.join(self.geslo)
            izpis1.set(self.geslo)
          

    

okno = Tk()
okno.title("Generator")
geslce = Geslo()
menubar = Menu(okno)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Novo", command=geslce.novo)
filemenu.add_separator()
filemenu.add_command(label="Izhod", command=okno.destroy)
filemenu.add_separator()
menubar.add_cascade(label="Datoteka", menu=filemenu)

menubar.add_command(label="Shrani", command=geslce.shrani)

menubar.add_command(label="Navodila", command=geslce.navodila)

menubar.add_command(label="Pomoč", command=geslce.pomoc)
okno.config(menu=menubar)


Label(okno, text="Vnesite dolžino gesla").grid(row=0, column=0, sticky=W)

Label(okno, text="Izberite katere simbole\nnaj vsebuje geslo.").grid(row=0, column=1)

vnos = Entry(okno, font = "1", width="25")
vnos.grid(row=1, column=0)

izpis1 = DoubleVar(okno)
izpis = Entry(okno, textvariable=izpis1, font = "2", width="25").grid(row=5, column=0, sticky=W)

Button(okno, text="Generiraj", command=geslce.generiraj, height=3, width=8).grid(row=5, column=1, sticky=W)


velike_crke= DoubleVar()
Checkbutton(okno, text="velike črke", variable=velike_crke).grid(row=1, column=1, sticky=W)
male_crke = DoubleVar()
Checkbutton(okno, text="male črke", variable=male_crke).grid(row=2, column=1, sticky=W)
stevilke = DoubleVar()
Checkbutton(okno, text="številke", variable=stevilke).grid(row=3, column=1, sticky=W)
znaki = DoubleVar()
Checkbutton(okno, text="znaki", variable=znaki).grid(row=4, column=1, sticky=W)

app = Geslo()
okno.mainloop()
