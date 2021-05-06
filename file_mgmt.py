#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 16:27:10 2021

@author: nnyimc
"""
f = open("../Test.txt", "w");
s = "Bonjour !!\r\nKonnichiwa !!\r\nBom Dia !!\r\n";
f.write(s);
l = ['a', 'b', 'c'];
f.writelines(l);
print("\r\nHello World", file = f);
f.close();

f = open("../Test.txt", "r", encoding="utf-8");
#s = f.read(30); # read the first 30 characters
s = f.readlines();
print(s);
f.close();

