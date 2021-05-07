#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
