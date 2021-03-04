#json只能和字典进行相互转化
#load()
#loads()

import json
mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 95658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
f=None
try:
    f=open('../testData/data.json', 'w')
    json.dump(mydict,f)

    f=open('../testData/data.json', 'r', encoding='utf-8')
    model=json.load(f)
    print(model['name'])
finally:
    if f:
        f.close()

