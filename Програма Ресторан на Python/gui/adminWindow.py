# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminWindow(object):
    def setupUi(self, adminWindow):
        adminWindow.setObjectName("adminWindow")
        adminWindow.resize(526, 393)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        adminWindow.setFont(font)
        self.line = QtWidgets.QFrame(adminWindow)
        self.line.setGeometry(QtCore.QRect(230, 30, 20, 351))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.detailsTextEdit = QtWidgets.QTextEdit(adminWindow)
        self.detailsTextEdit.setGeometry(QtCore.QRect(260, 40, 251, 321))
        self.detailsTextEdit.setStyleSheet("background: rgba(0,0,255,0%)")
        self.detailsTextEdit.setObjectName("detailsTextEdit")
        self.showDishAddFormButton = QtWidgets.QPushButton(adminWindow)
        self.showDishAddFormButton.setGeometry(QtCore.QRect(10, 70, 211, 31))
        self.showDishAddFormButton.setObjectName("showDishAddFormButton")
        self.dayProfitReportButton = QtWidgets.QPushButton(adminWindow)
        self.dayProfitReportButton.setGeometry(QtCore.QRect(10, 120, 211, 31))
        self.dayProfitReportButton.setObjectName("dayProfitReportButton")
        self.weekProfitReportButton = QtWidgets.QPushButton(adminWindow)
        self.weekProfitReportButton.setGeometry(QtCore.QRect(10, 170, 211, 31))
        self.weekProfitReportButton.setObjectName("weekProfitReportButton")
        self.monthProfitReportButton = QtWidgets.QPushButton(adminWindow)
        self.monthProfitReportButton.setGeometry(QtCore.QRect(10, 220, 211, 31))
        self.monthProfitReportButton.setObjectName("monthProfitReportButton")
        self.newPasswordGenerateButton = QtWidgets.QPushButton(adminWindow)
        self.newPasswordGenerateButton.setGeometry(QtCore.QRect(10, 270, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.newPasswordGenerateButton.setFont(font)
        self.newPasswordGenerateButton.setStyleSheet("multiline")
        self.newPasswordGenerateButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.newPasswordGenerateButton.setObjectName("newPasswordGenerateButton")
        self.dishNameLineEdit = QtWidgets.QLineEdit(adminWindow)
        self.dishNameLineEdit.setGeometry(QtCore.QRect(280, 50, 211, 41))
        self.dishNameLineEdit.setObjectName("dishNameLineEdit")
        self.dishPriceLineEdit = QtWidgets.QLineEdit(adminWindow)
        self.dishPriceLineEdit.setGeometry(QtCore.QRect(280, 100, 211, 41))
        self.dishPriceLineEdit.setObjectName("dishPriceLineEdit")
        self.addDishButton = QtWidgets.QPushButton(adminWindow)
        self.addDishButton.setGeometry(QtCore.QRect(280, 300, 211, 31))
        self.addDishButton.setObjectName("addDishButton")
        self.dishDescriptionPlainTextEdit = QtWidgets.QPlainTextEdit(adminWindow)
        self.dishDescriptionPlainTextEdit.setGeometry(QtCore.QRect(280, 150, 211, 141))
        self.dishDescriptionPlainTextEdit.setObjectName("dishDescriptionPlainTextEdit")
        self.infoLabel = QtWidgets.QLabel(adminWindow)
        self.infoLabel.setGeometry(QtCore.QRect(280, 340, 211, 41))
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.showReservesTableButton = QtWidgets.QPushButton(adminWindow)
        self.showReservesTableButton.setGeometry(QtCore.QRect(10, 330, 211, 31))
        self.showReservesTableButton.setObjectName("showReservesTableButton")
        self.detailsTextEdit.raise_()
        self.line.raise_()
        self.showDishAddFormButton.raise_()
        self.dayProfitReportButton.raise_()
        self.weekProfitReportButton.raise_()
        self.monthProfitReportButton.raise_()
        self.newPasswordGenerateButton.raise_()
        self.dishNameLineEdit.raise_()
        self.dishPriceLineEdit.raise_()
        self.addDishButton.raise_()
        self.dishDescriptionPlainTextEdit.raise_()
        self.infoLabel.raise_()
        self.showReservesTableButton.raise_()

        self.retranslateUi(adminWindow)
        QtCore.QMetaObject.connectSlotsByName(adminWindow)

    def retranslateUi(self, adminWindow):
        _translate = QtCore.QCoreApplication.translate
        adminWindow.setWindowTitle(_translate("adminWindow", "Адміністратор"))
        self.detailsTextEdit.setHtml(_translate("adminWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.showDishAddFormButton.setText(_translate("adminWindow", "Додати нове блюдо"))
        self.dayProfitReportButton.setText(_translate("adminWindow", "Виручка за сьогодні"))
        self.weekProfitReportButton.setText(_translate("adminWindow", "Виручка за тиждень"))
        self.monthProfitReportButton.setText(_translate("adminWindow", "Виручка за місяць"))
        self.newPasswordGenerateButton.setText(_translate("adminWindow", "Згенерувати новий пароль\n"
"для співробітників"))
        self.dishNameLineEdit.setPlaceholderText(_translate("adminWindow", "Назва страви"))
        self.dishPriceLineEdit.setPlaceholderText(_translate("adminWindow", "Ціна страви"))
        self.addDishButton.setText(_translate("adminWindow", "Додати"))
        self.dishDescriptionPlainTextEdit.setPlaceholderText(_translate("adminWindow", "Опис страви"))
        self.showReservesTableButton.setText(_translate("adminWindow", "Бронювання"))
