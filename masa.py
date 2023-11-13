#autor: jasmin tomas
#fecha: 02_11_23
#descripcion: Es te modulo sirve para saber 

def gramos_kilos(kg):
    return  kg / 1000

if __name__ == "__main__":
    gramos=int(input("ingrese datos en gramos: \n"))
    print(gramos_kilos(gramos),"Kilos")