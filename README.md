by *Marco Gullieuszik*

I will present matplotlib 
API for interacting with the figure via key presses and mouse movements.

A few simple codes will be used to show how to build interactive
applications using matplotlib event handling.
 
-----


First of all, you have to use an "interactive backend”

https://matplotlib.org/faq/usage_faq.html#what-is-a-backend

You may have an interactive backend set by default (as in most cases),
but, to be sure, you can set the backend with the following code:

```python
import matplotlib
matplotlib.use("TkAgg")
```

*Use these first line at the very beginning of the script*
>`matplotlib.use()` must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

# Interactive vs non-interactive mode
[ https://matplotlib.org/faq/usage_faq.html#what-is-interactive-mode ]

## interactive example
From an ordinary python prompt, or after invoking ipython with no options, try this:

```python
import matplotlib.pyplot as plt
plt.ion()
plt.plot([1.6, 2.7])
```
Assuming you are running version 1.0.1 or higher, and you have an interactive backend installed and selected by default, you should see a plot, and your terminal prompt should also be active; you can type additional commands such as:
```python
plt.title("interactive test")
plt.xlabel("index")
plt.plot([3.1,2])
```
and you will see the plot being updated after each line. This is because you are in interactive mode

## Non-interactive example
Start a fresh session as in the previous example, but now turn interactive mode off:
```python
import matplotlib.pyplot as plt
plt.ioff()
plt.plot([1.6, 2.7])
```
Nothing happened–or at least nothing has shown up on the screen (unless you are using macosx backend, which is anomalous). To make the plot appear, you need to do this:
```python
plt.show()
```
Now you see the plot, but your terminal command line is unresponsive; the show() command blocks the input of additional commands until you manually kill the plot window.

What good is this–being forced to use a blocking function? Suppose you need a script that plots the contents of a file to the screen. You want to look at that plot, and then end the script. Without some blocking command such as show(), the script would flash up the plot and then end immediately, leaving nothing on the screen.

In addition, non-interactive mode delays all drawing until show() is called; this is more efficient than redrawing the plot each time a line in the script adds a new feature.

# Event Handling

https://matplotlib.org/users/event_handling.html

With matplotlib it is possible to interact with the plots (with the `Figure` in general).



To receive events, you need to write a callback function and then connect your function to the event manager, 
```python
fig, ax = plt.subplots()
ax.plot(np.random.rand(10))

def onclick(event):
    # do something
    pass

cid = fig.canvas.mpl_connect('button_press_event', onclick)
```

The `FigureCanvas` method `mpl_connect()` returns a connection id which is simply an integer. When you want to disconnect the callback, just call:

```python
fig.canvas.mpl_disconnect(cid)
```

An `Event` object is passed as an argument to the callback function (`onclick` in the previous example).
The most common events (key press/release events and mouse press/release and movement) are derived from the `LocationEvent`, which has the following attributes

* `x` x position - pixels from left of canvas
* `y`y position - pixels from bottom of canvas
* `inaxes` the Axes instance if mouse is over axes
* `xdata` x coord of mouse in data coords
* `ydata` y coord of mouse in data coords


---

The following 3 scripts show how to handle mouse/keyboard events and object picking, which means making something happen when you:

* click and/or release a mouse button
* move the mouse
* click and/or release a key
* select an object in the canvas (e.g. a point in the plot)

1. `CODES/01_intro.py`: basic example, to show the idea
2. `CODES/02_line_build.py`: a working example with mouse press/release events
3. `CODES/03_picking.py` a working example with object picking
