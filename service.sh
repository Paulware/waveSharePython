if [ "$EUID" -ne 0 ]
	then echo "Must be root"
	exit
fi

file_exists() {
   if [ -e $1 ]
   then
       # file found 
       return 0
   else
       return 1
   fi
}

# return true if line exists
line_exists_in () {
   if grep -Fxq "$2" $1
   then
      return 0
   else
      return 1
   fi
}


cat > /lib/systemd/system/backdoor.service <<EOF
#filename:  /lib/systemd/system/backdoor.service
[Unit]
Description=Start Backdoor

[Service]
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/pi/.Xauthority
ExecStart=/bin/bash -c 'cd /boot;/usr/bin/python2.7 menuGrid.py > /boot/menuGrid.log 2>&1'
Restart=never
#RestartSec=10s
KillMode=process
TimeoutSec=infinity

[Install]
WantedBy=graphical.target


EOF

chmod 644 /lib/systemd/system/backdoor.service
systemctl daemon-reload
systemctl enable backdoor.service

echo "On reboot the service should start see /share/WOD/sshBackdoor.log for details"

