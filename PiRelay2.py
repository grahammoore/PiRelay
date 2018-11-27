#!/usr/bin/python

# Library for PiRelay
# Developed by: Graham Moore
# Author: Graham Moore
# Project: PiRelay2
# Python: 3.6

#import MockRPi.GPIO as GPIO
import RPi.GPIO as GPIO


class Relay:

    def __init__(self, relay, pin):
        self.pin = pin
        self.relay = str(relay)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        if Board.is_output_on():
            print("RELAY" + self.relay + " - ON")
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        if Board.is_output_on():
            print("RELAY  " + self.relay + " - OFF")
        GPIO.output(self.pin, GPIO.LOW)


class Board:

    RELAY_1 = None
    RELAY_2 = None
    RELAY_3 = None
    RELAY_4 = None

    show_operations = True

    @classmethod
    def init(cls):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        cls.RELAY_1 = Relay(1, 15)
        cls.RELAY_2 = Relay(2, 13)
        cls.RELAY_3 = Relay(3, 11)
        cls.RELAY_4 = Relay(4, 7)

    @classmethod
    def output_on(cls):
        cls.show_operations = True

    @classmethod
    def output_off(cls):
        cls.show_operations = False

    @classmethod
    def is_output_on(cls):
        return cls.show_operations


def __init__():
    Board.init()

