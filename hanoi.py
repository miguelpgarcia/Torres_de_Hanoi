
import math


def move(n, origem, destino):
    if 1==n:
        print ("move de:"+str(origem)+" para:"+str(destino))
    else:
        sobra  = 3-origem-destino
        move(n-1,origem,sobra)
        move(1,origem,destino)
        move(n-1,sobra,destino)

def main():
    n = int(input("Entre com a quantidade de discos a ser movida (de 0 para 2):"))
    move(n,0,2)

if __name__ == "__main__":
    main()
