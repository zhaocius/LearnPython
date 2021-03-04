from random import randint

# for-in循环
# range(1,101,2)  #步长为2
# range(100,0,-2) # 步长为-2
sum=0
for i in range(1,101):  # 前闭后开
    sum+=i
print(sum)


# while循环
score = randint(1,100)
time=0;
while True:
    time+=1
    if time > 7:
        print('尝试超过7次，笨个蛋')
        break
    num=int(input('请输入数字：'))
    if num>score:
        print('小一点')
    elif num<score:
        print('大一点')
    else:
        print('猜对了，真聪明')
        break




