from fontTools.ttLib import TTFont
import os

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

