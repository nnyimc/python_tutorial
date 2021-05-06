#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
from math import pi, sin
def somme(x,y):
    print(x, "+", y, "=", x+y)
    return x+y
reduce(somme, [1, 2, 3, 4]);

#Filtrer les nombres pairs
li = [0,1,2,3,4,5,6,7,8,9,10,11,12];
print(list(filter( lambda x : not (x % 2), li)));

#Elever au carré puis conserver les éléments pairs
print( list( map( lambda x : x**2, filter( lambda x : not (x % 2), li) ) ) );

#Importer des modules
print("Valeur de pi: " + str(pi), sin(0));
print("I am ", __name__);