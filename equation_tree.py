from numpy.random import random

class Node:
    def __init__(self):
        self.val = None
        self.name = None
        self.eq_class = None
        self.anon_fn = None
        self.nextL = None
        self.nextR = None

class EquationTree:

    def __init__(self):
        self.head = Node()

    def print_tree(self):
        def recurse(node,spacing):  
            if node.val is not None:          
                print(spacing+node.name+'='+str(node.val))
            else:
                print(spacing+node.name)
            if node.nextL is not None:
                recurse(node.nextL,spacing+'  ')
            if node.nextR is not None:
                recurse(node.nextR,spacing+'  ')
        recurse(self.head,'')

    def fix_constants(self,const_range):
        node = self.head
        def recurse(node):
            if node.eq_class == 'const' and node.name != 'x':
                node.val = const_range[0]+(const_range[1]-const_range[0])*random()
            if node.nextL is not None:
                recurse(node.nextL)
            if node.nextR is not None:
                recurse(node.nextR)
        recurse(node)

    def evaluate(self,x):
        node = self.head
        def get_value(node):
            if node.eq_class == 'const':
                if node.name == 'x':
                    return x
                else:
                    return node.val
            if node.eq_class == 'fn':
                return node.anon_fn(get_value(node.nextL))
            if node.eq_class == 'op':
                return node.anon_fn(get_value(node.nextL),get_value(node.nextR))
        return get_value(node)