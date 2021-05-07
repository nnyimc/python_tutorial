#!/usr/bin/env python3
# -*- coding: utf-8 -*-
unTuple = ("apple", "banana", "cherry");
iter = iter(unTuple);
type(iter);
print(next(iter));
print(next(iter));
print(next(iter));

class PrintNumber:
    def __init__(self, max):
        self.max = max;
    
    def __iter__(self):
        self.num = 0;
        return self;
    
    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration;
        self.num += 1;
        return self.num;

print_num = PrintNumber(3);
print_num_iter = iter(print_num);
print(next(print_num_iter));