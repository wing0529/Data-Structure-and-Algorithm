def factorial(n):
    if n ==0:
        return 1
    else:
        ans = n
        for i in range(n-1,0,-1):
            ans *=i
        return ans
    
num =7
print("%d! = %d" %(num,factorial(num)))