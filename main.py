import generate, originalTTF, os

fontfile = "Ubuntu-Regular.ttf"
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

    generate.generateCSS(fontfile, fontname, foldername)

main(fontfile,foldername,"Ubuntu")