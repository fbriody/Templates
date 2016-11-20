"""
Demo using fontdict to control style of text and labels.
"""
import numpy as np
import matplotlib.pyplot as plt


font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

#x = np.linspace(0.0, 5.0, 100)
x = np.linspace(0.5, 2.0, 100)
#y = np.cos(2*np.pi*x) * np.exp(-x)
y = np.tan(x-1) #* np.exp(-x)

plt.plot(x, y, 'b')
plt.title('Damped exponential decay', fontdict=font)
plt.text(2, 0.65, r'$\cos(2 \pi t) e^{-t}$', fontdict=font)
plt.xlabel('time (s)', fontdict=font)
plt.ylabel('voltage (mV)', fontdict=font)
plt.xlim(.5,2)#frame size
plt.ylim(-.5,1.5)#frame size
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')


#for x in range(0, 3):
    #print "We're on time %d" % (x)
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

for x in my_range(.5, 2, 0.1):
    y = np.tan(x-1)
    print x,y
    plt.plot(x, y, 'g^')
    
#added by FB; generates Euler ordered pairs
def euler(df, x0, y0, dx, x1):
    x, y = x0, y0
    while x < x1:
        y = y + dx * df(x, y)
        x += dx
    return y

def fprime(x, y):
    return (y**2) +1

x0 = 1
y0 = 0
x1 = 2.0
h=.1
yi = y0
#added by FB; generates Euler table values
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

for xi in my_range(x0,x1,h):
    print xi,yi,np.tan(xi-1)
    plt.plot(xi,yi,'ro')
    yi=yi+fprime(xi,yi)*h





# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.1)
plt.subplots_adjust(right=.85)
plt.show()
