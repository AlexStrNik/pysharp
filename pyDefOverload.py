
class DefOverload:
    defs = {}
class OverloadDecorator(object):
    def __init__(self,name):
        self.name = name
        if DefOverload.defs.get(name,'None')=='None':
            DefOverload.defs[name]=[]
    def __call__(self,fn,*args,**kwargs):
        DefOverload.defs[self.name].append(fn)
        def newfunc(*args,**kwargs):
            for fns in DefOverload.defs[self.name]:
                try:
                    return fns(*args,**kwargs)
                except TypeError as ter:
                    continue
        return newfunc
@OverloadDecorator('plus')
def plus(a,b):
    return a + b
@OverloadDecorator('plus')
def __plus(a):
    return a[0]+a[1]
print(plus(1,2))
print(plus([1,3]))
