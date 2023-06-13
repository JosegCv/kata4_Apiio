from criptoquery.view import test_input , output
from criptoquery.models import criptos, fiats, get_rate

class Controller:
    def mainloop(self):
        
        while True:
        #usando la vista para entrada de datos del usuario

            cripto = test_input(criptos, "que cripto quieres ")
            fiat = test_input(fiats, "que moneda quieres ")


     #usar modelo para obetener datode internet

            is_Ok, data = get_rate(cripto, fiat)

        #tendria que ir a la vista pero todavia no
            output(is_Ok, cripto, fiat, data)

            #preguntar si seguimos
            more_conversions = test_input(('S', 'N'),"quieres introducir mas monedas? ")
            if more_conversions != 'S':
                 break