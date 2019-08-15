from oceny_gui import Ui_oceny_window
from info_gui import Ui_informacje_window

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frekfencja_window(object):
    
    
    def info_action(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_informacje_window()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def oceny_action(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_oceny_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, frekfencja_window):
        frekfencja_window.setObjectName("frekfencja_window")
        frekfencja_window.resize(500, 600)
        frekfencja_window.setMinimumSize(QtCore.QSize(500, 600))
        frekfencja_window.setMaximumSize(QtCore.QSize(500, 600))
        frekfencja_window.setAutoFillBackground(False)
        frekfencja_window.setStyleSheet("background-color: #1D2226;")
        self.centralwidget = QtWidgets.QWidget(frekfencja_window)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 40, 441, 80))
        self.widget.setObjectName("widget")
        self.btn_oceny = QtWidgets.QPushButton(self.widget)
        self.btn_oceny.setGeometry(QtCore.QRect(10, 20, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_oceny.setFont(font)
        self.btn_oceny.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black")
        self.btn_oceny.setObjectName("btn_oceny")


        self.btn_frekfencja = QtWidgets.QPushButton(self.widget)
        self.btn_frekfencja.setGeometry(QtCore.QRect(120, 20, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_frekfencja.setFont(font)
        self.btn_frekfencja.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid #F0F1F2")
        self.btn_frekfencja.setObjectName("btn_frekfencja")
        self.btn_sprawdziany = QtWidgets.QPushButton(self.widget)
        self.btn_sprawdziany.setGeometry(QtCore.QRect(229, 20, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_sprawdziany.setFont(font)
        self.btn_sprawdziany.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black")
        self.btn_sprawdziany.setObjectName("btn_sprawdziany")
        self.btn_sprawdziany.setVisible(False)
        self.btn_informacje = QtWidgets.QPushButton(self.widget)
        self.btn_informacje.setGeometry(QtCore.QRect(339, 20, 91, 25))
        self.btn_informacje.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black")
        self.btn_informacje.setObjectName("btn_informacje")
        self.btn_informacje.setVisible(True)

        #################### BUTTON EVENT ####################
        self.btn_oceny.clicked.connect(self.oceny_action)
        self.btn_informacje.clicked.connect(self.info_action)

        self.widget_results = QtWidgets.QWidget(self.centralwidget)
        self.widget_results.setEnabled(True)
        self.widget_results.setGeometry(QtCore.QRect(30, 190, 441, 371))
        self.widget_results.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black")
        self.widget_results.setObjectName("widget_results")
        self.label = QtWidgets.QLabel(self.widget_results)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #F0F1F2; border: none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_results)
        self.textBrowser.setGeometry(QtCore.QRect(0, 70, 441, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.widget_results)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #F0F1F2; border: none;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        frekfencja_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(frekfencja_window)
        self.statusbar.setObjectName("statusbar")
        frekfencja_window.setStatusBar(self.statusbar)

        self.retranslateUi(frekfencja_window)
        QtCore.QMetaObject.connectSlotsByName(frekfencja_window)

    def retranslateUi(self, frekfencja_window):
        _translate = QtCore.QCoreApplication.translate
        frekfencja_window.setWindowTitle(_translate("frekfencja_window", "Dzienniczek"))
        self.btn_oceny.setText(_translate("frekfencja_window", "Oceny"))
        self.btn_frekfencja.setText(_translate("frekfencja_window", "Frekfencja"))
        self.btn_sprawdziany.setText(_translate("frekfencja_window", "Sprawdziany"))
        self.btn_informacje.setText(_translate("frekfencja_window", "Informacje"))
        self.label.setText(_translate("frekfencja_window", "Frekfencja"))
        file = open('files/wyniki_frekfencja')
        frekfencja_wyniki = file.read()
        file.close()
        self.textBrowser.setHtml(_translate("oceny_window", frekfencja_wyniki ))
        self.label_2.setText(_translate("frekfencja_window", "godziny obecne|godziny nieobecne|procent"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frekfencja_window = QtWidgets.QMainWindow()
    ui = Ui_frekfencja_window()
    ui.setupUi(frekfencja_window)
    frekfencja_window.show()
    sys.exit(app.exec_())
