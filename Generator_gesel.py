from tkinter import *
from tkinter import messagebox
import secrets


class Generiraj:
    def __init__(self, okno):
        okno.title("Generator")
        self.okno = okno
        
        menubar = Menu(okno)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Novo", command=self.novo)
        filemenu.add_separator()
        filemenu.add_command(label="Izhod", command=okno.destroy)
        filemenu.add_separator()
        menubar.add_cascade(label="Datoteka", menu=filemenu)

        menubar.add_command(label="Shrani", command=self.shrani)


        menubar.add_command(label="Navodila", command=self.navodila)

        menubar.add_command(label="Pomoč", command=self.pomoc)
        okno.config(menu=menubar)

        
        Label(okno, text="Vnesite dolžino gesla").grid(row=0, column=0, sticky=W)

        Label(okno, text="Izberite katere simbole\nnaj vsebuje geslo.").grid(row=0, column=1)

        self.vnos = Entry(okno, font = "1", width="25")
        self.vnos.grid(row=1, column=0)
        
        self.izpis1 = DoubleVar(okno)
        izpis = Entry(okno, textvariable=self.izpis1, font = "2", width="25").grid(row=5, column=0, sticky=W)

        Button(okno, text="Generiraj", command=self.generiraj, height=3, width=8).grid(row=5, column=1, sticky=W)

        Button(okno, text="Kopiraj", command=self.kopiraj).grid(row=6, column=0, sticky=W)
        
        self.var1 = IntVar()
        Checkbutton(okno, text="velike črke", variable=self.var1).grid(row=1, column=1, sticky=W)
        self.var2 = IntVar()
        Checkbutton(okno, text="male črke", variable=self.var2).grid(row=2, column=1, sticky=W)
        self.var3 = IntVar()
        Checkbutton(okno, text="številke", variable=self.var3).grid(row=3, column=1, sticky=W)
        self.var4 = IntVar()
        Checkbutton(okno, text="znaki", variable=self.var4).grid(row=4, column=1, sticky=W)


    def generiraj(self):
        a = int(self.var1.get())
        b = int(self.var2.get())
        c = int(self.var3.get())
        d = int(self.var4.get())
        with open("sestavni_deli_gesla.txt", "r") as dat:
            x = (self.vnos.get())
            try:
                x = int(x)
            except ValueError:
                return messagebox.showerror("NAPAKA", "Vnesite veljavno dolžino!")
            geslo = []
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
                geslo += sez_gesla[znak]
            self.geslo = ''.join(geslo)
            self.izpis1.set(self.geslo)

    def novo(self):
        self.izpis1.set(0.0)

    def shrani(self):
        with open("gesla.txt", "w") as gesla:
            gesla.write(self.geslo)
            print("Vaša datoteka je shranjena v isti mapi kot program.")
            

    def navodila(self):
        messagebox.showinfo("Navodila", """V prvo vrstico vnesite dolžino željenega gesla. Nato na desni strani izberite iz katerih znakov naj bo sestavljeno geslo. V nasprotnem primeru, bo geslo vsebovalo vse simbole. """)

    def pomoc(self):
        messagebox.showinfo("Pomoč", "Za  dodatna pojasnila nas kontaktirajte na: jan.sifrer@student.fmf.uni-lj.si")

    def kopiraj(self):
        okno.clipboard_clear()
        okno.clipboard_append(self.geslo)
        print('Geslo je skopirano!')
        

okno = Tk()
app = Generiraj(okno)
okno.mainloop()
