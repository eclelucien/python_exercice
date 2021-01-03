s, t, f=int(input()).split()

if soma == 24:
  result=0
else:
  if soma > 23:
    result=soma-24
  else: 
    if soma<0:
      result=soma+24
    else:
      result=soma
print(result)