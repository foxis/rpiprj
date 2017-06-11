sudo apt-get update
sudo apt-get upgrade
sudo apt-get install bluez pulseaudio-module-bluetooth python-gobject python-gobject-2 bluez-tools
sudo apt-get install omxplayer
sudo usermod -a -G Ip pi
sudo usermod -a -G lp pi
sudo hciconfig -a hci0
sudo vi /etc/bluetooth/main.conf 
sudo vi /etc/bluetooth/input.conf 
sudo vi /etc/bluetooth/audio.conf 
sudo vi /etc/bluetooth/main.conf 
sudo /etc/init.d/bluetooth restart
sudo hciconfig -a hci0
sudo ls /var/lib/bluetooth/
sudo ls /var/lib/bluetooth/B8:27:EB:41:94:20
sudo vi /var/lib/bluetooth/B8:27:EB:41:94:20/settings
sudo hciconfig -a hci0 restart
sudo hciconfig -a hci0 reset
sudo hciconfig -a hci0
sudo hciconfig -a hci0 class 0x20041C
sudo hciconfig -a hci0
sudo hciconfig -a hci0 name BluesPie
sudo hciconfig -a hci0
sudo vi /etc/udev/rules.d/99-input.rules
sudo ls -la /etc/udev/rules.d/
sudo vi /etc/udev/rules.d/99-com.rules 
sudo mkdir /usr/lib/udev
sudo vi /usr/lib/udev/bluetooth
sudo chmod 774 /usr/lib/udev/bluetooth
pactl list sources short
sudo vi /usr/lib/udev/bluetooth
sudo apt-get install pi-bluetooth
sudo apt-get install bluez
sudo apt-get install bluez-firmware
sudo usermod -G bluetooth -a pi
sudo sh -c "echo 'extra-arguments = --exit-idle-time=-1 --log-target=syslog' >> /etc/pulse/client.conf"
sudo hciconfig hci0 up
sudo hciconfig hci0 class 0x200420
sudo reboot
1
2
3
4
sudo hciconfig hci0
sudo hciconfig -a hci0
sudo vi /var/lib/bluetooth/B8:27:EB:41:94:20/settings
sudo vi /etc/dbus-1/system.d/bluetooth.conf 
sudo vi /etc/bluetooth/main.conf 
sudo vi /etc/bluetooth/audio.conf 
sudo /etc/init.d/bluetooth restart
sudo hciconfig -a hci0
sudo service bluetooth restart
sudo service bluetooth 
sudo service bluetooth force-reload
sudo service bluetooth status
sudo vi /etc/systemd/system/bluetooth.target.wants/bluetooth.service 
sudo systemctl daemon-reload
sudo service bluetooth status
sudo service bluetooth restart
sudo service bluetooth status
sudo hciconfig -a hci0
hciconfig -a hci0
hciconfig -a hci0 class
hciconfig -a hci0 up
sudo hciconfig -a hci0 up
hciconfig -a hci0 
sudo hciconfig -a hci0 reset
hciconfig -a hci0 
hciconfig -a hci0 down
sudo hciconfig -a hci0 down
sudo hciconfig -a hci0 reset
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 down
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 reset
sudo hciconfig -a hci0 
cd /usr/local/etc/
ls
sudo ln -s /etc/bluetooth bluetooth
sudo systemctl daemon-reload
sudo systemctl bluetooth.service
sudo systemctl restart bluetooth.service
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 reset
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 down
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0 
man bluetoothd
ls
ls -l
less bluetooth
ls
sudo systemctl status bluetooth.service
sudo vi /etc/bluetooth/main.conf 
sudo systemctl restart bluetooth.service
sudo systemctl status bluetooth.service
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0 
sudo reboot
sudo hciconfig -a hci0 
sudo vi /var/lib/bluetooth/B8:27:EB:41:94:20/settings
sudo rm -rf /var/lib/bluetooth/B8:27:EB:41:94:20
sudo systemctl restart bluetooth.service
sudo systemctl status bluetooth.service
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0 name BluesPie
sudo hciconfig -a hci0 class 0x20041C
sudo systemctl status bluetooth.service
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 piscan
sudo hciconfig -a hci0 down
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 class 0x20041C
sudo hciconfig -a hci0 
sudo vi /etc/udev/rules.d/99-com.rules 
sudo vi /etc/udev/rules.d/10-local.rules
sudo reboot
sudo hciconfig -a hci0 
dmesg | less
less /var/log/boot.log 
less /var/log/messages 
less /var/log/syslog 
less /var/log/bluetooth_dev 
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 reset
sudo hciconfig -a hci0
sudo vi /etc/bluetooth/main.conf 
sudo systemctl status bluetooth.service
sudo systemctl restart bluetooth.service
sudo systemctl status bluetooth.service
sudo vi /etc/bluetooth/main.conf 
sudo systemctl restart bluetooth.service
sudo systemctl status bluetooth.service
sudo hciconfig -a hci0
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0
pulseaudio --check -v
sudo vi /etc/bluetooth/audio.conf 
sudo systemctl restart bluetooth.service
sudo systemctl status bluetooth.service
sudo hciconfig -a hci0
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0
sudo ls /var/lib/bluetooth/
sudo ls /var/lib/bluetooth/B8:27:EB:41:94:20
sudo less /var/lib/bluetooth/B8:27:EB:41:94:20/settings
sudo vi /var/lib/bluetooth/B8:27:EB:41:94:20/settings
sudo systemctl restart bluetooth.service
sudo systemctl status bluetooth.service
sudo hciconfig -a hci0
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0
sudo hciconfig -a hci0 reset
sudo hciconfig -a hci0
raspi-config
sudo raspi-config
sudo hciconfig -a hci0
sudo vi /var/lib/bluetooth/B8:27:EB:41:94:20/settings
sudo vi /etc/bluetooth/main.conf 
sudo systemctl restart bluetooth.service
sudo systemctl status bluetooth.service
sudo vi /etc/bluetooth/main.conf 
sudo systemctl restart bluetooth.service
sudo systemctl status bluetooth.service
sudo hciconfig -a hci0
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0
sudo hciconfig -a hci0 reset
sudo hciconfig -a hci0
sudo systemctl force-reload bluetooth.service
sudo hciconfig -a hci0
sudo locate main.conf
whereis 
sudo whereis main.conf
sudo whereis "main.conf"
sudo whereis "bluetooth/main.conf"
sudo find / -name "bluetooth/main.conf"
sudo find / -name "main.conf"
sudo find / -name "bluetooth"
sudo less /sys/module/bluetooth
sudo ls /sys/module/bluetooth
sudo ls /sys/module/bluetooth/initstate
sudo less /sys/module/bluetooth/initstate
ls /var/lib/bluetooth/
sudo ls /var/lib/bluetooth/
sudo ls /var/lib/bluetooth/B8:27:EB:41:94:20
sudo vi /var/lib/bluetooth/B8:27:EB:41:94:20/settings
sudo systemctl force-reload bluetooth.service
sudo hciconfig -a hci0
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0
sudo hciconfig -a hci0 reset
sudo hciconfig -a hci0
sudo vi /etc/bluetooth/audio.conf 
sudo service bluetooth restart
sudo service bluetooth status
sudo hciconfig -a hci0
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0
sudo adduser root pulse-access
sudo adduser squeezeboxserver pulse-access
sudo vi /etc/dbus-1/system.d/pulseaudio-bluetooth.conf
sudo vi /etc/pulse/system.pa 
sudo vi /etc/systemd/system/pulseaudio.service
sudo systemctl daemon-reload
sudo systemctl enable pulseaudio.service
sudo systemctl restart bluetooth
sudo systemctl status bluetooth
sudo systemctl start pulseaudio.service
sudo systemctl status pulseaudio.service
sudo vi /etc/bluetooth/audio.conf 
sudo systemctl force-reload bluetooth
sudo systemctl status bluetooth
sudo hciconfig -a hci0
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0
sudo hciconfig -a hci0 piscan
sudo systemctl status bluetooth
sudo vi /etc/bluetooth/audio.conf 
sudo systemctl status bluetooth
sudo raspi-config
sudo systemctl status bluetooth
sudo hciconfig -a hci0
sudo vi /etc/bluetooth/audio.conf 
sudo systemctl restart bluetooth
sudo systemctl status bluetooth
sudo hciconfig -a hci0
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0
sudo systemctl status bluetooth
sudo vi /etc/dbus-1/system.d/bluetooth.conf 
sudo systemctl status bluetooth
sudo vi /etc/dbus-1/system.d/bluetooth.conf 
pulseaudio -D
sudo systemctl status bluetooth
sudo systemctl restart bluetooth
sudo systemctl status bluetooth
sudo hciconfig -a hci0
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0
sudo systemctl status bluetooth
sudo usermod -a -G lp pi
sudo vi /etc/pulse/daemon.conf 
pactl list short
sudo vi /etc/init.d/bluetooth 
sudo vi /etc/init.d/bluetooth-agent 
echo $BT_USER
sudo raspi-config
sudo chmod +x /etc/init.d/bluetooth-agent 
sudo rm /etc/udev/rules.d/10-local.rules 
sudo vi /etc/udev/rules.d/99-input.rules 
sudo mv /etc/init.d/bluetooth-agent /usr/lib/udev/bluetooth
pactl list sinks short
pactl list sources short
cat /proc/asound/modules 
sudo vi /etc/modprobe.d/alsa-base.conf
sudo reboot
tail -f /var/log/a2dp-autoconnect 
sudo watch systemctl status bluetooth
bluetoothctl
ls -l /var/run/pulse/
pactl list sources short
sudo pactl list sources short
sudo systemctl status bluetooth
less /var/log/a2dp-autoconnect 
sudo systemctl status bluetooth
sudo hciconfig -a hci0
sudo hciconfig -a hci0 class 0x2041c
sudo hciconfig -a hci0
sudo hciconfig -a hci0 class 0x20041c
sudo vi /usr/lib/udev/bluetooth
sudo hciconfig -a hci0 down
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0 reset
sudo hciconfig -a hci0 
sudo systemctl restart bluetooth
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0 
sudo systemctl status bluetooth
sudo vi /etc/init.d/bluetooth-agent
sudo chmod +x /etc/init.d/bluetooth-agent
sudo update-rc.d bluetooth-agent defaults
sudo systemctl start bluetooth-agent
sudo systemctl status bluetooth-agent
sudo systemctl status bluetooth
sudo systemctl status bluetooth-agent
sudo vi /etc/init.d/bluetooth
sudo vi /etc/init.d/bluetooth-agent 
sudo systemctl start bluetooth-agent
sudo systemctl daemon-reload
sudo systemctl start bluetooth-agent
sudo systemctl stop bluetooth-agent
sudo systemctl status bluetooth-agent
whereis bluetooth-agent
find / -name bluetooth-agent
man bluetoothctl 
sudo apt-get install bluez-utils
sudo apt-get install bluez
sudo vi /etc/bluetooth/main.conf 
sudo systemctl force-reload bluetooth
sudo systemctl status bluetooth
sudo hciconfig -a hci0 
sudo hciconfig -a hci0 up
sudo hciconfig -a hci0 
sudo bluetoothctl 
pactl show list sinks
pactl list sinks
sudo pactl list sinks
sudo pactl list sinks short
sudo pactl list sources short
sudo vi /usr/lib/udev/bluetooth 
pactl
pactl list
pulseaudio -D
pulseaudio
pactl
pactl list sources short
ls /etc/init.d
less /etc/init.d/alsa-utils 
sudo vi /etc/init.d/pulseaudio
sudo update-rc.d pulseaudio defaults
sudo chmod +x /etc/init.d/pulseaudio 
sudo update-rc.d pulseaudio defaults
pulseaudio --help
pulseaudio -k
sudo systemctl status pulseaudio
sudo systemctl start pulseaudio
sudo systemctl status pulseaudio
pactl list sinks short
sudo vi /etc/init.d/bluetooth-agent 
sudo systemctl start pulseaudio
sudo vi /etc/init.d/pulseaudio
sudo systemctl restart pulseaudio
sudo systemctl status pulseaudio
sudo vi /etc/init.d/pulseaudio
sudo systemctl restart pulseaudio
sudo systemctl status pulseaudio
sudo systemctl stop pulseaudio
sudo systemctl status pulseaudio
sudo systemctl start pulseaudio
sudo systemctl status pulseaudio
sudo systemctl stop pulseaudio
sudo systemctl daemon-reload
sudo systemctl stop pulseaudio
sudo systemctl status pulseaudio
sudo systemctl start pulseaudio
sudo systemctl status pulseaudio
sudo systemctl stop pulseaudio
sudo vi /etc/init.d/pulseaudio
sudo systemctl start pulseaudio
sudo systemctl status pulseaudio
pactl list
ls -l /var/run
ls -l /var/run/

