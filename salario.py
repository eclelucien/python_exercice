sal=float(input())



if 0<=sal<=400.00:
  p=15
  r=(sal*p)/100
  sala=sal+r

elif 400.01>=sal<=800:
  p=12
  r=(sal*p)/100
  sala=sal+r
    
elif 800.01>=sal<=1200.00:
  p=10
  r=(sal*p)/100
  sala=sal+r
    
elif 1200.01>=sal<=2000.00:
  p=7
  r=(sal*p)/100
  sala=sal+r
    
else:
  if sal>2000.00:
    p=4
    r=(sal*p)/100
    sala=sal+r

print("Novo salario: ",'{:.2f}'.format(sala))
print("Reajuste ganho: ",'{:.2f}'.format(r))
print("Em percentual: ",p ,"%")