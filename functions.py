#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def indique_age():
    print("fonction indique age");
    return 30;

def indique_mon_age(naissance, actuelle):
    return actuelle - naissance;

def affiche():
    print("Bonjour");
print(indique_age());


x = int(input("Année de naissance : "));
y = int(input("Année actuelle : "));
print(indique_mon_age(x, y));

def division(x,y):
    print(x%y);
    
def divisionEntiere(a,b):
    print(x//y);
    
#appel de fonction
def double(x):
    return x*2;

def triple(x):
    return x*3;

def call(fonct, x):
    return triple(x);

print (call(triple, x));