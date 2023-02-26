#!/usr/bin/env python3
'''
Simple arithmetic operations
'''


def add(x, y):
    '''Adds two numbers'''
    return x + y

def subtract(x, y):
    '''Subtraction'''
    return x - y

def multiply(x, y):
    '''Multiply two numbers'''
    return x * y

def divide(x, y):
    '''Division'''
    if y == 0:
        raise ValueError('Cannot divide by 0')
    return x / y