#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fsource = open("exercice1.py", "r", encoding="utf-8");
fdest = open("copyExercice.py", "w", encoding="utf-8");
s = fsource.read();
fdest.write(s);
print(s);
fdest.close();
fsource.close();