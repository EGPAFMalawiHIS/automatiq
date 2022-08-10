#!/bin/bash
echo Enter IP address of the Facility:
read ip_address
echo Enter username of the Facility:
read username
echo Enter password of the facility
read -s password
rm -rf /var/www/BHT-EMR-API/log/development.log

echo starting to transfer files...

sshpass -p $password rsync -r --progress /var/www/BHT-EMR-API/ $username@$ip_address:/var/www/BHT-EMR-API
sshpass -p $password rsync -r --progress /var/www/automatiq/VersionsScripts/ $username@$ip_address:/var/www/

python3 /var/www/automatiq/Services/PushService.py 1 $ip_address $username $password