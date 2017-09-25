i=5
x = ['import os', 'if __file__[-8:] != "Sully.py":', '    i=i-1', 'if i >= 0:', '    try:', '        f=open("Sully_"+str(i)+".py", "w")', '        f.write("i=%d"%i+chr(10)+"x = "+str(x)+chr(10)+chr(10).join(x))', '        f.close()', '        os.system("python Sully_"+str(i)+".py")', '    except:', '        raise']
import os
if __file__[-8:] != "Sully.py":
    i=i-1
if i >= 0:
    try:
        f=open("Sully_"+str(i)+".py", "w")
        f.write("i=%d"%i+chr(10)+"x = "+str(x)+chr(10)+chr(10).join(x))
        f.close()
        os.system("python Sully_"+str(i)+".py")
    except:
        raise