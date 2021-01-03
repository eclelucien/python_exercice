#! /usr/bin/env python3
#
# Tarefa de laboratorio 03 - Greve
#
# GEX605 AB 2020/1
#
# Nome:      XXXX
# Matricula: XXXX
#
# Data:      23/09/2020
#

r=int(input())

somaG = 0
somaV = 0

while (r > 0):
    r-=1
    tipo, val = input().split()

    if tipo == 'G':
        somaG+=int(val)
    else:
        somaV+=int(val)

if (somaG > somaV):
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")
