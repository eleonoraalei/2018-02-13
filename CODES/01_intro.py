import matplotlib
matplotlib.use("TkAgg") # backend

import matplotlib.pyplot as plt
plt.ioff()   # interactive mode off. [this should be the default]

import numpy as np

x1=np.random.rand(5)
y1=np.random.rand(5)
x2=np.random.rand(5)
y2=np.random.rand(5)

fig,ax=plt.subplots()

plt_points1=ax.plot(x1,y1,'or')[0]
plt_points2=ax.plot(x2,y2,'sk',picker=5)[0] ## note the picker here!

# callback functions
def onMousePress(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

def onMouseRelease(event):
    print ("mouse release: button=%d"%event.button)

def onKeyPress(event):
    print ("key press. Key: %s"%event.key)

def onKeyRelease(event):
    print ("key release. Key: %s"%event.key)

def onPick(event):
    if (event.artist==plt_points2):  # not necessary if you set the picker only for
                                     # plt_points_2
        xdata = event.artist.get_xdata()
        ydata = event.artist.get_ydata()
        ind = event.ind[0]
        
        print('   picked point %d; xdata=%f ydata=%f'%(ind,xdata[ind],ydata[ind]))

def onMove(event):
    if (event.inaxes==ax):
        print ("position: %6.4f %6.4f"%(event.xdata,event.ydata))

# connect the events to the callback functions
fig.canvas.mpl_connect('button_press_event',   onMousePress)
fig.canvas.mpl_connect('button_release_event', onMouseRelease)

fig.canvas.mpl_connect('key_press_event',   onKeyPress)
fig.canvas.mpl_connect('key_release_event', onKeyRelease)

fig.canvas.mpl_connect('pick_event', onPick)
fig.canvas.mpl_connect('motion_notify_event', onMove)

plt.show()
print ("DONE") # this is exectuted only when the figure windows is closed
               # because interactive mode is off
