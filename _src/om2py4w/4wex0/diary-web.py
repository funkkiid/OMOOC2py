# -*- coding: utf-8 -*-
from bottle import Bottle,route,run,debug,request,template

from datetime import datetime
import sys

diary=Bottle()

@diary.route('/')
@diary.route('/diary')
def greeting():
    return template('greeting.tpl')

@diary.route('/reading')
def reading():
    diaryFile = open('diary.txt')
    diaryContent = diaryFile.read()
    diaryFile.close()
    diaryContent=diaryContent.replace('\n', '<br />')
    output='<p>====日记====</p>'+diaryContent+"<br /><br /><a href='/writing'>写日记<a><br /><a href='/'>Back Home<a>"
    return output

@diary.route('/writing',method='GET')
def writing():
    if request.GET.get('save','').strip():
        
        today=datetime.now()
        newDiary=request.GET.get('newdiary', '').strip()
     
        diaryFile = open('diary.txt','a')
        diaryFile.write('\n'+today.strftime("%y/%m/%d")+ ' '+newDiary)
        diaryFile.close()

        return '''
<p>The new diary was saved.</p>
<a href='/writing'>写日记<a>
<a href='/reading'>读日记<a>
<a href='/'>Back Home<a>
'''
    else:
        return template('new_diary.tpl')

run(diary,host='localhost', port=1234, debug=True)
