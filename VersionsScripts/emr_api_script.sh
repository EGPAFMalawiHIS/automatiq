#!/bin/bash
echo "____________________________________________"
echo "Entering BHT-EMR-API"
echo "____________________________________________"
cd /var/www/BHT-EMR-API
echo "____________________________________________"
echo "Checkout to latest tag"
echo "____________________________________________"
git checkout v4.15.18 -f
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
echo THANK YOU

