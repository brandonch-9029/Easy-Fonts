import convert
import shutil

def convertTTF(fontfile,foldername):
    convert.TTFtoWOFF(fontfile,foldername)
    convert.TTFtoWOFF2(fontfile,foldername)
    shutil.copyfile(fontfile, foldername + '/' + fontfile)
