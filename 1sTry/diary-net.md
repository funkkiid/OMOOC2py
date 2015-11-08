# 小小日记-Net101

## 尝试一
- 完全不懂本周说的到底是什么，看到芝麻星上有提到socket和UDP，觉得应该从这里入手
- google搜索python socket tutorial 发现一个简短又看着比较舒服的教程 [Python socket network programming](http://pythontips.com/2013/08/06/python-socket-network-programming/),对server和client有一个大概的感受
- 文末有推荐另一个教程[Python socket – network programming tutorial](http://www.binarytides.com/python-socket-programming-tutorial/)
- 看着看着才发现上面说的都是tcp，关于udp的教程在这里[Programming udp sockets in python](http://www.binarytides.com/programming-udp-sockets-in-python/)
- 搜索python tcp udacity，看在udacity上有没有合适的资源，然后搜到了Computer Networking中的 What the Course is NOT About，意思是说学这门课需要有一些基础知识，下面给出了一些学习链接，我觉得可以从这里入手
- 瞬间有了一堆学习材料，其中最后部分才是和python相关的，而且最后两个链接也是上面搜到的binnarytides网站的，所以决定先从这里入手
- 还是觉得官方文档入门不够友好，适合懂得一些之后去查阅，但是给没有一点概念的人看太费劲了

#### Instructor Notes from Udacity

##### Some suggestions from Piazza:

- [Network Programming Study Guide](http://www.sal.ksu.edu/faculty/tim/NPstudy_guide/index.html)
- [TCP/IP Illustrated, Volume 1: The Protocols, Addison-Wesley, 1994, ISBN 0-201-63346-9](http://www.kohala.com/start/tcpipiv1.html)
- [Stanford Course: An Introduction to Computer Networks (Fall 2012)](http://f12.class2go.stanford.edu/networking/Fall2012)
- [Computer Networks: 5th Ed. by Tanenbaum & Wetherall](http://cse.hcmut.edu.vn/~minhnguyen/NET/Computer%20Networks%20-%20A%20Tanenbaum%20-%205th%20edition.pdf)

##### A quick google search turns up these slides for TCP/IP basics:

http://www.slideshare.net/sanjoysanyal/tcpip-basics

##### And a few python tutorials on socket programming:

- http://docs.python.org/2/howto/sockets.html
- http://www.tutorialspoint.com/python/python_networking.htm
- TCP: http://www.binarytides.com/python-socket-programming-tutorial
- UDP: http://www.binarytides.com/programming-udp-sockets-in-python

## 尝试二
- 使用udp要用到netcat,而不是telnet
- 安装netcat```brew install netcat```
- mac里用netcat要用netcat指令，而不是nc和ncat，如```netcat localhost 5000 -u -v```
- 通过上面的UDP学习文档，了解到了一个简单的socket和client的效果

## 尝试三
- 尝试与之前写的小小日记CLI版本结合起来
- client写一条message server能够回复print出时间+message
- 把时间改成了python2版本的了

```    import datetime  ```  
```today=datetime.now()  ```  
``` print today.strftime("%y/%m/%d")```
- 中文测试也是ok的
- 尝试在回复的同时，在server端打开diary.txt，并记录日记
- 发现改了代码还是无法在目录下建立diary.txt,后来发现while loop中，它是记录到我的Zoe文件夹（也就是默认的home路径下面去了）
- 推测，因为我的运行方式是```python /Users/Zoe/GitHub/socket/diary-server.py```尝试切换了目录再运行
- 顺利整合了原有功能
- 尝试多个客户端登陆，没问题
- 添加了代码，可以在diary.txt中体现是哪个端口登陆的```diaryFile.write('\n'+today.strftime("%y/%m/%d")+' client['+str(addr[1])+'] '+ diary)```

## 感想
- 喵，看到大家交作业好神速，觉得不可思议，因为当时还处于一头雾水什么也不知道的情况。结果自己一尝试，好像也没有想象中难耶。
- 吸取上次教训，上次开始就想做一个有点复杂的功能，给自己挖了一堆坑，完全出不来啊，写的代码也不知道是个什么，这次就是从实现最简单的功能开始，过程更流畅。
- 吸取上次教训，周三开始写代码，交作业急急忙忙，弄到很晚，还写得很烂。这次也是受到大家的影响，发现早点动手最最好，周六开发出来第一版，整周的节奏才更加的不紧不慢 ^_^
- python编程就是这么简单，一点点代码就可以搞定问题，噢耶！
- 回到熟悉的命令行模式，再次感受到命令行开发真的比GUI简单好用。