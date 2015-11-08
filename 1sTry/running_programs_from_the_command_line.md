# Running Programs from the Command Line

> 参考资料
> [Appendix B – Running Programs](https://automatetheboringstuff.com/appendixb/)

## Shebang Line
The first line of all your Python programs should be a shebang line, which tells your computer that you want Python to execute this program. 

- On Windows, the shebang line is #! python3.
- On OS X, the shebang line is #! /usr/bin/env python3.

You will be able to run Python scripts from IDLE without the shebang line, but the line is needed to run them from the command line.

## Running Python Programs on Windows
- create a .bat batch file 
	- @py.exe C:\path\to\your\pythonScript.py %*
- Replace this path with the absolute path to your own program, and save this file with a .bat file extension.
- The MyPythonScripts folder should be added to the system path  dialog. 
- run the batch files in it from the Run dialog.
	- pythonScript

## Running Python Programs on OS X
- Save your .py file to your home folder. (Or change the PATH)
- Then, change the .py file’s permissions to make it executable by running 
	- chmod +x pythonScript.py
- you will be able to run your script whenever you want by opening a Terminal window and entering 
	- ./pythonScript.py. 