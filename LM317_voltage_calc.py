#!/usr/bin/env python3

import math

power_range = 1

Vout = float(input("[?] Vout: "))

standard_resistor_values_base = [1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]

def get_ratio(v):
    v /= 1.25
    v -= 1
    return v


lowest_difference = [0, 0, math.inf]

# O(n^2*i) go brrrrrrrrrr
for R1 in standard_resistor_values_base:
    R2_opt = R1*get_ratio(Vout)
    basic_range = math.floor(math.log10(R1*R2_opt))
    extended_range = range(basic_range-power_range, basic_range+power_range+1)
    multipliers = [10**i for i in extended_range]
    for m in multipliers:
        for R2 in standard_resistor_values_base:
            R2 *= m
            difference = abs(R2-R2_opt)
            if difference<lowest_difference[2]:
                lowest_difference = [R1, R2, difference]


print()
print("Ratio R1/R2: ", get_ratio(Vout))
print()
print("Optimized resistor values (multiples can also be used):")
print("R1: ", lowest_difference[0])
print("R2: ", lowest_difference[1])
