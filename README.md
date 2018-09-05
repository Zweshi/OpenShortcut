# OpenShortcut
A tool for creating keyboard shortcuts to files, folders, programs and websites.  
OpenShortcut works both in the foreground and the background and will launch the  
desired file/folder/program or website when the user bound key is pressed.  

# General info
Current version: 1.0.0  
Current state: Stable  
Python version: 3.4.4 | 32bit | win32  
Tested on: Windows 10  
License: MIT(see LICENSE file)  
Binary version created with: cx_Freeze | cx_Freeze-4.3.4.win32-py3.4.exe  

# Binary version
If you do not want to compile the code yourself you can opt to download a binary
of the latest version via the following link:  
https://github.com/Zweshi/OpenShortcut/releases/download/1.0.0/OpenShortcut-1.0.0.zip

# Building the project(cx_Freeze)
OpenShortcut is setup and ready to be built with cx_Freeze via the Build.py file.  

Please note:  
You may need to move over the _cpyHook.pyd file from your python lib
directory into the output directory if its not copied over correctly by your
version of cx_Freeze.
