#!/usr/bin/python

""" TELIA stendo kontroleris

    Is esmes vaizduoja audio lygi, stebi power bei battery_low signalus.
    Teoriskai gali reaguoti i mygtukus ir kazka mirkseti su dviem LED'ais, 
    taciau sis funkcionalumas buvo apleistas gelezyje.


    Mazai tiketina, kad kas skaitys si teksta, bet jei jau skaitai tai pamojuok :)

    (c) FoxIS a.k.a. Andrius Mikonis 
    andrius.mikonis@gmail.com
    869954982 
"""


from RPi import GPIO
from pmon import PeakMonitor
import os
from math import floor
from datetime import datetime, timedelta


BUTTONS = [3, 22]
OE_PIN = 23
LED_PINS = [21, 20, 26, 16, 19, 13, 12, 06, 05, 07, 8, 11, 25, 9, 10, 24]
BAR_PINS = LED_PINS[:15] 
BARS = []
LOW_BATTERY = 18
POWER = 27
STAT_LED1 = 15
PWR_LED = None
STAT_LED2 = 17
AMP_SD = 04

OUTPUTS = [OE_PIN, STAT_LED1, STAT_LED2, AMP_SD] + LED_PINS
INPUTS = [POWER, LOW_BATTERY]


def init():
    """Initializuoja raspbery pinus"""

    global BARS
    global PWR_LED

    GPIO.setmode(GPIO.BCM)

    for port in OUTPUTS:
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, GPIO.LOW)

    #for port in BUTTONS:
    #    GPIO.setup(port, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LOW_BATTERY, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(POWER, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    BARS = [GPIO.PWM(port, 100) for port in BAR_PINS]
    for i in BARS:
        i.start(0)

    PWR_LED = GPIO.PWM(STAT_LED1, 100)
    PWR_LED.start(0)

    print(str(datetime.now()), "Init done.")
    print(str(datetime.now()), "INPUTS: ", [GPIO.input(i) for i in INPUTS])
    print(str(datetime.now()), "Turning on bar graph...")
    GPIO.output(OE_PIN, GPIO.LOW)
    GPIO.output(AMP_SD, GPIO.HIGH)


def display(rval, rval_max, on_val):
    """vaizduoja apskaiciuota ir animuota garso lygi
       naudoja subpixel korrekcija paskutiniam bin'ui
    """
    N = len(BAR_PINS)
    val = int(floor(rval * N / 128.0))
    val_max = int(floor(rval_max * N / 128.0))


    pins = [on_val if i < val else 0 for i in range(N)]
    pins[val] = on_val * (rval * N / 128.0 - val) # subpixel correction
    pins[val_max] = on_val # since we use subpixel correction we need this

    # this one is more efficient than plain for
    [BARS[i].ChangeDutyCycle(s) for i, s in enumerate(pins)]


