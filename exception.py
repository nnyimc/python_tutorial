#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    print(x);
except:
    print("An Exception occured!");
    
try:
    print(x);
except NameError as nameNotFound:
    print("Variable is not available");
except:
    print("Something went wrong...");