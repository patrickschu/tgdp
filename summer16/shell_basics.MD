#### Running scripts in a shell
After navigating to the right version of the script, click on "Raw" on the top right of the screen. Download the resulting textfile. Use the Terminal to navigate to the folder you saved the script in. If it is in Downloads, for instance, do this:

on the Mac:

`cd ~/User/Downloads`

on Windows:

`cd \Users\YOURUSERNAME\Downloads`

Hint: type `cd ..` to take a step back, `ls` on a Mac and `dir` on Windows to look at the contents of the folder you are in. Basic shell commands are listed for the Mac [here](https://www.git-tower.com/blog/command-line-cheat-sheet/) and for Windows [here](http://www.cs.columbia.edu/~sedwards/classes/2016/1102-spring/Command%20Prompt%20Cheatsheet.pdf).

Now you can run the script like so:

    python name_of_script settings

For instance, if you have a script called *analyzer.py* that takes a file name as input. To make the script work on a file called "data.txt", which is stored in Downloads, you would type:

    python analyzer.py ~/Downloads/data.txt 
