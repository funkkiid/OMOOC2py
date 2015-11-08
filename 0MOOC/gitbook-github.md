# Gitbook与Github互推
  
觉得Gitbook是个好东西，顿时有种想写书的感觉啦。  
只是之前以为gitbook和github是自动同步的，因为看上去都是git家族的嘛>_<  
结果没想到要实现这个还有自己设置，而且居然一下子还木有设置成功，这个问题就一直闲置在那里几天了。  
结果没想到今天试一下居然成功了，记录自己的体会。
##解决问题的启示
### 为什么第一次没解决
- 第一次有发现import tool，提示要输入git url，
其实是要输入book的git url，结果我以为是输入github的url，一直不成功。
- 看到英文界面，加上对github完全不熟悉，有种无从下手的感觉。
- help文档其实很容易看到，但是一直被我无视。
### 为什么今天尝试成功了
- 学习了一点github知识，对这个没有那么怕了。
- 正好看到有help文档，发现其实有提到这个，就跟着边看边做。
### 启示
- 学会使用帮助文档。
- 对一个知识不熟悉而害怕，可以先补一下入门知识。
- 当时解决不了没关系，过几天学了一些别的，回过头来可能忽然就会解决了。

>参考资料：[Gitbook帮助文档](https://help.gitbook.com/github/index.html)

## 步骤：
### 从Gitbook传送到Github
Transferring content to GitHub  

- [Use the Import Tool from GitHub](http://import.github.com/new)
- Enter your GitBook git url,   
for example: https://git.gitbook.com/MyName/MyBook.git   
(this url can be found in your book settings).  
打开网站右上角的“MY BOOKS”，点击你想传送的书名。  
打开后，选择右下角的“Settings”。  
页面往下翻，可以看到有个Git URL，就是这里要用的地址。
- Enter a name for your GitHub repository.
- Enter your GitBook credentials (you can use your API token instead of your password) when prompted.

### 连接Gitbook与Github账户

#### GitHub Integration
When your content as been transferred to GitHub, you can now setup the integration so that GitBook can still build your book from GitHub。

### 1. Connect your account / Permissions
In your account settings, connect your GitHub account with the correct permissions:
- 点击网站右上角自己的头像，选择Account Setting.
- 页面往下翻，看到有个Github设置的地方，设置自己的Github账户信息。  
- 注意这里有个三角形的下拉选框，选择Access to public repositories。




### 2.Link a book and a GitHub repository
Open the GitHub section in your book settings
Enter your repository id (such as: YourGitHubUserName/RepoName)
Save your settings
- 打开网站右上角的“MY BOOKS”，点击你想传送的书名。  
- 打开后，选择右下角的“Settings”。
- 进入Setting后，点击右边菜单栏最下面的Github。
- 你可以看到设置你GitHub Repository的地方。
- 输入你的repository id (如: YourGitHubUserName/RepoName)
- 保存设置。

### 3.测试
- 在gitbook里对图书修改，看是否同步到了github。
- 在github里对图书修改，看是否成功同步到了gitbook。
- 如果有问题可以对照帮助文档，继续解决。