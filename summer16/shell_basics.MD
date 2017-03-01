#### Running scripts in a shell
After navigating to the right version of the script, click on "Raw" on the top right of the screen. Download the resulting textfile. Use the Terminal to navigate to the folder you saved the script in. If it is in Downloads, for instance, do this:

on the Mac:

`cd ~/User/Downloads`

on Windows:

`cd \Users\YOURUSERNAME\Downloads`

Hint: type `cd ..` to take a step back, `ls` on a Mac and `dir` on Windows to look at the contents of the folder you are in. Basic shell commands are listed for the Mac [here](https://www.git-tower.com/blog/command-line-cheat-sheet/) and for Windows [here](http://www.cs.columbia.edu/~sedwards/classes/2016/1102-spring/Command%20Prompt%20Cheatsheet.pdf).

Now you can run the script like so:

    python faveconverter_py2.py "Patrick"
