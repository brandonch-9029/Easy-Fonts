import convert

def convertTTF(fontfile,foldername):
    convert.WOFFtoTTF(fontfile,foldername)
    convert.TTFtoWOFF2(fontfile,foldername)