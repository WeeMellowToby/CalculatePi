import sys
sys.path.append('../')
from CalculatePi import CalculatePi
#calculates pi to 1000 digits
pi = CalculatePi.calculate_pi(1000)
print(pi)