sudo vi /etc/init.d/pulseaudio
sudo systemctl daemon-reload
sudo /etc/init.d/pulseaudio
sudo /etc/init.d/pulseaudio start
sudo /etc/init.d/pulseaudio status
pactl
pactl list
sudo usermod -a -G pulseaudio pi
sudo usermod -a -G pulse pi
pactl list
sudo usermod -a -G lp pi
pactl list
sudo /etc/init.d/pulseaudio sttop
sudo /etc/init.d/pulseaudio stop
sudo vi btctl
sudo chmod +x btctl
sudo apt-get install expect
man expect
sudo vi btctl
pulseaudio -D
ls /usr/lib/udev/bluetooth 
less /usr/lib/udev/bluetooth 
sudo vi /etc/init.d/bluetooth-agent 
sudo vi btctl 
sudo vi /etc/init.d/bluetooth-agent 
pulseaudio -D
sudo vi /usr/lib/udev/bluetooth 
pulseaudio
ls /var/run/pulse/
ls /var/run/pulse/.config/pulse/
ls -r /var/run/pulse/
ls -ra /var/run/pulse/
ls -Ra /var/run/pulse/
ps -aux | grep pulse
sudo kill 5869
sudo systemctl start pulseaudio
sudo systemctl status pulseaudio
ps -aux | grep pulse
tail -f /var/log/a2dp-autoconnect 
sudo ./btctl 
ps -aux
ps -aux |bluetooth
ps -aux |grep bluetooth
sudo ./btctl 
sudo systemctl daemon-reload
sudo systemctl start bluetooth-agent
ps -aux |grep bluetooth
sudo systemctl stop bluetooth-agent
ps -aux |grep bluetooth
sudo kill 6373
sudo kill 6337
sudo kill 6380
ps -aux |grep bluetooth
sudo systemctl start bluetooth-agent
sudo systemctl daemon-reload
sudo systemctl start bluetooth-agent
sudo systemctl status bluetooth-agent
sudo reboot
sudo omxplayer high_hopes.mp3 
sudo omxplayer -o alsa high_hopes.mp3 
sudo vi /usr/lib/udev/bluetooth 
sudo vi player 
sudo vi /usr/lib/udev/bluetooth 
ls
omxplay -o alsa californication.mp3 
omxplayer -o alsa californication.mp3 
sudo omxplayer -o alsa californication.mp3 
du -h
du -h /
df -h
ls *.mp3
ls *.mp3 | sort -R
sudo pactl list sources short
sudo pactl 
sudo pactl list | grep -A16 ‘Sink Input’
sudo pactl list | grep -A16 'Sink Input'
sudo pactl set-sink-input-mute 1795 1
sudo pactl set-sink-input-mute 1795 0
sudo pactl set-sink-input-mute 1795 1
sudo pactl linst input
sudo pactl list inputs
sudo pactl list sink-inputs
sudo pactl list sink-inputs short
sudo pactl list sink-inputs short | grep protocol-native
awk
help awk
man awk
sudo pactl list sink-inputs short | grep protocol-native | awk -v RS=[0-9]+ '{print RT+0;exit}'
sudo pactl list sink-inputs short | grep protocol-native | awk -v RS=\d+ '{print RT+0;exit}'
sudo pactl list sink-inputs short | grep protocol-native | awk -v RS=^\d+ '{print RT+0;exit}'
sudo pactl list sink-inputs short | grep protocol-native | awk -v RS=^\d+ '{print RT;exit}'
sudo pactl list sink-inputs short | grep protocol-native | awk -v RS=\d+ '{print RT;exit}'
sudo pactl list sink-inputs short | grep protocol-native | awk -v RS=^\d+ '{print RT;exit}'
sudo pactl list sink-inputs short | grep protocol-native | awk '{print $1;}'
sudo pactl set-sink-input-mute 1795 0
sudo pactl list sink-inputs short | grep protocol-native | awk '{print $1;}'
sudo pactl set-sink-input-mute 1881 0
sudo vi /etc/bluetooth/main.conf 
sudo vi /etc/bluetooth/audio.conf 
sudo vi /etc/default/bluetooth 
sudo vi /etc/bluetooth/main.conf 
for i in {1..5}; do echo $i; done
for i in {5..1}; do echo $i; done
for i in {5 .. 1}; do echo $i; done
for i in {5..1}; do echo $i; done
man {
man for
$(seq 1 2 20)
seq 1 2 20
sudo hciconfig hci0 up
sudo hciconfig -a hci0
sudo reboot
sudo vi /usr/lib/udev/bluetooth 
man seq
seq 0 100
seq 0 3 100
seq 100 3 0
seq 100 -3 0
seq 100 0
seq 100 -3 0
sudo vi /usr/lib/udev/bluetooth 
sudo vi shutdown-pin
sudo chmod +x shutdown-pin 
ls
sudo vi player 
sudo mkdir /boot/audio
sudo mv *.mp3 /boot/audio
ls 
ls /boot/audio
sudo reboot
sudo vi /etc/bluetooth/main.conf 
sudo hciconfig hci0 -a
sudo hciconfig hci0 up
sudo hciconfig hci0 piscan
sudo vi /etc/init.d/bluetooth-agent 
sudo reboot
sudo hciconfig hci0 -a
sudo vi /etc/bluetooth/audio.conf 
sudo vi /etc/bluetooth/main.conf 
bluetoothctl
sudo vi btctl 
sudo hciconfig hci0 -a
sudo hciconfig hci0 up
sudo reboot
sudo systemctl status pulseaudio
sudo systemctl status bluetooth
sudo systemctl status bluetooth-agent
sudo systemctl status player-agent
sudo systemctl status bluetooth-agent
dmesg | grep bluetooth
dmesg | grep luetooth
sudo vi /etc/init.d/bluetooth-agent 
sudo vi /etc/init.d/player-agent 
sudo vi /etc/init.d/bluetooth-agent 
sudo systemctl reload-deamon
sudo systemctl daemon-reload
sudo systemctl stop bluetooth-agent
sudo systemctl start bluetooth-agent
sudo reboot
sudo systemctl status bluetooth-agent
sudo vi btctl 
sudo systemctl status bluetooth-agent
sudo systemctl stop bluetooth-agent
ps -aux | grep blue
sudo kill 3516
ps -aux | grep blue
sudo vi btctl 
sudo kill 3100
sudo kill 2560
ps -aux | grep blue
sudo kill -9 2560
sudo kill -9 3100

sudo btctl
sudo ./btctl
sudo bluetoothctl
sudo vi btctl
sudo reboot
sudo systemctl status bluetooth-agent
sudo vi btctl
sudo reboot
sudo systemctl status bluetooth-agent
sudo watch systemctl status bluetooth-agent
sudo hciconfig hci0 sspmode 0
sudo watch systemctl status bluetooth-agent
sudo bluetoothctl 
sudo vi btctl 
sudo reboot
sudo vi btctl 
sudo bluetoothctl
man bluetoothctl 
sudo vi btctl 
sudo reboot
sudo vi /etc/init.d/player-agent 
sudo vi /etc/init.d/bluetooth
sudo vi /etc/init.d/bluetooth-agent 
sudo vi btctl 
sudo vi /usr/lib/udev/bluetooth 
sudo vi /etc/init.d/bluetooth-agent 
sudo reboot
sudo vi /usr/lib/bluetooth/
sudo vi /usr/lib/udev/bluetooth 
sudo vi /etc/init.d/bluetooth-agent 
sudo reboot
ls
mv rpi_peak_monitor.py pmon.py
ln
ln --help
ln /boot/audio audio
ln -s /boot/audio audio
ls audio
pwd
vi player 
sudo vi player 
vi hardware.py
sudo apt-get install vim
ls
vi pmon
vim hardware.py 
sudo apt-get remove vim-tiny
vi 
sudo vi /etc/vim/
vi .vimrc
vi hardware.py 
python
vi hardware.py 
sudo vi player 
vi hardware.py 
chmod +x hardware.py 
less btctl 
locate python
where python
whereis python
vi hardware.py 
./hardware.py 
vi hardware.py 
./hardware.py 
vi hardware.py 
./hardware.py 
sudo apt-get python-pulse*
sudo apt-get install python-pulse*
vi lib_pulseaudio.py
ps -a
kill 15903
sudo ./hardware.py 
ls
ls -l
vi pmon.py
./hardware.py 
vi hardware.py 
sudo apt-get install libpulse
sudo apt-get install libpulseaudio
sudo apt-get install pulseaudio
sudo apt-get install pulseaudio-dev
sudo apt-get install pulse-dev
ls
vi libpulseaudio.py
whereis libpulse.so
ls /usr/lib | grep pulse
vi libpulseaudio.py
ls /lib | grep pulse
ldd
ldd omxplayer
ldd `whereis omxplayer`
aplay
ldd `whereis aplay`
ls /lib/arm-linux-gnueabihf/ | grep pulse
ls /usr/lib/arm-linux-gnueabihf/ | grep pulse
ls /usr/lib/arm-linux-gnueabihf/ | grep pulse | ldd
ls
./hardware.py 
vi hardware.py 
./hardware.py 
vi hardware.py 
./hardware.py 
vi hardware.py 
./hardware.py 
vi hardware.py 
./hardware.py 
sudo ./hardware.py 
vi hardware.py 
sudo vi btctl 
vi hardware.py 
sudo ./hardware.py 
sudo systemctl status player-agent
sudo systemctl status bluetooth-agent
sudo systemctl status bluetooth
sudo ./hardware.py 
vi hardware.py 
sudo ./hardware.py 
vi hardware.py 
sudo ./hardware.py 
sudo echo '17' > /sys/class/gpio/export
sudo echo 'out' > /sys/class/gpio/direction
sudo echo 'out' > /sys/class/gpio/gpio17/direction
sudo echo '1' > /sys/class/gpio/gpio17/value
sudo echo '18' > /sys/class/gpio/export
sudo echo 'out' > /sys/class/gpio/gpio18/direction
sudo echo '1' > /sys/class/gpio/gpio18/value
sudo echo '15' > /sys/class/gpio/export
sudo echo 'out' > /sys/class/gpio/gpio15/direction
sudo echo '1' > /sys/class/gpio/gpio15/value
sudo echo '0' > /sys/class/gpio/gpio15/value
help if
ls /etc/init.d/
sudo cp /etc/init.d/player-agent /etc/init.d/hardware-agent
sudo vi /etc/init.d/hardware-agent 
sudo reboot
less .bash_history 
sudo systemctl enable hardware-agent
sudo systemctl start hardware-agent
less /var/log/a2dp-autoconnect 
sudo cat /sys/class/gpio/gpio18/value
sudo cat /sys/class/gpio/gpio15/value
less /usr/lib/udev/bluetooth 
sudo vi /usr/lib/udev/bluetooth 
sudo vi hardware.py 
sudo systemctl restart hardware-agent
sudo vi /usr/lib/udev/bluetooth 
sudo systemctl restart hardware-agent
sudo vi /usr/lib/udev/bluetooth 
sudo systemctl restart hardware-agent
sudo vi /usr/lib/udev/bluetooth 
sudo vi hardware.py 
sudo systemctl restart hardware-agent
sudo vi hardware.py 
sudo reboot
sudo systemctl status hardware-agent
sudo systemctl restart hardware-agent
sudo systemctl status hardware-agent
sudo vi hardware.py 
sudo systemctl restart hardware-agent
sudo systemctl status hardware-agent
sudo vi hardware.py 
sudo systemctl restart hardware-agent
sudo vi hardware.py 
sudo systemctl status hardware-agent
sudo vi hardware.py 
sudo reboot
sudo vi /usr/lib/udev/bluetooth 
sudo pactl list sink-inputs short
sudo vi /usr/lib/udev/bluetooth 
exit
