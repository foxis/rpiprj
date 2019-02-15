#!/usr/bin/python


import sqlite3
import sys
import termios
import os
from datetime import datetime
import RPi.GPIO as GPIO
from time import sleep


LED_RED_SCANNER_PIN = 18
LED_GREEN_SCANNER_PIN = 27
LED_BLUE_SCANNER_PIN = 22
LED_RED_BALL_PIN = 23
LED_GREEN_BALL_PIN = 24
LATCH = [9, 25, 11]
PIN_ERR = 5
PIN_BUSY = 8
PIN_STATUS = 7
eternal = {
    'OpenSesame_01': 0,
    'OpenSesame_02': 1,
    'OpenSesame_03': 2
}

def flash_pin(pins, count=13, delay=250):
    for i in range(count):
        for value in range(100):
            for pin, pwm in pins.items():
                if value <= pwm:
                    pin.ChangeDutyCycle(value)
                sleep(delay / (1000 * 100 * 3))
        sleep(2 * delay / 3000.0)
        for value in range(100, -1, -1):
            for pin, pwm in pins.items():
                if value <= pwm:
                    pin.ChangeDutyCycle(value)
                sleep(delay / (1000 * 100 * 3))
        sleep(2 * delay / 3000.0)


def main():
    GPIO.setmode(GPIO.BCM)
    for pin in LATCH + [LED_RED_SCANNER_PIN, LED_RED_BALL_PIN, LED_GREEN_SCANNER_PIN, LED_GREEN_BALL_PIN, LED_BLUE_SCANNER_PIN]:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    GPIO.setup(PIN_ERR, GPIO.IN)
    GPIO.setup(PIN_BUSY, GPIO.IN)
    GPIO.setup(PIN_STATUS, GPIO.IN)
    led_pins = [
            GPIO.PWM(pin, 100)
            for pin in (LED_RED_SCANNER_PIN, LED_RED_BALL_PIN, LED_GREEN_SCANNER_PIN, LED_GREEN_BALL_PIN, LED_BLUE_SCANNER_PIN)
            ]
    for pin in led_pins:
        pin.start(0)
    (LED_RED_SCANNER, LED_RED_BALL, LED_GREEN_SCANNER, LED_GREEN_BALL, LED_BLUE_SCANNER) = led_pins
    while True:
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

        LED_RED_SCANNER.ChangeDutyCycle(8)
        LED_GREEN_SCANNER.ChangeDutyCycle(6)
        LED_BLUE_SCANNER.ChangeDutyCycle(9)
        guid = raw_input("QR: ")
        print datetime.now(), "Scanned QR: ", guid
    
        with sqlite3.connect("/home/pi/mydata.sql") as db:
            cursor = db.cursor()
            try:
                if guid not in eternal:
                    cursor.execute("SELECT valid, ball FROM ids WHERE id=?", (guid,))
                    record = cursor.fetchone()
                else:
                    record = (1, eternal[guid])
                
                if record and record[0]:
                    print datetime.now(), "valid, ball", record[1]
                    GPIO.output(LATCH[record[1]], GPIO.HIGH)
                    flash_pin({LED_GREEN_SCANNER: 100}, count=3)
                    if GPIO.input(PIN_ERR):
                        raise ValueError("No more balls")
                    flash_pin({LED_GREEN_BALL: 100}, delay=500)
                    GPIO.output(LATCH[record[1]], GPIO.LOW)

                    print datetime.now(), "Wait for busy go low"
                    LED_GREEN_BALL.ChangeDutyCycle(100)
                    status_checked = False
                    for _ in range(400):
                        if not GPIO.input(PIN_BUSY):
                            break
                        if GPIO.input(PIN_STATUS) and not status_checked:
                            LED_GREEN_BALL.ChangeDutyCycle(15)
                            LED_RED_BALL.ChangeDutyCycle(100)
                            status_checked = True
                        sleep(.2)
                    else:
                        print datetime.now(), "Busy timeout"
                    LED_GREEN_BALL.ChangeDutyCycle(0)
                    LED_RED_BALL.ChangeDutyCycle(0)

                    if guid not in eternal:
                        cursor.execute("UPDATE ids SET valid=? WHERE id=?", (0, guid))
                        db.commit()
                        print datetime.now(), "Databse updated"
                else:
                    raise NameError("Ticket spent")
            except ValueError as e:
                print datetime.now(), repr(e)
                flash_pin({LED_GREEN_SCANNER: 15, LED_RED_SCANNER: 100}, count=3)
            except Exception as e:
                print datetime.now(), repr(e)
                flash_pin({LED_RED_SCANNER: 100}, count=3)

            print datetime.now(), "Ready"
            GPIO.output(LATCH[0], GPIO.LOW)
            GPIO.output(LATCH[1], GPIO.LOW)
            GPIO.output(LATCH[2], GPIO.LOW)

if __name__ == "__main__":
    main()
