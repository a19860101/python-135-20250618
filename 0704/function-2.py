def foo(*args):
    return args

def foo2(*args):
    for i in args:
        print(i)

# foo2(1,2,3,'apple','banana',True,False)

# foo2(1,2,3,4,5)

def foo3(a,b,*args):
    return a,b,args

print(foo3('a','b',1,2,34,5,6,7,8,9))

def foo4(**kwargs):
    return kwargs

print(foo4(name='John', mail='asdf@mail.com'))

def foo5(x,y,*args,**kwargs):
    return x,y,args,kwargs

print(foo5(100,200,1,2,3,4,5,name='John'))