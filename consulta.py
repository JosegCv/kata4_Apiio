import requests
apikey = "DF223BB7-A821-4236-B337-42BC0FFC7A2D"

url = f"https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey={apikey}"

response = requests.get(url)

print(response.status_code)
print(response.text)