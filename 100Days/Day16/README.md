## Python相关函数解释  

### Python特殊输入格式  
* 输入中包含空格  
>a, b = map(int, input().split())  
a, b, c = map(int, input().split())
* 输入中包含'/'  
>a, b = map(int, input().split('/'))  
* 输入中包含','  
>a, b = map(int, input().split(','))  
 

### Python func(*args, **kwargs)    

#### Q:Python中* args和** kwargs的含义？  
A:在python中，* args和 ** kwargs通常使用在函数定义里。*args 和 ** kwargs 都允许你给函数传不定数量的参数，即使在定义函数的时候不知道调用者会传递几个参数。  
ps: * args和 ** kwargs只是一个大家都遵守的习惯，名字可以任意写的 。

#### 1.* args例子  
* args能够接收不定量的非关键字参数，会把位置参数转化为tuple（元组，非键值对的参数组），例子如下面代码所示：
>def func(* args):  
&emsp;&emsp;for i in args:  
&emsp;&emsp;&emsp;&emsp;print(i)  
func(1,2,3,4)  

运行结果：  
1  
2  
3  
4

#### 2.** kwargs例子
** kwargs允许你传递不定量个关键字参数。如果你需要在函数中定义不定量个命名参数，那么你就要使用** kwargs了，它会把关键字参数转化为dict（词典，键值对参数组），例子如下面代码所示：
>def func(** kwargs):  
&emsp;&emsp;for i in kwargs:  
&emsp;&emsp;&emsp;&emsp;print(i,kwargs[i])  
func(a=1,b=2,c=3,d=4)  

运行结果：  
a&nbsp;1  
b&nbsp;2  
c&nbsp;3  
d&nbsp;4  

下面演示个错误的案例，报错：  
>"func() takes 0 positional arguments but 4 were given"  
“未定义位置型参数，却收到了4个参数”  

>def func(** kwargs):  
&emsp;&emsp;for i in kwargs:  
&emsp;&emsp;&emsp;&emsp;print(i,kwargs[i])  
func(1,2,3,4)  

>运行结果：  
Traceback (most recent call last):  
&emsp;File "F:/pyworkspace/hello.py", line 4, in <module>  
&emsp;&emsp;func(1,2,3,4)  
TypeError: func() takes 0 positional arguments but 4 were given

也就是说，kwargs需要的是带名称的参数，而args代表位置型参数（无名称参数）。从英语上来说，kwargs多出来的kw其实就是keyword的意思，表示这是“键值对”参数，就像字典那样 。
