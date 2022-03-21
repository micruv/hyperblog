import random

def run ():
    num_ram = random.randint(1,100)
    num_elegido = int(input("Vamos a jugar un juego el cual consiste en adivinar el numero que la maquina a seleccionadod e manera a leatoria<-elije un numero del 1 al 100->:"))
    while num_elegido != num_ram:
        if num_elegido < num_ram:
           print("busca un numero mas grande")
        else:
            print("busca un numero mas pequeno")
        num_elegido = int(input("ingresa otro numero-> "))
            
    print("GANASTE!!!!")


if __name__ =='__main__':
 run()