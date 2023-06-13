def test_input(arrays, mensaje):
    arrays = list(map(lambda x: x.upper(), arrays))
    resp = input(mensaje).upper()

    while resp not in arrays:
        print("Debe Ser una de las siguientes opciones", arrays)
        resp= input(mensaje)
    return resp

def output(is_Ok, cripto, fiat, data):
    if is_Ok:
        print(f"1 {cripto} vale {data:.2f} {fiat}")
    else:
        print(f"se ha producido un error: {data}")

