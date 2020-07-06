echo "Run all scripts to configure the pi"
echo "Note: .img used for this should already have a wifi access point setup"
if [ $(id -u) -ne 0 ]; then echo "You must use sudo: sudo ./all.sh"; exit 1; fi
apt-get update
./ap.sh
./keyboard.sh
./ssd.sh
#./service.sh
