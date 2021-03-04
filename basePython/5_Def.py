from random import randint

#函数封装
def fac(num):
    result = 1
    for x in range(1,num+1):
        result*=x
    return result

m=5
n=3
print(fac(m)//fac(n)//fac(m-n))

#给定默认值
def roll_dice(n=2):
    total=0
    for x in range(1,n):
        total+=x
    return total
print(roll_dice(randint(1,7)))

#不可重载
def add(a=0,b=1,c=2):
    return a+b+c
print(add(),add(3,6),add(3,6,9),add(b=3,c=6))

#可变长参数


