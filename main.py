#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import logging
from rpi_rf import RFDevice

# nastavení GPIO pinu připojeného k přijímači
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

# nastavení frekvence přijímače
rfdevice = RFDevice(17)
rfdevice.enable_rx()
rfdevice.rx_code_timestamp = None

# nekonečná smyčka pro přijímání signálu
while True:
    if rfdevice.rx_code_timestamp != None:
        code = str(rfdevice.rx_code)
        logging.info("Received code: " + code)
        rfdevice.rx_code_timestamp = None
    time.sleep(0.01)

# uvolnění zdrojů
rfdevice.cleanup()
GPIO.cleanup()
