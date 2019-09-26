def power(a,b):
  if (b == 0):
    return print(1)
  elif (a == 0):
    return print(0)
  elif (b == 1):
    return print(a)
  else:
    return a*power(a,b-1)
    
 
power(3, 4)