def power(n,x):
    if x==0:
        return 1 
    else:
        return n*power(n,x-1)
    
a,b = 5,3
print("%d ** %d = %d" % (a,b,power(a,b)))