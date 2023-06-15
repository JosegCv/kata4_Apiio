import requests
criptos = ["BTC", "ETH","ETH", "USDT", "BNB", "USDC"]
fiats = ["EUR", "USD", " JPY"]
apikey = "DF223BB7-A821-4236-B337-42BC0FFC7A2D"


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