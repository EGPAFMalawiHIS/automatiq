#!/bin/bash
echo Enter IP address of the Facility:
read ip_address
echo Enter username of the Facility:
read username
echo Enter password of the Facility
read password

sshpass -p $password rsync -r --progress /var/www/BHT-EMR-API/ $username@$ip_address:/var/www/HIS-Core