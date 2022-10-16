import sys
import numpy as np
from PyQt5 import  QtWidgets
from window import Ui_MainWindow
import pyqtgraph as pg
import pickle


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):

    #初始化设置
    def __init__(self, ilineprofile, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.bottom_axis = pg.AxisItem(orientation='bottom')
        self.bottom_axis.setLabel(text="Trace")

        self.left_axis = pg.AxisItem(orientation='left')
        self.left_axis.setLabel(text="Time", units="ms")

        self.top_axis = pg.AxisItem(orientation='top', showValues=False)
        self.right_axis = pg.AxisItem(orientation='right', showValues=False)

        self.p1 = self.graphicsView.addPlot(row=0, col=0, rowspan=2, colspan=1, title="",
                                   axisItems={'bottom': self.bottom_axis, "left": self.left_axis,
                                              'top': self.top_axis, 'right': self.right_axis})
        self.top_axis.show()
        self.right_axis.show()
        self.p1.invertY(b=True)

        # 颜色棒
        self.hist = pg.HistogramLUTItem()
        self.graphicsView.addItem(self.hist, row=0, col=2, rowspan=2, colspan=1)

        self.img = pg.ImageItem(ilineprofile)

        self.hist.setImageItem(self.img)
        self.p1.addItem(self.img)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    path = "D:/workspace/数据集处理/地层/seismic/12.csv"
    import pandas as pd
    # profile = np.fromfile(path, dtype=np.float32)
    profile = pd.read_csv(path, header=None)
    print(profile.shape)
    profile = np.array(profile)
    mainWindow = MainWindow(profile)
    mainWindow.show()
    sys.exit(app.exec_())
