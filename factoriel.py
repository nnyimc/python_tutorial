#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def factoriel(x):
    if x == 0:
        return 1
    return (x*factoriel(x-1))

if __name__ == "__main__" :
    print(factoriel(5))
