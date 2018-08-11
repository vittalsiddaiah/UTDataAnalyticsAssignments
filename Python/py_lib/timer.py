# Copyright (c) 2018, Vittal Siddaiah
# All rights reserved.

import time
import math


class timer:
    """
    This function is set to get the timing, timer your modules ...
    Time is the fundamental unit, and it gives legitimacy to our perceptual existence...  -Vittal.
    """

    __begin_time__ = 0
    __delta_time__ = 0
    __comment__ = ''

    def __init__(self, comment=''):
        self.__begin_time__ = time.time()
        self.__comment__ = comment

    def delta(self):
        self.__delta_time__ = (time.time() - self.__begin_time__)
        return self.__delta_time__

    def reset(self):
        self.__begin_time__ = time.time()


    def delta_str(self):
        self.delta()
        temp  = self.__delta_time__ / (24.0 * 60.0 * 60.0)
        residue = math.fmod(temp, 1)
        days = temp - residue
        temp = residue * 24.0
        residue = math.fmod(temp, 1)
        hours  = temp - residue
        temp = residue * 60.0
        residue  = math.fmod(temp, 1)
        mins  = temp - residue
        secs = residue * 60.0
        timeValue =  "[%02d:%02d:%02d:%07.4f]  (dd:hh:mm:ss.ssss)" % (days, hours, mins, secs)
        return self.__comment__ + timeValue