import glob
import sys
#rotary sensor, potentiometer

import serial
def set_serial(b_rate=9600)
    temp_list = glob.glob ('/dev/tty[A-Za-z]*')
    for a_port in temp_list:
        try:
            s = serial.Serial(a_port,baudrate=b_rate)
            return s
        except serial.SerialException:
            pass
    print("No serial connection detected")
    sys.exit()

s=set_serial()
s.readline()


"""
import Rpi.GPIO as GPIO
#rpm_pin,lpin,rpin=(,,)
def set_pinIp(rpm_pin,lpin,rpin):
    GPIO.setup(rpm_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(lpin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(rpin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def get_pindata(rpm_pin,lpin,rpin):
    #print(GPIO.input(rpm_pin),GPIO.input(lpin),GPIO.input(rpin))
    
    vals=[]
    vals.append(GPIO.input(rpm_pin))
    if GPIO.input(lpin)==1:
       vals.append(-1)
    elif GPIO.input(rpin)==1:
       vals.append(1)
    else
       vals.append(0)
    return vals
"""
