#Dataset Downloader

###Description
The downloader downloads zipped files from a web site to a specified folder. It also returns a list containing the files names of the files found. 

Arguments:

    downloader(link, directory):
    link -- needs to be a URL of the format "http://xy.z", pointing to a web site containing .zip files. 
    directory -- an existing folder, this is where the files will be downloaded to.

###How to use the Dataset Downloader
Run it in an shell. Basic setup and shell operations are described here (XXX).

The Downloader takes a URL and a target directory as input. Thus

    python downloader.py link directory

For instance, 

    python downloader.py http://www.google.com ~/Desktop/dataset

will download all zip files found on google.com to the folder dataset which is located on the Desktop. 
The downloaders output will look like this:

    842 files to be downloaded
    File xzy.zip downloaded to Desktop/dataset
    File ...
