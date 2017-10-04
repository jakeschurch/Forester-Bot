#! usr/bin/env python3
from robot import *
# -*- coding: UTF-8 -*-

_author_ = "Jake Schurch"

left, right = robot.Motors("da")
Forward(left)
Backward(right)
Wait(3)

Backward(left, right)
Wait(3)

Off(left, right)
