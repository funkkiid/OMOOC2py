# 小小日记-桌面版

## 思考一

完全不懂GUI，所以需要一个教程来入门一下。  
- 本来准备用Udemy的一个关于PyQt的课程的，但是发现完全卡在了第一步安装上了。
- 改用python自带的Tkinter，先绕过安装的这个坑，开始练习再说。
- 搜索tkinter tuturial，选用了一个图文并茂并且看起来比较短的教程先学。
> 参考资料：[Python Tkinter](http://www.python-course.eu/python_tkinter.php)
- 发现时间不够用，所以先挑一些这次项目会用的相关章节先看。

## 思考二
#### 关于GUI
我希望我的GUI，有可爱的图片，字体好看一点啦。  
既然是GUI，就发挥一一下GUI图形界面里图形的作用。  
其实我觉得GUI就是要美美美，就是暂时实力还比较小白。

#### 关于网页交互
对网页交互这一块比较感兴趣，因为觉得网页端的跨平台性比较强，手机和电脑可以通用，而且也不用安装python就可以运行。  
这一部分有待发掘。

## 思考三
打开程序后，显示两个Button（带有图片显示）
- Write
- Read

Write版面
- 输入框
- 三个Button
    - Save
    - Read
    - Leave
    
Read版面
- 阅读框
- 一个Button
    - Write
    - 

## 尝试一
#### 添加图片界面
- 搜索read和write的图片，改成gif格式，宽度改成200
- 想使用带图片的button，google搜索，貌似和self.photo命令有关
- 搜到一段还有点类似的代码，button是在图片下，我觉得也可以
> 参考资料：[[Tutor] Images + Tkinter](https://mail.python.org/pipermail/tutor/2002-November/018610.html)
- 尝试着改一改，有个页面雏形
- Button改成了中文，程序开始要添加一行```# -*- coding: utf-8 -*-```

#### 添加界面跳转
- 想象中有几个界面，想在几个界面中进行切换，开始是搜索的tkinter button change window，后来发现其实我的意思是在几个frame中切换
- 在stackoverflow上有段超棒的解答，虽然我不太看得懂，但是看到程序运行出来的效果，我就觉得写得真的好棒
> 参考资料：[Switch between two frames in tkinter](http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter)
- 尝试把上面完成的图片界面程序和这个界面跳转程序连接到一起

#### 添加读日记界面
- 在尝试在读日记界面添加text的时候，遇到global name 'END' is not defined，搜索后发现END要改成tk.END就可以了
> 参考资料：[tkinter NameError: global name 'END' is not defined](http://www.scriptscoop.net/t/30e72bef2788/python-tkinter-nameerror-global-name-end-is-not-defined.html)
- 整合上一周的的阅读diary的代码

#### 添加写日记界面
- 添加input界面-Entry Widgets,还是有问题，尝试搜索self entry tkinter,发现了上一次回答界面跳转问题的人对方面也有回答,而且自带了get button，也是我等下会用到的
> 参考资料：[Tkinter Entry “get” function is returning nothing](http://stackoverflow.com/questions/10727131/tkinter-entry-get-function-is-returning-nothing)
- 发现[Bryan Oakley](http://stackoverflow.com/users/7432/bryan-oakley)关于tkinter的回答都很棒，值得细读
- 修改了一下Entry的padding，看起来更舒服一点 ```self.entry.pack(ipadx=100,ipady=10)```
- 保存完自动清空内容 ```self.entry.delete(0,tk.END)```
- 整合上一周的的书写diary的代码

#### 继续修改
- 发现阅读diary的内容没有正确展示出来，后来发现是因为height不够，后面的内容没有显示
- 考虑增加scrollbar
- 根据前面的tutorial中的scrollbar部分，一行行的尝试添加代码，看哪里可能出错，修正
- 添加```from Tkinter import *```减少报错
- 考虑修改阅读版面的字体


#### 中文支持
- 发现不能保存中文，将get()语句修改 ```diary=self.entry.get().encode('utf-8')```
- 发现可以保存复制的中文，但是中文不能打字
- 发现在python的idle中运行时可以打中文的，但是sublime中不行，推测是调用的tk版本不同的问题
- 但是在idle中运行程序，点击左上角关闭感觉有些死机，sublime中没有这个问题


### 问题
- 发现阅读diary中内容不是实时更新，而是启动时更新的,觉得这应该和init有些关系，待解决
- sumblime直接调用不能打中文
- idle调用不能直接关闭程序（貌似死机）