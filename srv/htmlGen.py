import os, sys

def getHtml():
    ret = ""

    files = os.listdir(path='./data/')
    ret += "<table>"
    for fn in files:
        ret += "<tr><td>"
        f = open('./data/' + fn)
        line = f.read()
        ret += '<h3>' + line + '</h3>'
        ret += "</td></tr>"
        f.close()
        
    ret += "</table>"

    return ret

if __name__ == "__main__":
    print(getHtml())
