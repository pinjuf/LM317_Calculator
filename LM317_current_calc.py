import math

I = float(input("[?] I: "))

power_range = (-2,
               2  +1)

standard_resistor_values_base = [1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]

def opt_resistance(I):
    # I = 1.25/R
    R = 1.25/I
    return R

def I_for_R(R):
    I = 1.25/R
    return I

closest = [math.inf, math.inf]

min_pow, max_pow = power_range

for i in range(min_pow, max_pow):
    for r in standard_resistor_values_base:
        R = r*10**i
        d = abs(I-I_for_R(R))
        if closest[1]>d:
            closest[0]=R
            closest[1]=d
  

print(f"Optimal resistance: {closest[0]}")
