#!/usr/bin/env python
#-*-coding:utf-8-*-
#This program shows messages on a 16x2 LCD Plug&Play custom board.
#Created by Iker García.

import Adafruit_CharLCD as LCD 
import socket 
import os 
import time

lcd_rs = 18 #GPIO pins are defined. These can't be changed if the design of the board is not changed. 
lcd_en = 23 
lcd_d4 = 12 
lcd_d5 = 16 
lcd_d6 = 20 
lcd_d7 = 21 
lcd_backlight = 4

lcd_columns = 16 #Size of the LCD is defined. 
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                           lcd_d6, lcd_d7, lcd_columns, lcd_rows,
                           lcd_backlight)

lcd.message("Plug&Play\n") #Writes the first row.
lcd.message("works") #Writes the second row.
time.sleep(10.0) #Message is available for 10 seconds.
lcd.clear() #LCD is cleared.

