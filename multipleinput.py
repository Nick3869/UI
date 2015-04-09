# -*- coding: utf-8 -*-

"""

@author: Nicolas Fanjat
 Scientific Computing and Imaging Institute
 University of Utah
 02/17/2015
 
"""

import os

def listdirectory(path):
    files_list=[]  
    for root, dirs, files in os.walk(path):  
        for i in files:  
            files_list.append(os.path.join(root, i))  
    return files_list

def execution(self , context):
    name = self.input.name
    files_list = listdirectory(name)
    
    for x in files_list:
        filename = x
        ext = os.path.splitext(x)[1]

        
#        if ((ext == '.nrrd') or (ext == '.nhdr')):