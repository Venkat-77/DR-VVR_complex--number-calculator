# --------------
import pandas as pd
import numpy as np
import math
class complex_numbers:
    def __init__(self, real,imag):
        self.real = real
        self.imag = imag
    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else                  "-", abs(self.imag))
    def __add__(self, other):
        x = self.real + other.real
        y = self.imag + other.imag
        return complex_numbers(x,y)   
    def __sub__(self, other):
        x = self.real - other.real
        y = self.imag - other.imag
        return complex_numbers(x,y)   
    def __mul__(self, other):
        x = (self.real*other.real)-(self.imag*other.imag)
        y = (self.imag*other.real) + (self.real*other.imag)
        return complex_numbers(x,y)  
    def __truediv__(self, other):
        sr, si, ore, oi = self.real, self.imag,                       other.real, other.imag # short forms
        r = float(ore**2 + oi**2)
        return complex_numbers((sr*ore+si*oi)/r, (si*ore-sr*oi)/r)
    def absolute(self):
        x  = self.real**2 + self.imag**2
        return math.sqrt(x)
    def argument(self):
        x  = math.atan(self.real/self.imag)
        x = 90-((x*180)/3.1415926535)
        return (x)    
    def conjugate(self):
        x = self.real
        y = self.imag
        return complex_numbers(x,-y)  

comp_1=complex_numbers(3,5)
comp_2=complex_numbers(4,4)
comp_sum=comp_1+comp_2
comp_diff=comp_1-comp_2
comp_prod=comp_1*comp_2
comp_quot=comp_1/comp_2
comp_abs = comp_1.absolute()
comp_conj = comp_1.conjugate()
comp_arg = comp_1.argument()
print(comp_1)
print(comp_2)
print(comp_sum)
print(comp_diff)
print(comp_prod)
print(comp_quot)
print(comp_abs)
print(comp_conj)
print(comp_arg)



#Code starts here



