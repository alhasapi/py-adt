# py-adt

Trying to implement something close to Algebraic Data Types and pattern matching in Python, with syntax similar to this.

```python
@adt
class List: 
    Nil  : Term()
    Cons : Term(type, type)

def size(q : List) -> int:
    res = match(q).when(
      Nil, do=lambda: 0
    ).when(
      Cons(_, rem=_), do=lambda: 1 + size(rem)
    ).unwrap()
    return res
    
    
@adt
class Tree: 
    Leaf  : Term()
    BinOp : Term(type, type)
    
def something(obj : Tree) -> str:
    case(obj).when(
        Leaf(), do=lambda: (
        print("Got a Leaf")
    )
    ).when(
        Leaf(a=10), do=lambda: (
        print(f"Got a Leaf with {a}"),
        print(f"It is cool")
    )
    ).when(
     # The structure analyzer is expected here ...
        _Tree(0, _Tree(10, Leaf(1), Leaf(2)), _Tree(9, Leaf(1), Leaf(2))), do=lambda: (
        print("A forest"),
        print("This is great!"),
        print("Nope"),
    )
    ).when(
        _Tree(Leaf(), Leaf())
    )    
    
```

```haskell
data Tree = Leaf Int | Node Int Tree Tree deriving Show

size :: Tree -> Int
size Leaf _ = 1
size (Node _ l, r) = 1 + size l + size r
```



