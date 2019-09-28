import time
import shutil
import os 

def fileTransfer(path1,path2):
    curDirectory = os.path.dirname(os.path.realpath(__file__))
    print(curDirectory)
    files=[]
    for r, d, f in os.walk(curDirectory + path1):
        for file in f:
            files.append(os.path.join(r, file))
    toDirectory = curDirectory + path2
    for f in files:
       result = shutil.move(f, toDirectory)

if __name__ == "__main__": 
    a = time.time()
    fileTransfer("\Directory1", "\Directory2")
    print (time.time() - a)
