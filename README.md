# Folder-Library
Download Icon for folder and change the folder icon.
requrement:-
install
```
Python:- (just install it)
https://www.python.org/downloads/ 

FolderIkon:-  (just install it in python)
https://github.com/demberto/FolderIkon

ffmpeg:- (after downloading add it in desktop path environment)
https://ffmpeg.org/download.html
```

## picDownloader.py:-
If you want to download image to every folder make sure folder name must be perfect:-
run:-
```
python picDownloader.py
```
It will ask for folder path where all folders are present.

Skip the above step if image already existed.

## change_all_folder_icon.bat:-
first copy two bat file into the folder.

then open "change_all_folder_icon.bat" here open it in edit mode.
change the rootDirectory and commandScript(copy as path)
```
set "rootDirectory=D:\Tools\New"
set "commandScript=D:\Tools\New\change_folder_icon.bat"
```
if it did not work make sure commandScript path use (copy as path).

## change_folder_icon.bat:-
if you want to change a single folde just copy this file there and run it.


Thanks to demberto for proving us the (FolderIkon).
