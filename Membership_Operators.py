x=24
if type(x) is int:
    print("True")
else:
    print("False")   
x=2.6     
if type(x) is float:
    print("True")
else:
    print("False")    
x=34
y=34
if (x is y):
    print("x and y have the same indentity")
y=46
if (x is not y):
    print("x and y have different identities")
