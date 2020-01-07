# 写入JSON文件

import json

teacher_dict =  {'name': '王五', 'age': 25, 'title': '讲师'}
json_str = json.dumps(teacher_dict) # 使用json.dumps函数将python对象转化为字符串再写入文件
print(json_str)
fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
json_str = json.dumps(fruits_list)
print(json_str)
print(type(json_str))