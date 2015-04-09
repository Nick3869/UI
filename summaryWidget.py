from PyQt5 import QtWidgets

class SumWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SumWidget, self).__init__(parent)
        self.initWidget()

    def initWidget(self):
        self.browseb = QtWidgets.QPushButton('Browse')
        self.browseinput = QtWidgets.QPushButton('Browse')
        self.browseb.clicked.connect(self.browse)
        self.browseinput.clicked.connect(self.browseInput)
        
        self.inEdit = QtWidgets.QLineEdit()
        self.proEdit = QtWidgets.QLineEdit()
        
        self.source = QtWidgets.QLabel('Input')
        self.protocol = QtWidgets.QLabel('Protocol')
        
        grid1 = QtWidgets.QGridLayout()
        
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
    
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",".","*.xml")
        
        if fileName:
            self.proEdit.setText(fileName)
            
    def browseInput(self):
    
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choose File",".","*.nrrd")
        
        if fileName:
            self.inEdit.setText(fileName)
            
    def updateXML(self):

        stepTree = etree.parse("../PROTOCOLS/HARDIPrep_temp.xml")