valor=input().split()
a=int(valor[0])
b=int(valor[1])
mul=a%b
mu=b%a
if mul==0 or mu==0:
  print("Sao Multiplos")
else:
  print("Nao sao Multiplos")