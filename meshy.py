
import inspect
AT = 'attr_'

# The matching algorithm implementation: hints and general principles
#   -> Given the fact that the original object is tree-like, there is necessary two cases:
#       + Full identity: The tree representations of the matcher and the matchee are the same
#       + Structure identity: 
#            +- Wilicards
#            

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

def Term(*args):
     argsize = len(args)
     def wrapper(*ag):
         if argsize + 1 != len(ag):
             raise TypeError(f"Expecting {argsize} positional arguments not {len(ag) - 1}.")
         def __init__(self, *arguments):
             issues = []
             for (n, obj) in enumerate(zip(args, arguments)):
                 clz, ins = obj
                 if clz is type:
                     continue
                 if ins.__class__ != clz:
                     print("--->", ins, clz.__name__)
                     issues.append(f"argument {n + 1} must be a {clz.__qualname__}")
             if issues:
                 raise TypeError(' and '.join(issues))
             for (k, arg) in enumerate(arguments):
                 setattr(self, '_'+str(k), arg)  
             items = list(self.__dict__.values())
             self.ego = O(items.pop(0), [O(z, []) for z in items ])
         return __init__(*ag)

     def __str__(self):
         return str(self.ego)
     def __eq__(self, other):
         return self.ego == other.ego

     def __mt__(self, other):
         # if reached eq, good!
         #
         pass
     return type("", (object,), { '__init__' : wrapper, 'argsize': argsize, '__str__': __str__, '__repr__': __str__ })

def adt(clz):
    annots = clz.__annotations__
    for clz_n in annots:
        annots[clz_n].__name__     = clz_n
        annots[clz_n].__qualname__ = clz_n
    print(clz.__dict__)
    globals().update(clz.__annotations__)
    return clz

# The most suitable representation of an ADT is
# a tree-like structure with n-1 first-level ramifications 

def melt_adt_to_tree(obj):
    items = list(obj.__dict__.items())
    return 
    
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
    def __init__(self, data,  kids):
        self.data = data
        self.kids = kids
        assert isinstance(kids, list)
    __str__  = lambda self: f"{self.__class__.__name__}({self.data}, [{','.join(map_(str, self.kids))}])"
    __repr__ = __str__

    def __eq__(self, other):
        return self.data == other.data and all(u.data == z.data and 
                                               z.kids == u.kids 
                                               for (u, z) in zip(self.kids, other.kids)
        )

    def __mt__(self, other):
        pass



@adt
class List: 
    Nil  : Term()
    Cons : Term(type, type)
#    def Cons(a : type, l : Term(List(type))) -> Term(List(type)): pass

def check(fn): pass

@check
def size(q : List) -> int:
    res = case(q).when(
      Nil, do=lambda: 0
    ).when(
      Cons(a, rem), do=lambda: 1 + size(rem)
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

