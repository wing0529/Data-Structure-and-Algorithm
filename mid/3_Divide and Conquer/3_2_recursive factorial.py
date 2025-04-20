

def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)
    
num = 7
print("%d ! = %d" % (num,factorial(num)))