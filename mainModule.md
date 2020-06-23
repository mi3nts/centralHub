# Main Module 
## For radiation module 
https://www.cooking-hacks.com/documentation/tutorials/geiger-counter-radiation-sensor-board-arduino-raspberry-pi-tutorial/index.html
# crontab 
```
## m h  dom mon dow   command
@reboot cd /home/teamlary/gitHubRepos/centralHub/firmware/xu4 && ./runAll.sh 
* * * * * rsync -avzrtu -e "ssh -p 2222" /home/teamlary/mintsData/raw/ mints@mintsdata.utdallas.edu:raw
*/5 * * * * cd /home/teamlary/gitHubRepos/centralHub/firmware/xu4 && python3 deleter.py
```
