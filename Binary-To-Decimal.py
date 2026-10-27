def btod(num):
  num=str(num)
  num=num[::-1]
  print(type(num))
  total=0
  for i in range(0,len(num)):
    total+= int(num[i])*2**(i)

  return total
  

print(btod(10011))
