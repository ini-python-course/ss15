
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

app = pg.QtGui.QApplication([])

x = np.random.rand(500,50)

pg.setConfigOptions(antialias=True)

# main graphics window
view = pg.GraphicsView()

# show the window
view.show()

# add a plotItem
p = pg.PlotItem()

# add the plotItem to the graphicsWindow and set it as central
view.setCentralItem(p)

# create an curve object
curve = pg.PlotCurveItem()

# add the curve object to the plotItem
p.addItem(curve)

# optionally set the visible ranges for X and Y axes (speeds up the animation).
# if this line is commented, the ranges are automatically found for each data update.
# try commenting this line to compare the performance.
p.setXRange(0,50); p.setYRange(0,1)

# set title
p.setTitle('Array Animation', size='25px', color='y')

# data generator
cnt=0
def animLoop():
    global cnt
    if cnt < x.shape[0]:
        curve.setData(x[cnt])
    cnt+=1
    
timer = QtCore.QTimer()
timer.timeout.connect(animLoop)
timer.start(0)

app.exec_()


