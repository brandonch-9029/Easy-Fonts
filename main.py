import os, generateCSS, originalTTF, originalWOFF, originalWOFF2

fontfile = "Ubuntu-Regular.woff2"
foldername = "uniquefolder"

def main(fontfile, foldername, fontname):
    os.mkdir(foldername)
    fileext = str(os.path.splitext(fontfile)[1])

    if fileext == ".ttf":
        originalTTF.convertTTF(fontfile,foldername)

    elif fileext == ".woff":
        originalWOFF.convertWOFF(fontfile,foldername)

    elif fileext == ".woff2":
        originalWOFF2.convertWOFF2(fontfile,foldername)
    

    generateCSS.generateCSS(fontfile, fontname, foldername)

main(fontfile,foldername,"Ubuntu")