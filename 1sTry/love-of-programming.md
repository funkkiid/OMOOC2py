# 让编程更有爱的一点 - 继续小小日记

>更新日志  
>20151024 增加哥哥写的日记  
>20151020 创建

## 小小日记任务回顾

- 完成一个极简交互式日记系统，需求如下：
	- 一次接收输入一行日记
	- 保存为本地文件
	- 再次运行系统时,能打印出过往的所有日记
- 第一次笔记
    - [小小日记系统-第一次尝试](https://zoejane.gitbooks.io/omooc2py/content/1sTry/diary101.html)
	
## 思考二

看issue回复的时候，觉得是不是还是在py里面进行互动和输入会更好一些？  
这样界面会更友好，提示性也更强一些，  
不会出现我自己过了好久都不记得怎么用的情况，  
别人用起来也觉得一目了然，不用去翻帮助文档。

同时，互动文字可以让程序更有爱一些。  
感觉好像有一个人在和你对话，而不是硬邦邦的代码。  
记得看那本和game有关的python的书时，最打动我的就是它的举例的程序，运用的互动语言都很有感情，让我觉得编程原来也可以是这么有感情的事。

- 输入diary.py
- 出现提示：
    - Hi. I am the diary of yours.
    - Do you have something want to share with me now?
    - Or you can just press Enter to read all of me.
- open file 'diary' , append mode
- newDiary=input()
- 出现提示：
    - Thank you for sharing with me.
    - Bye. I will miss you.
- close file


#### 尝试四：

感觉大家还是使用python2的比较多。  
所以这次编程准备在python2.7的环境下编写。

##### Question
- input() not working in python2
- 没发现中文有什么问题呀，大妈说的中文输入问题到底指的是什么呢？

##### Solution

>Use raw_input() instead of input():  
```testVar = raw_input("Ask user for something.")```  
input() actually evaluates the input as Python code.   
I suggest to never use it.  
raw_input() returns the verbatim string entered by the user.

>Although for anyone reading this using Python 3, input now works this way, and raw_input is gone.

> via [Python 2.7 getting user input and manipulating as string without quotations](http://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations)

##### 代码
```
import time

print('Hi, I am the diary of yours.')
print('Do you have something want to share with me now?')
print('Or you can just press Enter to read all of me.')

diary = raw_input('>>')

if diary == '':
    diaryFile = open('diary.txt')
    diary = diaryFile.read()
    print(diary)
    
else:
    diaryFile = open('diary.txt','a')
    diaryFile.write('\n' + time.strftime('%Y/%m/%d')+ ' ' +diary)

    print('Thank you for sharing with me.')
    print('Bye. I will miss you.')

diaryFile.close()
```

## 思考三

再次受到issue的启发，  
包括那时候上Kunal的课，其实最感动的是，当他们用python写出一些很简单但充满爱的小程序，和他们所爱的人一起分享的时刻。  
无论是给自己的小孩子上一课超简单的python课，还是用python做出一个小小照片游戏，告诉自己亲爱的人，说爱你。  
我想，这是我觉得python最有爱的时刻，也是最最让我感动的时刻。  
那些程序是那样的简单，却让我真的感觉到，这样简单的事情是如此的有意义。

我想，为什么要把编程这件事搞得好像那么深奥和复杂呢，好像难以和不了解编程的人沟通呢？  
想起之前都是自己在这里看视频，学写代码，感觉好像也不知道怎么和老公说这件事情一样，为什么不用一种别的形式来一起分享这个过程呢？  
包括他问起来我写了些什么，我好像一下子也难以描述清楚。  
为什么不把这件事情从自娱自乐，转变成和他一起来分享呢？  
虽然我自己也觉得好玩啦，不过是不是之前根本没这么想过？  
是这件事情很难，还是我根本没有尝试过呢？

失败也没有关系啦，起码我也可以看看他的反馈，自己再改进嘛。  
而且我觉得这样应该还蛮好玩的。  

喵，好高兴今天突然想起了那时候Kunal传达给我的这种充满爱的感觉。  
让我感觉，编程就是生活的一部分，编程让生命更有爱。  
编程不仅仅是关于计算机，更是关于人，关于我所爱的人。  

About People.   
About Love.   
About Life.  

Zoe, remember this feeling.

#### 尝试五 - Special Version for 哥哥

- 这次界面要用中文写啦。 

##### Question
- 才发现mac下的idle是不能写中文的...

#### Solution

> 1. IDLE 下中文输入法失效。这是因为 IDLE 界面使用的 Tkinter 需要依赖 Tcl/Tk，而系统自带的 Tcl/Tk 版本太低，造成了不兼容的问题。   
可以[下载新版本](http://www.activestate.com/activetcl/downloads)  
或者用homebrew安装 ```brew install tcl-tk```  
via [mac下的 idle为何不能输入中文?该如何解决?](http://www.zhihu.com/question/26532408)  

测试后，还是不行

>2. 根据IDLE的WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.  
Visit http://www.python.org/download/mac/tcltk/ for current information.  
If you are using OS X 10.9 or later and a Python from a python.org 64-bit/32-bit installer, application windows may not update properly due to a Tk problem. Install the latest ActiveTcl 8.5.18.0 if possible. 

发现是要下载8.5版本，而不是更新的8.6版本才可以。搞定。

##### Question
- 程序有中文需要declare

##### Solution
添加 ```# -*- coding: utf-8 -*-```

##### Question
- 想要能保存多条日记

##### Solution
用while loop和break

##### 代码
```
# -*- coding: utf-8 -*-
import time


                                                # ----问候----
print('哥哥，我是你的日记。')
print('你今天有什么想和我分享的吗？')
print('你也可以按"回车键"来阅读我。')

diary = raw_input('>>')


                                                # ----输入回车键，阅读日记----
if diary == '':                         
    diaryFile = open('diary.txt')
    diary = diaryFile.read()
    print('============日记============')
    print(diary)


                                                # ----输入文字，开始写日记啦 ----   
else:
    diaryFile = open('diary.txt','a')
    
    write='y'
    while write=='y':
        diaryFile.write('\n' + time.strftime('%Y/%m/%d')+ ' ' +diary)

                                                # ----还想继续写日记----        
        print('已经帮你记下来啦。你还有想和我说的话吗？(y/n)')
        write=raw_input()

                                                # ----不想写啦----        
        if write !='y':
            break
        
        diary = raw_input('>>')

                                                #----说再见----
    print('谢谢你和我分享这些。')
    print('再见。我会想你的。')

diaryFile.close()
```

##### Question
- 可不可以不通过命令行，而是双击直接运行呢


## 开心的反馈

把这个小小程序给哥哥用，哥哥不停的笑，写下了一行日记

> 2015/10/21 今天很开心，亲爱的老婆为我设计了个程序

喵，我也觉得很开心呢。心里超甜蜜！  
顿时觉得一起分享才是更开心。  
当他更明白我学编程是在做什么，也感受到我做的时候也会想到他，这样的感觉其实更好呀。

喵，不过哥哥平时也不写日记滴。  
偶问了哥哥，他最想要打游戏可以自动练级的程序。  
我现在倒是没有这水平啦，不过我觉得这种可以automate的是事情倒是很值得交给programming去干。  
喵，继续学习，继续创造一些更有爱的东西啦。