#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 08 Task 2"""

DAY = raw_input('What day is it?').lower()[:3:]

TIME = raw_input('What time is it? ')[:4:]
TIME = int(TIME)

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 0600 else False

if SNOOZE == False:
    print 'Beep! Beep! Beep! Beep! Beep!'
