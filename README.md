# Quickstart
```
git clone https://github.com/alexandrumot/organize-downloads.git
cd organize-downloads
```
## Install dependencies
```
pip3 install patool
```
## Use
If you want to use the script as it is, add the 4 folders to Downloads:
1. Apps
2. Zips
3. Images
4. Others

And add your <User> name in the const variables in main.py
    **OR**
You can **contribute** to make it better!

## I recommend...
Creating a start.bat that starts the script in background 
  [you can run this script on startup by adding the batch file to startup folder: ```Win+r``` type ```shell:startup``` and press Enter]:
``` 
@echo on

start pythonw main.py

exit
```
and end.bat file to stop the script:
```
@echo on

taskkill /IM pythonw.exe /F

exit
```


