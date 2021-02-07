# py-adt

```python
@adt
class List: 
    Nil  : Term()
    Cons : Term(type, type)

def abc():
    print("---->", rem)
    return 1 + size(rem)

def size(q : List) -> int:
    res = match(q).when(
      Nil, do=lambda: 0
    ).when(
      Cons(_, rem=_), do=lambda: 1 + size(rem)
    ).unwrap()
    return res
```

Trying to implement something close to Algebraic Data Types and pattern matching in Python.


