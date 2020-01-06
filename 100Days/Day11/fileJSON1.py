# 读写JSON文件

import json

def main():
    mydict = {
        'name':'张三',
        'age':25,
        'Gmail':12345,
        'friends':['李四','王五'],
        'cars':[
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')

if __name__ =='__main__':
    main()