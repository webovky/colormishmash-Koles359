# -*- coding: utf-8 -*-

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, Canvas, Entry, HORIZONTAL, StringVar, Label, Frame, messagebox, IntVar, Button

soubor = open("color.txt", "r")
bar = soubor.read()
soubor.close()


class Mishmash(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Color_Search")
        self.master.maxsize(1500, 3000)
        self.master.resizable(True, True)
        self.master.rowconfigure(0, weight=500)
        self.master.rowconfigure(1, weight=500)
        self.master.rowconfigure(2, weight=500)
        self.master.rowconfigure(3, weight=500)
        self.master.rowconfigure(4, weight=500)
        self.master.columnconfigure(0, weight=1500)
        self.master.columnconfigure(1, weight=1500)
        self.master.columnconfigure(2, weight=1500)
        self.rozmisteni()


        self.pole["background"] = bar
        self.varBarva.set(bar)



    def rozmisteni(self):
        self.napis = Label(text="Vítejte v míchačce barev!")
        self.napis.grid(row=0, column=1)
        self.napis2 = Label(text="Barva:")
        self.napis2.grid(row=1, column=2)

        self.r= Scale(from_=0, to=255, orient=HORIZONTAL, length=500, bg="red", command=self.setting)
        self.r.grid(row=1, column=1)
        self.vstupr = Entry(width=15, bd=10, justify="center")
        self.vstupr.grid(row=1, column=0)
       
        self.g = Scale(from_=0, to=255, orient=HORIZONTAL, length=500, bg="green", command=self.setting)
        self.g.grid(row=2, column=1)
        self.vstupg = Entry(width=15, bd=10, justify="center")
        self.vstupg.grid(row=2, column=0)
        
        self.b = Scale(from_=0, to=255, orient=HORIZONTAL, length=500, bg="blue", command=self.setting)
        self.b.grid(row=3, column=1)
        self.vstupb = Entry(width=15, bd=10, justify="center")
        self.vstupb.grid(row=3, column=0)

        self.tlacitko = Button(width=15, bd=10, justify="center", text="Použít", command=self.set)
        self.tlacitko.grid(row=4, column=0)

        self.pole = Canvas(background="#000000", width=200, height=100)
        self.pole.grid(row=2, column=2)

        self.varBarva = StringVar()
        self.vystup = Entry(textvariable=self.varBarva, width=15, bd=10, justify="center", state="readonly")
        self.vystup.grid(row=3, column=2)
    
    def setting(self, event):
        r = self.r.get()
        g = self.g.get()
        b = self.b.get()
        barva = "#%02x%02x%02x" % (r, g, b)
        barva = "#{:02x}{:02x}{:02x}".format(r, g, b)
        print(barva)
        self.pole.config(bg=barva)
        self.varBarva.set(barva)


        soubor = open("color.txt", "w")
        soubor.write(barva)
        soubor.close()

    def set(self):
        r2 = self.vstupr.get()
        g2 = self.vstupg.get()
        b2 = self.vstupb.get()

        if r2 != "" or g2 != "" or b2 != "": 
            if r2 == "":
                self.r.set(0)
                pass
            else:
                if r2 not in "qwertzuiopasdfghjklyxcvbnmůú,.-§)=éíáýžřčšě+-*/":
                    if 0 < int(r2) < 256:
                        self.r.set(int(r2))
                    else:
                        messagebox.showerror("Chyba", "Lze vkládat pouze čísla od 0 do 255 včetně.")
                else:
                    messagebox.showerror("Chyba", "Lze vkládat pouze čísla od 0 do 255 včetně.")
            

            if g2 == "":
                self.g.set(0)
                pass
            else:
                if g2 not in "qwertzuiopasdfghjklyxcvbnmůú,.-§)=éíáýžřčšě+-*/":
                    if 0 < int(g2) < 256:
                        self.g.set(int(g2))
                    else:
                        messagebox.showerror("Chyba", "Lze vkládat pouze čísla od 0 do 255 včetně.")
                else:      
                    messagebox.showerror("Chyba", "Lze vkládat pouze čísla od 0 do 255 včetně.")


            if b2 == "":
                self.b.set(0)
                pass
            else:
                if b2 not in "qwertzuiopasdfghjklyxcvbnmůú,.-§)=éíáýžřčšě+-*/":
                    if 0 < int(b2) < 256:
                        self.b.set(int(b2))
                    else:
                        messagebox.showerror("Chyba", "Lze vkládat pouze čísla od 0 do 255 včetně.")    
                else:
                    messagebox.showerror("Chyba", "Lze vkládat pouze čísla od 0 do 255 včetně.")

        else:
            messagebox.showerror("Chyba", "Vložte čísla od 0 do 255 včetně.")
            

        barva = "#%02x%02x%02x" % (int(r2), int(g2), int(b2))
        barva = "#{:02x}{:02x}{:02x}".format(int(r2), int(g2), int(b2))
        print(barva)
        self.pole.config(bg=barva)
        self.varBarva.set(barva)


        soubor = open("color.txt", "w")
        soubor.write(barva)
        soubor.close()

    



root = tk.Tk()
app = Mishmash(root)
root.mainloop()





