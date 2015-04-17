# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget0.ui'
#
# Created: Thu Feb 19 14:03:21 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QGridLayout, QComboBox
from lxml import etree
import os
import sys
from docutils.parsers.rst.directives import path
from __builtin__ import str

class Ui_widget0(QWidget):
	fileName = ""
	def __init__(self, parent):
		super(Ui_widget0, self).__init__(parent)
		parent.next.setEnabled(False)
		self.setupUi(parent)
	
	def setupUi(self, parent):
		
		self.vlayout = QtWidgets.QVBoxLayout()
		self.hlayout = QtWidgets.QHBoxLayout()
		self.frame = QtWidgets.QFrame(self)
		self.gridLayout = QGridLayout()
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		
		self.combo = QComboBox()
		self.combo.addItem("Whole process")
		self.combo.addItem("Step 1 :")
		self.combo.addItem("Step 2 :")
		self.combo.addItem("Step 3 :")
		self.combo.addItem("Step 4 :")
		self.combo.addItem("Step 5 :")
		self.combo.addItem("Step 6 :")
		self.combo.addItem("Step 7 :")
		self.combo.addItem("Step 8 :")
		self.combo.addItem("Step 9 :")
		self.combo.addItem("Step 10 :")
		self.combo.addItem("Step 11 :")
		
		self.multipleRadio = QtWidgets.QRadioButton("Directory")
		self.gridLayout.addWidget(self.multipleRadio, 3, 1, 1, 1)
		self.multipleRadio.clicked.connect(self.multipleCliked)
		
		self.multipleBrowse = QtWidgets.QPushButton("Browse")
		self.gridLayout.addWidget(self.multipleBrowse, 3, 3, 1, 1)
		self.multipleBrowse.setEnabled(False)
		self.multipleBrowse.clicked.connect(lambda: self.browseDir(parent))
		
		self.singleEdit = QtWidgets.QLineEdit()
		self.gridLayout.addWidget(self.singleEdit, 1, 2, 1, 1)
		self.singleEdit.setEnabled(False)
		
		self.singleBrowse = QtWidgets.QPushButton("Browse")
		self.gridLayout.addWidget(self.singleBrowse, 1, 3, 1, 1)
		self.singleBrowse.setEnabled(False)
		self.singleBrowse.clicked.connect(lambda: self.browse(parent))
		
		self.singleRadio = QtWidgets.QRadioButton("Single file")
		self.gridLayout.addWidget(self.singleRadio, 1, 1, 1, 1)
		self.singleRadio.clicked.connect(self.singleCliked)
		
		self.multipleEdit = QtWidgets.QLineEdit()
		self.gridLayout.addWidget(self.multipleEdit, 3, 2, 1, 1)
		self.multipleEdit.setEnabled(False)

		self.label = QtWidgets.QLabel("Choose input :")
		
		self.label_2 = QtWidgets.QLabel("MANDATORY OPTIONS")
		
		self.gridLayout.setContentsMargins(10, 10, 10, 10)
		self.gridLayout.setVerticalSpacing(10)
		
		self.frame.setLayout(self.gridLayout)
		self.frame.setFrameStyle(QtWidgets.QFrame.StyledPanel | QtWidgets.QFrame.Raised)
		
		self.hlayout.addStretch(1)
		self.hlayout.addWidget(self.label_2)
		self.hlayout.addStretch(1)
		
		self.vlayout.addStretch(1)
		self.vlayout.addLayout(self.hlayout)
		self.vlayout.addStretch(1)
		self.vlayout.addWidget(self.label)
		self.vlayout.addWidget(self.frame)
		self.vlayout.addStretch(1)
		self.vlayout.addWidget(self.combo)
		self.vlayout.addStretch(2)
		
		self.setLayout(self.vlayout)
		
		self.loadXML()
		
	def singleCliked(self):
		
		self.multipleEdit.setEnabled(False)
		self.multipleBrowse.setEnabled(False)
		self.singleEdit.setEnabled(True)
		self.singleBrowse.setEnabled(True)
		
	def multipleCliked(self):
		
		self.multipleEdit.setEnabled(True)
		self.multipleBrowse.setEnabled(True)
		self.singleEdit.setEnabled(False)
		self.singleBrowse.setEnabled(False)
		
	def browse(self, parent):
		
		self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",".","*.nrrd")
		
		if self.fileName:
			self.singleEdit.setText(self.fileName)
			parent.next.setEnabled(True)
			
	def browseDir(self, parent):
		
		self.fileName = QtWidgets.QFileDialog.getExistingDirectory(self, caption='Choose directory', directory='.')
				
		if self.fileName:
			self.multipleEdit.setText(self.fileName)
			parent.next.setEnabled(True)

			
	def loadXML(self):

		stepTree = etree.parse("../PROTOCOLS/HARDIPrep_temp.xml")
		steps = stepTree.getroot()
		step0 = steps[0]
		
		if not (step0.getchildren() == []):
		    path = step0[0]
		    
		    if not (path.text == "t"):
			    if os.path.isdir(path.text):
			    	self.multipleEdit.setText(path.text)
			    else:
			    	self.singleEdit.setText(path.text)
        
	def updateXML(self):	
		
		stepTree = etree.parse("../PROTOCOLS/HARDIPrep_temp.xml")
		steps = stepTree.getroot()
		step0 = steps[0]
		
		if (step0.xpath("/Steps/step/Files") == []):
			subel = etree.SubElement(step0, "Files")
			subel.text = "t"
			
		if self.fileName:
			path = step0[0]
			path.text = self.fileName

		if not (step0.xpath("/Steps/step/toStep") == []):
		    toStep = step0[1]
		    toStep.text = self.combo.currentText()
		else:
		    toStep = etree.SubElement(step0, "toStep")
		    toStep.text = self.combo.currentText()
		        	    
		xmlFile = open("../PROTOCOLS/HARDIPrep_temp.xml", "w")
		xmlFile.write(etree.tostring(stepTree, pretty_print = True))
		xmlFile.close()
	    