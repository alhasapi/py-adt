
"""
def f(a, q):
...     q()
...
>>> f(True, lambda: (
... print(1),
... d := 10,
... print(d)
... ))
1
10
>>>

"""
# Definition
#   class Tree: pass
#   class Leaf(a): pass
#   class _Tree(a, a): pass

class Bool:
    is_bool = lambda self, o: o.__class__ in [tRue, fAlse]
class tRue(Bool): pass
class fAlse(Bool): pass

def data_args(clazz):
    return list(filter(lambda s: not (s is clazz or s is object), clazz.__mro__))

#   data("Bool").either("T", "F")
#   data("Tree").either("T", "F")
def when(self, structure): pass

# Usage
# Bool case
"""
case(obj).when(
  T, lambda: (
      'a',
      'z',
      'w',
      's',
      't',
  )
).when(
  F, lambda: (
      'a',
      'z',
      'w',
      's',
      't',
  )
)
"""
def loop(cond, code, arg):
    while cond(arg):
        arg = code(arg)

def if_then_else(cond, code_if_true, code_if_not):
    if cond:
        code_if_true()
    else:
        code_if_not()

# Regular loop:
def from_one_to_10():
    n = 1
    while n < 11:
        print(n)
        n += 1

# encoded loop

(lambda: (
 n := 1,
 cond := lambda n: n < 11,
 loop(cond, lambda n: (
     print(n),
     n := n + 1,
     )[1], n)
))()

# Regular if then else:
def f(n):
    if n > 0:
        print("YES")
    else:
        print("NO")

# encoded if then else
(lambda n: (
 cond := n < 11,
 if_then_else(cond, lambda: (
     print("YES"),
     ), lambda: (
     print("NO")
 ))
))(10)

class case:
    def __init__(self, obj): pass
    def when(self, obj, do=None): return self
#Tree case:
obj = 10
case(obj).when(
  Leaf(), do=lambda: (
      print("Got a Leaf"),
  )
).when(
  Leaf(a=10), do=lambda: (
      print(f"Got a Leaf with {a}"),
      print(f"It is cool")
  )
).when(
  _Tree(_Tree(Leaf(1), Leaf(2)), _Tree(Leaf(1), Leaf(2))), do=lambda: (
      print("A forest"),
      print("That is great!"),
      print("Nope"),
  )
).when(
  _Tree(Leaf(10), Leaf(9))
)

# Output scenario:
#   -> non-exausted pattern matching
#   -> exception occuring
#   ->
#   -> non-exausted pattern matching
