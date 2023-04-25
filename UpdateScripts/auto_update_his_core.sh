#!/bin/bash
echo Enter IP address of the Facility:
read ip_address
echo Enter username of the Facility:
read username
echo Enter password of the Facility
read -s password
echo starting to transfer files...

sshpass -p $password rsync -rav --progress --exclude 'config.json' /var/www/HIS-Core/ $username@$ip_address:/var/www/HIS-Core

sshpass -p $password rsync -r --progress /var/www/automatiq/VersionsScripts/ $username@$ip_address:/var/www/

python3 /var/www/automatiq/Services/PushService.py 2 $ip_address $username $password