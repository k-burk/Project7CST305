# This code was created by Kara Sumpter
# The lorenz function was modified from project 5
# The funcanimate function is used to animate the lorenz function
# The data for part 2 a was calculated in class and then graphed
# To be able to graph part 2 c I increased the lambda and mu values
# to simulate what they would look like at different capacities
# to highlight the difference between the old and new values

import time
from part2a import *
from part2c import *
from lorenz import *

print("###### Lorenz ######")
runlorenz()
time.sleep(10) #gives time for graph to animate
print("###### Part 2 A ######")
runa()
time.sleep(5)
print("###### Part 2 C ######")
runc()

