## Python协程详解  

### Python协程(一) —— 从generator和yield表达式说起  

### 目录  
生成器generator以及yield表达式详解:  
[1.最简单的生成器](#1.最简单的生成器)  
[2.send()方法的使用](#2.send()方法的使用)  
[3.yield语句的用法总结](#3.yield语句的用法总结)  
[4.迭代器(生成器)的send方法详解](#4.迭代器(生成器)的send方法详解)  
[5.生成器throw的方法用法](#5.生成器throw的方法用法)  
[6.生成器的启动与关闭close](#6.生成器的启动与关闭close)  
&#8194;[6.1.生成器的启动](#6.1.生成器的启动)  
&#8194;[6.2.生成器的关闭](#6.2.生成器的关闭)  
[7.生成器的终止迭代](#7.生成器的终止迭代)

#### 1.最简单的生成器  
>def my_generator(n):  
&#8194;&#8195;for i in range(n):  
&#8194;&#8195;&#8194;&#8195;yield i

#### 2.send()方法的使用
>def my_generator(n):  
&#8194;&#8195;for i in range(n):  
&#8194;&#8195;&#8194;&#8195;temp=yield i  
&#8194;&#8195;&#8194;&#8195;print(f'我是{temp}')  
&#8195;  
g=my_generator(5)  
&#8195;  
print(next(g)) #输出0  
print(next(g)) #输出1  
g.send(100)    #本来输出2，但是传入新的值100，改为输出100  
print(next(g)) #输出3  
print(next(g)) #输出4


输出:
>0&#8195;&#8195;&#8195;&#8195;#第一次迭代  
&#8195;  
我是None  
1&#8195;&#8195;&#8195;&#8195;#第二次迭代  
&#8195;  
我是100&#8195;#第三次迭代  
&#8195;  
我是None   #第四次迭代  
3  
&#8195;  
我是None   #第五次迭代  
4  

从上面可以看出yield语句与普通函数的return语句的区别在哪里了，主要集中在以下几点:  
（1）return 不能写成“temp=return xxxx”的形式，会提示语法错误，但是yield可以写成“temp=yield xxxx”的形式；  
（2）普通函数return后面的语句都是不会再执行的，但是yield语句后面的依然会执行，但是需要注意的是，由于“延迟加载”特性，yield后面的代码并不是在第一次迭代的时候执行的，而是第二次迭代的时候才执行第一次yield后面没有执行的代码。也正是这个特性，构成了yield为什么是实现协程的最简单实现。  
（3）使用send()方法传进去的值，实际上就是yield表达式返回的值，这就是为什么前面每次输出print(temp)都打印出None，因为没有send值，所以temp为None，但是send（100）之后却打印100，因为此时temp就是100了。

还可以在yield后面不放任何东西，如下代码：  
>def my_generator(n):  
&#8195; for i in range(n):  
&#8195; &#8195; temp = yield   #yield后面没有任何东西，这时候无法迭代值，每次都是None  
&#8195; &#8195; print(f'我是{temp}')  
&#8195;   
g=my_generator(5)  
&#8195;   
print(next(g))  
print(next(g))  
g.send(100)  
print(next(g))  
print(next(g))

输出:  
>None  
&#8195;  
我是None  
None  
&#8195;  
我是100&#8195;#这个100并不是迭代的100哦，而是send进去100，实际上是temp的打印值  
&#8195;  
我是None     
None  
&#8195;  
我是None     
None  

#### 3.yield语句的用法总结  

yield的一般形式为：  
&#8195;  
temp=yield 表达式(每次迭代要返回的值）  
（1）如果要返回确定的值，后面的表达式不可省略，绝大部分情况下我们也不省略，否则只能返回None；  
（2）如果使用了send(value),传递进去的那个value回取代那个表达式的值，并且会将传递进去的那个值返回给yield表达式的结果temp，所以如果想在yield后面使用传递进去的那个值，必须要有使用temp，否则无法使用；  
（3）yield语句的一般形式  
&#8195;&#8195;&#8195;temp=yield expression  (推荐：既可以返回迭代的值，也可以接受send进去的参数并使用)  
&#8195;&#8195;&#8195;yield expression（也可以使用：）  
&#8195;&#8195;&#8195;temp=yield          (不推荐）  
&#8195;&#8195;&#8195;yield                   （不推荐）

### 4.迭代器(生成器)的send方法详解  
查看send的定义，得到send(arg)是有返回值的，而且他的返回值就是原本我应该迭代出来的那个值，如下所示：  
>def my_generator(n):  
&#8195;for i in range(n):  
&#8195;&#8195;yield i  
&#8195;  
g=my_generator(5)  
&#8195;  
print(next(g))  
print(next(g))  
g.send(100)  
print(next(g))  
print(next(g))

输出:  
>0  
1    
3  
4  
#我们发现虽然100传进去了，但是他并没有迭代出来，那原来的2去哪里了呢？send(100)实际上就是返回的2

如果改为以下代码： 
>print(next(g))  
print(next(g))  
a=g.send(100)  
print('我是{0}'.format(a))  
print(next(g))  
print(next(g))

输出:  
>0  
1  
我是2  
3  
4  

send(arg)方法总结：  
（1）它的主要作用是，当我需要手动更改生成器里面的某一个值并且使用它，则send发送进去一个数据，然后保存到yield语句的返回值，以提供使用  
（2）send(arg)的返回值就是那个本来应该被迭代出来的那个值。这样既可以保证我能够传入新的值，原来的值也不会弄丢

### 5.生成器throw的方法用法  
这个函数相比较于前面的next()、send()来说更加复杂，先看一下它的函数描述：  
&#8195;  raise exception in generator，return next yielded value or StopIteration，即在生成器中抛出异常，并且这个throw函数会返回下一个要迭代的值或者是StopIteration。还是通过几个例子来看吧！  
>def my_generator():  
&#8195;yield 'a'  
&#8195;yield 'b'  
&#8195;yield 'c'  
&#8195;  
g=my_generator()  
&#8195;  
print(next(g))  
print(next(g))  
print('-------------------------')  
print(g.throw(StopIteration))  
print(next(g))

输出:  
>a  
b  
&#8194;-------------------------  
StopIteration

因为在迭代完 b 之后，就触发了StopIteration异常，这相当于后面的 ‘c’ 已经没用了，跳过了c ,c再也不会执行，就中断了，所以后面的 'c'再也不会迭代，所以这里不会再返回任何值，返回的是StopIteration。  
&#8194;  
再看一个例子：  
>def my_generator():  
&#8195;try:  
&#8195;&#8195;yield 'a'  
&#8195;&#8195;yield 'b'  
&#8195;&#8195;yield 'c'  
&#8195;&#8195;yield 'd'  
&#8195;&#8195;yield 'e'  
&#8195;except ValueError:  
&#8195;&#8195;print('触发“ValueError"了')  
&#8195;except TypeError:  
&#8195;&#8195;print('触发“TypeError"了')  
&#8195;  
g=my_generator()  
&#8195;  
print(next(g))  
print(next(g))  
print('-------------------------')  
print(g.throw(ValueError))  
print('-------------------------')  
print(next(g))  
print(next(g))  
print('-------------------------')  
print(g.throw(TypeError))  
print('-------------------------')  
print(next(g))

输出:  
>a  
b  
&#8194;-------------------------  
触发“ValueError"了    
StopIteration  

当前面两次执行了a和b之后，向生成器扔进去一个异常，触发ValueError异常，这时候意味着try后面的c、d、e已经作废了，不会再有用，这个生成器已经终止了，因此g.throw()会返回StopIteration。  
&#8194;  
再看一个例子：    
>def my_generator():   
&#8195;while True:
&#8195;&#8195;try:  
&#8195;&#8195;&#8195;yield 'a'  
&#8195;&#8195;&#8195;yield 'b'  
&#8195;&#8195;&#8195;yield 'c'  
&#8195;&#8195;&#8195;yield 'd'  
&#8195;&#8195;&#8195;yield 'e'  
&#8195;&#8195;except ValueError:  
&#8195;&#8195;&#8195;print('触发“ValueError"了')  
&#8195;&#8195;except TypeError:  
&#8195;&#8195;&#8195;print('触发“TypeError"了')  
&#8195;  
g=my_generator()  
&#8195;  
print(next(g))  
print(next(g))  
print('-------------------------')  
print(g.throw(ValueError))  
print('-------------------------')  
print(next(g))  
print(next(g))  
print('-------------------------')  
print(g.throw(TypeError))  
print('-------------------------')  
print(next(g))

输出:  
>a  
b  
&#8194;-------------------------  
触发“ValueError"了     
a  
&#8194;------------------------- 
b  
c  
&#8194;-------------------------  
触发“TypeError"了    
a  
&#8194;------------------------- 
b    

解释：  
出现这样的结果是不是很意外？它和上面的那个例子只有一个while只差，为什么结果差这么多，解释如下：  
首先print(next(g))两次：会输出a、b，并停留在c之前。  
然后由于执行了g.throw(ValueError)，所以会跳过所有后续的try语句，也就是说yield 'c'、yield 'd'、yield 'e'不会被执行，然后进入到except语句，打印出触发“ValueError"了。然后再次进入到while语句部分，消耗一个yield，此时因为是重新进入的while，小号的依然是第一个yield 'a'，所以会输出a。实际上这里的a也就是g.throw()的返回值，因为它返回的是下一个迭代的数；  
在print(next(g))两次，会执行yield b’、yield 'c’语句，打印出b、c，并停留在执行完该语句后的位置，即yield 'd'之前。  
&#8194;  
然后再g.throw(TypeError)：会跳出try语句，从而后面的d,e不会被执行，下次自一次进入while，依然打印出a。  
&#8194;  
最后，执行了一次print(next(g))，打印出b。

### 6.生成器的启动与关闭close  
#### 6.1生成器的启动
使用close（）方法手动关闭生成器函数，后面的调用会直接返回StopIteration异常.  
这里所讨论的启动不是使用for循环迭代，我们在使用for循环迭代的时候可能没有去考虑“启动”与“关闭”这些事情，这里指的是使用next()内置方法一个一个迭代的情形。在第一次迭代的时候，一定要先启动生成器，启动的两种方法为：  
第一：直接使用next(g)，这会直接开始迭代第一个元素（推荐使用这个启动）  
第二：使用g.send(None)进行启动，注意第一次启动的时候只能传入None，如果传入其他具体的指则会报错哦！  
>def my_generator():  
&#8195;yield 1  
&#8195;yield 2  
&#8195;yield 3  
&#8195;yield 4  
&#8195;  
g = my_generator()  
g.send(None)   #第一次启动，本来第一次应该迭代的1，这里被取代了，但是send(None)会返回1  
print(next(g))  
print(next(g))  
print(next(g)) 

输出:  
>2  
3  
4 

#### 6.2生成器的关闭  
如果一个生成器被中途关闭之后，在此调用next()方法，则会显示错误，如下：
>def my_generator():  
&#8195;yield 1  
&#8195;yield 2  
&#8195;yield 3  
&#8195;yield 4  
&#8195;  
g = my_generator()  
print(next(g))     
print(next(g))    
g.close()  
print(next(g))    #在此处会显示错误  
print(next(g)) 

输出:
>1  
2  
显示StopIteration  

#### 7.生成器的终止迭代——StopIteration  
前面讲的手动关闭生成器，使用close（）方法，后面的迭代或抛出StopIteration异常。另外在一个生成器中，如果没有return，则默认执行到函数完毕时返回StopIteration；
>def g1():  
&#8195;yield 1  
&#8195;  
g=g1()
next(g)    #第一次调用next(g)时，会在执行完yield语句后挂起，所以此时程序并没有执行结束。
next(g)    #程序试图从yield语句的下一条语句开始执行，发现已经到了结尾，所以抛出StopIteration异常。

输出:  
>1  
Traceback (most recent call last):  
&#8195;File "<stdin>", line 1, in <module>  
StopIteration

如果遇到return,如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。  
>def g2():  
&#8195;yield 'a'  
&#8195;return  
&#8195;yield 'b'  
&#8195;  
g=g2()  
next(g)    #程序停留在执行完yield 'a'语句后的位置。  
next(g)    #程序发现下一条语句是return，所以抛出StopIteration异常，这样yield 'b'语句永远也不会执行。

输出:  
>a  
b
Traceback (most recent call last):  
&#8195;File "<stdin>", line 1, in <module>  
StopIteration

如果在return后返回一个值，那么这个值为StopIteration异常的说明，不是程序的返回值。
>def g3():  
&#8195;yield 'a'  
&#8195;return '这是错误说明'  
&#8195;yield 'b'      #有一些编辑器会提示错误，此处为unreachable code，即不可到达的代码
&#8195;  
g=g3()  
next(g)      
next(g)      

注意：生成器没有办法使用return来返回值。因为return返回的那个值是通过StopIteration的异常信息返回的，所以我没办法直接获取这个return返回的值。  

当然上面所说的无法获取return返回值，我们指的是没有办法通过result=g3()这种形式获取return的返回值。实际上还是有相依欧诺个的手段获取这个return的值的，有两种方法：  
方法一：使用后面的yield from 语句（下文在讲解）  
方法二：因为return返回的值是作为StopIteration的一个value属性存在的，StopIteration本质上是一个类，所以可以通过访问它的value属性获取这个return返回的值。  

使用下面的代码：  
>def g3():  
&#8195;yield 'a'  
&#8195;return '这是错误说明'  
&#8195;yield 'b'  
&#8195;g=g3()  
&#8195;  
try:  
&#8195;print(next(g))  #a  
&#8195;print(next(g))  #触发异常  
except StopIteration as exc:  
&#8195;result=exc.value  
&#8195;print(result)  

输出:  
>a  
这是错误说明  

### 总结  
上面详细讲解了关于python生成器的各个方法的详细使用情况，还没有正式进入到协程的部分，关于协程的详细讲解将会在后续的系列文章中逐渐讲解

#### 内容源自公众号"机器学习与python集中营"
