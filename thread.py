#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import os
import time

def doChore():
    time.sleep(0.5)


class BoothThread(threading.Thread):
    def __init__(self, tid, monitor):
        self.tid = tid
        self.monitor = monitor
        threading.Thread.__init__(self)
    def run(self):
        while True:
            monitor['lock'].auquire()
            if monitor['tick'] != 0:
                monitor['tick'] = monitor['tick'] - 1
                print(threading.currentThread().getName())
                doChore()
            else:
                print("Thread_id", self.tid,"No thanks")
                os._exit()
            monitor['lock'].release()
            print(threading.currentThread().getName() + "release")
            doChore()

monitor = {'tick':15, 'lock':threading.Lock()}

for k in range(10):
    t = BoothThread(k,monitor)
    t.start()


