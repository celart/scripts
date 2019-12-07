import nodes
import re

def parse(fName):
    arr=[]
    f=open(fName, "r")
    for i in f:
        p = re.compile("\s*[-0-9E.]+")
        l = p.findall(i)
        obj=nodes.node()
        if len(l)>=4:        
            obj.setNum(int(l[0].replace(" ", "")))
            obj.setX(float(l[1].replace(" ", "")))
            obj.setY(float(l[2].replace(" ", "")))
            obj.setZ(float(l[3].replace(" ", "")))
            #print(obj)
            arr.append(obj)
    return arr

