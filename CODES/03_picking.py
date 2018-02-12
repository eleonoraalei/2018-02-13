import matplotlib
matplotlib.use("TkAgg") # backend

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

plt.ioff()   # interactive mode off. [this should be the default]


p=np.random.uniform(1,3,20)
a=np.random.uniform(1,3,20)

fig,(ax1,ax2)=plt.subplots(2,1,figsize=(8,8))

# plot period vs amplitude
# set the picker radius
ax1.plot(p,a,'ok',picker=5)

l,=ax2.plot([],[]) # create an empty line, to be used later


ax1.set_xlabel("Period")
ax1.set_ylabel("Amplitude")
ax1.xaxis.set_major_locator(MultipleLocator(.25))
ax1.yaxis.set_major_locator(MultipleLocator(.5))
ax1.grid(which='both',ls="--")

ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.xaxis.set_minor_locator(MultipleLocator(.25))
ax2.yaxis.set_minor_locator(MultipleLocator(1.))
ax2.grid(which='both',ls="--")

ax1.set_xlim(.9,3.1)
ax1.set_ylim(.9,3.1)
ax2.set_xlim(0,3)
ax2.set_ylim(-3,3)

ax2.set_title("No data")

def onPick(event):
    ind = event.ind[0]  # id of the datapoint
    pp = event.artist.get_xdata()[ind] # get the period (x)
    aa = event.artist.get_ydata()[ind] # get the amplitude (y)

    # generate the "light curve"
    x=np.linspace(0,3,100) 
    y=aa*np.sin(x*2*np.pi/pp)

    # set the title of ax2
    ax2.set_title("P=%.2f  A=%.2f"%(pp,aa))

    # update x and y values for the line
    l.set_xdata(x) # set the data
    l.set_ydata(y) # 
     

    # redraw the whole figure
    # NOT THE MOST EFFICIENT SOLUTION if you need performances
    # (use blit or other animation techniques)
    fig.canvas.draw ()

fig.canvas.mpl_connect('pick_event', onPick)

fig.tight_layout()
plt.show()

