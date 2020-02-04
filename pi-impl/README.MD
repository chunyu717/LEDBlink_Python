# make led blink.
$ pythoen led_blink.py

# Read IR signal. 
$ python ir_read.py

-----------------------------------
# command for lircd
sudo systemctl status lircd
sudo service lirc restart
sudo service lircd restart


# test if ir receiver is ok.
$ mode2 -d /dev/lirc1

# recored  ir signal to config
$ irrecord -d /dev/lirc1   #$irrecord -d /dev/lirc1 ~/lircd0228.conf
=> enter name : TV  

#after record it will gen tv.lircd.conf
#list available button 
$ irsend LIST ./tv.lircd.conf ""


#send ir single by config and key. 
$ irsend send_once ./ttv.lircd.conf KEY_POWER


sudo vim /etc/lircd.conf
sudo vim /etc/lirc/lirc_options.conf
 
 
 
 # issue 
/etc/lirc/lirc_options.conf
driver = default 
device = auto 