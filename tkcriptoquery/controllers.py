import tkinter as tk
import requests
from criptoquery.models import get_rate
class Desplegable(tk.Frame):
    def __init__(self, location, title, *options):

        super().__init__(location, width=200, height= 50)
        # Variable para almacenar la opción seleccionada
        self.selected_option = tk.StringVar(self)
        self.selected_option.set(title)  # Opción seleccionada por defecto

    # Crear el menú desplegable
        option_menu = tk.OptionMenu(self,self.selected_option,*options)
        option_menu.pack()

class Converter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.criptos=Desplegable(self, "CRIPTO", "BTC", "ETH", "USDT", "BNB", "USDC")
        self.criptos.grid(column=0, row=0)
        

        self.fiats= Desplegable(self,"FIAT", "USD", "EUR", "JPY")
        self.fiats.grid(column=1,row=0)
        

        self.result = tk.Label(self)
        self.result.grid(row=1,column=1)

        tk.Button(self, text="Consultar",
                  command= lambda: "Aqui Llamaria a Coinapiio y mostraria el resultado en el self.result").grid(
            column=1, row=1)
    
    def validate_button(self, *args):
        cripto = self.criptos.selected_option.get()
        fiat = self.fiats.selected_option.get()

        status= cripto != "CRIPTO" and fiat != "FIATS"

    def get_rate(self):
        cripto = self.criptos.selected_option.get()
        fiat = self.fiats.selected_option.get()

    

        if cripto != "CRIPTO" and fiat != "FIAT":
            url = f"https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat}?apikey=858A97FA-0E48-4922-BDEC-E464C918B842"
            try: # Este try except es un print para el programador por si la url es equivoca.
                response = requests.get(url)
                data = response.json()

                if response.status_code == 200:
                    self.result.config(text=data['rate'])
                else:
                    self.result.config(text=data['error'])    
                
            except requests.exceptions.RequestException as e:
                self.result.config(text=str(e))    
        
        else:

            self.result.config(text="Debes seleccionar ambos valores")
    def get_rate(self):
        cripto = self.criptos.selected_option.get()
        fiat = self.fiats.selected_option.get()

        if cripto != "CRIPTO" and fiat != "FIAT":
            is_ok, data = get_rate(cripto, fiat)
            if is_ok:
                self.result.config(text=data)
            else:
                self.result.config(text="Se ha producido un error en la consulta")
        else:
            self.result.config(text="Debes seleccionar ambos valores")