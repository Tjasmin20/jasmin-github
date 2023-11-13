#autor: jasmin tomas
#fecha: 02_11_23
#descripcion: Este Modulo es el menu de conversion de unidades

import masa as ma
import temperatura as temp
import tiempo as tm

def main():
    while True:
        opcion = input("Bienvenido, que unidades desea convertir?: \n" 
                "0. Salir del Programa\n"
                "1. Gramos a Kilos\n"
                "2. Celsius a Farenheit\n"
                "3. Minutos a Segundos\n")
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            
            elif opcion == (1):
                gramos=int(input("ingrese datos en gramos: \n"))
                print(ma.gramos_kilos(gramos),"Kilos")
            
            elif opcion == (2):
                celsius= float(input("Ingrese los grados a convertir \n"))
                print(temp.celsius_fahrenheit(celsius))

            elif opcion == (3):
                minutos=int(input("ingrese los minutos: \n"))
                print(tm.minutos_segundos(minutos), "Segundos")

        except ValueError:
            print("Solo puede ingresar valores numéricos.")

main()


