# Definition

def data_args(clazz):
    return list(
        filter(
            lambda s: not (
                s is clazz or s is object
            ), 
            clazz.__mro__
        )
    )

def loop(cond, code, arg):
    while cond(arg):
        arg = code(arg)

def if_then_else(cond, code_if_true, code_if_not):
    if cond:
        code_if_true()
    else:
        code_if_not()

# encoded loop

(lambda: (
 n := 1,
 cond := lambda n: n < 11,
 loop(cond, lambda n: (
     print(n),
     n := n + 1,
     )[1], n)
))()

# encoded if then else
(lambda n: (
 cond := n < 11,
 if_then_else(cond, lambda: (
     print("YES"),
     ), lambda: (
     print("NO")
 ))
))(10)


class BinT:
    def __init__(self, x, fg=None, fd=None):
        self.content = x
        self.fg = fg
        self.fd = fd

    def __str__(self):
        cnt = str(self.content)
        if self.fg == self.fd == None:
            return 'Leaf(' + str(cnt) + ')'
        return "Tree(" + cnt + ", " +  str(self.fg) + ", " + str(self.fd) + ")"

    def to_prefix(self):
        if self.fg == self.fd == None:
            return [self.content]
        return [self.content, self.fg.to_prefix(), self.fd.to_prefix()]

    def __eq__(self, other):
        return self.to_prefix() == other.to_prefix()

    __repr__ = __str__

#Tree case:

"""
obj = 10
case(obj).when(
  Leaf(), do=lambda: (
      print("Got a Leaf"),
      print("Got a Leaf"),
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
"""

# Output scenario:
#   -> non-exausted pattern matching
#   -> exception occuring
