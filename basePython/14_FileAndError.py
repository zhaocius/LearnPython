f=None
try:
    f=open('../testData/test.txt', 'r', encoding='utf-8')
    print(f.read())
except FileNotFoundError:  #未找到文件
    print('FileNotFoundError')
except LookupError:  #指定了未知编码
    print('LookupError')
except UnicodeDecodeError:  #指定了未知解码
    print('UnicodeDecodeError')
finally:
    if f:
        f.close()

try:
    f=open('../testData/test.txt', 'r', encoding='utf-8')
    for line in f:
        print(line)
finally:
    if f:
        f.close()

#读文件到列表中
try:
    f=open('../testData/test.txt', 'r', encoding='utf-8')
    lines=f.readlines()
    print(type(lines))
finally:
    if f:
        f.close()

# 写文件
list=[1,2,3,4,5,6,7,8,9,0]
try:
    f=open('../testData/test.txt', 'w', encoding='utf-8')
    for item in list:
        f.write(str(item)+'\n')
finally:
    if f:
        f.close()

# 读写二进制文件
try:
    f=open('../testData/liudehua.jpg', 'rb')
    data=f.read()
    f=open('../testData/刘德华.jpg', 'wb')
    f.write(data)
finally:
    if f:
        f.close()
        




