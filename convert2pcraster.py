# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 18:43:14 2016

@author: jkw
"""

import os, glob
import sys

def convert(pattern,outputprefix):
    count = 0
    inputFiles = glob.glob(pattern)
    inputFiles.sort()
    print "\nConverting files to PCRaster format",
    for inputFile in inputFiles:
        count += 1
        sys.stdout.write('.')
        if count < 10:
            extension = "00" + str(count)
        else:
            extension = "0" + str(count)
        cmd = "gdal_translate -of PCRaster -ot Float32 " + inputFile + " " + outputprefix + "." + extension    
        os.system(cmd)
        
def rename(pattern,outputprefix, offset):
    count = 0
    inputFiles = glob.glob(pattern)
    inputFiles.sort()
    for inputFile in inputFiles:
        count += 1
        print "converting file", count, " " + inputFile
        if count + offset < 10:
            extension = "00" + str(count + offset)
        else:
            extension = "0" + str(count + offset)
        os.rename(inputFile,outputprefix + "." + extension)
        
def resample(pattern,outputprefix,cloneName):
    count = 0
    inputFiles = glob.glob(pattern)
    inputFiles.sort()
    print "\nResampling files",
    for inputFile in inputFiles:
        count += 1
        sys.stdout.write('.')
        if count < 10:
            extension = "00" + str(count)
        else:
            extension = "0" + str(count)
        cmd = "resample " + inputFile + " " + outputprefix + "." + extension + " --clone " + cloneName
        os.system(cmd)
        

        