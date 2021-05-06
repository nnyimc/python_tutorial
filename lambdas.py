#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# définition d'une fonction à l'aide de lambda
s = lambda x : 0 if x < 0 else x
print(s(12));

def f(x):
    return x**2;

carre = lambda x : x**2
print (carre(6));

R = map(carre, range(10));
print(list(R));

# fonction --->  lambda y : 0 if y < 0 else y
#itérateur ---> [-1, 20, 3, 6, 11, -4, 8, 4]
R2 = map(lambda y : 0 if y < 0 else y*-1, [-1, 20, 3, 6, 11, -4, 8, 4])
print(list(R2))
