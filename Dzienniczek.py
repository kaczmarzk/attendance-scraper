# -*- coding: utf-8 -*-

import fix_qt5  # import to fix  pyinstaller qt5
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep as wait
import sys
from error import Ui_error_window
import base64 as pyCy
from load_gui import Ui_load_window

#################################################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re
import os
from urllib.request import urlretrieve
from pathlib import Path
from PyQt5.QtCore import pyqtSignal


class Ui_MainWindow(object):

	def shutdown(self):
		print('zamkniecie drivera')
		self.driver.close()

	def open_error(self):
		MainWindow.hide()
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_error_window()
		self.ui.setupUi(self.window)
		self.window.show()

	def open_app(self):
		from frekfencja_gui import Ui_frekfencja_window
		MainWindow.hide()
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_frekfencja_window()
		self.ui.setupUi(self.window)
		self.window.show()

	def save_login(self):
		def fencode(string):
			encoded_string = string.encode()
			encoded = pyCy.b64encode(encoded_string)
			return encoded
		data = open('files/data', 'wb+')
		data.write(fencode(self.login) + b'\n' + fencode(self.password))

	def obecnosci(self):

		if os.path.exists('files/obecnosci.html'):
			os.remove('files/obecnosci.html')
		WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
			(By.ID, 'btn_obecnosci')))
		self.driver.find_element_by_id('btn_obecnosci').click()
		wait(1)
		self.driver.execute_script("javascript:switchTab(this, 1)")

		def odlicz():
			import datetime
			datetime = datetime.datetime.now()
			now_month = datetime.month
			do_wrzesnia = 0
			if now_month > 9:
				for i in range(now_month - 9):
					do_wrzesnia += 1
			elif now_month < 9:
				for i in range(now_month + 3):
					do_wrzesnia += 1
			elif now_month == 9:
				do_wrzesnia = 0
			return do_wrzesnia

		do_wrzesnia = odlicz() + 1  # for september + one month
		for i in range(do_wrzesnia):
			wait(0.5)
			try:
				self.driver.execute_script("javascript:switchTab(this, 1)")
				print('naprawiono blad widoku')
			except:
				pass
			WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
				(By.XPATH, '//*[@id="tabelaObecnosci"]')))
			obecnosci_text = self.driver.find_element_by_xpath(
				'//*[@id="tabelaObecnosci"]').get_attribute('innerHTML')
			print('pobrano_miesiac')
			obecnosci_file = open('files/obecnosci.html', 'a', encoding='utf-8')
			obecnosci_file.write(obecnosci_text + '\n\n #################### \n\n')
			obecnosci_file.close()
			self.driver.execute_script("javascript:prevMonth()")
			wait(0.5)

	def oceny(self):
		self.driver.find_element_by_id('btn_oceny').click()
		WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
			(By.XPATH, '/html/body/div[1]/form/table/tbody/tr[5]/td/div/table[1]/tbody/tr[5]')))
		oceny_html = self.driver.find_element_by_xpath(
			'/html/body/div[1]/form/table/tbody/tr[5]/td/div/table[1]/tbody').get_attribute('outerHTML')

		print('pobrano oceny')
		oceny_file = open('files/oceny.html', 'w+', encoding='utf-8')
		oceny_file.write(oceny_html)
		oceny_file.close()

	def start_website(self):
		self.url = 'https://iuczniowie.progman.pl/idziennik/login.aspx?ReturnUrl=%2fidziennik%2fuser'
		fp = webdriver.FirefoxProfile()
		options = Options()
		options.headless = True  # True to hide a web browser
		self.driver = webdriver.Firefox(options = options, firefox_binary="webbrowser//firefox.exe", firefox_profile=fp,
										executable_path='files//geckodriver.exe')
		self.driver.get(self.url)
		img = self.driver.find_element_by_id('imgCaptcha')

		src = img.get_attribute('src')
		location = 'images/captcha'
		urlretrieve(src, location)


	def login_failed(self):
		self.error_login.setStyleSheet("color: #D92525;")



