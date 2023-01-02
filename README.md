# Auto wish importer for paimon.moe
## Project archived
There is no way to update browser data with selenium, so this importer is literally useless.
## About
This python script automatically runs powershell script provided by paimon.moe and imports it's output into the website without any user interaction needed. At the time it only works for Firefox but it will support Google Chrome soon.

## Windows installation
1. Install [Python 3.10.4](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)
2. Open PowerShell terminal (Shift + Right click -> Open PowerShell window here) in the same folder as 'autowish.py'
3. Run 'pip install -r requirements.txt'
4. Run 'Unblock-File -Path .\importer.ps1'
5. Open 'autowish.py' with any text editor and find '# Config'
6. Open Firefox and head to 'about:profile' and copy the path to the currently used profile
7. Paste it in place of 'yourPathHere', save and exit
8. To run the script double click 'Genshin import wishes.bat'

NOTE: Running the script will delete your clipboard contents.
