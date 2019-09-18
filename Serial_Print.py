#!/usr/bin/python3
 
import threading
import time
import serial
from serial import Serial
import datetime
from time import sleep
import re
import linecache

def writelog():
  data = ''
  data2 = ''
  logpath = 'E:/sdklog/logprint.txt'                                    #将串口输出到E盘指定txt文件，以追加的方式
  logbugpath = 'E:/sdklog/bug_log.txt'                                  #获取bug的log路径
  bug1 = "Panic..."                                                     #配置查询点
  bug2 = "offline"
  while True:
    data = serialOuput.readline()
    ct = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) #获取当前时间，精确到毫秒级
    data_secs = (time.time() - int(time.time())) * 1000
    time_stamp = "%s.%03d" % (ct, data_secs)
    print(time_stamp , ':' , data.decode('utf-8'))
   
    f = open(logpath, 'a')                             
    if data.decode('utf-8') != '' :                                     #剔除输出间隔导致的空字符，后续用缓存优化
      f.writelines(time_stamp + ':' + data.decode('utf-8'))
    else :
      continue
    f.close()

    f1 = open(logpath, "r", encoding='utf-8')                           #打开test.txt文件，以只读得方式，注意编码格式，含中文
    data2 = f1.readlines()                                              #循环文本中得每一行，得到的是一个列表的格式<class 'list'>
    f1.close() 

    for line in data2:
      f2 = open(logbugpath, "a" ,encoding='utf-8') 
      if line.find(bug1) != -1 | line.find(bug2) != -1 :                #查询点判断，可以添加多个判断字段       
        f2.write(line + '\n')       
      else :
        continue
      f2.close() 
    f1.close()

if __name__ == '__main__':
  log_comm = 'COM10'                                                     #输出串口号
  log_baudrate = 921600                                                  #波特率
 
  serialOuput = serial.Serial(log_comm, log_baudrate, timeout=0.001)
  datacomplete = writelog()
