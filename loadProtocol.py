# -*- coding: utf-8 -*-

"""

@author: Nicolas Fanjat
 Scientific Computing and Imaging Institute
 University of Utah
 02/17/2015
 
"""
from PyQt5.QtWidgets import QFileDialog, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QRadioButton
from PyQt5.QtCore import QObject, QDir, Qt

from lxml import etree

class MainWidget(QWidget):
	def __init__(self, parent):
		
		super(MainWidget, self).__init__(parent)
		self.initWidget()

	def initWidget(self):		
		
		self.browseb = QPushButton('Browse')
		self.browseinput = QPushButton('Browse')
		self.browseb.clicked.connect(self.browse)
		self.browseinput.clicked.connect(self.browseInput)
		
		self.inEdit = QLineEdit()
		self.proEdit = QLineEdit()
		
		self.source = QLabel('Input')
		self.protocol = QLabel('Protocol')
		
		grid1 = QGridLayout()
		
		grid1.setVerticalSpacing(20)
		
		grid1.setRowStretch(3,1)
		grid1.setRowStretch(0,1)
		
		grid1.addWidget(self.source,1,0)
		grid1.addWidget(self.inEdit,1,1)
		grid1.addWidget(self.browseinput,1,2)
		
		grid1.addWidget(self.protocol,2,0)
		grid1.addWidget(self.proEdit,2,1)
		grid1.addWidget(self.browseb,2,2)
		
		self.setLayout(grid1)
		
	def browse(self):
	
		fileName, _ = QFileDialog.getOpenFileName(self, "Open File",".","*.xml")
		
		if fileName:
			self.proEdit.setText(fileName)
			
	def browseInput(self):
	
		fileName, _ = QFileDialog.getOpenFileName(self, "Choose File",".","*.nrrd")
		
		if fileName:
			self.inEdit.setText(fileName)