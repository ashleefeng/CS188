import pdb

def foo():
    a = 5
    b = [7,8,9]
    print a*b

def bar():
    a = 3
    b = "cool "
    pdb.set_trace() # This sets a breakpoint here
    foo()
    print a*b