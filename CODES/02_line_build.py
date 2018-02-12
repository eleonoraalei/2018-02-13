from matplotlib import pyplot as plt

class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        # line.figure.canvas to get the canvas
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self.addSegment)

    def addSegment(self, event):
        print('click', event)
        if event.inaxes!=self.line.axes: return
        if event.button==1:
            self.xs.append(event.xdata)
            self.ys.append(event.ydata)
            self.line.set_data(self.xs, self.ys)
            self.line.figure.canvas.draw()
        if event.button==3:
            print ("disconnect")
            self.line.figure.canvas.mpl_disconnect(self.cid)
            self.line.set_data(self.xs+[self.xs[0]], self.ys+[self.ys[0]])
            self.line.set_color('r')
            self.line.figure.canvas.draw()
                                        
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click to build line segments')
line, = ax.plot([], [],'o-')  # empty line
lb = LineBuilder(line)

plt.show()
