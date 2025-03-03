#!/usr/bin/python3.6
import os
import random


def BetterRename(oldname,newname):
    f1 = open(oldname,'rb')
    data = f1.read()
    f1.close
    f2 = open(newname,'wb')
    f2.write(data)
    f2.close()
    os.remove(oldname)
    
dirs = os.listdir()
cwd = os.getcwd()
for directory in dirs:
    basename = os.path.basename(directory)
    if (not os.path.isfile(directory)) and basename != 'MISC':
        try:
            base = cwd+'/'
            os.chdir(base+directory)
            wavfilename = directory
            iName = 1
            files = os.listdir(base+directory)
            xtraZeros = len(str(len(files)))
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext == '.wav' and os.path.exists(file):
                    xtra = ''
                    for i in range(xtraZeros-len(str(iName))):
                        xtra += '0'
                    ext = '.wav'
                    newfn = '{}_{}{}_{}{}'.format(wavfilename,xtra,iName,random.randint(0,5000),ext)
                    while os.path.exists(newfn):
                        newfn = '{}_{}{}_{}{}'.format(wavfilename,xtra,iName,random.randint(0,5000),ext)
                    #print(newfn)
                    BetterRename(file,newfn)
                    iName += 1
        except:
            pass
            

