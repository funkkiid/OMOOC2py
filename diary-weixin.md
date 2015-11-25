# 微信平台-小小日记

> 更新日志：  
20151124 完成“测试存储日记”  
20151124 创建


### 注册公众平台账号
微信.公众平台 https://mp.weixin.qq.com/  
点击右上角进行注册  
个人类型只支持注册订阅号

### 成为开发者
登陆“微信.公众平台”  
点击左边目录的“开发者中心”  
接受协议即可
在“开发者工具”里有提供[开发者文档](http://mp.weixin.qq.com/wiki/home/index.html)


### 服务器配置
阅读开发者文档的[接入指南](http://mp.weixin.qq.com/wiki/16/1e87586a83e0e121cc3e808014375b74.html)部分,  
了解到是要在自己的网站上添加一段代码，  
使得它能够获取微信服务器所发送的GET参数请求中携带的四个参数，   
完成相关的校验流程，  
返回echostr参数的内容。

具体这段代码要怎么写呢？  
在[Alan同学的笔记](https://wp-lai.gitbooks.io/learn-python/content/1sTry/wechat.html)中找到了[具体的实现方式](http://www.cnblogs.com/weishun/p/weixin-publish-developing.html)。

对照接入指南中的流程，对代码进行了一下梳理与注释。

将这段代码加入到自己的网站中，  
并将微信的服务器配置URL设为“http://自己的网址/wechat”，  
比如我的就是http://zoejane.pythonanywhere.com/wechat

验证成功，搞定！
启用服务器配置

##### 代码

```
@route("/wechat")
def checkSignature():

    # 获取微信服务器所发送的GET参数请求中携带的四个参数
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)

    token = "mytoken" # 你在微信公众平台上设置的TOKEN

    # 将token、timestamp、nonce三个参数进行字典序排序
    tmpList = [token, timestamp, nonce]
    tmpList.sort()

    # 将三个参数字符串拼接成一个字符串进行sha1加密
    import hashlib
    tmpstr = "%s%s%s" % tuple(tmpList)
    hashstr = hashlib.sha1(tmpstr).hexdigest()

    #开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
    # 若确认此次GET请求来自微信服务器，请原样返回echostr参数内容，则接入生效
    if hashstr == signature:
        return echostr
    else:
        return "error"
```

### Just for fun,绕过复杂的服务器配置
其实服务器的配置只是检测有没有返回echostr   
所以，看似复杂的服务器配置根本也可以不用这么麻烦  
只要这一段就可以了
```
@route("/wechat")
def checkSignature():
    echostr = request.GET.get('echostr', None)
    return echostr
```
测试通过！  

所以其实写不出上一段中的那一段略微复杂的代码也没有关系，因为这个根本也不是重点...  
不过我差点就卡在这里了 因为开发者模式一定会很复杂 我开始的时候根本看不懂校验流程说的到底是什么

### 测试Echo功能
受到[Alan同学的笔记](https://wp-lai.gitbooks.io/learn-python/content/1sTry/wechat.html)的启发，测试了他写的Echo功能的代码，  
也就是用户发一句话，我就可以回复同样一句话。  
结合阅读“开发者文档的[接收普通消息](http://mp.weixin.qq.com/wiki/17/fc9a27730e07b9126144d9c96eaf51f9.html)”部分，对微信的文本格式有了一个大概的了解。

而且在微信公众号上看到自己给自己的回复，感觉好好玩，哈哈，有种自己给自己做了一个玩具的感觉。  

对于字典这一部分，还有些不了解，需要补课。  
考虑这几天把Learn python the hard way的相关部分补完。

不过既然都可以echo了，那我也就可以测试存储日记啦。

### 测试存储日记

把我之前写的写日记的相关代码添加进来。

将Alan同学代码的这一部分，

    # 更新时间
    import time
    mydict['CreateTime'] = int(time.time())

    # 现在不对内容做任何操作，只是原样返回

    
改写成现在我想用的新功能


    # 添加日记
    today=datetime.now()
    newDiary=mydict['Content']
    user_name=mydict['FromUserName']

    with open('diary.txt', 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        newDiaryLine=today.strftime("%Y/%m/%d/ %T")+ '  ['+user_name+'] '+newDiary
        f.write(newDiaryLine.rstrip('\r\n') + '\n' + content)

    # 更新时间
    import time
    mydict['CreateTime'] = int(time.time())
    # 更新回复内容
    mydict['Content'] = mydict['Content']+'已保存'

就实现了两个小小功能：
1. 将用户发送的内容自动添加到diary.txt中
2. 回复用户 ‘XXX已保存’

其实有了mydict['Content']这部分内容，就会发现和第一周命令行的开发差不多了