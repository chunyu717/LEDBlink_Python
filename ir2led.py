#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
KeyCurrent=range(100)
i=0                     #以下是遙控器實際的按鈕訊號
key2=[];
key4=[];
key6=[];
key8=[];

keys=[key2,key4,key6,key8];
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO_ECHO = 24
print "IR Signal"

def Funcheck(a,b,i) :   #判斷用戶按的按鈕是否為此4個按鈕
    if (a-b)>0.1:       #等待多久沒反影就算是遙控器訊號結束了
        i=0
    
    for j1 in range(len(keys)):
        isThisKey=True
        for j2 in range(5, len(keys[j1]-4)) :    #要扣掉最前面與最後面等待用戶按下按鈕的時間
            value=keys[j1][j2]
            currentValue=KeyCurrent[j2];
            rangeValue=100                       #注意 : 要依實際情況調整，越小越精準
            if( (currentValue-rangeValue)<value and
                (currentValue+rangeValue)>value )==False :
                isThisKey=False
                break
        if isThisKey==True:     # 判斷為按鈕後 做出對應的動作. 
            print "Get it key%d" % j1
            if j1==0:
                GPIO.output(21,True)
            elif j1==1:
                GPIO.output(21,False)
            elif j1==2:
                GPIO.output(22,True)
            elif j1==3:
                GPIO.output(22,False)
            i=0                                   #清除紀錄
            for j3 in range(len(KeyCurrent)):
                KeyCurrent[j3]=0

            return i

GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
start = 0
stop = 0 
while True: 
    start = time.time()
    duringDown=start-stop;

    while GPIO.input(GPIO_ECHO)==0:     #等待接腳變成高電位
        start = time.time()

    while GPIO.input(GPIO_ECHO)==1:     #等待接腳變成低電位
        stop = time.time()
        i=Funcheck(stop,start,i)
    
    duringUp = stop - start             #計算接腳高電位的時間
    KeyCurrent[i]=(duringUp *100000)
    i=i+1
    KeyCurrent[i]=(duringDown*100000)
    i=i+1
    i=Funcheck(stop,start,i)

# 結束離開程式並還原 GPIO 的設定
GPIO.cleanup()


            