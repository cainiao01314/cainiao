#!/usr/bin/python3
 
import threading
import time
import serial
from serial import Serial
import datetime
from time import sleep
import re
import linecache
import schedule

def send(topicone,topictwo,topicthree):                                     #每隔100毫秒发送一个topic信息    
    serialInput.write(topicone.encode('utf-8'))                             #utf-8 编码发送
    time.sleep(0.1)
    serialInput.write(topictwo.encode('utf-8'))  
    time.sleep(0.1)
    serialInput.write(topicthree.encode('utf-8'))  

if __name__ == '__main__':
    debug_comm = 'COM8'                                                     #输入串口号
    debug_baudrate = 115200                                                 #波特率

    topicone = "TEST_PUBLISH sys/thing/event/Error/post {'id':'123','version':'1.5','params':{'ErrorCode':1,}} QOS0 one"     #topic、内容、传输模式、次数
    topictwo = "TEST_PUBLISH sys/thing/service/property/set {'id':'456','version':'1.5','params':{'ErrorCode':1,}} QOS0 one"
    topicthree = "TEST_PUBLISH sys/thing/event/property/post_reply {'id':'789','version':'1.5','params':{'ErrorCode':1,}} QOS0 one"
      
    serialInput = serial.Serial(debug_comm, debug_baudrate, timeout=0.001)
    schedule.every(0.3).seconds.do(send,topicone,topictwo,topicthree)       #对send函数定时执行
    while True:
        schedule.run_pending()