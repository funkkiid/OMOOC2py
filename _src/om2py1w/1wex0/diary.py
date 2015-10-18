import sys
diary=open('diary.txt','a')

if len(sys.argv) >1:
    content = ' '.join(sys.argv[1:])
    diary.write(content)
    
else:
    diary=open('diary.txt')
    content = diary.read()

diary.close()
