#! /usr/bin/env python3
#
# Tarefa de laboratorio 02 - Bazinga
#
# GEX605 AB 2020/1
#
# Nome:      XXXX
# Matricula: XXXX
#
# Data:      23/09/2020
#

r=int(input())
i =0;
while (i < r):
    i+=1
    sheldon, raj = input().split()
    if sheldon == raj:
        print("Caso #%d: De novo!"%i)
    else:
        if (sheldon == "tesoura" and (raj == "papel" or raj == "lagarto" )):
            print("Caso #%d: Bazinga!"%i)
        else:
            if (sheldon == "papel" and (raj == "pedra" or raj == "Spock")):
                print("Caso #%d: Bazinga!"%i)
            else:
                if (sheldon == "pedra" and (raj == "lagarto" or raj == "tesoura")):
                    print("Caso #%d: Bazinga!"%i)
                else:
                    if (sheldon == "lagarto" and (raj == "Spock" or raj == "papel")):
                        print("Caso #%d: Bazinga!"%i)
                    else:
                        if (sheldon == "Spock" and (raj == "tesoura" or raj == "pedra")):
                            print("Caso #%d: Bazinga!"%i)
                        else:
                            print("Caso #%d: Raj trapaceou!"%i)

