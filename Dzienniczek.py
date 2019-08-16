
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep as wait
import sys
from error import Ui_error_window





#################################################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os
from urllib.request import urlretrieve
from pathlib import Path



class Ui_MainWindow(object):

    def shutdown(self):
        print('zamkniecie drivera')
        # wait(1)
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
        data = open('files/data', 'w+')
        data.write(self.login + '\n' + self.password)

    def obecnosci(self):

        if os.path.exists('files/obecnosci.html'):
            os.remove('files/obecnosci.html')

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

        do_wrzesnia = odlicz()
        for i in range(do_wrzesnia):
            wait(0.5)
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="tabelaObecnosci"]')))
            obecnosci_text = self.driver.find_element_by_xpath(
                '//*[@id="tabelaObecnosci"]').get_attribute('innerHTML')
            print('pobrano_miesiac')
            # nazwa_miesiaca = 'months/miesiac' + str(i) + '.html'
            obecnosci_file = open('files/obecnosci.html', 'a')
            obecnosci_file.write(obecnosci_text + '\n\n #################### \n\n')
            obecnosci_file.close()
            self.driver.execute_script("javascript:prevMonth()")



    def oceny(self):
        self.driver.find_element_by_id('btn_oceny').click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/form/table/tbody/tr[5]/td/div/table[1]/tbody/tr[5]')))
        oceny_html = self.driver.find_element_by_xpath(
            '/html/body/div[1]/form/table/tbody/tr[5]/td/div/table[1]/tbody').get_attribute('outerHTML')

        print('pobrano oceny')
        oceny_file = open('files/oceny.html', 'w+')
        oceny_file.write(oceny_html)
        oceny_file.close()

    def start_website(self):
        url = 'https://iuczniowie.progman.pl/idziennik/login.aspx?ReturnUrl=%2fidziennik%2fuser'
        try:
            self.driver = webdriver.Firefox()
        except:
            self.driver = webdriver.Chrome('/path/to/chromedriver')
        self.driver.get(url)
        img = self.driver.find_element_by_id('imgCaptcha')
        src = img.get_attribute('src')
        urlretrieve(src, 'images/captcha')

    def check_successful_log_in(self):
        if self.driver.current_url == 'https://iuczniowie.progman.pl/idziennik/login.aspx?ReturnUrl=%2fidziennik%2fuser':
            return False

    def login_failed(self):
        self.error_login.setStyleSheet("color: #D92525;")



    #################### KOD PROGRAMU ####################

    def check_log_in(self):
        if self.dane_checkbox.isChecked():
            self.shutdown()
            self.open_app()
        else:
            try:
                _translate = QtCore.QCoreApplication.translate
                self.login_button.setVisible(False)
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
                    self.error_login.setText(_translate("MainWindow", "Trwa ładowanie ..."))
                    self.error_login.setStyleSheet("color: #F0F1F2;")
                    login_key = self.driver.find_element_by_id('UserName')
                    password_key = self.driver.find_element_by_id('Password')
                    school_key = self.driver.find_element_by_id('NazwaSzkoly')
                    captcha_key = self.driver.find_element_by_id('captcha')
                    self.driver.find_element_by_id('UserName').clear()
                    self.driver.find_element_by_id('Logowanie')
                    login_key.send_keys(self.login)
                    password_key.send_keys(self.password)
                    school_key.send_keys('zsotlubliniec')
                    captcha_key.send_keys(captcha)
                    self.driver.find_element_by_id('Logowanie').click()
                    # os.remove('images/captcha')  # remove captcha after log in
                    successful_login = self.check_successful_log_in()
                    if successful_login is False:
                        self.error_login.setText(_translate("MainWindow", "Blad przy logowaniu"))
                        self.login_failed()
                        wait(2)
                        self.driver.quit()
                        self.open_error()

                    else:
                        self.save_login()
                        self.oceny()
                        self.obecnosci()  #
                        self.shutdown()

                        import parse
                        parse.pobierz_oceny()
                        parse.pobierz_frekfencje()
                        self.open_app()
            except Exception as error_log:
                print('blad przy ladowaniu')
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
        MainWindow.setStyleSheet("background-color: #1D2226;")
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


        #################### autocomplete data ####################

        file = Path("files/data")
        if file.is_file():
            self.my_data = open('files/data')
            data_tab = []
            for line in self.my_data:
                data_tab.append(str(line).rstrip())
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
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #F0F1F2")
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.log_in)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 54, 31))
        font = QtGui.QFont()
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
        font.setPointSize(11)
        self.login_button.setFont(font)
        self.login_button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.login_button.setStyleSheet("background-color: #1D2226; color: #F0F1F2 ; border: 1px solid black")
        self.login_button.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        self.login_button.setFlat(False)
        self.login_button.setObjectName("login_button")
        self.widget_captcha = QtWidgets.QWidget(self.centralwidget)
        self.widget_captcha.setGeometry(QtCore.QRect(20, 490, 111, 71))
        self.widget_captcha.setObjectName("widget_captcha")
        self.captcha_label = QtWidgets.QLabel(self.widget_captcha)
        self.captcha_label.setGeometry(QtCore.QRect(20, 10, 71, 21))
        font = QtGui.QFont()
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
        font.setPointSize(11)
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

        self.dane_checkbox.setGeometry(QtCore.QRect(310, 540, 161, 20))
        self.dane_checkbox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dane_checkbox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.dane_checkbox.setStyleSheet("color: #F0F1F2;")
        self.dane_checkbox.setChecked(False)
        self.dane_checkbox.setTristate(False)
        self.dane_checkbox.setObjectName("dane_checkbox")
        self.dane_checkbox.setVisible(True)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dzienniczek"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Hasło"))
        self.login_button.setText(_translate("MainWindow", "Zaloguj"))
        # self.error_login.setText(_translate("MainWindow", "Nie udało się zalogować"))
        self.dane_checkbox.setText(_translate("MainWindow", "Nie ładuj nowych danych"))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.start_website()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())



