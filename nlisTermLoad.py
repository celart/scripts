import nodes
import re

def parse(fName):
    arr=[]
    f=open(fName, "r")
    n=1
    for i in f:
        p = re.compile("[-0-9.]+[Ee]*[-0-9.]*")
        l = p.findall(i)
        obj=nodes.node()
        if len(l)==4:        
            obj.setNum(n)
            obj.setX(float(l[0].replace(" ", "")))
            obj.setY(float(l[1].replace(" ", "")))
            obj.setZ(float(l[2].replace(" ", "")))
            obj.setT(float(l[3].replace(" ", "")))
            #print(obj)
            arr.append(obj)
            n+=1
    return arr

