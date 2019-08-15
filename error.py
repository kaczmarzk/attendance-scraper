
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_error_window(object):

    def setupUi(self, error_window):
        error_window.setObjectName("error_window")
        error_window.resize(500, 600)
        error_window.setMinimumSize(QtCore.QSize(500, 600))
        error_window.setMaximumSize(QtCore.QSize(500, 600))
        error_window.setAutoFillBackground(False)
        error_window.setStyleSheet("background-color: #1D2226;")
        self.centralwidget = QtWidgets.QWidget(error_window)
        self.centralwidget.setObjectName("centralwidget")
        self.line1 = QtWidgets.QLabel(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(0, 70, 501, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.line1.setFont(font)
        self.line1.setStyleSheet("color: #D92525;")
        self.line1.setAlignment(QtCore.Qt.AlignCenter)
        self.line1.setObjectName("line1")
        self.zamknij_btn = QtWidgets.QPushButton(self.centralwidget)
        self.zamknij_btn.setGeometry(QtCore.QRect(190, 490, 121, 51))
        self.zamknij_btn.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black")
        self.zamknij_btn.setObjectName("zamknij_btn")
        self.line2 = QtWidgets.QLabel(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(0, 390, 501, 25))
        self.line2.setStyleSheet("color: #D92525;")
        self.line2.setAlignment(QtCore.Qt.AlignCenter)
        self.line2.setObjectName("line2")
        self.logo_label_zsot = QtWidgets.QLabel(self.centralwidget)
        self.logo_label_zsot.setGeometry(QtCore.QRect(100, 186, 301, 111))
        self.logo_label_zsot.setText("")
        self.logo_label_zsot.setPixmap(QtGui.QPixmap(""))
        self.logo_label_zsot.setScaledContents(True)
        self.logo_label_zsot.setObjectName("logo_label_zsot")
        error_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(error_window)
        self.statusbar.setObjectName("statusbar")
        error_window.setStatusBar(self.statusbar)

        self.retranslateUi(error_window)
        QtCore.QMetaObject.connectSlotsByName(error_window)

    def retranslateUi(self, error_window):
        _translate = QtCore.QCoreApplication.translate
        error_window.setWindowTitle(_translate("error_window", "Dzienniczek"))
        self.line1.setText(_translate("error_window", "Nie udało się zalogować do idziennika."))
        self.zamknij_btn.setText(_translate("error_window", "Zamknij"))
        self.zamknij_btn.clicked.connect(error_window.close)
        self.line2.setText(_translate("error_window", "Jednym z powodów mogły być niezgadząjące się dane"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error_window = QtWidgets.QMainWindow()
    ui = Ui_error_window()
    ui.setupUi(error_window)
    error_window.show()
    sys.exit(app.exec_())

