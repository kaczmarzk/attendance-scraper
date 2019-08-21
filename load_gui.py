# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_load_window(object):
    def setupUi(self, app_window):
        app_window.setObjectName("app_window")
        app_window.resize(500, 600)
        app_window.setMinimumSize(QtCore.QSize(500, 600))
        app_window.setMaximumSize(QtCore.QSize(500, 600))
        app_window.setAutoFillBackground(False)
        app_window.setStyleSheet("background-color: #181F27;")
        app_window.setWindowIcon(QtGui.QIcon('images/icon.ico'))
        self.centralwidget = QtWidgets.QWidget(app_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 90, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: #F2F2F2; background-color: #181F27;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.loading_frame = QtWidgets.QLabel(self.centralwidget)
        self.loading_frame.setGeometry(QtCore.QRect(77, 270, 345, 258))
        self.loading_frame.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.loading_frame.setFrameShadow(QtWidgets.QLabel.Raised)
        self.loading_frame.setObjectName("loading_frame")
        self.movie = QtGui.QMovie("images/loading.gif")
        self.movie.start()
        self.loading_frame.setMovie(self.movie)
        app_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(app_window)
        self.statusbar.setObjectName("statusbar")
        app_window.setStatusBar(self.statusbar)

        self.retranslateUi(app_window)
        QtCore.QMetaObject.connectSlotsByName(app_window)

    def retranslateUi(self, app_window):
        _translate = QtCore.QCoreApplication.translate
        app_window.setWindowTitle(_translate("app_window", "Dzienniczek"))
        self.label.setText(_translate("app_window", "Pobieranie danych ze strony"))

def run_me():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_load_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