#################### MAIN CODE ####################
	def loading(self):
		MainWindow.hide()
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_load_window()
		self.ui.setupUi(self.window)
		self.window.show()

	def check_log_in(self):
		if self.dane_checkbox.isChecked():
			self.shutdown()
			self.open_app()
		else:
			try:
				_translate = QtCore.QCoreApplication.translate
				self.login = self.line_login.text()
				self.password = self.line_pass.text()
				captcha = self.captcha_line.text()
				if ' ' in self.login or ' ' in self.password:
					self.error_login.setText(_translate("MainWindow", "Spacja w danych"))
					self.login_failed()
				elif self.login == '' or self.password == '':
					self.error_login.setText(_translate("MainWindow", "Uzupełnij dane logowania"))
					self.login_failed()
				elif ' ' in captcha:
					self.error_login.setText(_translate("MainWindow", "Spacja w captcha"))
					self.login_failed()
				elif captcha == '':
					self.error_login.setText(_translate("MainWindow", "Uzupełnij captcha"))
					self.login_failed()
				else:
						school_name = self.driver.find_element_by_xpath('//*[@id="NazwaSzkoly"]')
						school_name.clear()
						school_name.send_keys('zsotlubliniec')
						user_name = self.driver.find_element_by_xpath('//*[@id="UserName"]')
						user_name.clear()
						user_name.send_keys(self.login)
						password = self.driver.find_element_by_xpath('//*[@id="Password"]')
						password.clear()
						password.send_keys(self.password)
						captcha_input = self.driver.find_element_by_xpath('//*[@id="captcha"]')
						captcha_input.clear()
						captcha_input.send_keys(captcha)
						logowanie_btn = self.driver.find_element_by_id('Logowanie')
						logowanie_btn.click()

						if self.driver.current_url == self.url:
							print('nieprawidlowe dane logowania')
							self.error_login.setText(_translate("MainWindow", "Blad przy logowaniu"))
							self.login_failed()
							self.driver.quit()
							self.open_error()

						else:
							MainWindow.hide()
							self.save_login()
							self.oceny()
							self.obecnosci()  #
							self.shutdown()

							import parse
							parse.pobierz_oceny()
							parse.pobierz_frekfencje()
							self.open_app()
			except Exception as error_log:
				print('blad podczas ladowania')
				self.shutdown()
				self.open_error()
				print(error_log)


