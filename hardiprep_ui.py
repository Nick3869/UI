# -*- coding: utf-8 -*-

"""

@author: Nicolas Fanjat
 Scientific Computing and Imaging Institute
 University of Utah
 02/17/2015
 
"""

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QGridLayout, QMessageBox, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import os
import glob
import numpy as np
import ntpath
import time
import subprocess

import loadProtocol
import preliminaryWidget, paramWidget, summaryWidget

from lxml import etree

from PyQt5.Qt import QDialog

class PrepWindow(QMainWindow):
	
	xmlFile = str()
	xmlSaved = False
	
	def __init__(self):
		
		super(PrepWindow, self).__init__()
		self.initUI()
		
	def initUI(self):
		
		global k
		k = 0
		
		self.createXML()
		
		self.widget = QWidget()
		
		self.cwidget = QLabel()
		pix = QPixmap("logo.png")
		self.cwidget.setPixmap(pix)
		
		self.statusbar = self.statusBar()
		
		self.next = QPushButton("Create your own Protocol")
		self.next.setStatusTip('Proceed to next step')
		self.next.clicked.connect(self.nextf)
		
		self.back = QPushButton("Load existing Protocol")
		self.back.setStatusTip('Go back to previous step')
		self.back.clicked.connect(self.backf)
		
		hbox = QHBoxLayout()
		hbox.addWidget(self.back)
		hbox.addStretch(1)
		hbox.addWidget(self.next)
		
		self.wgrid = QGridLayout()
		self.wgrid.addWidget(self.cwidget, 0, 0)
		self.wgrid.addLayout(hbox, 1, 0)
		
		self.widget.setLayout(self.wgrid)
		
		self.setCentralWidget(self.widget)
		
		self.resize(600, 900)
		
		self.setWindowTitle('HARDIPrep')    
		self.show()
		
	def keyPressEvent(self, e):
		
		if e.key() == Qt.Key_Escape:
			self.close()
			
	def nextf(self):
		
		global k
		k += 1
		print(k)
		
		if k>0:
			self.next.setText("Next")
			self.back.setText("Back")
			
		if k>1:
			self.cwidget.updateXML(self)
			self.xmlSaved = False
				
		if not k:
			self.next.setText("Create your own Protocol")
			self.back.setText("Load existing Protocol")
			self.back.clicked.connect(self.backf)
			self.back.clicked.disconnect(self.nextf)
			self.next.clicked.disconnect(self.runLoaded)
			self.next.clicked.connect(self.nextf)
		elif k==3:
			self.next.setText("Run")
			self.next.clicked.connect(self.runCreated)
			self.next.clicked.disconnect(self.nextf)
			
		self.changeWidget(k)
	
	def backf(self):
		
		global k
		k -= 1
		print(k)
		
		if not k:
			self.next.setText("Create your own Protocol")
			self.back.setText("Load existing Protocol")
		elif k == -1:
			self.next.setText("Run")
			self.back.setText("Back")
			self.back.clicked.connect(self.nextf)
			self.back.clicked.disconnect(self.backf)
			self.next.clicked.connect(self.runLoaded)
			self.next.clicked.disconnect(self.nextf)
		elif k==2:
			self.next.setText("Next")
			self.next.clicked.disconnect(self.runLoaded)
			self.next.clicked.connect(self.nextf)
		self.changeWidget(k)
			
	def changeWidget(self, i):
		
		self.wgrid.removeWidget(self.cwidget)
		self.cwidget.hide()
		
		if i==-1:
			self.cwidget = loadProtocol.MainWidget(self)
		elif i==1:
			self.cwidget = preliminaryWidget.Ui_widget0(self)
		elif i==0:
			self.cwidget = QLabel()
			pix = QPixmap("logo.png")
			self.cwidget.setPixmap(pix)
		elif i==2:
			self.cwidget = paramWidget.PrepWidget(self)
		elif i==3:
			self.cwidget = summaryWidget.SumWidget(self)
		else:
			self.cwidget = QWidget()
			
		self.wgrid.addWidget(self.cwidget, 0, 0)
		
	def createXML(self):
		
		xmlTree = etree.Element("Steps")
		stepList = ["Mandatory Parameters", "Optional Parameters"]
		
		for step in stepList:
			etree.SubElement(xmlTree, "step", stage=step)
		
		xmlFile = open("../PROTOCOLS/HARDIPrep_temp.xml", "w")
		xmlFile.write(etree.tostring(xmlTree, pretty_print = True))
		xmlFile.close()
		
	def closeEvent(self, event):
	
		if not self.xmlSaved:
			reply = QMessageBox.question(self, 'Message',
			    "Would you like to save protocol before quitting ?", QMessageBox.Discard | 
			    QMessageBox.Save | QMessageBox.Cancel, QMessageBox.Save)
	
			if reply == QMessageBox.Save:
				self.cwidget.updateXML(self)
				xmlFile1 = open("../PROTOCOLS/HARDIPrep.xml", "w")
				stepTree = etree.parse("../PROTOCOLS/HARDIPrep_temp.xml")
				xmlFile1.write(etree.tostring(stepTree, pretty_print=True))
				xmlFile1.close()
				os.remove("../PROTOCOLS/HARDIPrep_temp.xml")
				event.accept()
			elif reply == QMessageBox.Discard:
				os.remove("../PROTOCOLS/HARDIPrep_temp.xml")
				event.accept()
			else:
				event.ignore()
		else:
			os.remove("../PROTOCOLS/HARDIPrep_temp.xml")
		
	def runLoaded(self):
		
		inText = self.cwidget.inEdit.text()
		proText = self.cwidget.proEdit.text()
		
		if ((inText != "") & (proText != "")):
			print("Run ! You fool !")
		elif (inText != ""):
			print("Run if you can !")
		else:
			QMessageBox.warning(self, "Error", "Choose an input Directory !", buttons=QMessageBox.Ok)
			
	def runCreated(self):

		
		proText = self.cwidget.proEdit.text()
		
		if (proText != ""):
			proc = subprocess.Popen(["python", "test.py"], stdout=self.out).pid
			
		else:
			QMessageBox.warning(self, "Error", "Choose a valid protocol name !", buttons=QMessageBox.Ok)
		
		
if __name__ == '__main__':
	import sys

	app = QApplication(sys.argv)
	ex = PrepWindow()
	sys.exit(app.exec_())
	
