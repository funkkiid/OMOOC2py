# Git学习笔记

## Lesson 1
###  How did viewing a diff between two versions of a file help you see the bug that was introduced?

不用费劲的去比较每一行，而是可以轻松的看到更改的地方，立马让自己回忆起来自己的每一次update。  
让发现bug的过程变得简单了很多。  
以前居然不知道有这个功能，常常不知道两个文件内容是不是一样的，也不知道哪个文件是更新的版本，更新了哪些地方，因为一个个比较太费劲了。  
现在可以让这些费劲的工作让计算机自动帮我完成，我只要根据结果进行判断就ok了，繁琐的工作交给计算机自动化，我自己进行决策就ok。这就是自动化的好处。  
以前觉得决策难，是因为要获得决策的数据，和进行决策，这其实是两个部分。  
就好像之前一边写文章一边还要排版一样。当我把这两个角色分开，世界就变得更清楚了。  
回想起来我日常工作中觉得很累很头疼，应该也是因为有很多角色很多功能混在一起的缘故。  
我觉得计算机的练习一个是可以让我学会自动化，一个是可以让我有一双眼睛能够把复杂的事情逐个分解成更简单的东西，不是混为一谈，而是条理清晰，这样解决起来就变得更容易了。  
我现在觉得写reflect很有好处，我也逐渐感觉到了计算机学习对思维的训练，因为它真的可以让我看到以前没想到的维度，用我以前没用过的方式去解决问题，比如diff，比如git。  
我现在真的觉得，学习python其实并不是为了学习python这种语言去编程，而是去练习一种新的看待问题和解决问题的方式。不是混为一谈，而是一点点的去拆分，分解成更简单的。  

### How could having easy access to the entire history of a file make you a more efficient programmer in the long term?

我可以看到我是怎么一步步改进的，看到自己的成长，看到自己从前的局限，也可以回忆起自己好的想法。  
这是一种成长的印记，记录了自己改进的每一步，也容易唤起自己的记忆，知道自己是怎么走过来的。  
我可以快速的找到自己更改的地方在哪里，版本更新了什么内容。  
不用担心某些东西消失了，某个版本被误删了，找不到最近版本了，漏掉了之前版本里的好的内容。  
不用一遍遍的保存版本1234了。更容易修改了。

### What do you think are the pros and cons of manually choosing when to create a
commit, like you do in Git, vs having versions automatically saved, like Google
docs does?

好处：
每一次的commit都更有意义，都是一个独立的可运行的作品。  
而不是一些无意义的半成品。回顾起来更清晰。  
每一个版本更新也更有意义。 
坏处：
有时候可能写了很多东西，但是不记得保存了。  
需要自己记得要进行手工保存。  

### Why do you think some version control systems, like Git, allow saving multiple
files in one commit, while others, like Google Docs, treat each file separately?

因为git中的文件常常是相互关联的，一个地方改变，可能引起其他文件的变化；或者一个改变，需要几个文件的配合才能实现。这几个文件是一个联系的整体。  
而google doc中的文件基本都是独立的

### How can you use the commands git log and git diff to view the history of files?

用git log看自己的更新的不同的版本，注意commit的提示   
找到对应的id后，使用git diff作为对比

### How might using version control make you more confident to make changes that could break something?

知道自己随时都可以方便的恢复到以前的状态，方便的追溯到问题在哪，
知道自己无论做出多么大的改变，有多么大的错误，都不会有不会挽回的后果。  
有一个安全网！我就可以更自由大胆的玩耍，试验，测试。
不会再害怕冒险。  
可以去尝试非常大的改变。  
我觉得这样一个自由探索的空间，无论是programming，还是生活中，都是我所渴望的。

### Now that you have your workspace set up, what do you want to try using Git for?

写书，包括可以进行大的改版  
写文章，写作业，写心得  
写小程序

## Lesson 2
### What happens when you initialize a repository? Why do you need to do it?

创建了一个.git文件夹，记录版本信息的变化  
如果没有init的话，就无法追踪版本，只是一个普通文件夹，无法使用git的功能

