import convert
import shutil

def convertWOFF(fontfile,foldername):
    newTTFname = convert.WOFFtoTTF(fontfile,foldername)
    convert.WOFFtoTTFtoWOFF2(newTTFname)
    shutil.copyfile(fontfile, foldername + '/' + fontfile)