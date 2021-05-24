@echo off

C: && cd /
cd "C:\Program Files (x86)\Google\Chrome\Application" 
chrome.exe --remote-debugging-port=9224 --user-data-dir="C:/Chrome_debug_temp"

exit: