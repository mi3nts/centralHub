# Main Module 
## For radiation module 
https://www.cooking-hacks.com/documentation/tutorials/geiger-counter-radiation-sensor-board-arduino-raspberry-pi-tutorial/index.html
# crontab 
```
## m h  dom mon dow   command
@reboot cd /home/teamlary/gitHubRepos/centralHub/firmware/xu4 && ./runAll.sh 
#@reboot cd /home/teamlary/gitHubRepos/Lakitha/v2DisplayMints/firmware/xu4 && ./runAll.sh
#* * * * * rsync -avzrtu -e "ssh -p 2222" /home/teamlary/mintsData/raw/ mints@mintsdata.utdallas.edu:raw
#*/2 * * * * cd /home/teamlary/gitHubRepos/Lakitha/centralHub/firmware/xu4 && python3 skyCamReaderWithSave.py
#2,4,6,8,12,14,16,18,22,24,26,28,32,34,36,38,42,44,46,48,52,54,56,58 * * * * cd /home/teamlary/gitHubRepos/Lakitha/CentralHub/firmware/xu4 && python3 skyCamReaderNoSave.py
*/5 * * * * cd /home/teamlary/gitHubRepos/centralHub/firmware/xu4 && python3 deleter.py
```
