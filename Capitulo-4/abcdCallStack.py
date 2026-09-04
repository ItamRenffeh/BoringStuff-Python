def a():
    print("a() Starts")
    b()
    d()
    print("a() Returns")

def b():
    print("b() Starst")
    c()
    print("b() Retuns")

def c() :
    print ("c() Stars")
    print("c() Returns")

def d() :
    print("d() Starts")
    print("d() Returns")

a()
