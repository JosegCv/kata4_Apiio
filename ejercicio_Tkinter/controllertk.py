
from ejercicio_Tkinter.viewtk import  Display, Desplegable, Bottom
import tkinter as tk
WIDTH = 600
HEIGHT = 800

class Controller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("cripto conversor")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
        self.desplegable1= Desplegable(self,"CRIPTOS", "BTC", "ETH", "USDT", "BNB", "USDC")
        self.desplegable1.grid(column=1, row=2)
        

        self.desplegable2= Desplegable(self, "FIAT","EUR","USD", "JYP")
        self.desplegable2.grid(column=3,row=2 )
        
        self.display=Display(self)
        self.display.grid(column=1, row=6,columnspan=5, sticky="WE")

        self.botonsito= Bottom(self,"convertir")
        self.botonsito.grid(column=5, row=2)
