valor=int(input())
print(valor)
#total=valor
ced=100
totced=0
while True:
  if valor >=ced:
    valor -=ced
    totced+=1
    
  else:
       print("{} nota(s) de R$ {},00".format( totced, ced))
       if ced==100:
         ced=50
       elif ced==50:
        ced=20
       elif ced==20:
        ced=10
       elif ced==10:
        ced=5
       elif ced==5:
        ced=2
       elif ced==2:
         ced=1
       elif ced==1:
         ced=0
       totced=0
       if valor==0:
        break