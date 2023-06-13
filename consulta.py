import requests
apikey = "DF223BB7-A821-4236-B337-42BC0FFC7A2D"
criptos = ["BTC", "ETH","ETH", "USDT", "BNB", "USDC"]
fiats = ["EUR", "USD", " JPY"]

def test_input(arrays, mensaje):
    money = input(mensaje)
    while money not in arrays:
        print("Debe Ser una de las siguientes opciones", arrays)
        money = input(mensaje)
    return money

def get_rate(cripto, fiat):

    url = f"https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat}?apikey={apikey}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return True, data['rate']
            
        else:
            return data['error']
            
    except requests.exceptions.RequestException as e:
        return False, str(e)

        

cripto = test_input(criptos, "Que criptomoneda quieres usar? ")

fiat = test_input(fiats, "en que moneda la quieres? ")


is_Ok, data = get_rate(cripto, fiat)

if is_Ok:
    
    print(f"1 {cripto} vale {data:.2f}{fiat}")

else:
    print("se ha producido el error : {data}")

#print(response.status_code)
#print(response.text)

# 1 BTC Vale 23000.00 EUR



