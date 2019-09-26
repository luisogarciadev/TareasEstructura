#def fact(n):
    #if n == 1:
        #return n
    #return n*fact(n -1)

#print(fact(5))

def power(a,b):
    if b==0:
        return 1
    else:
        if a == 0:
            return 0
        else:
            if b==1:
             return a
            else:
                return a*power(a, b-1)

print(power(3,4));