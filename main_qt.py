# general import
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib as mpl
from matplotlib.figure import Figure

# pyqt imports
from PyQt5 import QtCore, QtGui, QtWidgets
from main_window import Ui_MainWindow

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Data Collection")
        self._connection()
        self.time = 1.5
        self.rest = 20 * 60
        self.no_cycle = 300 / 3


    def _connection(self):
        self.start.setCheckable(True)
        self.start.toggle()
        self.start.clicked.connect(self._start)
        self.stop.setCheckable(True)
        self.stop.toggle()
        self.stop.clicked.connect(self._stop)
        self.info.setCheckable(True)
        self.info.toggle()
        self.info.clicked.connect(self._info)
        self.START = False
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self._clock)
        self.timer.setInterval(1)
        self.timer.start()
        self.counter = 0



    def _start(self):
        print('start')
        l = QtWidgets.QVBoxLayout(self.main_1)
        test = Mplotcanvas(self.main_1)
        l.addWidget(test)
        self.main_1.setFocus()
        self.START = True
        self.my_ploter = test

    def _stop(self):
        pass



    def _info(self):
        self.open_window()

    def _read_sub_window(self):
        self.time = int(self.ui.squat_time.toPlainText())
        self.rest = int(self.ui.rest_time.toPlainText())
        self.cycle = int(self.ui.no_cycle.toPlainText())
        print(self.time,self.rest, self.cycle)
        self.sub_window.close()

    def _sub_window_connection(self):
        self.sub_window.buttonBox.accept.connect(self._read_sub_window)
        self.sub_window.buttonBox.rejected.connect(self.sub_window.close)

    def _clock(self):
        if self.START == True:
            self.counter += 10
            if self.counter  > self.time * 1000 * 2:
                self.counter = 0
            self.my_ploter.myplot(abs(self.counter - self.time * 1000)/(self.time * 1000))


class Mplotcanvas(FigureCanvas):
    def __init__(self, parent = None,  width = 10, height = 10, dpi=100):
        fig = Figure(figsize = (width,height), dpi = dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def myplot(self, i):
        print(i)
        self.axes.cla()
        circle = plt.Circle((0.5,0.5), radius = 0.5, fc = 'blue', alpha = i)
        self.axes.add_patch(circle)
        self.axes.axis('off')
        circle = plt.Circle((0.5,0.5), radius = 0.5, fc = 'green', alpha = 1 -i)
        self.axes.add_patch(circle)
        self.draw()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Main()
    application.show()
    sys.exit(app.exec_())
