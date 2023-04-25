#!/bin/bash --login
echo "____________________________________________"
echo "Changing directory"
echo "____________________________________________"
cd /var/www/HIS-Core
echo "____________________________________________"
echo "Checkout to latest tag in Core"
echo "____________________________________________"
git checkout v1.8.2 -f
echo "____________________________________________"
echo "Describing Head"
echo "____________________________________________"
git describe > HEAD
echo "____________________________________________"
echo "Copying config.json.example to config.json"
echo "____________________________________________"
cp config.json.example config.json
echo "____________________________________________"
echo "Configuring IP address and Port in config.json"
echo "____________________________________________"
sed -i 's/0.0.0.0/'$1'/g' config.json
sed -i 's/3000/'$2'/g' config.json
clear
echo "The following parameters have been ammended in config.json"
echo IP address : $1
echo API port   : $2
echo THANK YOU

