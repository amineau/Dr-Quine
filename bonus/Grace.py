x = ['"""\n    comment\n"""', 'def define1():', '    None', 'def define2():', '    None', 'def define3():', '    f=open("Grace_kid.py", "w")', '    f.write("x = "+str(x)+chr(10)+chr(10).join(x))', '    f.close()', 'try:', '    define3()', 'except:', '    raise']
"""
    comment
"""
def define1():
    None
def define2():
    None
def define3():
    f=open("Grace_kid.py", "w")
    f.write("x = "+str(x)+chr(10)+chr(10).join(x))
    f.close()
try:
    define3()
except:
    raise