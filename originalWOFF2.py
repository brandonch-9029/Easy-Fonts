import convert
import shutil

def convertWOFF2(fontfile,foldername):
    newTTFname = convert.WOFFtoTTF(fontfile,foldername)
    convert.WOFF2toTTFtoWOFF(newTTFname)
    shutil.copyfile(fontfile, foldername + '/' + fontfile)