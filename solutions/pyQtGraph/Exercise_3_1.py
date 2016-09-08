 
# imports 
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

# init qApp
app = pg.QtGui.QApplication([])

# setup the main window
view = pg.GraphicsView()
view.resize(900,500)
view.setWindowTitle('Notebook')
view.show()

# main layout
layout = pg.GraphicsLayout(border='r')     # with a red bordercolor 

# set the layout as a central item
view.setCentralItem(layout)

# create a text block
label = pg.LabelItem('PyQtGraph Grid Layout Example', size='25px', color='y')

# create a plot with two random curves
p1 = pg.PlotItem()
curve11 = pg.PlotCurveItem(pen=pg.mkPen(color='g', width=1))
curve12 = pg.PlotCurveItem(pen=pg.mkPen(color='b', width=1, style=QtCore.Qt.DashLine))
p1.addItem(curve11); p1.addItem(curve12)
curve12.setData(np.random.rand(100)-0.5)
p1.setXRange(0,100); p1.setYRange(-1.1,2.1)

# create another plot with two random curves
p2 = pg.PlotItem()
curve21 = pg.PlotCurveItem(pen=pg.mkPen(color='w', width=1, style=QtCore.Qt.DotLine))
curve22 = pg.PlotCurveItem(pen=pg.mkPen(color='c', width=1, style=QtCore.Qt.DashLine))
p2.addItem(curve21); p2.addItem(curve22)
curve21.setData(np.random.rand(100) + 0.5)
curve22.setData(np.random.rand(100) - 0.5)
p2.setXRange(0,100); p2.setYRange(-1.1,2.1)

# finally organize the layout
layout.addItem(label, row=0, col=0, colspan=2)
layout.addItem(p1, row=1, col=0)
layout.addItem(p2, row=1, col=1)

# data to animate
x = np.random.rand(500,100) + 0.5

# repeating data generator
cnt=0
def animLoop():
    global cnt
    curve11.setData(x[cnt%x.shape[0]])
    cnt+=1
    
timer = QtCore.QTimer()
timer.timeout.connect(animLoop)
timer.start(0)

app.exec_()