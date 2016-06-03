### How to run the scripts
#### Preparations
All the instructions below apply to all the tools provided here. If you are not familiar with basic shell / Unix commands or Python, this should get you oriented. Different for Mac and Win
#### What do I need on my computer?
Most of it will already be on there, the rest you can download for free. 

It's easiest run to these tools from the **command line**. On a Mac, all you need to do is open the Terminal (search for *Terminal.app* in the "Applications" folder). On Windows, you can use the command line tool (just type *cmd* into the "All Programs" window) or install [Cygwin](https://www.cygwin.com/) (free), which is essentially a small Linux you can run inside your Windows environment. Within Cygwin, you can just follow the instructions for Mac. 

All the code is written in [Python](https://www.python.org/). Mac computers come with Python pre-installed. If you are running Windows, you might have to [download](https://www.python.org/downloads/windows/) and install a copy of Python first (which is free).  
You will also, and this is the only real headache you will have to suffer through, [change](http://www.anthonydebarros.com/2015/08/16/setting-up-python-in-windows-10/) the command line settings. 

You will see that all scrips come in two versions: One for Python 2, and one for Python 3. The file name will end in *_py2.py* or *_py3.py* respectively. This is necessary because while a lot of people have moved on to version 3 of Python, most Mac computers still run version 2. 
If you are unsure which version you have on your computer, type 

`python -V`

into the command line prompt. 

#### How do I run the scripts?
Every script will have slightly different settings, which are explained on the Readme page that comes with each of them. Let's assume I want to work with the Downloader. I need the downloader_py2.py because my computer runs Python 2.7.10. After navigating to the right version of the script, I click on "Raw" on the top right of the screen and download the resulting textfile. In Chrome, for instance, I click on File, then I click Save page - note how the menu already suggests saving it as a Python script. Then I save the script someplace on my computer. It does not matter where, but you need to know / remember where it is. Now open the Terminal / Command line tool. 

Now we will use the Terminal to run the script with the right setting. We will communicate with it through the Terminal rather than a graphical interface. First, we need to navigate to the folder the script is saved in. If it is in *Downloads*, for instance, do this:

on the Mac:

    cd ~/User/Downloads



`cd` stands for change directory; the `~/` is short for your user folder on a Mac and thus the top directory for Desktop, Downloads, Documents, etc. 

on Windows:

    cd \Users\YOURUSERNAME\Downloads

`cd` stands for change directory; replace the capitalized letters with your own user name. You can find it by locating your user folder in the Windows explorer by opening your Windows folder, then the Users folder. 

Hint: type `cd ..` on both systems to take a step back, `ls` on a Mac and `dir` on Windows to look at the contents of the folder you are currently in. Basic shell commands are listed for the Mac XX and for Windows XX.
