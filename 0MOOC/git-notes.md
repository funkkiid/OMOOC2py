# Git操作笔记

##Git Cheat Sheat
[Git Cheat Sheat pdf下载](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)

## Q & A
### 什么是Repository
一些互相关联的文件群。

### 为什么需要Repository
因为有时候一处修改会影响几个地方。  
有时候功能的实现需要几个文件共同完成。  
所以git的推送是将这些文件群作为一个整体来推送的。

### git log是什么
修改日志。  
里面可以看到每次修改的详细情形，比如描述，ID，更改的地方等。

## 练习步骤
### 复制Repository
1. 在Terminal中，输入"git clone 你想要复制的的Repository的URL",  
它会复制这个Repository的内容在你现有的工作目录下，  
2. 如果你不知道你现在的工作目录是哪里，可以输入"pwd"
3. 如果你想更改自己的工作目录，可以使用"cd 你想使用的文件夹路径" 
4. 如果想更好地使用Terminal，建议先学习一些command line的基础知识.

### 查看git log
1. 使用cd命令，进入你想查看的某个git项目的目录中。可以用pwd命令检验是否到达了对的目录。
2. 输入"git log"。就可以查看到具体的git log啦。
3. 如果想退出git log的浏览，输入q（代表quit，退出）。

### 使用git diff比较两个版本的不同
1. 根据git log，找到自己想要比较哪两个版本。
2. 复制commit后的一长串字母和数字组合的id。
3. 输入“git diff 第一个id 第二个id”进行比较。
4. 如果觉得id太长，也可以只输入id的前面4个字符。
5. 如果想退出，输入q。

### 回到上一个版本的状态
1. 输入"git checkout 想回到的版本的id"