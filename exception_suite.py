#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sin
for x in range (-4, 5):
    try:
        print("{:.3f}".format(sin(x)/x), end = " ");
    except ZeroDivisionError as e:
        print("{:.3f}".format(1.0), end = " ");

def divByZero():
    return 5/0;

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg;

err = MyError("Program aborted");

try:
    divByZero();
except ZeroDivisionError :
    print("Division par zéro impossible");
except Exception:
    print("Fin du programme");

x = 2;
if not (0 <= x <= 1):
    raise ValueError("x doesn't belong to the domain!");



    