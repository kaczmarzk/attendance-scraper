
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_informacje_window(object):


    def setupUi(self, informacje_window):
        informacje_window.setObjectName("informacje_window")
        informacje_window.resize(500, 600)
        informacje_window.setMinimumSize(QtCore.QSize(500, 600))
        informacje_window.setMaximumSize(QtCore.QSize(500, 600))
        informacje_window.setAutoFillBackground(False)
        informacje_window.setStyleSheet("background-color: #1D2226;")
        self.centralwidget = QtWidgets.QWidget(informacje_window)
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
        self.btn_oceny.setVisible(False)
        self.btn_frekfencja = QtWidgets.QPushButton(self.widget)
        self.btn_frekfencja.setGeometry(QtCore.QRect(120, 20, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_frekfencja.setFont(font)
        self.btn_frekfencja.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black")
        self.btn_frekfencja.setObjectName("btn_frekfencja")
        self.btn_frekfencja.setVisible(False)
        self.btn_sprawdziany = QtWidgets.QPushButton(self.widget)
        self.btn_sprawdziany.setEnabled(True)
        self.btn_sprawdziany.setGeometry(QtCore.QRect(229, 20, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_sprawdziany.setFont(font)
        self.btn_sprawdziany.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black")
        self.btn_sprawdziany.setObjectName("btn_sprawdziany")
        self.btn_sprawdziany.setVisible(False)
        self.btn_informacje = QtWidgets.QPushButton(self.widget)
        self.btn_informacje.setGeometry(QtCore.QRect(339, 20, 91, 25))
        self.btn_informacje.setAccessibleDescription("")
        self.btn_informacje.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid #F0F1F2")
        self.btn_informacje.setObjectName("btn_informacje")
        self.btn_informacje.setVisible(False)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 100, 441, 350))
        self.textBrowser.setObjectName("textBrowser")
        informacje_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(informacje_window)
        self.statusbar.setObjectName("statusbar")
        informacje_window.setStatusBar(self.statusbar)



        self.retranslateUi(informacje_window)
        QtCore.QMetaObject.connectSlotsByName(informacje_window)

    def retranslateUi(self, informacje_window):
        _translate = QtCore.QCoreApplication.translate
        informacje_window.setWindowTitle(_translate("informacje_window", "Dzienniczek "))
        self.btn_oceny.setText(_translate("informacje_window", "Oceny"))
        self.btn_frekfencja.setText(_translate("informacje_window", "Frekfencja"))
        self.btn_sprawdziany.setText(_translate("informacje_window", "Sprawdziany"))
        self.btn_informacje.setText(_translate("informacje_window", "Informacje"))
        self.textBrowser.setHtml(_translate("informacje_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#eeeeec;\">Frekfencja</span><span style=\" color:#eeeeec;\"> </span><span style=\" font-style:italic; color:#eeeeec;\">jest pobierana z całego roku szkolnego, od pierwszego dnia szkoły do dziś.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic; color:#eeeeec;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#eeeeec;\">Oceny</span><span style=\" font-style:italic; color:#eeeeec;\"> są dokładnie takie same jak na idzienniku. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic; color:#eeeeec;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic; color:#eeeeec;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic; color:#eeeeec;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic; color:#eeeeec;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#eeeeec;\">Program został stworzony przez ucznia klasy</span><span style=\" font-weight:600; font-style:italic; color:#eeeeec;\"> 4TI - 2019/2020</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic; color:#eeeeec;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#2e3436;\">kod źródłowy programu: </span><span style=\" font-weight:600; font-style:italic; color:#2e3436;\">github.com/kczmvk/Dzienniczek</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    informacje_window = QtWidgets.QMainWindow()
    ui = Ui_informacje_window()
    ui.setupUi(informacje_window)
    informacje_window.show()
    sys.exit(app.exec_())
