#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = int(input("Submit a number: "));
if a > 5:
    a = a + 1;
else:
    a = a * 2;
print("a =", a);

# Obtenir 100 itérations
i = 0
while i <= 100:
    print(i)
    i += 10;

for x in range(0, 100): 
    print (i, "bonjour");

v = input("Submit a sentence: ");
for lettre in v :
    print(lettre);
    
#Afficher les entiers entre 10 et 30
y = 9
for f in range(0, 21):
    print(y);
    y += 1;

for x in range (-10, 11):
    print(x);
    
for l in range(10):
    for c in range(l):
        print(c, end=".")
    print()
    
symboles = { "A":"Apple", "B":"Banana", "C":"Carrot", "D":"" }
for k,v in symboles.items():
    print(k, ":", v);
    
for k,v in symboles.items():
    print("{:2}:{}".format(k, v));