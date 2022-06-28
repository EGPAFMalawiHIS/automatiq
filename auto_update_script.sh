#!/bin/bash
echo "____________________________________________"
echo "Entering BHT-EMR-API"
echo "____________________________________________"
cd BHT-EMR-API
echo "____________________________________________"
echo "Checkout to latest tag"
echo "____________________________________________"
git checkout v4.15.15 -f
echo "____________________________________________"
echo "Describing Head"
echo "____________________________________________"
git describe > HEAD
echo "____________________________________________"
echo "Removing Gemfile.lock"
echo "____________________________________________"
rm Gemfile.lock
echo "____________________________________________"
echo "Installing Local Gems"
echo "____________________________________________"
bundle install --local
echo "____________________________________________"
echo "running bin_update art"
echo "____________________________________________"
./bin/update_art_metadata.sh development
echo "____________________________________________"
echo "Changing directory"
echo "____________________________________________"
cd ../HIS-Core
echo "____________________________________________"
echo "Checkout to latest tag in Core"
echo "____________________________________________"
git checkout v1.2.7 -f
echo "____________________________________________"
echo "Describing Head"
echo "____________________________________________"
git describe > HEAD
echo "____________________________________________"
echo "Copying config.json.example to config.json"
echo "____________________________________________"
cp config.json.example config.json
echo "____________________________________________"
echo "Coonfiguring IP address and Port in config.json"
echo "____________________________________________"
clear
echo "____________________________________________"
echo Enter IP address of the Facility:
read ip_address
echo "____________________________________________"
echo Enter API port the facility uses:
read api_port
echo "____________________________________________"
sed -i 's/0.0.0.0/'$ip_address'/g' config.json
sed -i 's/3000/'$api_port'/g' config.json
clear
echo "The following parameters have been ammended in config.json"
echo IP address : $ip_address
echo API port   : $api_port
echo THANK YOU

