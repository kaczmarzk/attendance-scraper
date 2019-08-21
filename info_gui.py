
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_informacje_window(object):
	def setupUi(self, informacje_window):
		informacje_window.setObjectName("informacje_window")
		informacje_window.resize(500, 600)
		informacje_window.setMinimumSize(QtCore.QSize(500, 600))
		informacje_window.setMaximumSize(QtCore.QSize(500, 600))
		informacje_window.setAutoFillBackground(False)
		informacje_window.setStyleSheet("background-color: #181F27;")
		informacje_window.setWindowIcon(QtGui.QIcon('images/icon.ico'))
		self.centralwidget = QtWidgets.QWidget(informacje_window)
		self.centralwidget.setObjectName("centralwidget")
		self.widget = QtWidgets.QWidget(self.centralwidget)
		self.widget.setGeometry(QtCore.QRect(30, 40, 441, 80))
		self.widget.setObjectName("widget")
		self.btn_oceny = QtWidgets.QPushButton(self.widget)
		self.btn_oceny.setGeometry(QtCore.QRect(10, 20, 91, 25))
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI")
		font.setPointSize(8)
		self.btn_oceny.setFont(font)
		self.btn_oceny.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black")
		self.btn_oceny.setObjectName("btn_oceny")
		self.btn_oceny.setVisible(False)
		self.btn_frekfencja = QtWidgets.QPushButton(self.widget)
		self.btn_frekfencja.setGeometry(QtCore.QRect(120, 20, 91, 25))
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI")
		font.setPointSize(8)
		self.btn_frekfencja.setFont(font)
		self.btn_frekfencja.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black")
		self.btn_frekfencja.setObjectName("btn_frekfencja")
		self.btn_frekfencja.setVisible(False)
		self.btn_sprawdziany = QtWidgets.QPushButton(self.widget)
		self.btn_sprawdziany.setEnabled(True)
		self.btn_sprawdziany.setGeometry(QtCore.QRect(229, 20, 91, 25))
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI")
		font.setPointSize(8)
		self.btn_sprawdziany.setFont(font)
		self.btn_sprawdziany.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black")
		self.btn_sprawdziany.setObjectName("btn_sprawdziany")
		self.btn_sprawdziany.setVisible(False)
		self.btn_terminy = QtWidgets.QPushButton(self.widget)
		self.btn_terminy.setGeometry(QtCore.QRect(339, 20, 91, 25))
		self.btn_terminy.setAccessibleDescription("")
		self.btn_terminy.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid #F0F1F2; ")
		self.btn_terminy.setObjectName("btn_terminy")
		self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
		self.textBrowser.setGeometry(QtCore.QRect(30,150, 441, 400))
		self.textBrowser.setObjectName("textBrowser")
		informacje_window.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(informacje_window)
		self.statusbar.setObjectName("statusbar")
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI")
		font.setPointSize(10)
		self.textBrowser.setFont(font)
		informacje_window.setStatusBar(self.statusbar)

		self.retranslateUi(informacje_window)
		QtCore.QMetaObject.connectSlotsByName(informacje_window)

	def retranslateUi(self, informacje_window):
		_translate = QtCore.QCoreApplication.translate
		informacje_window.setWindowTitle(_translate("informacje_window", "Dzienniczek"))
		self.btn_oceny.setText(_translate("informacje_window", "Oceny"))
		self.btn_frekfencja.setText(_translate("informacje_window", "Frekfencja"))
		self.btn_sprawdziany.setText(_translate("informacje_window", "Sprawdziany"))
		self.btn_terminy.setText(_translate("informacje_window", "Informacje"))
		self.textBrowser.setHtml(_translate("informacje_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Yu Gothic UI\'; font-size:11pt; font-weight:400; font-style:normal;\" bgcolor=\"#1d2226\">\n"
"<p align=\"center\" style=\" margin-top:40px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Yu Gothic UI\'; font-size:8pt; color:#f0f1f2;\">Aplikacja powstała z inicjatywy oraz pomysłu klasy </span><span style=\" font-family:\'Yu Gothic UI\'; font-size:8pt; font-weight:600; color:#f0f1f2;\">4TI - 2019/2020</span><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; font-style:italic; color:#f0f1f2;\"> </span></p>\n"
"<h4 align=\"center\" style=\" margin-top:20px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Yu Gothic UI\'; font-size:8pt; font-weight:600; color:#f0f1f2;\">Informacje: </span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; color:#f0f1f2;\">Wszystkie informacje powinny się z tymi z idziennika, autor nie odpowiada za </span><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; font-weight:600; color:#f0f1f2;\">możliwe błędy </span><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; color:#f0f1f2;\"> oraz </span><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; font-weight:600; color:#f0f1f2;\">skutki korzystania z aplikacji. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; color:#f0f1f2;\">Sposób obliczania frekfencji procentowej był tworzony z pomocą nauczyciela naszej szkoły. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; color:#f0f1f2;\">Używanie programu jest w pełni bezpieczne. Wszystkie dane zapisywane są lokalnie na komputerze uzytkownika. Aplikacja wymaga tylko dostępu do internetu oraz praw do zapisu plików. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; color:#f0f1f2;\">Aplikacja jest cały czas wspierana, jeżeli widzisz jakieś błędy zgłoś je na maila: </span><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; font-weight:600; color:#f0f1f2;\">kaczmarzvk@gmail.com </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; color:#f0f1f2;\">Cały kod programu jest dostępny w formie Open Source. Oznacza to że każdą linijkę programu możesz przejrzeć na stronie </span><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; font-weight:600; color:#d9d9d9;\">github.com/kczmvk/Dzienniczek </span><span style=\" font-family:\'Yu Gothic UI\'; font-size:7pt; color:#f0f1f2;\">oraz zmodyfikować kod na własne potrzeby. </span></p>\n"
"<p align=\"center\" style=\" margin-top:20px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Yu Gothic UI\'; font-size:8pt; color:#f0f1f2;\">Wykonanie: </span><span style=\" font-family:\'Yu Gothic UI\'; font-size:8pt; font-weight:600; color:#d9d9d9;\">kczmvk </span></p></body></html>"))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	informacje_window = QtWidgets.QMainWindow()
	ui = Ui_informacje_window()
	ui.setupUi(informacje_window)
	informacje_window.show()
	sys.exit(app.exec_())