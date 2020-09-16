# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'update_project.ui'
# Created by: PyQt5 UI code generator 5.11.3

###################################################################################
# Written by Intern(Rashail Tech Labs) :- Govinda Patidar
# Guided by Director(Rashail Tech Labs) :- Mr. Saral Jain
###################################################################################

###################################################################################
# Whenever we want to use different modules in python first we have to import
# them to use their functionality in the program...
from PyQt5 import QtCore, QtGui, QtWidgets    ### we import different classes from            
from PyQt5.QtWidgets import *                 ### PyQt5 module and the property of
from PyQt5.QtGui import *                     ### imported class also in different
from PyQt5.QtCore import *                    ### lines
import xlsxwriter                             # To download table as excel file
import sys                                    # To use sys.argv camand line argument
from reportlab.pdfgen import canvas           # To make and download the invoice as PDF
import sqlite3                                # For connecting the data with database
###################################################################################

###################################################################################
# Here we connect the system with SQLite database and create connection variable
# and cursor.
#---------------------Code Start---------------------------------------------------
conn = sqlite3.connect('ItemDetail.db')
cur=conn.cursor()
#---------------------Code End-----------------------------------------------------
###################################################################################

# We create a class as Ui_MainWindow and pass the QWidget class as parameter

class Ui_MainWindow(QWidget):

