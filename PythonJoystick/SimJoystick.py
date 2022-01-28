# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7
"""
Created on Tue Jun  1 09:25:56 2021

@author: ErikWilhelm
"""
from XInput import *
import time
import sys
import numpy as np


def ev(vibL,vibR,prevSteer,prevThrottle,prevA,prevB,prevX,prevY):

    A=prevA
    B=prevB
    X=prevX
    Y=prevY
    tol=0.01
    Steer=prevSteer
    Throttle=prevThrottle

    events = get_events()
    for event in events:
        if event.type == EVENT_BUTTON_PRESSED:
            if event.button == "A":
                A=1
            elif event.button == "B":
                B=1
            elif event.button == "X":
                X=1
            elif event.button == "Y":
                Y=1
        if event.type == EVENT_BUTTON_RELEASED:
            if event.button == "A":
                A=0
            elif event.button == "B":
                B=0
            elif event.button == "X":
                X=0
            elif event.button == "Y":
                Y=0
        elif event.type == EVENT_STICK_MOVED:
            if event.stick == LEFT and np.abs(event.x-prevSteer)>tol:
                Steer=event.x
            else:
                Steer=prevSteer
            if event.stick == RIGHT and np.abs(event.y-prevThrottle)>tol:
                Throttle = event.y
            else:
                Throttle = prevThrottle


    if vibL>0 or vibR>0:
        if vibL>0:
            set_vibration(0,np.clip(vibL,0,2**16),0) #Values between 0 and 2^16 are allowed
        if vibR>0:
            set_vibration(0,0,np.clip(vibR,0,2**16)) #Values between 0 and 2^16 are allowed
    else:
        set_vibration(0,0,0)


    return A,B,X,Y,Steer,Throttle

