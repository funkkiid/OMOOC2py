# -*- coding: utf-8 -*-
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app,Bottle,route,run,debug,request,template,get

from datetime import datetime
import pytz

import sys





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

@route('/wechat', method="POST") # mypath需要跟微信公众号里注册的信息一致
def check_signature():
    # 获取post请求body内容
    data = request.body.read()

    # 解析xml
    import xml.etree.ElementTree as ET
    root = ET.fromstring(data)
    mydict = {child.tag:child.text for child in root}

    user_name=mydict['FromUserName']
    user_diary=str(user_name)+'.txt'

    # 添加帮助
    if mydict['Content'].lower() =='help':
        mydict['Content'] = '''
        这里是一个让你书写自己思绪的地方。
        有什么话直接对我说就好啦，我会为你保存好的。
        输入“help”可以看到帮助。
        输入“read”可以阅读历史日记。
        '''

    # 添加阅读
    elif mydict['Content'].lower() =='read':
        diaryFile = open(user_diary)
        diaryContent = diaryFile.read()
        diaryFile.close()
        mydict['Content'] = diaryContent

    else:
        # 添加日记
        today = datetime.now(pytz.timezone('Asia/Shanghai'))
        newDiary=mydict['Content'].encode('UTF-8')

        diaryFile = open(user_diary,'a')
        diaryFile.close()

        with open(user_diary, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            newDiaryLine=today.strftime("%Y/%m/%d/ %T")+ ' '+newDiary
            f.write(newDiaryLine.rstrip('\r\n') + '\n' + content)

        # 更新时间
        import time
        mydict['CreateTime'] = int(time.time())
        # 更新回复内容
        mydict['Content'] = mydict['Content'].encode('UTF-8')+'-已保存'


    # 重构xml
    myxml = '''\
    <xml>
    <ToUserName><![CDATA[{}]]></ToUserName>
    <FromUserName><![CDATA[{}]]></FromUserName>
    <CreateTime>12345678</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[{}]]></Content></xml>
    '''.format(mydict['FromUserName'],mydict['ToUserName'],mydict['Content'])

    return myxml

@route('/',method='GET')
@route('/<user_name>')
def diary(user_name='小小游侠'):

    diaryFile = open('diary.txt')
    diaryContent = diaryFile.read()
    diaryFile.close()
    diaryContent=diaryContent.replace('\n', '<br />')

    output_start ='''
<head>
<meta charset="utf-8">
<title>Diary of Yours</title>
<!-- Bootstrap core CSS -->
<link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
<!-- Custom styles for this template -->
<link href="css/cover.css" rel="stylesheet">
</head>
<body>

<h1>小小游侠的聊天室</h1>
<p>欢迎小小游侠来到聊天室小憩一会。
<br />
<br />如果想用自己的名字加入交谈，
<br />可以用 “zoejane.pythonanywhere.com/YOURNAME”进行登录，
<br />名字可以是字母和数字和下划线的组合。
<br />
<br />想搭建一个相似的网页，可以看这里的<a href='https://zoejane.gitbooks.io/omooc2py/content/1sTry/first-internet-web.html'>教程</a>。
<br />这个网页的具体的<a href='https://github.com/zoejane/python-anywhere/blob/master/diary-web.py'>代码</a>也可以在这里看到。
<br />
<br />我是<a href='mailto:dadac123@gmail.com'>Zoe Jane</a>，欢迎一起分享你的心得和感悟。
<br />我的<a href='mailto:dadac123@gmail.com'>Email</a>
<br />我的<a href='https://github.com/zoejane'>GitHub</a>
<br />我的<a href='http://zoejane.github.com'>GitBook</a>
<br /></p>

<p><b>Share your feeling:</b></p>
<form action="'''

    output_middle='''" method="GET">
<input type="text" size="70" maxlength="100" name="newdiary">
<input type="submit" name="save_diary" value="Save">
</form>
<p>====Diary====</p>'''

    output_end='''<br /><br />
<div class="inner">
<p><i>life is wonderful</i></p>
</div>
</body>'''

    if request.GET.get('save_diary','').strip():

        today=datetime.now()
        newDiary=request.GET.get('newdiary', '').strip()

        diaryFile = open('diary.txt')
        diaryContent = diaryFile.read()
        diaryFile.close()

        with open('diary.txt', 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            newDiaryLine=today.strftime("%Y/%m/%d/ %T")+ '  ['+user_name+'] '+newDiary
            f.write(newDiaryLine.rstrip('\r\n') + '\n' + content)

        diaryFile = open('diary.txt')
        diaryContent = diaryFile.read()
        diaryFile.close()
        diaryContent=diaryContent.replace('\n', '<br />')

        return output_start+user_name+output_middle+diaryContent+output_end
    return output_start+user_name+output_middle+diaryContent+output_end


application = default_app()

#run(host='localhost', port=1234, debug=True)
