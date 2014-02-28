+++++++++++++++++++++++++
 python-note
+++++++++++++++++++++++++

Eclipse下Python开发环境搭建
=========================

﻿官网下载安装包并安装：
------------------

http://www.python.org/downloads/

到Eclipse Marketplace中安装插件：
------------------------------

PyDev - Python IDE for Ecilpse

（由于网络问题下载失败，可以尝试通过Install New Software...安装：Location: http://pydev.org/updates）

或者直接到：http://sourceforge.net/projects/pydev/files/下载PyDev for Eclipse.zip，解压得到plugin和feature两个目录，分别将plugins和feature目录下的所有文件复制到eclipse的相应目录下，最后启动Eclipse即可

重启Eclipse，设置Eclipse的Pydev的插件的环境
---------------------------------------

截图：001 http://www.cnblogs.com/xuqiang/archive/2011/04/18/2019484.html
选择刚才Python安装包哦下的python.exe解析器

使用Eclipse创建一个Hello World!
-----------------------------

新建一个python工程
~~~~~~~~~~~~~~~~

在工程里面创建一个HelloWorld.py文件：

.. parsed-literal::

'''
Created on 2014-2-28
'''
print("hello world")

.. @example.prepend('#include <cassert>')
.. @example.replace_emphasis('''
   assert(title == "foo");
   assert(height == 20);
   assert(width == 400);
   ''')


运行快捷键：ctrl + f11
~~~~~~~~~~~~~~~~~~~~

调试：
~~~~~~~~~~~~~~~~~~~~

和Java调试基本一致
