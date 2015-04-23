# -*- coding: utf-8 -*-

"""

@author: Nicolas Fanjat
 Scientific Computing and Imaging Institute
 University of Utah
 02/17/2015
 
"""

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QObject, QDir, Qt

from lxml import etree

class PrepWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(PrepWidget, self).__init__(parent)
        self.initWidget()

    def initWidget(self):
        
        tab = QtWidgets.QTabWidget()
        
        simpleWidget = QtWidgets.QWidget()
        advancedWidget = QtWidgets.QWidget()
        
        """ Simple Options """
        #DTI Prep stage
        frame1 = QtWidgets.QFrame()
        title1 = QtWidgets.QLabel("DTI Prep (Step 1)")
        browse = QtWidgets.QPushButton('Browse')
        browse.clicked.connect(self.browse)
        self.xmlEdit = QtWidgets.QLineEdit("Default protocol")
        self.xmlEdit.setAlignment(QtCore.Qt.AlignRight)
        source = QtWidgets.QLabel('XML File')
        
        hbox1 = QtWidgets.QHBoxLayout()
        
        hbox1.addWidget(source)
        hbox1.addWidget(self.xmlEdit)
        hbox1.addWidget(browse)
        
        frame1.setLayout(hbox1)  
        frame1.setFrameStyle(QtWidgets.QFrame.StyledPanel | QtWidgets.QFrame.Raised)
        
        #MCFLIRT Stage
        frame2 = QtWidgets.QFrame()
        title2 = QtWidgets.QLabel("MCFLIRT (Step 6)")
        
        maskUseLabel = QtWidgets.QLabel("Do you want to use a BrainMask ?")
        self.maskUseRadioYes = QtWidgets.QRadioButton("Yes")
        self.maskUseRadioYes.setChecked(True)
        maskUseRadioNo = QtWidgets.QRadioButton("No")
        
        self.comboMethod = QtWidgets.QComboBox()
        self.comboMethod.addItem("Trilinear", userData=None)
        methodLabel = QtWidgets.QLabel("Choose an interpolation method :")
        
        hbox2 = QtWidgets.QHBoxLayout()
        
        hbox2.addWidget(maskUseLabel)
        hbox2.addStretch(1)
        hbox2.addWidget(self.maskUseRadioYes)
        hbox2.addStretch(1)
        hbox2.addWidget(maskUseRadioNo)
        hbox2.addStretch(1)
        
        hbox3 = QtWidgets.QHBoxLayout()
        
        hbox3.addWidget(methodLabel)
        hbox3.addWidget(self.comboMethod)
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        
        frame2.setLayout(vbox)  
        frame2.setFrameStyle(QtWidgets.QFrame.StyledPanel | QtWidgets.QFrame.Raised)
        
        """ Advanced Options """
        # Filter step 4
        filtFrame = QtWidgets.QFrame()
        title41 = QtWidgets.QLabel("Filtering - Gradient-wise denoising (step 4)")
        map = QtGui.QPixmap("Help.png")
        
        estRadXlabel = QtWidgets.QLabel("Estimation_radius_x =")
        self.estRadXedit = QtWidgets.QLineEdit("11")
        estRadXhelp = QtWidgets.QLabel()
        estRadXhelp.setPixmap(map)
        
        estRadYlabel = QtWidgets.QLabel("Estimation_radius_y =")
        self.estRadYedit = QtWidgets.QLineEdit("11")
        estRadYhelp = QtWidgets.QLabel()
        estRadYhelp.setPixmap(map)
        
        estRadZlabel = QtWidgets.QLabel("Estimation_radius_z =")
        self.estRadZedit = QtWidgets.QLineEdit("0")
        estRadZhelp = QtWidgets.QLabel()
        estRadZhelp.setPixmap(map)
        
        filtRadXlabel = QtWidgets.QLabel("Filtering_radius_x =")
        self.filtRadXedit = QtWidgets.QLineEdit("11")
        filtRadXhelp = QtWidgets.QLabel()
        filtRadXhelp.setPixmap(map)
        
        filtRadYlabel = QtWidgets.QLabel("Filtering_radius_y =")
        self.filtRadYedit = QtWidgets.QLineEdit("11")
        filtRadYhelp = QtWidgets.QLabel()
        filtRadYhelp.setPixmap(map)
        
        filtRadZlabel = QtWidgets.QLabel("Filtering_radius_z =")
        self.filtRadZedit = QtWidgets.QLineEdit("0")
        filtRadZhelp = QtWidgets.QLabel()
        filtRadZhelp.setPixmap(map)
        
        numberItlabel = QtWidgets.QLabel("Number of iterations =")
        self.numberItedit = QtWidgets.QLineEdit("1")
        numberIthelp = QtWidgets.QLabel()
        numberIthelp.setPixmap(map)
        
        minVoxFiltlabel = QtWidgets.QLabel("Minimum voxel filtering =")
        self.minVoxFiltedit = QtWidgets.QLineEdit("7")
        minVoxFilthelp = QtWidgets.QLabel()
        minVoxFilthelp.setPixmap(map)
        
        minVoxEstlabel = QtWidgets.QLabel("Minimum voxel estimation =")
        self.minVoxEstedit = QtWidgets.QLineEdit("7")
        minVoxEsthelp = QtWidgets.QLabel()
        minVoxEsthelp.setPixmap(map)
        
        histReslabel = QtWidgets.QLabel("Histogram resolution =")
        self.histResedit = QtWidgets.QLineEdit("2")
        histReshelp = QtWidgets.QLabel()
        histReshelp.setPixmap(map)
        
        minStdlabel = QtWidgets.QLabel("Minimum std =")
        self.minStdedit = QtWidgets.QLineEdit("0")
        minStdhelp = QtWidgets.QLabel()
        minStdhelp.setPixmap(map)
        
        maxStdlabel = QtWidgets.QLabel("Maximum std =")
        self.maxStdedit = QtWidgets.QLineEdit("100")
        maxStdhelp = QtWidgets.QLabel()
        maxStdhelp.setPixmap(map)
        
        absVallabel = QtWidgets.QLabel("Absolute value =")
        self.absValedit = QtWidgets.QLineEdit("0")
        absValhelp = QtWidgets.QLabel()
        absValhelp.setPixmap(map)
        
        filtGrid = QtWidgets.QGridLayout()
        filtGrid.addWidget(estRadXlabel, 0, 0)
        filtGrid.addWidget(self.estRadXedit, 0, 1)
        filtGrid.addWidget(estRadXhelp, 0, 2)
        filtGrid.addWidget(estRadYlabel, 1, 0)
        filtGrid.addWidget(self.estRadYedit, 1, 1)
        filtGrid.addWidget(estRadYhelp, 1, 2)
        filtGrid.addWidget(estRadZlabel, 2, 0)
        filtGrid.addWidget(self.estRadZedit, 2, 1)
        filtGrid.addWidget(estRadZhelp, 2, 2)
        filtGrid.addWidget(filtRadXlabel, 3, 0)
        filtGrid.addWidget(self.filtRadXedit, 3, 1)
        filtGrid.addWidget(filtRadXhelp, 3, 2)
        filtGrid.addWidget(filtRadYlabel, 4, 0)
        filtGrid.addWidget(self.filtRadYedit, 4, 1)
        filtGrid.addWidget(filtRadYhelp, 4, 2)
        filtGrid.addWidget(filtRadZlabel, 5, 0)
        filtGrid.addWidget(self.filtRadZedit, 5, 1)
        filtGrid.addWidget(filtRadZhelp, 5, 2)
        filtGrid.addWidget(numberItlabel, 6, 0)
        filtGrid.addWidget(self.numberItedit, 6, 1)
        filtGrid.addWidget(numberIthelp, 6, 2)
        filtGrid.addWidget(minVoxFiltlabel, 7, 0)
        filtGrid.addWidget(self.minVoxFiltedit, 7, 1)
        filtGrid.addWidget(minVoxFilthelp, 7, 2)
        filtGrid.addWidget(minVoxEstlabel, 8, 0)
        filtGrid.addWidget(self.minVoxEstedit, 8, 1)
        filtGrid.addWidget(minVoxEsthelp, 8, 2)
        filtGrid.addWidget(histReslabel, 9, 0)
        filtGrid.addWidget(self.histResedit, 9, 1)
        filtGrid.addWidget(histReshelp, 9, 2)
        filtGrid.addWidget(minStdlabel, 10, 0)
        filtGrid.addWidget(self.minStdedit, 10, 1)
        filtGrid.addWidget(minStdhelp, 10, 2)
        filtGrid.addWidget(maxStdlabel, 11, 0)
        filtGrid.addWidget(self.maxStdedit, 11, 1)
        filtGrid.addWidget(maxStdhelp, 11, 2)
        filtGrid.addWidget(absVallabel, 12, 0)
        filtGrid.addWidget(self.absValedit, 12, 1)
        filtGrid.addWidget(absValhelp, 12, 2)
        
        filtFrame.setLayout(filtGrid)
        filtFrame.setFrameStyle(QtWidgets.QFrame.StyledPanel | QtWidgets.QFrame.Raised)
        
        # Filter step 9
        filtFrame9 = QtWidgets.QFrame()
        title92 = QtWidgets.QLabel("Filtering - Joint denoising (step 9)")
        
        neighDirLabel = QtWidgets.QLabel("Number of neighboring directions =")
        self.neighDirEdit = QtWidgets.QLineEdit("6")
        neighDirHelp = QtWidgets.QLabel()
        neighDirHelp.setPixmap(map)
        
        estRadXlabel9 = QtWidgets.QLabel("Estimation_radius_x =")
        self.estRadXedit9 = QtWidgets.QLineEdit("2")
        estRadXhelp9 = QtWidgets.QLabel()
        estRadXhelp9.setPixmap(map)
        
        estRadYlabel9 = QtWidgets.QLabel("Estimation_radius_y =")
        self.estRadYedit9 = QtWidgets.QLineEdit("2")
        estRadYhelp9 = QtWidgets.QLabel()
        estRadYhelp9.setPixmap(map)
        
        estRadZlabel9 = QtWidgets.QLabel("Estimation_radius_z =")
        self.estRadZedit9 = QtWidgets.QLineEdit("2")
        estRadZhelp9 = QtWidgets.QLabel()
        estRadZhelp9.setPixmap(map)
        
        filtRadXlabel9 = QtWidgets.QLabel("Filtering_radius_x =")
        self.filtRadXedit9 = QtWidgets.QLineEdit("2")
        filtRadXhelp9 = QtWidgets.QLabel()
        filtRadXhelp9.setPixmap(map)
        
        filtRadYlabel9 = QtWidgets.QLabel("Filtering_radius_y =")
        self.filtRadYedit9 = QtWidgets.QLineEdit("2")
        filtRadYhelp9 = QtWidgets.QLabel()
        filtRadYhelp9.setPixmap(map)
        
        filtRadZlabel9 = QtWidgets.QLabel("Filtering_radius_z =")
        self.filtRadZedit9 = QtWidgets.QLineEdit("2")
        filtRadZhelp9 = QtWidgets.QLabel()
        filtRadZhelp9.setPixmap(map)
        
        filtGrid9 = QtWidgets.QGridLayout()
        filtGrid9.addWidget(estRadXlabel9, 0, 0)
        filtGrid9.addWidget(self.estRadXedit9, 0, 1)
        filtGrid9.addWidget(estRadXhelp9, 0, 2)
        filtGrid9.addWidget(estRadYlabel9, 1, 0)
        filtGrid9.addWidget(self.estRadYedit9, 1, 1)
        filtGrid9.addWidget(estRadYhelp9, 1, 2)
        filtGrid9.addWidget(estRadZlabel9, 2, 0)
        filtGrid9.addWidget(self.estRadZedit9, 2, 1)
        filtGrid9.addWidget(estRadZhelp9, 2, 2)
        filtGrid9.addWidget(filtRadXlabel9, 3, 0)
        filtGrid9.addWidget(self.filtRadXedit9, 3, 1)
        filtGrid9.addWidget(filtRadXhelp9, 3, 2)
        filtGrid9.addWidget(filtRadYlabel9, 4, 0)
        filtGrid9.addWidget(self.filtRadYedit9, 4, 1)
        filtGrid9.addWidget(filtRadYhelp9, 4, 2)
        filtGrid9.addWidget(filtRadZlabel9, 5, 0)
        filtGrid9.addWidget(self.filtRadZedit9, 5, 1)
        filtGrid9.addWidget(filtRadZhelp9, 5, 2)
        filtGrid9.addWidget(neighDirLabel, 6, 0)
        filtGrid9.addWidget(self.neighDirEdit, 6, 1)
        filtGrid9.addWidget(neighDirHelp, 6, 2)
        
        filtFrame9.setLayout(filtGrid9)
        filtFrame9.setFrameStyle(QtWidgets.QFrame.StyledPanel | QtWidgets.QFrame.Raised)
        
        # Bias Field
        biasFrame9 = QtWidgets.QFrame()
        titlebias = QtWidgets.QLabel("Bias Field (step 8)")
        
        imDimLabel = QtWidgets.QLabel("Image Dimension =")
        self.imDimEdit = QtWidgets.QLineEdit("3")
        imDimHelp = QtWidgets.QLabel()
        imDimHelp.setPixmap(map)
        
        shrinkFactLabel = QtWidgets.QLabel("Shrink factor =")
        self.shrinkFactEdit = QtWidgets.QLineEdit("3")
        shrinkFactHelp = QtWidgets.QLabel()
        shrinkFactHelp.setPixmap(map)
        
        bsplineFitLabel = QtWidgets.QLabel("B-Spline fitting =")
        self.bsplineFitEdit = QtWidgets.QLineEdit("[1000,3]")
        bsplineFitHelp = QtWidgets.QLabel()
        bsplineFitHelp.setPixmap(map)
        
        biasGrid = QtWidgets.QGridLayout()
        biasGrid.addWidget(imDimLabel, 0,0)
        biasGrid.addWidget(self.imDimEdit, 0,1)
        biasGrid.addWidget(imDimHelp, 0,2)
        biasGrid.addWidget(shrinkFactLabel, 1,0)
        biasGrid.addWidget(self.shrinkFactEdit, 1,1)
        biasGrid.addWidget(shrinkFactHelp, 1,2)
        biasGrid.addWidget(bsplineFitLabel, 2,0)
        biasGrid.addWidget(self.bsplineFitEdit, 2,1)
        biasGrid.addWidget(bsplineFitHelp, 2,2)
        
        biasFrame9.setLayout(biasGrid)
        biasFrame9.setFrameStyle(QtWidgets.QFrame.StyledPanel | QtWidgets.QFrame.Raised)
        
        
        """ Layouts """
        simpleLayout = QtWidgets.QVBoxLayout()
        simpleLayout.addStretch(1)
        simpleLayout.addWidget(title1)
        simpleLayout.addWidget(frame1)
        simpleLayout.addStretch(1)
        simpleLayout.addWidget(title2)
        simpleLayout.addWidget(frame2)
        simpleLayout.addStretch(1)
        
        advancedLayout = QtWidgets.QVBoxLayout()
        advancedLayout.addStretch(1)
        advancedLayout.addWidget(title41)
        advancedLayout.addWidget(filtFrame)
        advancedLayout.addStretch(1)
        advancedLayout.addWidget(title92)
        advancedLayout.addWidget(filtFrame9)
        advancedLayout.addStretch(1)
        advancedLayout.addWidget(titlebias)
        advancedLayout.addWidget(biasFrame9)
        advancedLayout.addStretch(1)
        
        simpleWidget.setLayout(simpleLayout)
        
        advancedWidget.setLayout(advancedLayout)
        
        tab.addTab(simpleWidget, "Basic Options")
        tab.addTab(advancedWidget, "Advanced Options")
        
        t = QtWidgets.QHBoxLayout()
        t.addWidget(tab)
        
        self.setLayout(t)
        
        self.fileName = 0
        
        self.loadXML()
        
    def browse(self):
        
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File","../PROTOCOLS","*.xml")
    
        if self.fileName:
            self.xmlEdit.setText(self.fileName)
            self.updateXML()
            
    def loadXML(self):

        stepTree = etree.parse("../PROTOCOLS/HARDIPrep_temp.xml")
        steps = stepTree.getroot()
        step1 = steps[0]
        
        if not (step1.xpath("/Steps/step/xmlFile") == []):
            path = step1[0]
            self.xmlEdit.setText(path.text)
        
    def updateXML(self, parent):

        parent.xmlSaved = True
        stepTree = etree.parse("../PROTOCOLS/HARDIPrep_temp.xml")
        steps = stepTree.getroot()
        step1 = steps[1]
        
        if not (step1.getchildren() == []):
            step1[0].text = self.xmlEdit.text()
            
            if self.maskUseRadioYes.isChecked():
                step1[1].text = "yes"
            else:
                step1[1].text = "no"
                
            step1[2].text = self.comboMethod.currentText()
            
            step1[3].text = self.estRadXedit.text()
            
            step1[4].text = self.estRadYedit.text()
        
            step1[5].text = self.estRadZedit.text()
            
            step1[6].text = self.filtRadXedit.text()
            
            step1[7].text = self.filtRadYedit.text()
            
            step1[8].text = self.filtRadZedit.text()
            
            step1[9].text = self.numberItedit.text()
            
            step1[10].text = self.minVoxEstedit.text()
            
            step1[11].text = self.minVoxFiltedit.text()
            
            step1[12].text = self.histResedit.text()
            
            step1[13].text = self.minStdedit.text()
            
            step1[14].text = self.maxStdedit.text()
            
            step1[15].text = self.absValedit.text()
            
            step1[16].text = self.imDimEdit.text()
            
            step1[17].text = self.shrinkFactEdit.text()
            
            step1[18].text = self.bsplineFitEdit.text()
            
            step1[19].text = self.neighDirEdit.text()
            
            step1[20].text = self.estRadXedit9.text()
            
            step1[21].text = self.estRadYedit9.text()
        
            step1[22].text = self.estRadZedit9.text()
            
            step1[23].text = self.filtRadXedit9.text()
            
            step1[24].text = self.filtRadYedit9.text()
            
            step1[25].text = self.filtRadZedit9.text()
                
        else :
            xmlFile = etree.SubElement(step1, "DTIPrep_XMLFile")
            xmlFile.text = self.xmlEdit.text()
            
            maskUse = etree.SubElement(step1, "Mask_Use")
            if self.maskUseRadioYes.isChecked():
                maskUse.text = "yes"
            else:
                maskUse.text = "no" 
                
            method = etree.SubElement(step1, "method")
            method.text = self.comboMethod.currentText()
            
            estradX = etree.SubElement(step1, "estradX")
            estradX.text = self.estRadXedit.text()
            
            estradY = etree.SubElement(step1, "estradY")
            estradY.text = self.estRadYedit.text()
            
            estradZ = etree.SubElement(step1, "estradZ")
            estradZ.text = self.estRadZedit.text()
            
            filtradX = etree.SubElement(step1, "filtradX")
            filtradX.text = self.filtRadXedit.text()
            
            filtradY = etree.SubElement(step1, "filtradY")
            filtradY.text = self.filtRadYedit.text()
            
            filtradZ = etree.SubElement(step1, "filtradZ")
            filtradZ.text = self.filtRadZedit.text()
            
            nbIt = etree.SubElement(step1, "NbIt")
            nbIt.text = self.numberItedit.text()
            
            voxEst = etree.SubElement(step1, "minVoxEst")
            voxEst.text = self.minVoxEstedit.text()
            
            voxFilt = etree.SubElement(step1, "minVoxFilt")
            voxFilt.text = self.minVoxFiltedit.text()
            
            histRes = etree.SubElement(step1, "histRes")
            histRes.text = self.histResedit.text()
            
            minStd = etree.SubElement(step1, "minStd")
            minStd.text = self.minStdedit.text()
            
            maxStd = etree.SubElement(step1, "maxStd")
            maxStd.text = self.maxStdedit.text()
            
            absVal = etree.SubElement(step1, "absVal")
            absVal.text = self.absValedit.text()
            
            imDim = etree.SubElement(step1, "imDim")
            imDim.text = self.imDimEdit.text()
            
            shrinkF = etree.SubElement(step1, "shrinkF")
            shrinkF.text = self.shrinkFactEdit.text()
            
            bsplineFit = etree.SubElement(step1, "bsplineFit")
            bsplineFit.text = self.bsplineFitEdit.text()
            
            neighDir = etree.SubElement(step1, "numbNeighboringDir")
            neighDir.text = self.neighDirEdit.text()
            
            estradX9 = etree.SubElement(step1, "estradX9")
            estradX9.text = self.estRadXedit9.text()
            
            estradY9 = etree.SubElement(step1, "estradY9")
            estradY9.text = self.estRadYedit9.text()
            
            estradZ9 = etree.SubElement(step1, "estradZ9")
            estradZ9.text = self.estRadZedit9.text()
            
            filtradX9 = etree.SubElement(step1, "filtradX9")
            filtradX9.text = self.filtRadXedit9.text()
            
            filtradY9 = etree.SubElement(step1, "filtradY9")
            filtradY9.text = self.filtRadYedit9.text()
            
            filtradZ9 = etree.SubElement(step1, "filtradZ9")
            filtradZ9.text = self.filtRadZedit9.text()
        
        xmlFile = open("../PROTOCOLS/HARDIPrep_temp.xml", "w")
        xmlFile.write(etree.tostring(stepTree, pretty_print = True))
        xmlFile.close()
        
        
