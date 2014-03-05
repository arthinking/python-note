'''
Created on Mar 3, 2014

@author: arthinking

02 开始编程吧
==========
两种模式：
------
进入交互模式：python
退出交互模式：exit();
方便调试

文本模式：
执行：python 1.py

Python的文件类型：
-------------
源代码
直接编写的python文本文件，有Python解析执行，不需要编译

字节代码
编译后生成的pyc
编译方法：
import py_compile
py_compile.compile('1.py');

优化代码
经过优化后的源文件， pyo
python -o -m py_compile hello.py

上面三种均可直接执行


03 变量
========
字母，数字，下划线组成，不可以数字开头，不可以使用关键字

id(a) 查看内存区块标示
a = 123
a = 456
id(a) 得到不同的地址空间
a = 123
b = 123
id(a) id(b)得到相同的地址空间


04 运算符  表达式
=============
赋值运算符
-------

算法运算符
-------
整除：  3.0//2   1.0
幂次方： 2**3   8

关系运算符
-------

逻辑运算符
-------
and or not

优先级由低到高：
-------
Lambda
逻辑运算： or
逻辑运算： and
逻辑运算： not
成员测试： in, not in
同一性测试： is, is not
比较：<  <=  >  >=  !=  ==
按位或： |
按位异或： ^
按位与： &
移位： <<  >>
加减法：  +  -
乘除取余： * / %
正负号: +x, -x
按位翻转： ~x
指数：**

终端输入
-------
a = raw_input()  #字符串
a = int(a)  #转换为整数
raw_input("please input number1:")  #终端提示


05 数据类型 数字  字符串
=================
python不需要声明，由存储的数据决定
数据类型：
-------
数字
字符串
列表
元组
字典

数字类型：
------
整型
type(123)  #查看类型   <type 'int'>
长整型
type(123456789123456)  #<type 'long'>
为了区分整型和长整型，长整型加个l：  a = 12L
浮点
0.0   12.0  -18.0  3e+7
复数
c=3.14j  #<type 'complex'>

字符串
------
'test'
"test\nabc"
"""test"""   #保存格式化输入   或者作为注释
"""test
    abc"""

字符串  列表 元组 都被称作序列类型的数据
--------------------------
切片和索引：
a='asfasdfasf'
a[2] f
a[2] + a[1]  fs
a[1:4]  sfa
a[:4]  asfa
a[1:]  sfasdfasf
a[::2] afsfs  2为步长
a[-4:-1] fas
a[-2:-4:-1]  sa


06 数据类型  序列
=================
列表，元组和字符串都是序列
序列的两个主要特点是索引操作符和切片操作符：
----------------------------
索引操作符：从序列中抓取一个特定项目
切片操作符：获取一个切片，即一部分序列
str="abcd"
str[1]  b
str[1:4]  bcd
str[-1]  d
abc[:]  abcd
str[::]  abcd

序列的基本操作：
-----------
len()  len(str}
+   'a' + 'b'
*    'a' * 3    aaa
in   'c' in str   True
max()   max(str)  d
min()   min(str)  a
cmp(tuple1, tuple2)    
cmp('abc', '123')   1  大于

元组()
------
元组和列表十分类似，元组的值和字符串一样不可修改
元组通过圆括号用都好分割的项目定义
~~~~~~~~~~
t=("Jason", 20, "male")
t[0]  Jason
~~~~~~~~~~
元组通常用在使语句或用户定义的函数能够安全的采用一组值的时候
空元组
~~~~~~~~~~
a=()
~~~~~~~~~~
单一元组
~~~~~~~~~~
a=(20,)
~~~~~~~~~~
元组的操作：
-----------
和字符串类型一样，可以通过索引和切片操作，元组的值不可改变
t=("Jason", 20, "male")
t[1] = 30  TypeError:'tuple' oblect does not support item assignment

拆分元组
name, age, gender = t;
name  Jason
扩展：a,b,c = 1,2,3


07 数据类型  序列 - 列表
元组不可变，存储可变的数值，可以使用列表
列表时可变类型的数据
列表的组成：用户[]表示列表，半酣了多个以逗号分隔开的数字，或字符串
listmilo = []
listmilo = ['arthinking', 'Jason', 1]
listmilo[0]   #output: arthinking
listmilo[0:2]  #output: [arthinking, Jason]
l2 = ['abc']   # 不用逗号

列表操作：
取值：
切片和索引
list[]
添加：
list.append()
删除：
del(list[i])
del(list)
list.remove(1)  # 删除第一个出现的元素
list.remove(list[i])
元素重新赋值后，内存空间地址不变
修改
list[i] = x
查找
var in list

help(list.append)  #方法的帮助信息


08 数据类型 - 字典
t1=["a", "b"]
t2=["1", "2"]
zip(t1, t2)

字典是python中唯一的映射类型（哈希表）
字典对象是可变，但是字典的键必须使用不可变对象，并且一个字典中可以使用不同类型的键值
keys()或者values()返回键列表或者值列表
items()返回包含键值对的元组

创建字典：
{'a':1, 'b':2}
c='cc'
{'a':1, 'b':2, c:3, 1:4}
使用工厂方法dict():
dict(a=1, b=2)
内建方法：fromkeys()，字典中的元素具有相同的值，默认为None
{}.fromkeys(('x', 'y'), -1)   output: {'x': -1, 'y': -1}

访问字典中的值：
直接使用key访问：key不存在会报错，可使用had_key()或者in和not in判断，但是has_key()方法即将废弃
循环遍历：
for key in dict1.keys()
使用迭代器：
for key in dict1

更新和删除：
直接用键值访问更新

del dict1['a'] 删除键为a的元组
  dict1.pop('a') 删除并且返回键为a的元素
  dict1.clear()删除字段所有元素
  del dict1 删除整个字典
  
字典相关的内建函数：
type(), str(), (cmp很少用于字典的比较，比较依次是字典的大小，键，值)
工厂函数dict();
dict(zip('x','y'),(y=2) 或者dict(x=1,y=2)

使用字典生成字典比用copy慢，这种情况下推荐使用copy()


09 流程控制
if 1<2:
    print '<'
print '不管条件是否成立，都会打印这句话'
if只能控制缩进的代码

true：表示非空的量（string, tuple, list, set, dictonary等），所有非零数
false：表示0，None，空的量等

if x<0:
    statuments(s)
elif x=0:
    statuments(s)
else:
    statuments(s)


10 逻辑运算符
and
or
not


11 for循环
for iterating_var in sequence:
    statements(s)
格式遵循代码块缩进原则

for x in [0,1,2,3,4,5,6]:
    print x, "testabc"

range(i,j[,步进值])
  如果所创建的对象为整数，可以用range
  i为初始值，默认为0
  j为终止值，但不包括在内，步值默认为1

for x in range(100):


12 遍历
for x in "hello":
    print x

# 迭代索引
for index in range(len(list)):
    print list[index]

遍历字典：
a = {'a':1,'b':2}
for x in a:
    print a[x]    #输出key
元组拆分的方式遍历：
for k,v in a.items():
    print k,v


13 循环控制
for k,v in a.items():
    print k,v
else:
    print "end"  # 正常执行完for之后会执行
    
import time

for x in range(20):
    print x
    #time.sleep(1)
    if x == 3:
        pass  #代码中起到占位的作用
    if x == 4:
        continue
    if x == 5:
        exit()  #退出程序
    if x>=6:
        break
else：
    print "end"  #break之后就不会执行这句了


14 while
while expression
    statements(s)

while True:
    print "=========="
    x = raw_input("enter q for quit:")
    if x == 'q'：
        break
else:
    print "end"  # break退出的，这句话不会被执行；当while条件为False的时候会执行


15 函数
工具集
排序
极值

函数的定义和调用：
使用def语句：
def 函数名(参数列表): # 可以没有参数
    函数体

def add(a, b):
    c = a + b
    print c

add(100,200)

def fun():
    print 10

if fun():
    print "ok"  #这个ok并没有输出，跟函数的返回值有关


16 函数
形式参数和实际参数
在定义函数时函数名后面圆括号中的变量名称成为“形式参数”
在调用函数是，函数名后面圆括号中变量名称叫做“实际参数”

文件头写编码：
#coding:utf8
#coding=utf8
#enoding:utf8
#encoding=utf8

缺省参数（默认参数）
def fun(x, y="cat"):   #设置默认参数的时候一定是自右向左的
    print x,y
fun("test")    #这个时候就可以不用传入第二个参数了


17 函数
局部变量和全局变量：
Python中任何变量都有其特定的作用域；
在函数中定义的变量一般只能在该函数内部使用，这些只能在程序的特定部分使用的变量我们称之为局部变量
在一个文件顶部定义的变量可供该文件中的任何函数调用，这些可以为整个程序所使用的变量称为全局变量

x = 'Jason'
def fun2():
    global x  
    x = 100  #全局变量被改写了
    global y
    y = 200
    print x
fun2()
print x  #获取到的是全局的变量
print y  #y被声明为全局变量，可以引用到，前提是函数要被调用过


18 函数
返回值
函数被调用后悔返回一个指定的值
函数调用后默认返回None
return 返回值
返回值可以使任意类型
return执行后，函数终止
区分返回值和打印

def f(x,y):
    print "execute"
    return x + y

a = f(1,2)
print a


def f2():
    return "===="  #函数返回终止，后面的不会执行
    return "===="


19 函数
多类型传值
    向函数传元组和字典
    fun(*args)
    fun(**k)
    
def f(x,y):
    print x,y

t = ('a','b')
f(t, 'b')   #output: ('a', 'b') b

t = ("name", "Jason")
def f(x,y):
    print "%s, %s" % (x,y)
f(*t)  #加星号传值，表示传递一个元组

def f2(name="Jason",age=20):
    print "name: %s" % name
    print "age: %d" % age
d = {"age":10, "name":"Jack"}
f2(**d)  #两个星号表示传递字典
f2(age=10, name="Jack")

传值冗余
    处理多余实参
    def fun(*args, **k)
def f3(x, *args):
    print x,args  #args是一个元组
f3(1)  #output: 1 ()
f3(1,2,3)  #output: 1 (2, 3)

def f4(x, *args, **k):
    print x, args, k

f4(1, 3, name="Jason")  #output: 1 (3,) {'name': 'Jason'}


20 Lambda表达式
匿名函数：lambda韩式是一种快速定义单行的最小函数，是从List借用来的，可以用在任何需要函数的地方
def f(x,y):
   return x*y
Lambda表达式写法：
g=lambda x,y:x*y
g(2,3)

使用Python写一些执行脚本时，使用lambda可以省去定义函数的过程，让代码更加精简；
对于一些抽象的，不会别的地方重复调用的函数，有时候给函数起个名字也是个难题，使用lambda不需要考虑命名的问题；
使用lambda在某些时候让代码更容易理解；

lambda语句中，冒号前面是参数，可以有多个，用逗号隔开，冒号右边是返回值。lambda语句构建的其实是一个函数对象。

g=lambda x:x**2
print g   #output: <function <lambda> at 0x02564DB0>

reduce为逐次操作list里的每项，接收的参数为2个，最后返回的为一个结果：
def add(x,y):
    return x+y
sum = reduce(add, (1,2,3))   #6
#递归
def f(n):
    if n>0:
        return n*int(f(n-1))
    else:
        return 1
print f(5)
#reduce实现递归的功能
l = range(1,6)
def f(x,y):
    ret urn x*y
reduce(f, l)  #120
#lambda的写法
reduce(lambda x,y:x*y,l)


21 switch
==========
python没有提供switch语句
python可以通过字典实现switch语句的功能：
    首先定义一个字典
    其次，调用字典的get()获取相应的表达式
    
通过字典调用函数：
{1:case1,2:case}.get(x,lambda*arg,**key:)()
~~~~~~~~~~
from __future__ import division
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

operator = {"+":add, "-":sub, "*":mul, "/":div}
operator["+"](1,2)
~~~~~~~~~~
实现switch：
~~~~~~~~~~
def f(x,o,y):
    print operator.get(o)(x,y)
f(1,"+",2)
~~~~~~~~~~


22 内置函数
=========
一个获取绝对值的函数：
~~~~~~~~~~
#获取绝对值
def f(x):
    if x<0:
        return -x
    return x
n = f(-1)
~~~~~~~~~~
系统内部的绝对值函数：
abs()  #绝对值
max()  #最大值
min()  #最小值
~~~~~~~~~~
print abs(-1)
print max(1,2,4)
print max([1,2,3,4])
~~~~~~~~~~
常用函数：
len()  #一个列表或者一个序列 长度
divmod()  #取得两个数的商和模
pow()  #乘方
round()  #取整
~~~~~~~~~~
print divmod(5,2)  #output: (2, 1)
print pow(2,3)  #output: 8
print pow(2,3,4)  #output: 0  8可以被4整除
print round(3.2)  #output: 3.0
print round(3.6)  #output: 4.0
~~~~~~~~~~
callable()  #测试某个函数是否可被调用
isinstance()  #判断对象是什么类型的
cmp()  #比较两个字符串
range()  #快速生成一个序列
xrange()  #快速生成一个序列，大数据xrange效率高很多
~~~~~~~~~~
print callable(min)  #True
f=1
print callable(f)  #False

l = [1,2]
print type(l)  #<type 'list'>
if(type(l) == type([])):
    print "list"

print isinstance(l, list)  #true

print cmp(1,2)  #-1
print cmp(1,1)  #0
~~~~~~~~~~
类型转换函数：
int()
tuple()
int()
long()
float()
complex()
str()
list()
hex()
oct()
chr()
ord()


23 内置函数
=========
string函数：
str.capitalize()  #字符串首字母大写
str.replace()  #替换
str.split()  #分割
~~~~~~~~~~
a='hello'
print a.capitalize();  #Hello
print a.replace('e', '_', 1);  #h_llo  不给第三个参数，表示替换所有的
print a.split('e');  #['h', 'llo']  不给第二个参数，表示切割所有的
help(a.replace)
~~~~~~~~~~
引入模块的方式调用
~~~~~~~~~~
import string
string.replace('hejsoislekjfk', 's', '_')  #hej_oi_lekjfk
~~~~~~~~~~
序列处理函数
len()
max()
min()
filter()
zip()
map()
reduce()
~~~~~~~~~~
def f(x):
    if(x > 5):
        return True
print filter(f, range(10))  #[6, 7, 8, 9]
~~~~~~~~~~


24 序列处理函数
===========
下面是zip和map的演示：
~~~~~~~~~~
name=['Jason', 'Jack']
age=['10', '12']
print zip(name, age)  #[('Jason', '10'), ('Jack', '12')]

print map(None, name, age)  #[('Jason', '10'), ('Jack', '12')]

#zip和map的区别：map会用None填充空缺的内容，zip则只会去掉多出的
test=[10]
print zip(name, age, test)  #[('Jason', '10', 10)]
print map(None, name, age, test)  #[('Jason', '10', 10), ('Jack', '12', None)]

#map还可以用于两个序列的并行计算：
a=[1,2,3]
b=[4,5,6]
def ff(x,y):
    return x*y
map(None, a, b)  #[('Jason', '10', 10)]
map(ff, a, b)  #[('Jason', '10', 10), ('Jack', '12', None)]
~~~~~~~~~~
下面是reduce的演示：
~~~~~~~~~~
#使用reduce演示1加到100
l=range(1,101)
print reduce(lambda x,y:x+y, l)  #5050
~~~~~~~~~~


25 模块
代码封装
模块是Python组织代码的基本方式
Python的脚本都是扩展名为py的文本文件保存的，一个脚本可以单独运行，也可以导入另一个脚本运行。当一个脚本被打入运行时，我们将其成为模块（module）

模块名与及哦啊本的文件名相同
例如写一个名为item.py的脚本，则可以再另外一个脚本中用import item语句来导入它
~~~~~~~~~~
def add(x,y):
    return x+y
if __name__ == "__main__":  #当前模块下才执行下面的代码
    print add(1,2)

~~~~~~~~~~
包：
Python的模块可以按照目录组织为包
创建一个包的步骤是：
    简历一个名字为包名字的文件夹
    在该文件夹下创建一个__init__.py文件
    根据需要在该文件夹下存放脚本围巾啊，已编译的扩展及子包
    import pack.module1, pack.module2
别名：
~~~~~~~~~~
import string as str
print str.split("Hello world!", " ", 1)  #['Hello', 'world!']
~~~~~~~~~~
直接导入方法：
~~~~~~~~~~
from string import split
print split("Hello world!"," ");  #['Hello', 'world!']
~~~~~~~~~~





'''



