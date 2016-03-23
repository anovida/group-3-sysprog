# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search.ui'
#
# Created: Tue Mar 22 16:04:34 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogSearch(object):
    def setupUi(self, DialogSearch):
        DialogSearch.setObjectName(_fromUtf8("DialogSearch"))
        DialogSearch.resize(414, 252)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        DialogSearch.setFont(font)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(DialogSearch)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(DialogSearch)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.SearchlineEdit = QtGui.QLineEdit(DialogSearch)
        self.SearchlineEdit.setObjectName(_fromUtf8("SearchlineEdit"))
        self.horizontalLayout.addWidget(self.SearchlineEdit)
        self.FindpushButton = QtGui.QPushButton(DialogSearch)
        self.FindpushButton.setObjectName(_fromUtf8("FindpushButton"))
        self.horizontalLayout.addWidget(self.FindpushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtGui.QTableView(DialogSearch)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DialogSearch)
        QtCore.QMetaObject.connectSlotsByName(DialogSearch)

    def retranslateUi(self, DialogSearch):
        DialogSearch.setWindowTitle(_translate("DialogSearch", "Dialog", None))
        self.label.setText(_translate("DialogSearch", "ID Number:", None))
        self.FindpushButton.setText(_translate("DialogSearch", "Sea&rch", None))

