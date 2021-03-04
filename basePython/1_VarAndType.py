# 整型
a=100
b=0b100
c=0o100
d=0x100
print(a,b,c,d)

# 浮点型
e=123.456
f=1.23456e2
print(e,f)
print('%.3f是浮点型, %.3f是科学计数法' %(e,f))

# 字符串型
g='hello'
h="hello"
s="""
hello
world
"""
t='\'hello\''     # 转义字符
u='\\\nhello\n\\'
print('zzz',u)

# 布尔型
i=True
j=False

# 复数
k=3+5j
print(k)

# 使用type()检查变量的类型
l=100
m=12.345
n='hello'
print(type(l))
print(type(m))
print(type(n))

# 变量类型转换
o='123'
p=123.456
q=int(o)
r=str(p)
print(q,r)
