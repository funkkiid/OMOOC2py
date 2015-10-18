#! /usr/bin/env python

import sys
import time

diary=open('diary.txt','a')

if len(sys.argv) >1:
    content = ' '.join(sys.argv[1:])
    diary.write("\n" + time.strftime("%Y/%m/%d")+ ' ' +content)
    
else:
    diary=open('diary.txt')
    content = diary.read()
    print(content)

diary.close()