def power_check(state):
    """
	stebi power on/off ciklus ir stengiasi apie 11val isjungti viska ir ijungti apie 6val
    
	initial start is without power or power is for very short time (perhaps less than 1 h)
   
    	power goes on at around 17:30 and lasts at least until 01 (8h)

    	power disappears at 01
    	power goes on at 06 till ~08-09
    	cycle repeats

	we must detect that it is past 17:30 and try to turn stuff off before 23h

    """
    def wake_up(s=None):
        # TODO
        os.system('reboot')

    def sleep(s=None):
        os.system('systemctl stop bluetooth-agent')
        os.system('systemctl stop bluetooth')
        os.system('systemctl stop player-agent')
        os.system('killall omxplayer')
        os.system('killall omxplayer.bin')

    def dt(p):
        return (p[0][1] - p[1][1]).total_seconds() / 60 if len(p) > 1 else None

    if state is None:
        state = {
             'state': 'init',
             'allowed': True,
             'power': [],
	}

    power =  [(not GPIO.input(POWER), datetime.now())] + state['power']
    delta = dt(power)


    #if delta:
    #     print "{:.3f}".format(delta), [(i[0], i[1].strftime("%M %S")) for i in power], '           ', state['state'], '              \r',
    """
	state transitions:

	init -> day
	day -> evening
	evening -> morning
	morning -> day
    """

    morning_on = ((8 - 6) * 60)        
    evening_on = ((23 - 17.1) * 60)   
    morning_off = ((6 - 1) * 60)     
    day_off = ((17.5 - 8) * 60)     
    min_on = min(morning_on, evening_on)
    min_off = min(day_off, morning_off) 
    min_time = min(min_on, min_off) / 6.0

    if delta and power[0][0] != power[1][0]:
        """
	1. a, b  < min_time           drop b
	2. a, b  > min_time           process states
	3. a, b, c; a, b < min_time   drop b
	4. a, b, c; a, b > min_time   drop c
        """

        if len(power) > 2:
            print ''
            print('Power change duration too short, discarding')
            state['power'] = [power[-1]]
        else:
            state['power'] = power
    elif delta is None:
        state['power'] = power
        print 'morning_on', morning_on
        print 'evening_on', evening_on
        print 'morning_off', morning_off
        print 'day_off', day_off
        print 'min_on', min_on
        print 'min_off', min_off
        print 'min_time', min_time
    elif delta > min_time:
        if len(power) > 2:
            print ''
            print('Power change accepted, 1')
            state['power'] = [power[1]]
         
        if state['state'] == 'evening':
            state['allowed'] = True
            if delta > evening_on:
                state['state'] = 'night'
                print("Reached 23h mark, going to sleep...")
                sleep(state)
        elif state['state'] == 'night':
            state['allowed'] = False
            if not power[0][0]:
                state['state'] = 'evening_off'
        elif state['state'] == 'evening_off':
            state['allowed'] = False
            if power[0][0]:
                state['state'] = 'morning'
        elif state['state'] == 'morning':
            state['allowed'] = False
            if delta > morning_on * .7:
                print("Turning on the device from sleep...")
                wake_up(state)
                state['state'] = 'morning_on'
        elif state['state'] == 'morning_on':
            state['allowed'] = True
            if not power[0][0]:
                state['state'] = 'day'
        elif state['state'] in ('day', 'init') or (delta > morning_off * 1.3 and not power[0][0]):
            state['allowed'] = True
            if state['state'] not in ('day', 'init'):
                print("Forcing day time after long period of off")
                wake_up(state)
                state['state'] = 'day'
            elif power[0][0] and delta > min_on * 1.3:
                print("Going to evening")
                state['state'] = 'evening'
            else:
                state['state'] = 'day'
        
    return state

def main(sink, freq):
    """pagrindine auksto levelio logika"""
    init()

    avg = 0
    avg_max = 0

    peak_hold = freq * .5
    drop = 7 * freq / 127.0
    peak_cnt = 0
    btn_cnt = [0, 0]
    PWR_START = 300
    pwr = PWR_START
    pwr_inc = .1 * drop
    last_peak = datetime.now()
    start_time = datetime.now()
    on_val = 20
    l_peak = 0
    # power_state = None

    for peak in PeakMonitor(sink, freq):
        # power_state = power_check(power_state)
        # determine peak value and calculate abg/etc
        if peak > avg:
            avg = peak

        if avg > avg_max:
            peak_cnt = 0
            avg_max = peak
        if peak != l_peak and peak > 10:
            last_peak = datetime.now()
            
        l_peak = peak

        if (datetime.now() - last_peak).total_seconds() > 60 * 3 or \
           (datetime.now() - start_time).total_seconds() > 3600 * 3:
            print(str(datetime.now()), "Reboot due to three minutes of silence")
            os.system("reboot")
            return

        # read buttons and other stuff
        if not GPIO.input(LOW_BATTERY) and pwr == PWR_START:
            print(str(datetime.now()), "Low battery condition detected... shutting down counter: ", pwr)
            # TODO: issue shutdown
            pwr_inc = - .1 * drop
        elif pwr != PWR_START:
            print(str(datetime.now()), "Low battery condition removed")
            pwr_inc = 0
            pwr = PWR_START

        on_val += .1*drop if not GPIO.input(POWER) else -.1*drop
        if on_val < 20:
            on_val = 20
        elif on_val > 100:
            on_val = 100

        try:
            display(avg, avg_max, on_val)
        except:
            pass
        
        avg -= drop
        if peak_cnt > peak_hold:
            avg_max -= drop
        if avg < 0:
            avg = 0
        if avg_max < 0:
            avg_max = 0

        pwr = pwr + pwr_inc
        peak_cnt += 1

        if pwr < 0:
            GPIO.output(OE_PIN, GPIO.HIGH)
            GPIO.cleanup()
            print(str(datetime.now()), "Shutting down due to low battery...")
            os.system("shutdown now")
            return

        if pwr > PWR_START:
            pwr = PWR_START

	

if __name__ == "__main__":
    print(str(datetime.now()), "Starting audio level meter service...")
    main("alsa_output.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00-Device.analog-stereo", 50)
    print(str(datetime.now()), "Audio level meter service exiting...")

