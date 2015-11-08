# 用python快速打开网页
> 更新日志  
- 20151016 第一次-第四次尝试

## 第一次尝试 遇见webbrower
搜索how to open web browser in python，学习到了webbrower

```
import webbrowser  
webbrowser.open(url)
```

发现是是Safari打开的，我想用chrome打开

## 第二次尝试 使用chrome
搜索python webbrower chrome
发现
[Python webbrowser.open() to open Chrome browser @stackoverflow](http://stackoverflow.com/questions/22445217/python-webbrowser-open-to-open-chrome-browser)  
非常棒的解决方案，好好学习

```
import webbrowser

url = 'http://docs.python.org/'

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)
```

## 第三次尝试 在python外运行
参见[Running Programs from the Command Line](http://zoejane.gitbooks.io/zoe-py-tutorial/content/running_programs_from_the_command_line.html)

- Add shebang line in python file 
    - ```#! /usr/bin/env python3```
- change the .py file’s permissions in Terminal
    - ```chmod +x pythonScript.py```
- run it in Terminal 
    - ```./pythonScript.py. ```

## 第四次尝试 制定不同的网址（使用参数）
尝试搜索 python webbrowser parameter|argument  
看不懂  
试着使用sys.argv未果  
不过正好链接到了我在学习的Automate the boring stuff的课程  
于是决定继续学习课程

学习到了sys.argv的使用方式

以下代码实现的是  
Terminal打开```./mapit.py ADDRESS(或者复制ADDRESS到剪贴板上)```  
能够自动用google map打开该地址的地图

```
#! /usr/bin/env python3
import webbrowser, sys, pyperclip

sys.argv #['mapit.py', '870','Valencia','St.']

# Check if command line arguments were passed
if len(sys.argv) >1:
    #['mapit.py',      '870','Valencia','St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>

webbrowser.open('https://www.google.com/maps/place/' + address)

```