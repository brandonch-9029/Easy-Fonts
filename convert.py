from fontTools.ttLib import TTFont
import os

# This file contains the functions that perform a direct conversion from one file format to another

# TTF to WOFF
def TTFtoWOFF(filename, folder):
    f = TTFont(filename)
    f.flavor = 'woff'
    f.save(str(folder) + '/' + str(os.path.splitext(filename)[0]) +'.woff')

# TTF to WOFF2
def TTFtoWOFF2(filename, folder):
    f = TTFont(filename)
    f.flavor = 'woff2'
    f.save(str(folder) + '/' + str(os.path.splitext(filename)[0]) +'.woff2')

# WOFF/WOFF2 to TTF
def WOFFtoTTF(filename, folder):
    f = TTFont(filename)
    f.flavor = None
    f.save(str(folder) + '/' + str(os.path.splitext(filename)[0]) +'.ttf')
    newTTFname = str(folder) + '/' + str(os.path.splitext(filename)[0]) +'.ttf'
    return newTTFname

# WOFF to TTF to WOFF2
def WOFFtoTTFtoWOFF2(filename):
    f = TTFont(filename)
    f.flavor = 'woff2'
    f.save(str(os.path.splitext(filename)[0]) +'.woff2')

# WOFF2 to TTF to WOFF
def WOFF2toTTFtoWOFF(filename):
    f = TTFont(filename)
    f.flavor = 'woff'
    f.save(str(os.path.splitext(filename)[0]) +'.woff')