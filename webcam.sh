echo "This will setup the webcam to take a picture once every 10 seconds" 
if [ $(id -u) -ne 0 ]; then echo "You must use sudo: sudo ./all.sh"; exit 1; fi
apt-get install fswebcam -y

cat > /lib/systemd/system/webcam.service <<EOF
#filename:  /lib/systemd/system/webcam.service
[Unit]
Description=Start Backdoor

[Service]
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/pi/.Xauthority
ExecStart=/bin/bash -c 'cd /var/www/html;fswebcam -r 640x480 -S 15 --flip h --jpeg 95 --save /var/www/html/webcam.jpg -q -l 1 > /var/www/html/fswebcam.log 2>&1'
Restart=never
KillMode=process
TimeoutSec=infinity

[Install]
WantedBy=graphical.target


EOF

chmod 644 /lib/systemd/system/webcam.service
systemctl daemon-reload
systemctl enable webcam.service

echo "On reboot the service should start see /var/www/html/fswebcam.log for details"

