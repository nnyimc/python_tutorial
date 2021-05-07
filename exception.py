#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    print(x);
except:
    print("An Exception occured!");
    
try:
    print(x);
except NameError as nameNotFound:
    print("Variable x is not available");
except:
    print("Something went wrong...");
    
try:
    print("Hello");
except:
    print("Something went wrong");
else:
    print("ALL GREEN");
finally:
    print("Goodbye");
    
try:
    f = open("demo.txt", "w", endoced="UTF-8");
except:
    print("Something went wrong while attempting to write on the file");
else:
    f.write("Lorem Ipsum");
    f.close;