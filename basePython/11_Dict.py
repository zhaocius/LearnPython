scores={'a':44,'b':45}
print(scores['a'])
scores['a']=55
print(scores['a'])
scores.update(c=4)
print(scores.pop('a')) # 删除元素
print(scores.popitem())# 删除元素

#zip 组成字典
keys=[1,2,3]
values=['一','二','三']
d=dict(zip(keys,values))
print(d)

#生成式#
d1={key:value for key,value in d.items() if key>1}
print(d1)

#EAFP:easier to ask forgiveness then permission
#LBYL: look before you leap
d={'x':'5'}
try:
    value=int(d['x'])
    print(value)
except(KeyError,TypeError,ValueError):
    value=None
print(value)
