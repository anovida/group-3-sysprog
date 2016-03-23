#!/usr/bin/env python
#Author: Group 3 (BSIT-3A)


import sip
sip.setapi('QVariant',2)

import sys
from OurGui import Ui_DialogMain 
from Search import  Ui_DialogSearch 
from PyQt4 import QtSql, QtGui, QtCore 

def createConnection():
	db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
	db.setHostName('127.0.0.1')
	db.setDatabaseName('db_student_info')
	db.setUserName('root')
	db.setPassword('') 
	db.open()
	print (db.lastError().text())
	return True
class Ourg(QtGui.QDialog):
	recno = 0
	def __init__(self, parent=None):
		super(Ourg, self).__init__(parent)
		self.ui = Ui_DialogMain()
		self.ui.setupUi(self)		
		self.model=QtSql.QSqlQueryModel(self)		
		
		self.model.setQuery("select * from tbl_student_info ")
		self.record=self.model.record(0)
		self.ui.StudlineEdit.setText(str(self.record.value("student_id")))
		self.ui.FNlineEdit.setText(str(self.record.value("fname")))
		self.ui.LNlineEdit.setText(str(self.record.value("lname")))
		self.ui.CourselineEdit.setText(str(self.record.value("course")))
		self.ui.YearlineEdit.setText(str(self.record.value("year")))
		self.ui.StudlineEdit_2.setText(str(self.record.value("section")))
		
		self.model = QtSql.QSqlTableModel(self)
		self.model.setTable("tbl_student_info")	
		self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.model.select()


		QtCore.QObject.connect(self.ui.SearchpushButton, QtCore.SIGNAL('clicked()'),self.MyFormShow)
		QtCore.QObject.connect(self.ui.FirstpushButton, QtCore.SIGNAL('clicked()'),self.dispFirst)
		QtCore.QObject.connect(self.ui.FirstpushButton, QtCore.SIGNAL('clicked()'),self.DisableLineEdits)
		QtCore.QObject.connect(self.ui.PreviouspushButton, QtCore.SIGNAL('clicked()'),self.DisableLineEdits)
		QtCore.QObject.connect(self.ui.PreviouspushButton, QtCore.SIGNAL('clicked()'),self.dispPrevious)
		QtCore.QObject.connect(self.ui.LastpushButton, QtCore.SIGNAL('clicked()'),self.DisableLineEdits)
		QtCore.QObject.connect(self.ui.LastpushButton, QtCore.SIGNAL('clicked()' ),self.dispLast)
		QtCore.QObject.connect(self.ui.NextpushButton, QtCore.SIGNAL('clicked()'),self.DisableLineEdits)
		QtCore.QObject.connect(self.ui.NextpushButton, QtCore.SIGNAL('clicked()' ),self.dispNext)
		QtCore.QObject.connect(self.ui.EditpushButton, QtCore.SIGNAL('clicked()' ),self.EnableLineEdits)
		QtCore.QObject.connect(self.ui.ClosepushButton, QtCore.SIGNAL('clicked()' ),self.close)
		QtCore.QObject.connect(self.ui.AddpushButton, QtCore.SIGNAL('clicked()' ),self.AddRecord)
		QtCore.QObject.connect(self.ui.AddpushButton, QtCore.SIGNAL('clicked()' ),self.AlertBoxAddRecord)
		QtCore.QObject.connect(self.ui.UpdatepushButton, QtCore.SIGNAL('clicked()' ),self.UpdateRecord)
		QtCore.QObject.connect(self.ui.UpdatepushButton, QtCore.SIGNAL('clicked()' ),self.AlertBoxUpdateRecord)
		QtCore.QObject.connect(self.ui.EditpushButton, QtCore.SIGNAL('clicked()' ),self.EditRecords)
		#QtCore.QObject.connect(self.ui.EditpushButton, QtCore.SIGNAL('clicked()' ),self.AlertBoxEditRecord)
		QtCore.QObject.connect(self.ui.DeletepushButton, QtCore.SIGNAL('clicked()' ),self.AlertBoxDeleteRecord)
		QtCore.QObject.connect(self.ui.DeletepushButton, QtCore.SIGNAL('clicked()' ),self.DeleteRecord)
		QtCore.QObject.connect(self.ui.ClearpushButton, QtCore.SIGNAL('clicked()' ),self.cls)

	def MyFormShow(self):
		MyFormShowWindow = FormSearch(self)
		MyFormShowWindow.show()
	
	def EnableLineEdits(self):
		self.ui.StudlineEdit.setEnabled(True)
		self.ui.FNlineEdit.setEnabled(True)
		self.ui.LNlineEdit.setEnabled(True)
		self.ui.CourselineEdit.setEnabled(True)
		self.ui.YearlineEdit.setEnabled(True)
		self.ui.StudlineEdit_2.setEnabled(True)
		self.ui.StudlineEdit.setFocus()
		
	def DisableLineEdits(self):
		self.ui.StudlineEdit.setEnabled(False)
		self.ui.FNlineEdit.setEnabled(False)
		self.ui.LNlineEdit.setEnabled(False)
		self.ui.CourselineEdit.setEnabled(False)
		self.ui.YearlineEdit.setEnabled(False)
		self.ui.StudlineEdit_2.setEnabled(False)

	def dispFirst(self):
		Ourg.recno=0
		self.record=self.model.record(Ourg.recno)
		self.ui.StudlineEdit.setText(str(self.record.value("student_id")))
		self.ui.FNlineEdit.setText(str(self.record.value("fname")))
		self.ui.LNlineEdit.setText(str(self.record.value("lname")))
		self.ui.CourselineEdit.setText(str(self.record.value("course")))
		self.ui.YearlineEdit.setText(str(self.record.value("year")))
		self.ui.StudlineEdit_2.setText(str(self.record.value("section")))
							
	def dispPrevious(self):
		Ourg.recno-=1
		if Ourg.recno < 0:
			Ourg.recno=self.model.rowCount()-1
		self.record=self.model.record(Ourg.recno)
		self.ui.StudlineEdit.setText(str(self.record.value("student_id")))
		self.ui.FNlineEdit.setText(str(self.record.value("fname")))
		self.ui.LNlineEdit.setText(str(self.record.value("lname")))
		self.ui.CourselineEdit.setText(str(self.record.value("course")))
		self.ui.YearlineEdit.setText(str(self.record.value("year")))
		self.ui.StudlineEdit_2.setText(str(self.record.value("section")))
		
	def dispLast(self):
		Ourg.recno=self.model.rowCount()-1
		self.record=self.model.record(Ourg.recno)
		self.ui.StudlineEdit.setText(str(self.record.value("student_id")))
		self.ui.FNlineEdit.setText(str(self.record.value("fname")))
		self.ui.LNlineEdit.setText(str(self.record.value("lname")))
		self.ui.CourselineEdit.setText(str(self.record.value("course")))
		self.ui.YearlineEdit.setText(str(self.record.value("year")))
		self.ui.StudlineEdit_2.setText(str(self.record.value("section")))
			
	def dispNext(self):
		Ourg.recno+=1
		if Ourg.recno > self.model.rowCount()-1:
			Ourg.recno=0
		self.record=self.model.record(Ourg.recno)
		self.ui.StudlineEdit.setText(str(self.record.value("student_id")))
		self.ui.FNlineEdit.setText(str(self.record.value("fname")))
		self.ui.LNlineEdit.setText(str(self.record.value("lname")))
		self.ui.CourselineEdit.setText(str(self.record.value("course")))
		self.ui.YearlineEdit.setText(str(self.record.value("year")))
		self.ui.StudlineEdit_2.setText(str(self.record.value("section")))
		
	def AddRecord(self):
		studentId = self.ui.StudlineEdit.text()
		studentFName = self.ui.FNlineEdit.text()
		studentLName = self.ui.LNlineEdit.text()
		studentCourse = self.ui.CourselineEdit.text()
		studentYear = self.ui.YearlineEdit.text()
		studentSection = self.ui.StudlineEdit_2.text()
			
		self.model.setData(self.model.index(0, 1), studentId)
		self.model.setData(self.model.index(0, 2), studentFName)
		self.model.setData(self.model.index(0, 3), studentLName)
		self.model.setData(self.model.index(0, 4), studentCourse)
		self.model.setData(self.model.index(0, 5), studentYear)
		self.model.setData(self.model.index(0, 6), studentSection)
		self.model.submitAll()
								
	def UpdateRecord(self):
		studentId = self.ui.StudlineEdit.text()
		studentFName = self.ui.FNlineEdit.text()
		studentLName = self.ui.LNlineEdit.text()
		studentCourse = self.ui.CourselineEdit.text()
		studentYear = self.ui.YearlineEdit.text()
		studentSection = self.ui.StudlineEdit_2.text()
			
		self.model.setData(self.model.index(0, 1), studentId)
		self.model.setData(self.model.index(0, 2), studentFName)
		self.model.setData(self.model.index(0, 3), studentLName)
		self.model.setData(self.model.index(0, 4), studentCourse)
		self.model.setData(self.model.index(0, 5), studentYear)
		self.model.setData(self.model.index(0, 6), studentSection)
		self.model.submitAll()
		
		
	def EditRecords(self):
		self.model.insertRows(0,1)
		self.model.insertRows(0,2)
		self.model.insertRows(0,3)
		self.model.insertRows(0,4)
		self.model.insertRows(0,5)
		self.model.insertRows(0,6)
		self.model.submitAll()
		
	def cls(self):
		self.ui.StudlineEdit.setText("")
		self.ui.FNlineEdit.setText("")
		self.ui.LNlineEdit.setText("")
		self.ui.CourselineEdit.setText("")
		self.ui.YearlineEdit.setText("")
		self.ui.StudlineEdit_2.setText("")
		self.ui.StudlineEdit.setFocus()
	
	def DeleteRecord(self): 
		self.model.removeColumn(1) 
		self.model.removeColumn(2) 
		self.model.removeColumn(3) 
		self.model.removeColumn(4) 
		self.model.removeColumn(5) 
		self.model.removeColumn(6) 
		self.model.submitAll()
		
	def CancelChanges(self):
		self.model.revertAll()
		
	def AlertCanChan(self):
		msgBox = QtGui.QWidget(self)
		res = QtGui.QMessageBox.information(msgBox, 'Message', "Are you sure you want to Apply the Changes?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		msgBox.show()
		
	def AlertBoxAddRecord(self):       
		msgBox = QtGui.QWidget(self)
		res = QtGui.QMessageBox.information(msgBox, "Message", "new record successfully added!")
		msgBox.show()

	def AlertBoxUpdateRecord(self):       
		msgBox = QtGui.QWidget(self)
		res = QtGui.QMessageBox.information(msgBox, "Message", "new record saved!")
		msgBox.show()
	
	def AlertBoxDeleteRecord(self):
		msgBox = QtGui.QWidget(self)
		res = QtGui.QMessageBox.question(msgBox, 'Message', "Are you sure you want to continue?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		msgBox.show()

		
class FormSearch(QtGui.QDialog):
	def __init__(self, parent=None):
		super(FormSearch, self).__init__(parent)
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_DialogSearch()
		self.ui.setupUi(self)	
		self.model = QtSql.QSqlTableModel(self)		
		self.model.setTable("tbl_student_info")		
		self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.model.removeColumn(0) 
		self.model.select()
		
		
		
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, "student_id")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, "fname")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, "lname")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, "course")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, "year")
		self.model.setHeaderData(5, QtCore.Qt.Horizontal, "section")
		

		self.ui.tableView.setModel(self.model)		
		QtCore.QObject.connect(self.ui.FindpushButton, QtCore.SIGNAL('clicked()' ),self.SearchRecord)
		QtCore.QObject.connect(self.ui.FindpushButton, QtCore.SIGNAL('clicked()' ),self.AlertSearchRecord)
		
	def SearchRecord(self):
		self.model.setFilter("student_id like '"+self.ui.SearchlineEdit.text()+"%'")
		#self.model.setFilter("fname like '"+self.ui.SearchlineEdit.text()+"%'")
		#self.model.setFilter("lname like '"+self.ui.SearchlineEdit.text()+"%'")
		#self.model.setFilter("course like '"+self.ui.SearchlineEdit.text()+"%%'")
		#self.model.setFilter("year like '"+self.ui.SearchlineEdit.text()+"%'")
		#self.model.setFilter("section like '"+self.ui.SearchlineEdit.text()+"%'")
		
	def AlertSearchRecord(self):
		msgBox = QtGui.QWidget(self)
		res = QtGui.QMessageBox.information(msgBox, "Message", "Record Has Been Found!")
		msgBox.show()	
		
		
	

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)

if not createConnection():
	sys.exit(1)

myapp = Ourg()
myapp.show()
sys.exit(app.exec_())


