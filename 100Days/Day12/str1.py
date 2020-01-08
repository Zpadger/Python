# 字符串常用操作

import pyperclip

# 转义字符
print('My brother\'s name is \'007\'')
# 原始字符串
print(r'My brother\'s name is \'007\'')

str = 'hello123world'
print('he' in str)
print('her' in str)
# 字符串是否只包含字母
print(str.isalpha())
# 字符串是否只包含字母和数字
print(str.isalnum())
# 字符串是否只包含数字
print(str.isdecimal())

print(str[0:5].isalpha())
print(str[5:8].isdecimal())

list =  ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
print('-'.join(list))
sentence = 'You go your way I will go mine'
worlds_list = sentence.split()
print(worlds_list)
email = '     zhangpeiji01@gmail.com          '
print(email)
print(email.strip())
print(email.lstrip())

# 将文本放入系统剪切板中
pyperclip.copy('吃葡萄不吐葡萄皮')
# 从系统剪切板获得文本
print(pyperclip.paste())

# Windows系统不会报错,但是Linux系统会报错:
# pyperclip.PyperclipException:
#     Pyperclip could not find a copy/paste mechanism for your system.
# 解决方法 Terminal    sudo apt-get install xsel xclip

