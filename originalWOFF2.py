import convert

def convertTTF(fontfile,foldername):
    convert.TTFtoWOFF(fontfile,foldername)
    convert.TTFtoWOFF2(fontfile,foldername)