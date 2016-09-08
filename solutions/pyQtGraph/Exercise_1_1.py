
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

app = pg.QtGui.QApplication([])

x = np.random.rand(500,50,50,3)

pg.setConfigOptions(antialias=True)

# main graphics window
view = pg.GraphicsView()

# show the window
view.show()

# add a plotItem
p = pg.PlotItem()

# add the plotItem to the graphicsWindow and set it as central
view.setCentralItem(p)

# create an image object
img = pg.ImageItem(border='w', levels=(x.min(),x.max()))

# add the imageItem to the plotItem
p.addItem(img)

# hide axis and set title
p.hideAxis('left'); p.hideAxis('bottom'); p.hideAxis('top'); p.hideAxis('right')
p.setTitle('Array Animation', size='25px', color='y')

# data generator
cnt=0
def animLoop():
    global cnt
    if cnt < x.shape[0]:
        img.setImage(x[cnt])
    cnt+=1
    
timer = QtCore.QTimer()
timer.timeout.connect(animLoop)
timer.start(0)

app.exec_()

