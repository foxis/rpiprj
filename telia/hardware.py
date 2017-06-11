#!/usr/bin/python

from RPi import GPIO
from pmon import PeakMonitor
import os
from math import floor

BUTTONS = [3, 22]
OE_PIN = 23
BAR_PINS = [21, 20, 26, 16, 19, 13, 12, 06, 05, 07, 8, 11, 25, 9, 10, 24][::-1]
BARS = []
LOW_BATTERY = 18
POWER = 27
STAT_LED1 = 15
PWR_LED = None
STAT_LED2 = 17
AMP_SD = 04

OUTPUTS = [OE_PIN, STAT_LED1, STAT_LED2] + BAR_PINS
INPUTS = [POWER, LOW_BATTERY] + BUTTONS


def init():
    global BARS
    global PWR_LED

    GPIO.setmode(GPIO.BCM)

    for port in OUTPUTS:
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, GPIO.LOW)

    for port in BUTTONS:
        GPIO.setup(port, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LOW_BATTERY, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(POWER, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    BARS = [GPIO.PWM(port, 100) for port in BAR_PINS]
    for i in BARS:
        i.start(0)

    PWR_LED = GPIO.PWM(STAT_LED1, 100)
    PWR_LED.start(0)

    print("Init done.")
    print("INPUTS: ", [GPIO.input(i) for i in INPUTS])
    print("Turning on bar graph...")
    GPIO.output(OE_PIN, GPIO.LOW)


def display(rval, rval_max, power):
    N = len(BAR_PINS)
    val = int(floor(rval * N / 127.0))
    val_max = int(floor(rval_max * N / 127.0))

    on_val = 15 if power else 100

    pins = [on_val if i < val or i == val_max else 0 for i in range(N)]
    pins[val] = on_val * (rval * N / 127.0 - val)

    #print "{} {} {}\r".format(val, rval, rval * N / 127 - val),
    #pins[val] = on_val

    for i, s in enumerate(pins):
        BARS[i].ChangeDutyCycle(s)


def main(sink, freq):
    init()

    avg = 0
    avg_max = 0

    peak_hold = freq * .5
    drop = 7 * freq / 127.0
    peak_cnt = 0
    btn_cnt = [0, 0]
    pwr = 0
    pwr_inc = .1 * drop

    for peak in PeakMonitor(sink, freq):
        # determine peak value and calculate abg/etc
        if peak > avg:
            avg = peak

        if peak > avg_max:
            peak_cnt = 0
            avg_max = peak

        if peak_cnt > peak_hold:
            avg_max -= drop

        avg -= drop
        if avg < 0:
            avg = 0


        # read buttons and other stuff
        if not GPIO.input(LOW_BATTERY):
            print("Low battery condition detected... shutting down")
            # TODO: issue shutdown
            pwr_inc = -drop

        for i, pin in enumerate(BUTTONS):
            if not GPIO.input(pin):
                btn_cnt[i] += 1
            else:
                if btn_cnt[i] > 0:
                    print("Button {} was held for {} seconds".format(i, btn_cnt[i] / float(freq)))
                    if i == 0 and btn_cnt[i] / freq > 10:
                        print("Shutting down...")
                        pwr_inc = -drop
                    elif i == 0 and btn_cnt[i] / freq > 3:
                        print("Rebooting...")
                        GPIO.cleanup()
                        os.system("shutdown -r now")
                btn_cnt[i] = 0

        # display data
        try:
            display(avg, avg_max, GPIO.input(POWER))
        except:
            pass
        
        pwr = pwr + pwr_inc
        peak_cnt += 1

        if pwr < 0:
            GPIO.output(OE_PIN, GPIO.HIGH)
            GPIO.cleanup()
            os.system("shutdown now")
            return

        if pwr > 100:
            pwr = 100
        else:
            PWR_LED.ChangeDutyCycle(pwr)


if __name__ == "__main__":
    print("Starting audio level meter service...")
    main("alsa_output.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00-Device.analog-stereo", 50)
    print("Audio level meter service exiting...")

