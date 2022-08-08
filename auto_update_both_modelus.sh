#!/bin/bash
echo Enter IP address of the Facility:
read ip_address
echo Enter username of the Facility:
read username
echo Enter password of the Facility
read password
cd /var/www/BHT-EMR-API
rm -rf log/development.log

sshpass -p $password rsync -r --progress /var/www/BHT-EMR-API/ $username@$ip_address:/var/www/BHT-EMR-API
sshpass -p $password rsync -r --progress /var/www/BHT-EMR-API/ $username@$ip_address:/var/www/HIS-Core