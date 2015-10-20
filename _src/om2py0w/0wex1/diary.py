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
