#autor: jasmin tomas
#fecha: 02_11_23
#descripcion:

def minutos_segundos(min):
    return min * 60

if __name__ == "__main__":
    minutos=int(input("ingrese los minutos: \n"))
    print(minutos_segundos(minutos))

