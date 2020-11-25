
import inspect
AT = 'attr_'

# The matching algorithm implementation: hints and general principles
#   -> Given the fact that the original object is tree-like, there is necessary two cases:
#       + Full identity: The tree representations of the matcher and the matchee are the same
#       + Structure identity: 
#            +- Wilicards
#            
# Addressing the willicard issue:
_ = 'any'

def map_(fn, cl):
    return list(map(fn, cl))

class case:
    def __init__(self, obj):
        self.obj = obj
    def when(self, p_obj, do=None): # return self
        if self.obj.__class__ is p_obj.__class__:
            if (not p_obj.__dict__):
                if do: do()
            elif p_obj.__dict__:
                globals().update(p_obj.__dict__)
                for attr in p_obj.__dict__:
                    if hasattr(p_obj, attr):
                        pass
            if do: 
                do()

def yieldtree(*alfas):
    def qz(alf):
        if hasattr(alf, 'ego'):
            return alf.ego
        elif alf.__class__ == O:
            return alf
        return O(alf, [])
    return [qz(alf) for alf in alfas]

class match:
    def __init__(self, obj):
        self.obj = obj
    def when(self, p_obj, do=None): # return self
        if self.obj.__class__ is p_obj.__class__:
            if self.obj.ego >> p_obj.ego:
                if p_obj.kwargs: 
                    globals().update({
                        o:self.obj.ego.kids[subtree_idx - 1].data 
                            for o, subtree_idx in p_obj.kwargs.items()
                    })
                if p_obj.__dict__:
                    globals().update(p_obj.__dict__)
                do()

def Term(*args):
     argsize = len(args)
     def wrapper(*ag, **kargs):
         if argsize + 1 != len(ag) + len(kargs):
             raise TypeError(f"Expecting {argsize} positional arguments not {len(ag) - 1}.")

         def __init__(self, *arguments, **kwargs):
             issues = []
             for (n, obj) in enumerate(zip(args, arguments)):
                 clz, ins = obj
                 if str(ins) == _: continue
                 if clz is type: continue
                 if ins.__class__ != clz:
                     issues.append(f"argument {n + 1} must be a {clz.__qualname__}")
             if issues:
                 raise TypeError(' and '.join(issues)) 

             for (k, arg) in enumerate(arguments):
                 setattr(self, '_'+str(k), arg)

             for s in range(k+1, len(kwargs)+1):
                 setattr(self, '_'+str(s), _)

             items = list(self.__dict__.values())
             self.ego2 = yieldtree(*items)
             self.ego = O(items.pop(0), [])
             for z in items:
                 if getattr(z, 'argsize', False):
                     if hasattr(z, 'ego'):
                         self.ego.kids.append(z)
                     elif z.__class__ != O:
                         self.ego.kids.append(O(z, []))
                     else:
                         self.ego.kids.append(z)
             self.kwargs = {m: idx for m, idx in zip(kwargs, range(k+1, len(kwargs)+1))}
         return __init__(*ag, **kargs)

     def __repr__(self):
         clz_nm = self.__class__.__name__ + '('
         for i in range(argsize):
            q = getattr(self, '_'+str(i))
            q = q.__name__ if hasattr(q, 'mro') else repr(q)
            if q == repr(_):
                clz_nm += '_'
            else: 
                clz_nm += q
            clz_nm += ', '
         return clz_nm[:-2] + ')'

     def __str__(self):
         return str(self.ego)

     __eq__ = lambda self, other: self.ego == other.ego
     return type(f"ADT_{argsize}_CLAZZ", (object,), {
                                 '__init__' : wrapper, 
                                 'argsize': argsize, 
                                 '__str__': __str__, 
                                 '__eq__': __eq__,
                                 '__repr__': __repr__ })

def adt(clz):
    annots = clz.__annotations__
    for clz_n in annots:
        annots[clz_n].__name__     = clz_n
        annots[clz_n].__qualname__ = clz_n
    #print(clz.__dict__)
    globals().update(clz.__annotations__)
    return clz

# The most suitable representation of an ADT is
# a tree-like structure with n-1 first-level ramifications 
    
@adt
class List: 
    Nil  : Term()
    Cons : Term(type, type)

@adt
class Tree:
    Leaf : Term(int)
    Node : Term(int, type, type)

class __Logos__(type):
     def __new__(cls, name, bases, dictionary):
         anns = dictionary['__annotations__']
         for name in anns:
             sig = inspect.signature(dictionary[name].__init__)
             dictionary[name] = type(name, (object,), {
                 method : generate_method(dictionary[name], method) for method in [ 
                                                                                    '__init__',
                                                                                    '__str__',
                                                                                    '__eq__', 
                                                                                    '__mt__'  
                                                                                  ]
            })
         globals().update(dictionary)
         return super().__new__(cls, name, bases, dictionary)

def generate_show(arg): pass

class O(object):
    def __init__(self, data, kids):
        self.data = data
        self.kids = kids
        assert isinstance(kids, list)
    __str__  = lambda self: \
        f"{self.__class__.__name__}({'_' if str(self.data) == _ else self.data}, [{', '.join(map_(str, self.kids))}])"
    __repr__ = __str__

    def __eq__(self, other):
        return self.data == other.data and all(u.data == z.data and 
                                               z.kids == u.kids 
                                               for (u, z) in zip(self.kids, other.kids)
        )

    def __mt__(self, other):
        zq = lambda u, z: (u.data == z.data or str(z.data) == _)
        return zq(self, other) and all(zq(z, u) and 
                                         all(s >> w 
                                             for (s, w) in zip(z.kids, u.kids))
                                                         for (u, z) in zip(self.kids, other.kids))
    __rshift__ = __mt__




@adt
class List: 
    Nil  : Term()
    Cons : Term(type, type)
#   def Cons(a : type, l : Term(List(type))) -> Term(List(type)): pass

def check(fn): pass

@check
def size(q : List) -> int:
    res = case(q).when(
      Nil, do=lambda: 0
    ).when(
      Cons(_, rem), do=lambda: 1 + size(rem)
    )
    return res

"""
class List:
    Nil  = Term()
    Cons = Term(type, List(type))

@adt
class List: 
    Nil  : Term()
    Cons : Term(type, List(type))

Cons("A", Cons("B", Cons("C", Nil)))

List.fromList([10])
class Tree(A):
    Leaf = Term(A)
    FG   = Term(Tree(A))
    FD   = Term(Tree(A))
"""
