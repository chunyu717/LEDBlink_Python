#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO_ECHO = 24
print "IR Signal"
GPIO.setup(GPIO_ECHO,GPIO.IN)

start = 0
stop = 0 
while True: 
    start = time.time()
    duringDown=start-stop;
    while GPIO.input(GPIO_ECHO)==0:     #等待接腳變成高電位
        start = time.time()

    while GPIO.input(GPIO_ECHO)==1:     #等待接腳變成低電位
        stop = time.time()
    
    duringUp = stop - start             #計算接腳高電位的時間
    info = "Up:%7.f" % (duringUp *100000) + ",Down:%7.f" % (duringDown*100000)
    print info
    if duringUp>0.1:
        print("--------------------")

# 結束離開程式並還原 GPIO 的設定
GPIO.cleanup()
