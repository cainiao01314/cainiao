#!/usr/bin/python3
 
import threading
import time
import serial
import datetime
from time import sleep
import re

def writelog():
   data = ''
   data2 = ''
   while True:
    data = serial.readline()
    ct = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(ct , ':' , data.decode('utf-8'))
   
    f = open('E:/sdklog/logprint.txt', 'a')                             #将串口输出到E盘指定txt文件，以追加的方式
    if data.decode('utf-8') != '' :                                     #剔除输出间隔导致的空字符，后续用缓存优化
        f.writelines(ct + ':' + data.decode('utf-8'))
    else :
        continue
    f.close()

    f1 = open('E:/sdklog/logprint.txt', "r", encoding='utf-8')           #打开test.txt文件，以只读得方式，注意编码格式，含中文
    data2 = f1.readlines()                                               #循环文本中得每一行，得到的是一个列表的格式<class 'list'>
    f1.close() 

    for line in data2:
     f2 = open("E:/sdklog/bug_log.txt", "a" ,encoding='utf-8') 
     if line.find("Panic...") != -1 :                                       #以panic为bug字符判断是否有异常，可以添加多个判断字段         
       f2.write(line + '\n')                                       
     else :
       continue
     f2.close() 
    f1.close()

if __name__ == '__main__':
 
 serial = serial.Serial('COM10', 921600, timeout=0.01)
 datacomplete = writelog()