##################################################

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(500, 600)
		MainWindow.setMinimumSize(QtCore.QSize(500, 600))
		MainWindow.setMaximumSize(QtCore.QSize(500, 600))
		MainWindow.setAutoFillBackground(False)
		MainWindow.setStyleSheet("background-color: #181F27;")
		MainWindow.setWindowIcon(QtGui.QIcon('images/icon.ico'))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.log_in = QtWidgets.QWidget(self.centralwidget)
		self.log_in.setGeometry(QtCore.QRect(100, 200, 300, 191))
		self.log_in.setMinimumSize(QtCore.QSize(300, 0))
		self.log_in.setMaximumSize(QtCore.QSize(300, 16777215))
		self.log_in.setAutoFillBackground(False)
		self.log_in.setObjectName("log_in")
		self.line_login = QtWidgets.QLineEdit(self.log_in)
		self.line_login.setGeometry(QtCore.QRect(50, 60, 201, 25))
		self.line_login.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.line_login.setAutoFillBackground(False)
		self.line_login.setStyleSheet("color: #F0F1F2; border: 1px solid black")
		self.line_login.setObjectName("lineEdit")


		#################### AUTOCOMPLETE DATA ####################

		file = Path("files/data")
		if file.is_file():
			def fdecode(string):
				encoded_string = string.encode()
				decoded = pyCy.b64decode(encoded_string)
				decoded_string = decoded.decode()
				return decoded_string
			self.my_data = open('files/data', 'r')
			data_tab = []
			for line in self.my_data:
				x = fdecode(line)
				data_tab.append(x)
			self.line_login.setText(data_tab[0])
		self.line_pass = QtWidgets.QLineEdit(self.log_in)
		self.line_pass.setGeometry(QtCore.QRect(50, 140, 201, 25))
		self.line_pass.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.line_pass.setAutoFillBackground(False)
		self.line_pass.setStyleSheet("color: #F0F1F2; border: 1px solid black")
		self.line_pass.setEchoMode(QtWidgets.QLineEdit.Password)
		self.line_pass.setObjectName("lineEdit_2")
		if file.is_file():
			self.line_pass.setText(data_tab[1])
		self.label = QtWidgets.QLabel(self.log_in)
		self.label.setGeometry(QtCore.QRect(120, 20, 54, 31))
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI")
		font.setPointSize(12)
		self.label.setFont(font)
		self.label.setStyleSheet("color: #F0F1F2")
		self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.log_in)
		self.label_2.setGeometry(QtCore.QRect(120, 100, 54, 31))
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI")
		font.setPointSize(12)
		self.label_2.setFont(font)
		self.label_2.setStyleSheet("color: #F0F1F2;")
		self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(140, 50, 221, 91))
		self.label_3.setText("")
		self.label_3.setPixmap(QtGui.QPixmap("images/white-logo.png"))
		self.label_3.setScaledContents(True)
		self.label_3.setObjectName("label_3")
		self.login_button = QtWidgets.QPushButton(self.centralwidget)
		self.login_button.setGeometry(QtCore.QRect(200, 450, 100, 32))
		self.login_button.setMinimumSize(QtCore.QSize(100, 32))
		self.login_button.setMaximumSize(QtCore.QSize(100, 32))

		#################### BUTTON EVENT ####################
		self.login_button.clicked.connect(self.check_log_in)


		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI")
		font.setPointSize(10)
		self.login_button.setFont(font)
		self.login_button.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.login_button.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black; border-radius: 6px;")
		self.login_button.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
		self.login_button.setFlat(False)
		self.login_button.setObjectName("login_button")
		self.widget_captcha = QtWidgets.QWidget(self.centralwidget)
		self.widget_captcha.setGeometry(QtCore.QRect(20, 490, 111, 71))
		self.widget_captcha.setObjectName("widget_captcha")
		self.captcha_label = QtWidgets.QLabel(self.widget_captcha)
		self.captcha_label.setGeometry(QtCore.QRect(20, 10, 71, 21))
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI")
		font.setPointSize(11)
		self.captcha_label.setFont(font)
		self.captcha_label.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
		self.captcha_label.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.captcha_label.setAutoFillBackground(False)
		self.captcha_label.setStyleSheet("background-color: #F0F1F2; ")
		self.captcha_label.setAlignment(QtCore.Qt.AlignCenter)
		self.captcha_label.setObjectName("captcha_label")
		self.captcha_label.setPixmap(QtGui.QPixmap("images/captcha"))
		self.captcha_line = QtWidgets.QLineEdit(self.widget_captcha)
		self.captcha_line.setEnabled(True)
		self.captcha_line.setGeometry(QtCore.QRect(10, 40, 91, 21))
		self.captcha_line.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.captcha_line.setStyleSheet("color: #F0F1F2; border: 1px solid black")
		self.captcha_line.setObjectName("captcha_line")
		self.error_login = QtWidgets.QLabel(self.centralwidget)
		self.error_login.setGeometry(QtCore.QRect(160, 410, 181, 21))
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI")
		font.setPointSize(9)
		font.setBold(False)
		font.setWeight(50)
		self.error_login.setFont(font)
		self.error_login.setStyleSheet("color: #1D2226;")
		self.error_login.setAlignment(QtCore.Qt.AlignCenter)
		self.error_login.setObjectName("error_login")
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.dane_checkbox = QtWidgets.QCheckBox(self.centralwidget)
		file = Path("files/wyniki_frekfencja")
		if file.is_file():
			self.dane_checkbox.setEnabled(True)
		else:
			self.dane_checkbox.setEnabled(False)

		self.dane_checkbox.setGeometry(QtCore.QRect(320, 540, 180, 20))
		self.dane_checkbox.setFocusPolicy(QtCore.Qt.NoFocus)
		self.dane_checkbox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.dane_checkbox.setStyleSheet("color: #F0F1F2;")
		self.dane_checkbox.setChecked(False)
		self.dane_checkbox.setTristate(False)
		self.dane_checkbox.setObjectName("dane_checkbox")
		self.dane_checkbox.setVisible(True)
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI")
		font.setPointSize(8)
		self.error_login.setFont(font)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Dzienniczek"))
		self.label.setText(_translate("MainWindow", "Login"))
		self.label_2.setText(_translate("MainWindow", "Hasło"))
		self.login_button.setText(_translate("MainWindow", "Zaloguj"))
		# self.error_login.setText(_translate("MainWindow", "Nie udało się zalogować"))
		self.dane_checkbox.setText(_translate("MainWindow", "Bez aktualizacji danych"))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.start_website()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