####################################################################################
# Whenever this function is called a message box will pop-up with some message
#---------------------Code Start----------------------------------------------------
    def messagebox(self,title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# When we click on the delete button this function will called and delete the
# content from database and call the display function to display the valid detail
# on the screen
#
# take all data from database
# check for current row
# delete the current row
#---------------------Code start----------------------------------------------------
    def Delete_Data(self):
        sql = "SELECT * FROM Detail;"
        res = conn.execute(sql)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                Item1 = data[0]
                Price1 = data[1]
                Quantity1 = data[2]
                Total_Price1 = data[3]
                conn.execute("DELETE FROM Detail WHERE Item = ? AND Price = ? AND Quantity = ? AND Total_Price = ?;",(Item1,Price1,Quantity1,Total_Price1,))
                conn.commit()
                self.Displaytable()
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# When we click on the Add button this function will called and Add the
# content to database and call the display function to display the added detail
# on the screen, and if we don't give all the detail then it will call the message
# box function to show message 'Please Enter All Detail'
#
# take data from line edit
# check data is empty or not if yes then show message
# add data into SQLite database
# Display the data on the screen
#---------------------Code start----------------------------------------------------
    def Add_into_table(self):
        item1=self.lineEdit.text()
        price1=self.lineEdit_2.text()
        quantity1=self.lineEdit_3.text()
        if item1.strip(" ") != "" and price1.strip(" ") != "" and quantity1.strip(" ") != "":
            total_price1=int(price1)*int(quantity1)
            query="INSERT INTO Detail(Item, Price, Quantity, Total_Price) VALUES(?,?,?,?);"
            conn.execute(query,(item1, int(price1), int(quantity1), total_price1))
            conn.commit()
            self.Displaytable()
        else :
            self.messagebox("Error","Please Enter All Detail")
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# When we run the program this function is called and display the contents of table
# from database to screen and besides it when we click on the Refresh icon this
# function will also called.
#
# take all data from database
# display the data into row and column of screen table
#---------------------Code start----------------------------------------------------
    def Displaytable(self):
        query1 = "SELECT * FROM Detail"
        result = conn.execute(query1)
        self.tableWidget.setRowCount(0)
        count = 0

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            self.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(count+1)))
            count=count+1
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number+1, QtWidgets.QTableWidgetItem(str(data)))
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# For performing select operation first we have to select a row in table and click
# on the Select button then this function will called and and display the selected
# itemes in lineEdits.
#
# take all data from database
# check for current row
# show current row data into line edits
#---------------------Code start----------------------------------------------------                
    def Select_Data(self):
        sql = "SELECT * FROM Detail;"
        res = conn.execute(sql)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                Item1 = data[0]
                Price1 = data[1]
                Quantity1 = data[2]
                self.lineEdit.setText(Item1)
                self.lineEdit_2.setText(str(Price1))
                self.lineEdit_3.setText(str(Quantity1))
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# After performing select operation write the detail on the lineEdits that we want
# to update and click on the Update button then this function will called and replace
# the content to updated content in database and call the display function to display
# the added updated detail on the screen.
#
# take all data from database
# check for current row
# update the current row with updated data
#---------------------Code start----------------------------------------------------
    def Update_Data(self):
        sql = "SELECT * FROM Detail;"
        res = conn.execute(sql)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                item1 = data[0]
                price1 = data[1]
                quantity1 = data[2]
                item2=self.lineEdit.text()
                price2=self.lineEdit_2.text()
                quantity2=self.lineEdit_3.text()
                if item1.strip(" ") != "" and price1 != "" and quantity1 != "":
                    total_price2=int(price2)*int(quantity2)
                    query=("UPDATE Detail SET Item=?, Price=?, Quantity=?, Total_Price=? WHERE Item=? AND Price=? AND Quantity=?;")
                    conn.execute(query,(item2,int(price2),int(quantity2),total_price2,item1,price1,quantity1))
                    conn.commit()
                    self.Displaytable()
                else :
                    self.messagebox("Error","Please enter all the detail")
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# When the execution of program will start then it will call this function to display
# the main window on the screen with all tha details like butons, labels, table, menu
# bar, toolbar etc. at there fix position that we have defined through the Qt-designer.
#---------------------Code start----------------------------------------------------
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 390)
        MainWindow.setWindowIcon(QIcon('logo1.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 10, 1)
        self.pushButton_Format = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_Format.setFont(font)
        self.pushButton_Format.setObjectName("pushButton_Format")
        self.gridLayout.addWidget(self.pushButton_Format, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 6, 1, 1, 2)
        self.pushButton_Add = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setStyleSheet("")
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.gridLayout.addWidget(self.pushButton_Add, 7, 1, 1, 1)
        self.pushButton_Reset = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Reset.setFont(font)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.gridLayout.addWidget(self.pushButton_Reset, 7, 2, 1, 1)
        self.pushButton_Delete = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Delete.setFont(font)
        self.pushButton_Delete.setObjectName("pushButton_Delete")
        self.gridLayout.addWidget(self.pushButton_Delete, 8, 1, 1, 2)
        self.pushButton_Edit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Edit.setFont(font)
        self.pushButton_Edit.setObjectName("pushButton_Edit")
        self.gridLayout.addWidget(self.pushButton_Edit, 9, 1, 1, 1)
        self.pushButton_Update = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Update.setFont(font)
        self.pushButton_Update.setObjectName("pushButton_Update")
        self.gridLayout.addWidget(self.pushButton_Update, 9, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Users/govin/Desktop/Platfourma_Project/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionSave_PDF = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Users/govin/Desktop/Platfourma_Project/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_PDF.setIcon(icon1)
        self.actionSave_PDF.setObjectName("actionSave_PDF")
        self.actionSave_Excel = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Users/govin/Desktop/Platfourma_Project/excal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Excel.setIcon(icon2)
        self.actionSave_Excel.setObjectName("actionSave_Excel")
        self.actionPrint_PDF = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Users/govin/Desktop/Platfourma_Project/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint_PDF.setIcon(icon3)
        self.actionPrint_PDF.setObjectName("actionPrint_PDF")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../Users/govin/Desktop/Platfourma_Project/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon4)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAdd_Data = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../Users/govin/Desktop/Platfourma_Project/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Data.setIcon(icon5)
        self.actionAdd_Data.setObjectName("actionAdd_Data")
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_PDF)
        self.menuFile.addAction(self.actionPrint_PDF)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Excel)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addAction(self.actionSave_PDF)
        self.toolBar.addAction(self.actionSave_Excel)
        self.toolBar.addAction(self.actionPrint_PDF)
        self.toolBar.addAction(self.actionQuit)

        # When we clicked on the button or any icon a signal will emit so here we
        # connect that signal to the function to perform different tasks
        # buttons use 'clicked' and menu bar, toolbar use 'triggered' to connect
        #-------------------------start---------------------------------------------
        self.Displaytable()
        self.pushButton_Add.clicked.connect(self.Add_into_table)
        self.pushButton_Delete.clicked.connect(self.Delete_Data)
        self.pushButton_Edit.clicked.connect(self.Select_Data)
        self.pushButton_Update.clicked.connect(self.Update_Data)
        self.pushButton_Format.clicked.connect(self.Select_Format)
        self.actionRefresh.triggered.connect(self.Displaytable)
        self.actionSave_PDF.triggered.connect(self.get_detail)
        self.actionPrint_PDF.triggered.connect(self.get_detail)
        self.actionSave_Excel.triggered.connect(self.exportexcel)
        self.actionQuit.triggered.connect(self.quit)
        #-------------------------End-----------------------------------------------

        self.retranslateUi(MainWindow)
        self.pushButton_Reset.clicked.connect(self.lineEdit.clear)
        self.pushButton_Reset.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_Reset.clicked.connect(self.lineEdit_3.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# One more button we have designed on our screen with the name 'Format' but we have
# not add any functionality yet so whenever we click on the format button a message
# box will pop-up with message.
#---------------------Code start----------------------------------------------------
    def Select_Format(self):
        self.Form_2 = QtWidgets.QWidget()
        self.ui = Ui_Form_2()
        self.ui.setupUi(self.Form_2)
        self.Form_2.show()
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# When we want to get the data of table as excel the we click on the Save_Excel icon
# then this function will called and system window will pop-up to select the name and
# the location of the file then the file will save as .xls file.
#
# use predefined library to save
# create an empty sheet
# write the detail of table in row and column of sheet
# save it
#---------------------Code start----------------------------------------------------
    def exportexcel(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File'," "'.xls','(*.xls)')
        if filename:
            wb = xlsxwriter.Workbook(filename)
            self.sheetBook = wb.add_worksheet()
            self.export()
            wb.close()

    def export(self):
        row = 0
        col = 0
        for i in range(self.tableWidget.columnCount()):
            for x in range(self.tableWidget.rowCount()):
                try:
                    text = str(self.tableWidget.item(row, col).text())
                    self.sheetBook.write(row, col, text)
                    row += 1
                except AttributeError:
                    row += 1
            row = 0
            col += 1
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# When we want to download the table data as an invoice then click on the 'Save_PDF
# or Print' icon that will call this function, in this function we call a second
# window to take the necessary detail from user to make an invoice in predefined
# format.
#
# create a second window
# create a object of class
# call the setupUi function
# show the window
#---------------------Code start----------------------------------------------------
    def get_detail(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# When we click on the Quit icon this function will closs the window.
#---------------------Code start----------------------------------------------------
    def quit(self):
        MainWindow.close()
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# When we use Qt-designer and set text on the buttons, labels, menu bar, toolbar etc.
# first it will assign them as default and then translate them to the defined text.
#---------------------Code start----------------------------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Invoice Generator"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S, No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total Price"))
        self.pushButton_Format.setText(_translate("MainWindow", "Format"))
        self.label.setText(_translate("MainWindow", "Item Name "))
        self.label_2.setText(_translate("MainWindow", "Price"))
        self.label_3.setText(_translate("MainWindow", "Quantity"))
        self.pushButton_Add.setText(_translate("MainWindow", "Add"))
        self.pushButton_Reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_Delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_Edit.setText(_translate("MainWindow", "Edit"))
        self.pushButton_Update.setText(_translate("MainWindow", "Update"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionRefresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionSave_PDF.setText(_translate("MainWindow", "Save PDF"))
        self.actionSave_PDF.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_Excel.setText(_translate("MainWindow", "Save Excel"))
        self.actionSave_Excel.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionPrint_PDF.setText(_translate("MainWindow", "Print PDF"))
        self.actionPrint_PDF.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAdd_Data.setText(_translate("MainWindow", "Add Data"))
#---------------------Code End------------------------------------------------------
####################################################################################

####################################################################################
# New class is created for new window.
#---------------------Code start----------------------------------------------------
class Ui_Form(object):

    ################################################################################
    # When the execution of program will start then it will display the second
    # window on the screen
    #---------------------Code start------------------------------------------------
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(443, 469)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_date = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.gridLayout.addWidget(self.label_date, 0, 0, 1, 1)
        self.lineEdit_date = QtWidgets.QLineEdit(Form)
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.gridLayout.addWidget(self.lineEdit_date, 0, 2, 1, 1)
        self.label_invoice_no = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_invoice_no.setFont(font)
        self.label_invoice_no.setObjectName("label_invoice_no")
        self.gridLayout.addWidget(self.label_invoice_no, 1, 0, 1, 1)
        self.lineEdit_invoice_no = QtWidgets.QLineEdit(Form)
        self.lineEdit_invoice_no.setObjectName("lineEdit_invoice_no")
        self.gridLayout.addWidget(self.lineEdit_invoice_no, 1, 2, 1, 1)
        self.label_company = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_company.setFont(font)
        self.label_company.setObjectName("label_company")
        self.gridLayout.addWidget(self.label_company, 2, 0, 1, 1)
        self.lineEdit_company = QtWidgets.QLineEdit(Form)
        self.lineEdit_company.setObjectName("lineEdit_company")
        self.gridLayout.addWidget(self.lineEdit_company, 2, 2, 1, 1)
        self.label_project = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_project.setFont(font)
        self.label_project.setObjectName("label_project")
        self.gridLayout.addWidget(self.label_project, 3, 0, 1, 2)
        self.lineEdit_project = QtWidgets.QLineEdit(Form)
        self.lineEdit_project.setObjectName("lineEdit_project")
        self.gridLayout.addWidget(self.lineEdit_project, 3, 2, 1, 1)
        self.label_client_add = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_client_add.setFont(font)
        self.label_client_add.setObjectName("label_client_add")
        self.gridLayout.addWidget(self.label_client_add, 4, 0, 1, 1)
        self.label_street = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_street.setFont(font)
        self.label_street.setObjectName("label_street")
        self.gridLayout.addWidget(self.label_street, 4, 1, 1, 2)
        self.lineEdit_street = QtWidgets.QLineEdit(Form)
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.gridLayout.addWidget(self.lineEdit_street, 4, 3, 1, 1)
        self.label_city = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_city.setFont(font)
        self.label_city.setObjectName("label_city")
        self.gridLayout.addWidget(self.label_city, 5, 1, 1, 2)
        self.lineEdit_city = QtWidgets.QLineEdit(Form)
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.gridLayout.addWidget(self.lineEdit_city, 5, 3, 1, 1)
        self.label_pin_no = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_pin_no.setFont(font)
        self.label_pin_no.setObjectName("label_pin_no")
        self.gridLayout.addWidget(self.label_pin_no, 6, 1, 1, 2)
        self.lineEdit_pin_no = QtWidgets.QLineEdit(Form)
        self.lineEdit_pin_no.setObjectName("lineEdit_pin_no")
        self.gridLayout.addWidget(self.lineEdit_pin_no, 6, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 2, 1, 1)

        # here we use lambda function to pass Form window as argument in function
        self.pushButton.clicked.connect(lambda:self.address(Form)) 

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    #---------------------Code End--------------------------------------------------
    ################################################################################
        
    ################################################################################
    # for showing the message box with some message
    #---------------------Code start------------------------------------------------
    def messagebox(self,title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    #---------------------Code End--------------------------------------------------
    ################################################################################
        
    ################################################################################
    # this functin will call when submit button is pressed and make an invoice in 
    # defined format, firstly we import the reportlab module inside the function
    # because we call the class from different program so it do not recognize it
    # thats why we import the module inside the function.
    # then establish a connection with database.
    # take the inputes from lineEdits.
    # create a PDF with the name of invoice no.
    # Take each column of data from database in differ different lists
    # check whether the line edits are empty or not, if yes the show message box
    # put text, line, image on the PDF at desired location with the help of cordinate geomatery
    # give only 8 entries in one page, if more than that change the page
    # save the PDF
    #---------------------Code start------------------------------------------------
    def address(self, Form):
        from reportlab.pdfgen import canvas
        import math

        conn = sqlite3.connect('ItemDetail.db')
        cur=conn.cursor()

        date = self.lineEdit_date.text()
        invoice_no = self.lineEdit_invoice_no.text()
        company = self.lineEdit_company.text()
        overview = self.lineEdit_project.text()
        street = self.lineEdit_street.text()
        city = self.lineEdit_city.text()
        pin = self.lineEdit_pin_no.text()

        pdf = invoice_no+'.pdf'
        canvas = canvas.Canvas(pdf)
        canvas.setLineWidth(.3)

        F = []
        sql = "SELECT * FROM Format_Detail;"
        res = conn.execute(sql)
        for row in enumerate(res):
            F = row[1]

        A = []
        B = []
        C = []
        D = []
        E = []
        sql = "SELECT * FROM Detail;"
        res = conn.execute(sql)
        for row in enumerate(res):
            A.append(row[0])
            extra = row[1]
            B.append(extra[0])
            C.append(extra[1])
            D.append(extra[2])
            E.append(extra[3])
        count = len(A)
        n = count
        page = math.ceil(n/8)

        if date.strip(" ") != "" and invoice_no.strip(" ") != "" and company.strip(" ") != "" and overview.strip(" ") != "" and street.strip(" ") != "" and city.strip(" ") != "" and pin.strip(" ") != "":

            for j in range(0, page):
            
                canvas.drawInlineImage('images.png', 40,725, width=210,height=70)
                canvas.drawInlineImage('logo1.png', 460,30, width=95,height=95)
                canvas.setFont('Helvetica-Bold', 30)
                canvas.drawString(40,689,'INVOICE')
                canvas.drawString(180,689,invoice_no)

                canvas.setFont('Helvetica', 14)
                canvas.drawString(40,663,date)
                canvas.setFont('Helvetica-Bold', 14)
                canvas.drawString(22,525,'S.No.')
                canvas.drawString(90,525,'Item Name')
                canvas.drawString(330,525,'Price')
                canvas.drawString(397,525,'Quantity')
                canvas.drawString(475,525,'Total Price')
                canvas.drawString(330,170,'Total')
                canvas.drawString(330,205,'GST 5%')

                canvas.setFont('Helvetica-Bold', 16)
                canvas.drawString(350,770,'PAYABLE TO')
                canvas.drawString(350,660,'CLIENT')
                canvas.drawString(40,605,'PROJECT OVERVIEW')
                canvas.drawString(30,111,F[3])

                canvas.setFont('Helvetica', 12)
                canvas.drawString(350,743,F[0])
                canvas.drawString(350,725,'CIN No.-')
                cin_no = F[1]
                canvas.drawString(405,725,cin_no)
                canvas.drawString(350,707,'PAN No.-')
                pan_no = F[2]
                canvas.drawString(405,707,pan_no)

                #company = 'Health ATM India Pvt. Ltd.'
                canvas.drawString(350,638,company)
                gstin = '27AADCH6ZI7QIZ4'
                canvas.drawString(350,620,street)
                canvas.drawString(350,602,city)
                canvas.drawString(520,602,pin)
                canvas.drawString(350,584,'GSTIN -')
                canvas.drawString(400,584,gstin)
                canvas.drawString(40,583,overview)

                canvas.line(20,545,580,545)
                canvas.line(20,510,580,510)
                
                canvas.line(20,475,580,475)
                canvas.line(20,440,580,440)
                canvas.line(20,405,580,405)
                canvas.line(20,370,580,370)
                canvas.line(20,335,580,335)
                canvas.line(20,300,580,300)
                canvas.line(20,265,580,265)
                canvas.line(20,230,580,230)
                canvas.line(20,195,580,195)
                canvas.line(20,160,580,160)

                canvas.line(20,545,20,160)
                canvas.line(60,545,60,230)
                canvas.line(310,545,310,230)
                canvas.line(390,545,390,230)
                canvas.line(460,545,460,160)
                canvas.line(580,545,580,160)

                canvas.setFont('Helvetica', 12)
                
                canvas.drawString(30,81,F[4])
                canvas.drawString(30,64,F[5])
                canvas.drawString(30,47,F[6])
                canvas.drawString(30,30,F[7])

                GST = 0
                Total = 0

                for i in range(0, 8):
                    if i==0 :
                        if j*8+i < n:
                            canvas.drawString(30,483,str(1+A[j*8 + 0]))
                            canvas.drawString(70,483,str(B[j*8 + 0]))
                            canvas.drawString(320,483,str(C[j*8 + 0]))
                            canvas.drawString(405,483,str(D[j*8 + 0]))
                            canvas.drawString(475,483,str(E[j*8 + 0]))
                            Total = Total + E[j*8 + i]
                    if i==1:
                        if j*8+i < n:
                            canvas.drawString(30,448,str(1+A[j*8 + 1]))
                            canvas.drawString(70,448,str(B[j*8 + 1]))
                            canvas.drawString(320,448,str(C[j*8 + 1]))
                            canvas.drawString(405,448,str(D[j*8 + 1]))
                            canvas.drawString(475,448,str(E[j*8 + 1]))
                            Total = Total + E[j*8 + i]
                    if i==2:
                        if j*8+i < n:
                            canvas.drawString(30,413,str(1+A[j*8 + 2]))
                            canvas.drawString(70,413,str(B[j*8 + 2]))
                            canvas.drawString(320,413,str(C[j*8 + 2]))
                            canvas.drawString(405,413,str(D[j*8 + 2]))
                            canvas.drawString(475,413,str(E[j*8 + 2]))
                            Total = Total + E[j*8 + i]
                    if i==3:
                        if j*8+i < n:
                            canvas.drawString(30,378,str(1+A[j*8 + 3]))
                            canvas.drawString(70,378,str(B[j*8 + 3]))
                            canvas.drawString(320,378,str(C[j*8 + 3]))
                            canvas.drawString(405,378,str(D[j*8 + 3]))
                            canvas.drawString(475,378,str(E[j*8 + 3]))
                            Total = Total + E[j*8 + i]
                    if i==4:
                        if j*8+i < n:
                            canvas.drawString(30,343,str(1+A[j*8 + 4]))
                            canvas.drawString(70,343,str(B[j*8 + 4]))
                            canvas.drawString(320,343,str(C[j*8 + 4]))
                            canvas.drawString(405,343,str(D[j*8 + 4]))
                            canvas.drawString(475,343,str(E[j*8 + 4]))
                            Total = Total + E[j*8 + i]
                    if i==5:
                        if j*8+i < n:
                            canvas.drawString(30,308,str(1+A[j*8 + 5]))
                            canvas.drawString(70,308,str(B[j*8 + 5]))
                            canvas.drawString(320,308,str(C[j*8 + 5]))
                            canvas.drawString(405,308,str(D[j*8 + 5]))
                            canvas.drawString(475,308,str(E[j*8 + 5]))
                            Total = Total + E[j*8 + i]
                    if i==6:
                        if j*8+i < n:
                            canvas.drawString(30,273,str(1+A[j*8 + 6]))
                            canvas.drawString(70,273,str(B[j*8 + 6]))
                            canvas.drawString(320,273,str(C[j*8 + 6]))
                            canvas.drawString(405,273,str(D[j*8 + 6]))
                            canvas.drawString(475,273,str(E[j*8 + 6]))
                            Total = Total + E[j*8 + i]
                    if i==7:
                        if j*8+i < n:
                            canvas.drawString(30,238,str(1+A[j*8 + 7]))
                            canvas.drawString(70,238,str(B[j*8 + 7]))
                            canvas.drawString(320,238,str(C[j*8 + 7]))
                            canvas.drawString(405,238,str(D[j*8 + 7]))
                            canvas.drawString(475,238,str(E[j*8 + 7]))
                            Total = Total + E[j*8 + i]

                GST = Total * 5 / 100
                Total = Total + GST

                canvas.drawString(475,170,str(Total))
                canvas.drawString(475,205,str(GST))
                canvas.showPage()

            canvas.save()
            self.messagebox("Done","PDF is Downloaded successfully with Invoice No. and saved in same folder in which application is running")
            Form.hide()

        else:
            self.messagebox("Error","Please enter all detail")
    #---------------------Code End--------------------------------------------------
    ################################################################################
        
    ################################################################################
    # When we use Qt-designer and set text on the buttons, labels, menu bar, toolbar
    # etc. first it will assign them as default and then translate them to the
    # defined text.
    #---------------------Code start------------------------------------------------
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Invoice Detail"))
        self.label_date.setText(_translate("Form", "Date"))
        self.label_invoice_no.setText(_translate("Form", "Invoice No."))
        self.label_company.setText(_translate("Form", "Company Name :"))
        self.label_project.setText(_translate("Form", "Project Overview :"))
        self.label_client_add.setText(_translate("Form", "Client Address :"))
        self.label_street.setText(_translate("Form", "Building No, Street :"))
        self.label_city.setText(_translate("Form", "City, State :"))
        self.label_pin_no.setText(_translate("Form", "Pin No. : "))
        self.pushButton.setText(_translate("Form", "Submit"))
    #---------------------Code End--------------------------------------------------
    ################################################################################

#---------------------Code End------------------------------------------------------
#################################################################################### 

class Ui_Form_2(object):

    def messagebox(self,title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, Form_2):
        Form_2.setObjectName("Form_2")
        Form_2.resize(322, 553)
        self.gridLayout = QtWidgets.QGridLayout(Form_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(Form_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(Form_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 2)
        self.label_9 = QtWidgets.QLabel(Form_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(Form_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 2)
        self.lineEdit_6 = QtWidgets.QLineEdit(Form_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 2)
        self.lineEdit_7 = QtWidgets.QLineEdit(Form_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 2)
        self.lineEdit_8 = QtWidgets.QLineEdit(Form_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 2)
        self.pushButton.clicked.connect(lambda:self.format(Form_2))

        self.retranslateUi(Form_2)
        QtCore.QMetaObject.connectSlotsByName(Form_2)

    def format(self, Form_2):
        c_name = self.lineEdit.text()
        cin = self.lineEdit_2.text()
        pan = self.lineEdit_3.text()
        footer = self.lineEdit_4.text()
        mbl_no = self.lineEdit_5.text()
        line1 = self.lineEdit_6.text()
        line2 = self.lineEdit_7.text()
        line3 = self.lineEdit_8.text()

        if c_name.strip(" ") != "" and cin.strip(" ") != "" and pan.strip(" ") != "" and footer.strip(" ") != "" and mbl_no.strip(" ") != "" and line1.strip(" ") != "" and line2.strip(" ") != "" and line3.strip(" ") != "":
            F = []
            sql = "SELECT * FROM Format_Detail;"
            res = conn.execute(sql)
            for row in enumerate(res):
                F = row[1]
                
            query=("UPDATE Format_Detail SET Cmp_Name=?, CIN_No=?, PAN_No=?, Footer=?, Add_1=?, Add_2=?, Add_3=?, Mbl_No=?;")#WHERE Item=? AND Price=? AND Quantity=?;")
            conn.execute(query,(c_name,cin,pan,footer,line1,line2,line3,mbl_no))
            conn.commit()
            self.messagebox("Error","Format have been changed succesfully")
            Form_2.hide()

        else:
            self.messagebox("Error","Please enter all detail")


    def retranslateUi(self, Form_2):
        _translate = QtCore.QCoreApplication.translate
        Form_2.setWindowTitle(_translate("Form_2", "Change Format"))
        self.label.setText(_translate("Form_2", "Company Name :"))
        self.label_2.setText(_translate("Form_2", "CIN No. :"))
        self.label_3.setText(_translate("Form_2", "PAN No. :"))
        self.label_4.setText(_translate("Form_2", "Footer :"))
        self.label_9.setText(_translate("Form_2", "Mobile No. :"))
        self.label_5.setText(_translate("Form_2", "Address :"))
        self.label_6.setText(_translate("Form_2", "line 1 :"))
        self.label_7.setText(_translate("Form_2", "Line 2 :"))
        self.label_8.setText(_translate("Form_2", "Line 3 :"))
        self.pushButton.setText(_translate("Form_2", "Submit"))

####################################################################################
# This is the place from where the flow of control will start and execute the
# program as the flow to control is designed.
#
# create a window
# create a object of class
# call the setupUi function
# show the window
# close the window
#---------------------Code start----------------------------------------------------
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#---------------------Code End------------------------------------------------------
####################################################################################
