#return - para regresar un resultado
# def para crear funciones

from ast import Return


def conver(tipo_peso, dollar, opcion):
    print("has seleccionado la " + opcion)
    peso = input ("digite el monto a convertir de " + tipo_peso +" a dollar: ")
    peso = float(peso)
    dolar = (dollar)
    resultado = peso / dolar
    resultado = round(resultado, 3)
    resultado = str(resultado)
    print ("usted tiene:" + resultado + " dolares")
menu = """
bienvenidos al conversor de monedas asu equivalente en dollar, elija que tipo de moneda decea convertir
 
 1-pesos Dominicanos
 2-pesos Colombianos
 3-pesos Mexicano
 4-pesos Argentino
 5-Bolivares
 
 elige una ocpion: """

opcion = int(input(menu))
if opcion == 1:
    conver(" Pesos Dominicano", 57.64, "  opcion 1")

elif opcion ==2:
   conver(" Pesos Colombiano", 3875, "  opcion 2")
elif opcion ==3:
   conver(" Pesos Mexicano", 65.57, "  opcion 3")
elif opcion ==4:
    conver(" Pesos Argentino", 65.57, "  opcion 3")
elif opcion ==5:
    conver(" Bolivares", 65.57, "  opcion 3")
else:
    print("ingrece una opcopn valida que contenga solo numeros del 1 al 5")
    #return menu;




