import os

def generateCSS(filename, familyname, folder):

    cssFile = str(os.path.splitext(filename)[0]) + ".css"

    template = "@font-face {\
        \n\tfont-family: '" + familyname + "';\
        \n\tsrc: url('" + filename + ".woff2') format('woff2'),\
        \n\turl('" + filename + ".woff') format('woff'),\
        \n\turl('" + filename + ".ttf') format('truetype');\
        \n\tfont-style: normal;\
        \n\tfont-weight: normal;\
        \n\tfont-display: swap;\
        \n}\n\n"

    open(folder + '/' + cssFile, "a").writelines(template)
