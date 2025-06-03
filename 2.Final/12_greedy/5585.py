def charge(m,ch):
    char = 1000-m
    ans =0
    c=[]
    for i in ch:
        while char-i>=0:
            char = char-i
            c.append(i)
            ans +=1

    return ans

money = int(input())

ch = [500,100,50,10,5,1]

print(charge(money,ch))