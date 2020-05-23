#!/bin/python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_manager.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import datetime
import random
import string

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def loadData(self):
        query = "SELECT * FROM password"
        result = self.conn.execute(query)
        self.table_data.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table_data.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_data.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def setupUi(self, MainWindow):
        self.conn = sqlite3.connect('password_manager.db')
        self.c = self.conn.cursor()
        self.c.execute("ATTACH DATABASE 'password_manager.db' AS plaintext KEY '';")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data-lock.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(0, 0, 931, 80))
        self.top_frame.setStyleSheet("background-color: rgb(116, 116, 116);")
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.label_title = QtWidgets.QLabel(self.top_frame)
        self.label_title.setGeometry(QtCore.QRect(90, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label = QtWidgets.QLabel(self.top_frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 61, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("w-lan.png"))
        self.label.setObjectName("label")
        self.button_load = QtWidgets.QPushButton(self.top_frame)
        self.button_load.setGeometry(QtCore.QRect(800, 50, 75, 23))
        self.button_load.setObjectName("button_load")
        self.button_load.clicked.connect(self.loadData)
        self.table_data = QtWidgets.QTableWidget(self.centralwidget)
        self.table_data.setGeometry(QtCore.QRect(190, 80, 721, 591))
        self.table_data.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_data.setLineWidth(1)
        self.table_data.setMidLineWidth(1)
        self.table_data.setRowCount(20)
        self.table_data.setColumnCount(4)
        self.table_data.setObjectName("table_data")
        self.table_data.horizontalHeader().setCascadingSectionResizes(True)
        self.table_data.horizontalHeader().setDefaultSectionSize(170)
        self.table_data.horizontalHeader().setHighlightSections(True)
        self.table_data.horizontalHeader().setSortIndicatorShown(False)
        self.table_data.horizontalHeader().setStretchLastSection(False)
        self.table_data.verticalHeader().setCascadingSectionResizes(False)
        self.table_data.verticalHeader().setHighlightSections(True)
        self.table_data.verticalHeader().setStretchLastSection(False)
        self.table_data.cellClicked.connect(self.database_get_row_column)
        self.left_widget = QtWidgets.QWidget(self.centralwidget)
        self.left_widget.setGeometry(QtCore.QRect(0, 80, 191, 601))
        self.left_widget.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.left_widget.setObjectName("left_widget")
        self.label_title_add = QtWidgets.QLabel(self.left_widget)
        self.label_title_add.setGeometry(QtCore.QRect(10, 0, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_title_add.setFont(font)
        self.label_title_add.setObjectName("label_title_add")
        self.input_website = QtWidgets.QLineEdit(self.left_widget)
        self.input_website.setGeometry(QtCore.QRect(10, 70, 141, 20))
        self.input_website.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_website.setText("")
        self.input_website.setObjectName("input_website")
        self.label_website = QtWidgets.QLabel(self.left_widget)
        self.label_website.setGeometry(QtCore.QRect(10, 50, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_website.setFont(font)
        self.label_website.setObjectName("label_website")
        self.label_name = QtWidgets.QLabel(self.left_widget)
        self.label_name.setGeometry(QtCore.QRect(10, 110, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.input_name = QtWidgets.QLineEdit(self.left_widget)
        self.input_name.setGeometry(QtCore.QRect(10, 130, 141, 20))
        self.input_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_name.setText("")
        self.input_name.setObjectName("input_name")
        self.label_password = QtWidgets.QLabel(self.left_widget)
        self.label_password.setGeometry(QtCore.QRect(10, 180, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.label_password_length = QtWidgets.QLabel(self.left_widget)
        self.label_password_length.setGeometry(QtCore.QRect(10, 210, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_password_length.setFont(font)
        self.label_password_length.setObjectName("label_password_length")
        self.input_length_password = QtWidgets.QLineEdit(self.left_widget)
        self.input_length_password.setGeometry(QtCore.QRect(10, 230, 141, 20))
        self.input_length_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_length_password.setText("")
        self.input_length_password.setObjectName("input_length_password")
        self.label_password_length_2 = QtWidgets.QLabel(self.left_widget)
        self.label_password_length_2.setGeometry(QtCore.QRect(10, 250, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_password_length_2.setFont(font)
        self.label_password_length_2.setObjectName("label_password_length_2")
        self.input_new_password = QtWidgets.QLineEdit(self.left_widget)
        self.input_new_password.setGeometry(QtCore.QRect(10, 270, 141, 20))
        self.input_new_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_new_password.setText("")
        self.input_new_password.setObjectName("input_new_password")
        self.button_generate_password = QtWidgets.QPushButton(self.left_widget)
        self.button_generate_password.setGeometry(QtCore.QRect(10, 300, 101, 23))
        self.button_generate_password.setObjectName("button_generate_password")
        self.button_generate_password.clicked.connect(self.generate_password)
        self.button_add_row = QtWidgets.QPushButton(self.left_widget)
        self.button_add_row.setGeometry(QtCore.QRect(10, 450, 151, 21))
        self.button_add_row.setObjectName("button_add_row")
        self.button_add_row.clicked.connect(self.instert_data)
        self.button_delete_row = QtWidgets.QPushButton(self.left_widget)
        self.button_delete_row.setGeometry(QtCore.QRect(10, 480, 151, 23))
        self.button_delete_row.setObjectName("button_delete_row")
        self.button_delete_row.clicked.connect(self.delete_data)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Password manager"))
        self.button_load.setText(_translate("MainWindow", "Load data"))
        self.label_title_add.setText(_translate("MainWindow", "Add a new password"))
        self.label_website.setText(_translate("MainWindow", "Website"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.label_password_length.setText(_translate("MainWindow", "Length of the password"))
        self.label_password_length_2.setText(_translate("MainWindow", "New password"))
        self.button_generate_password.setText(_translate("MainWindow", "Generate password"))
        self.button_add_row.setText(_translate("MainWindow", "Add data"))
        self.button_delete_row.setText(_translate("MainWindow", "Delete data"))

    def instert_data(self):
        website = self.input_website.text()
        name = str(self.input_name.text())
        password = str(self.input_new_password.text())
        date = str(datetime.datetime.today().strftime('%d.%m.%Y %H:%M:%S'))

        # Name, Webiste, Password, Adress
        # 'name', 'website', 'password', 'date'
        insert_values = " ' " + name + " ',' " + website + " ',' " + password + " ',' " + date + " ' "
        insert = "INSERT INTO password VALUES (" + insert_values + ")"
        self.conn.execute(insert)
        self.conn.commit()
        self.loadData()

    def database_get_row_column(self):
        self.row = self.table_data.currentRow()
        self.column = self.table_data.currentColumn()
        item = self.table_data.item(self.row, self.column)
        self.ID = item.text()
        self.column = self.database_column(self.column)

    def delete_data(self):
        insert = "DELETE FROM password WHERE " + self.column + "='" + self.ID + "'"
        self.conn.execute(insert)
        self.conn.commit()
        self.loadData()

    def database_column(self, column):
        if column == 0:
            column = "website"
        elif column == 1:
            column = "name"
        elif column == 2:
            column = "password"
        else:
            column = "date"
        return column

    def generate_password(self):
        length = int(self.input_length_password.text())
        letters_and_numbers = string.ascii_letters + string.digits
        self.new_password = (''.join(random.choice(letters_and_numbers) for x in range(length)))
        self.input_new_password.setText(self.new_password)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
