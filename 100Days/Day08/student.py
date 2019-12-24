#另一种创建类的方式

def bar(self,name):
    self._name =  name

def foo(self,course_name):
    print('%s正在学习%s.'%(self._name,course_name))

def main():
    Student = type('Student',(object,),dict(__init__=bar,study=foo))
    stu1 = Student('张三')
    stu1.study('Python程序设计')

if __name__ == '__main__':
    main()