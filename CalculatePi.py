from decimal import Decimal, getcontext
import time
# calculates pi to the specified number of digits using the bailey borwein plouffe formula (BBP)
def calculate_pi(precision):
    getcontext().prec = precision
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)
    pi = Decimal(0)
    i = 0
    while True:
        a_next = (a + b) / Decimal(2)
        b_next = (a * b).sqrt()
        t_next = t - p * (a - a_next) * (a - a_next)
        p_next = 2 * p
        i += 1
        pi_next = Decimal((a_next + b_next) * (a_next + b_next)) / (Decimal(4) * t_next)
        if pi == pi_next:
            
            break
        a = a_next
        b = b_next
        t = t_next
        p = p_next
        pi = pi_next
    return str(pi)