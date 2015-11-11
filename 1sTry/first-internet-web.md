# 互联网的世界，让我们启程吧！- 搭建你的第一个python小小网页

受到[liangpeili](https://liangpeili.gitbooks.io/omooc2py/content/week3/week3-day5-web.html)童鞋把网页搭建在互联网上的启发，  
觉得既然都用bottle把网页都写出来了，也是时候把这个网页放在互联网上啦。  
不用每次想用的时候，还得从自己的电脑上启动，或者从别人的电脑上还要下载python环境才能用。  
直接打开网页访问，这才叫帅。  
这也是我最开始想实现的效果，总觉得自己写的程序，给哥哥用，哥哥都不知道从哪里开。  
放上互联网，哥哥也好，妈妈也好，朋友也好，小白也好，秒懂。

## 发布平台的选择
开始是上传到自己的网站空间，后来想，不对啊，虽然我的python程序放上去了，又没人给我运行。  
不像html放上去，就直接显示了。

然后联想到以前参加Rails Girls的活动的时候，用ruby的代码写的很简单的程序，也是放到heroku上就变成网页了。

猜想这个应该涉及到支持一个可以在后台可以运行python的平台，或者说后台经过某种部署后，python文件是可以以某种方式运行出来的。  

当然，这个我也不太懂，看了[官方的文档的Deployment部分](http://bottlepy.org/docs/dev/deployment.html)。  
了解了一下bottle的Deployment。  
不过还是不是很懂，提到的一堆方式我都不熟悉，唯一一个稍微眼熟一点的，是Google App Engine。  
推测这个用Google App Engine 是可以部署出来的。

获得一个粗略印象后，还是先用google搜索网站获取灵感。
搜索关键词‘bottle python web deploy’。  
有提到[Red Hat Openshift](https://www.openshift.com/) 和[Simple Bottle Hosting: PythonAnywhere](https://www.pythonanywhere.com/details/bottle_hosting)。

浏览了一下网站，在(PythonAnywhere)[https://www.pythonanywhere.com/details/bottle_hosting]上提到‘From sign-up to a live Bottle app in 2 minutes...’，顿时觉得就这个了。   
因为我确实看不懂一大堆的Deployment文档啊。  

事实也证明，PythonAnywhere上搭建bottle网站确实很方便，什么都帮你设置好了。我要做的就是写一个Python文件，然后就等网站自动设置就OK。
