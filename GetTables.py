import re
import sys
import os

#  list all files with a special directory
filepath='D:\\Desktop\\test'
tableset=set()
constr='@'
def listfiles(filepath):
    for root,pathname,filename in os.walk(filepath):
        for fn in filename:
            path=os.path.join(root,fn)
            #print path
            fr=open(path)
            str=fr.read()
            reg = r'((?i)(from)|(join))\s+[a-zA-Z0-9\_]+\.\s*([a-zA-Z0-9\_]+)'
            rsl=re.findall(reg,str)
            for m in rsl:
                tableset.add(m[3].lower())
            str1=constr.join(tableset)
            fw=open('D:\\Desktop\\test\\result.txt','w')
            (x,y)=os.path.splitext(fn)
            wstr =x+'\t'+str1
            fw.write(wstr)
            fw.close()
            fr.close()
listfiles(filepath)

f2=open('D:\\Desktop\\test\\result.txt')
str=f2.read()
print str
f2.close()
sys.exit()