### How is the staging area different from the working directory and the repository? What value do you think it offers?

可以把所有文件都放在working directory里面，可以去修改，  
但是在上传的时候，可以有选择性的上传几个文件，而不是所有文件。  
这样可以保证我能更好地做到one commit per logical change
我可以把握修改成熟的文件上传，或者逻辑相似的文件上传，  
同时继续在working directory修改。  
这能搞保证我每次都可以做一个接近展示的小成品，而不是一堆草稿。  
比如写文章，我可以发布我写得成熟的，或者某几个重大改变，但是其他的草稿我也可以方便的在working directory里面写下来。  

### How can you use the staging area to make sure you have one commit per logical change?

把这次commit需要的文件加入 staging area  
不需要的文件移除staging area  
同时使用git diff 确保是这次需要的添加  
给了一个可以随时修改的缓冲区  
这样在推送前可以有更多考虑

### What are some situations when branches would be helpful in keeping your history organized? How would branches help?

试验一些新的功能 做一些探索 测试不同的方向 风格  
可以让不同的版本独立发展 又可以容易的共用代码 修改代码  
master相当于正式发布版保持稳定  
branch可以有很多探索  

### How do the diagrams help you visualize the branch structure?

语言描述会比较复杂，要动用比喻，有很多分岔，不好描述  
但是画图 就会感觉非常直观，会理解是怎么回溯的，一个分支为什么到不了另一个分支  
所以有些概念 还是借助图  
我决定在我的笔记也放些图

### What is the result of merging two branches together? Why do we represent it in the diagram the way we do?

合并两个branch的功能 两个branch的commit按时排序  
图的方式更直观



### What are the pros and cons of Git’s automatic merging vs. always doing merges manually?

自动的优点是方便快捷 对协作 或者同时开发几个方面很有帮助  
缺点是可能有冲突或者冗余   
手动当然更优美 结构更清晰   
但是确实也更费时 尤其是多人协作时  

## Lesson 3
### What happens when you initialize a repository? Why do you need to do it?

创建了一个.git文件夹，记录版本信息的变化

如果没有init的话，就无法追踪版本，只是一个普通文件夹，无法使用git的功能

### How is the staging area different from the working directory and the repository? What value do you think it offers?

可以把所有文件都放在working directory里面，可以去修改，  
但是在上传的时候，可以有选择性的上传几个文件，而不是所有文件。

这样可以保证我能更好地做到one commit per logical change  
我可以把握修改成熟的文件上传，或者逻辑相似的文件上传，  
同时继续在working directory修改。    
这能搞保证我每次都可以做一个接近展示的小成品，而不是一堆草稿。  
比如写文章，我可以发布我写得成熟的，或者某几个重大改变，但是其他的草稿我也可以方便的在working directory里面写下来。

### How can you use the staging area to make sure you have one commit per logical change?

把这次commit需要的文件加入 staging area  
不需要的文件移除staging area  
同时使用git diff 确保是这次需要的添加  
给了一个可以随时修改的缓冲区  
这样在推送前可以有更多考虑

### What are some situations when branches would be helpful in keeping your history organized? How would branches help?

试验一些新的功能 做一些探索 测试不同的方向 风格  
可以让不同的版本独立发展 又可以容易的共用代码 修改代码  
master相当于正式发布版保持稳定  
branch可以有很多探索  

### How do the diagrams help you visualize the branch structure?

语言描述会比较复杂，要动用比喻，有很多分岔，不好描述  
但是画图 就会感觉非常直观，会理解是怎么回溯的，一个分支为什么到不了另一个分支  
所以有些概念 还是借助图  
我决定在我的笔记也放些图

### What is the result of merging two branches together? Why do we represent it in the diagram the way we do?

合并两个branch的功能 两个branch的commit按时排序  
图的方式更直观



### What are the pros and cons of Git’s automatic merging vs. always doing merges manually?

自动的优点是方便快捷 对协作 或者同时开发几个方面很有帮助  
缺点是可能有冲突或者冗余    
手动当然更优美 结构更清晰   
但是确实也更费时 尤其是多人协作时



