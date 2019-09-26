#def rec(n):
 #   if n < 5:
  #      rec(n+1)
   # print(n)

#rec(1)

#def fib (n): # 1 1 2 3 5 8 13 21 34 55 89 ...
 #   if n < 2:
  #      return 1
   # return fib(n-1) + fib(n-2)

#print(fib(8))

#def factorial (n):
 #   if n < 2:
  #      return 1
   # return n * factorial(n-1)
#print (factorial(5))

#TAREA
def power(a,b):
    if b==0:
        return 1
    else:
        if a==0:
            return 0
        else:
            if b==1:
                return a
            else:
                return a*power(a,b-1)
print(power(3,4))