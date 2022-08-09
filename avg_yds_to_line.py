#2 years of avg yards into a line

import numpy as np
import matplotlib.pyplot as plt

x1 = 1
y1 = float(input("Enter Year 1 average yards per game: "))

x2 = 2
y2 = float(input("Enter Year 2 average yards per game: "))

a = (y2 - y1) / (x2 - x1)
b = y1 - a * x1
  
if a == 0:
   print('y =','x','+ ',b)

else:
    print('y = ', a,'x', '+ ',b)

y = ('y = ', a,'x', '+ ',b)
x = np.linspace(1,5,5)

plt.plot(x,y)
plt.show() 
