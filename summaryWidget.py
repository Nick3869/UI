from PyQt5 import QtWidgets, Qt
from lxml import etree
import os

class SumWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SumWidget, self).__init__(parent)
        self.initWidget(parent)

    def initWidget(self, parent):
        self.browseb = QtWidgets.QPushButton('Browse')
        self.browseb.clicked.connect(lambda: self.browse(parent))

        self.proEdit = QtWidgets.QLineEdit()
        self.text = QtWidgets.QTextEdit()
        self.protocol = QtWidgets.QLabel('Protocol')
        
        grid1 = QtWidgets.QGridLayout()
        
        grid1.setVerticalSpacing(20)
        
        grid1.setRowStretch(3,1)
        grid1.setRowStretch(0,1)
        
        grid1.addWidget(self.text,1,0,1,3)
        grid1.addWidget(self.protocol,2,0)
        grid1.addWidget(self.proEdit,2,1)
        grid1.addWidget(self.browseb,2,2)
        
        self.setLayout(grid1)
        
    def browse(self, parent):
    
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",".","*.xml")
        
        if fileName:
            self.proEdit.setText(fileName)
            self.updateXML(parent)
            
            
    def updateXML(self, parent):

        parent.xmlSaved = True
        stepTree = etree.parse("../PROTOCOLS/HARDIPrep_temp.xml")
        xmlFile = open(self.proEdit.text(), "w")
        xmlFile.write(etree.tostring(stepTree, pretty_print = True))
        xmlFile.close()
        os.remove("../PROTOCOLS/HARDIPrep_temp.xml")