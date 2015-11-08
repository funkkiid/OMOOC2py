# Sublime

## Sublime
[Download Sublime](http://www.sublimetext.com/2)

##  Launch your editor from the command line
1. Find where the subl command is located. 
subl comes with Sublime, 
so it should be in the directory 
where Sublime is located for you.  
For many people, 
this is /Applications/Sublime\ Text\ 2.app/
Contents/SharedSupport/bin.  
To test this, 
run ls /Applications/Sublime\ Text\ 2.app/
Contents/SharedSupport/bin.  
You should see the subl command listed.  
If you get the error No such file or directory, 
Sublime is located somewhere else for you 
and you'll need to find it.

2. If you do not have a file 
named .bash_profile in your home directory, 
create it.  
Because the name of this file begins with a period, 
it will not appear in most file navigators 
or when you run ls.  
Instead, run ls -a to see if you have the file.

3. Add the line export PATH=$PATH:/Applications/
Sublime\ Text\ 2.app/Contents/SharedSupport/bin 
to the end of your .bash_profile.  
If subl was in a different directory 
for you in step 1, use that directory.

4. Close and re-open your terminal.  
5. Typing subl in the terminal should now open Sublime.

## 参考资料
[Setting up Sublime@Udacity](https://www.udacity.com/wiki/ud775/sublime)