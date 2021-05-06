#!/usr/bin/env python3
# -*- coding: utf-8 -*-


L = ["C", "C#", "Java", "python", "php"];
print(len(L));

for i in range(len(L)): 
    print("L[{}]={}".format(i, L[i]));

print()

for i,v in enumerate(L):
    print("L[{}]={}".format(i, v));



#Exercice
symboles = ["H", "O", "He", "N", "Ca", "At"];

for v in symboles:
    print(v)

print()

for i,v in enumerate(symboles):
    print("{}---->{}".format(i, v));   
    
print()
    
for i,v in enumerate(symboles):
        if v == "Ca":
            break
        print("{}--->{}".format(i, v))

z = zip(['a', 'b', 'c', 'd'], ['d', 'e', 'f', 'g', 'h']);
print(list(z));

