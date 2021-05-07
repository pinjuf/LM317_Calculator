import math

I = float(input("[?] I: "))

standard_resistor_values_base = [1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]

def opt_resistance(I):
    # I = 1.25/R
    R = 1.25/I
    return R
