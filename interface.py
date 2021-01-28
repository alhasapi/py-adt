#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import *

def adt(clz):
    annots = clz.__annotations__
    for clz_n in annots:
        annots[clz_n].__name__     = clz_n
        annots[clz_n].__qualname__ = clz_n
    #print(clz.__dict__)
    globals().update(clz.__annotations__)
    return clz

@adt
class Tree:
    Leaf : Term(int)
    Node : Term(int, type, type)

@adt
class List: 
    Nil  : Term()
    Cons : Term(type, type)
#   def Cons(a : type, l : Term(List(type))) -> Term(List(type)): pass

def check(fn): pass

def abc():
    print("---->", rem)
    return 1 + size(rem)

def size(q : List) -> int:
    res = match(q).when(
      Nil, do=lambda: 0
    ).when(
      #Cons(_, rem=_), do=lambda: 1 + size(rem)
      Cons(_, rem=_), do=abc
    ).unwrap()
    return res
