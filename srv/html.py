import os, sys

def getHtml():
    ret = ""

    files = os.listdir(path='./data/')
    ret += "<td>"
    for fn in files:
        ret += "<tr>"
        f = open('./data/' + fn)
        line = f.read()
        ret += line
        ret += "</tr>"
        
    ret += "</td>"

    return ret

if __name__ == "__main__":
    print(getHtml())
