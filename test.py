#!/usr/bin/python3

from __future__ import print_function
import sys
import time
import datetime
import apsw
import RPi.GPIO as GPIO

py3=sys.version_info >= (3, 0)
def inext(v):  # next value from iterator
    return next(v) if py3 else v.next()

gpio1_counter = 0
gpio2_counter = 0
gpio3_counter = 0 
gpio4_counter = 0 
gpio5_counter = 0
gpio6_counter = 0
gpio7_counter = 0
gpio8_counter = 0

def incr1(channel):
    global gpio1_counter
    gpio1_counter += 1

def incr2(channel):
    global gpio2_counter
    gpio2_counter += 1

def incr3(channel):
    global gpio3_counter
    gpio3_counter += 1

def incr4(channel):
    global gpio4_counter
    gpio4_counter += 1

def incr5(channel):
    global gpio5_counter
    gpio5_counter += 1

def incr6(channel):
    global gpio6_counter
    gpio6_counter += 1

def incr7(channel):
    global gpio7_counter
    gpio7_counter += 1

def incr8(channel):
    global gpio8_counter
    gpio8_counter += 1

def main():

    global gpio1_counter
    global gpio2_counter
    global gpio3_counter 
    global gpio4_counter
    global gpio5_counter
    global gpio6_counter
    global gpio7_counter
    global gpio8_counter

    print("      Using APSW file",apsw.__file__)                # from the extension module
    print("         APSW version",apsw.apswversion())           # from the extension module
    print("   SQLite lib version",apsw.sqlitelibversion())      # from the sqlite library code
    print("SQLite header version",apsw.SQLITE_VERSION_NUMBER)   # from the sqlite header file at compile time

    gpio1_number = 3
    #gpio2_number = 
    #gpio3_number = 
    #gpio4_number = 
    #gpio5_number = 
    #gpio6_number = 
    #gpio7_number = 
    #gpio8_number = 

    gpio1_counter = 0
    gpio2_counter = 0
    gpio3_counter = 0 
    gpio4_counter = 0 
    gpio5_counter = 0
    gpio6_counter = 0
    gpio7_counter = 0
    gpio8_counter = 0

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(gpio1_number, GPIO.IN)
    #GPIO.setup(gpio2_number, GPIO.IN)
    #GPIO.setup(gpio3_number, GPIO.IN)
    #GPIO.setup(gpio4_number, GPIO.IN)
    #GPIO.setup(gpio5_number, GPIO.IN)
    #GPIO.setup(gpio6_number, GPIO.IN)
    #GPIO.setup(gpio7_number, GPIO.IN)
    #GPIO.setup(gpio8_number, GPIO.IN)

    GPIO.add_event_detect(gpio1_number, GPIO.RISING, callback=incr1)

    connection=apsw.Connection("sqlite.db")
    cursor=connection.cursor()  

    cursor.execute("CREATE TABLE IF NOT EXISTS gpio1(datetime TEXT, impulses INTEGER)")
    #cursor.execute("CREATE TABLE IF NOT EXISTS gpio2(datetime TEXT, impulses INTEGER)")
    #cursor.execute("CREATE TABLE IF NOT EXISTS gpio3(datetime TEXT, impulses INTEGER)")
    #cursor.execute("CREATE TABLE IF NOT EXISTS gpio4(datetime TEXT, impulses INTEGER)")
    #cursor.execute("CREATE TABLE IF NOT EXISTS gpio5(datetime TEXT, impulses INTEGER)")
    #cursor.execute("CREATE TABLE IF NOT EXISTS gpio6(datetime TEXT, impulses INTEGER)")
    #cursor.execute("CREATE TABLE IF NOT EXISTS gpio7(datetime TEXT, impulses INTEGER)")
    #cursor.execute("CREATE TABLE IF NOT EXISTS gpio8(datetime TEXT, impulses INTEGER)")

    while True:
        time.sleep(60)

        print("GPIO1 Counter is {0}".format(gpio1_number))
        #print "GPIO2 Counter is {0}".format(gpio2_number)
        #print "GPIO3 Counter is {0}".format(gpio3_number)
        #print "GPIO4 Counter is {0}".format(gpio4_number)
        #print "GPIO5 Counter is {0}".format(gpio5_number)
        #print "GPIO6 Counter is {0}".format(gpio6_number)
        #print "GPIO7 Counter is {0}".format(gpio7_number)
        #print "GPIO8 Counter is {0}".format(gpio8_number)

        cursor.execute("INSERT INTO gpio1 VALUES(?,?)", (str(datetime.datetime.now), gpio1_counter))
        gpio1_counter = 0
        gpio2_counter = 0
        gpio3_counter = 0
        gpio4_counter = 0
        gpio5_counter = 0
        gpio6_counter = 0
        gpio7_counter = 0
        gpio8_counter = 0

if __name__=="__main__": 
    main()

