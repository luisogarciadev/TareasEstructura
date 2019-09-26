#def rec(n):
 #   if n < 5:
  #      rec(n+1)
   #     print(n)

#rec(1)

#def fib(n):
 #   if n < 2:
  #      return 1
   # return fib(n-1) + fib(n-2)

#print(fib(8))

#def factorial(n):
 #   if n == 1:
  #      return n
   # return n * factorial(n-1)

#print(factorial(5))

def power(a,b):
    if b == 0:
        return 1
    if  a == 0:
        return 0
    if b == 1:
        return a
    else:
        return a*power(a,b-1)

print(power(2,3))