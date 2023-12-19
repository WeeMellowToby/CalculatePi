import time
#import the module
import sys
sys.path.append('../')
from CalculatePi import CalculatePi
#time how long it takes to calculate 100,000 digits (around 10 seconds on my machine)
start_time = time.time()
CalculatePi.calculate_pi(100000)
end_time = time.time()
#print time taken
print(end_time - start_time)