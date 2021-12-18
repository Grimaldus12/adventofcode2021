import math
import sys


class Value:
    def __init__(self, value, parent):
        self.value = value
        self.parent=parent

    def print(self):
        print(self.value)

    def split(self):
        new_pair = Pair(self.parent.indent, parent=self.parent)
        new_pair.left,new_pair.right = Value(math.floor(self.value/2), parent=new_pair), Value(math.ceil(self.value/2), parent=new_pair)
        if self.parent.left == self: self.parent.left = new_pair
        else: self.parent.right = new_pair

    def magnitude(self):
        return self.value

    def toString(self):
        return str(self.value)


class Pair:
    def __init__(self, indent, left=None, right=None, parent=None):
        self.indent = indent
        self.parent = parent
        self.left = left
        self.right = right


    @classmethod
    def parse_children(cls, expression_str, indent, parent = None):
        if expression_str[0] == '[':
            expression_str = expression_str[1:len(expression_str) - 1]
        opened = 0
        pair_split = None
        for i,c in enumerate(expression_str):
            if c == ',' and opened == 0:
                pair_split = i
                break
            elif c == '[': opened += 1
            elif c == ']': opened -= 1
        left,right = expression_str[:pair_split], expression_str[pair_split + 1:]

        pair = Pair(indent, expression_str, parent=parent)
        pair.left = Value(int(left),pair) if left[0] != '[' else cls.parse_children(expression_str[:pair_split], indent + 1, pair)
        pair.right = Value(int(right),pair) if right[0] != '[' else cls.parse_children(expression_str[pair_split + 1:], indent + 1, pair)
        return pair

    def print(self):
        print(self.parent)
        self.left.print()
        self.right.print()

    def traverse(self, indent=1):
        if isinstance(self.left, self.__class__): yield from self.left.traverse(indent+1)
        else: yield self.left, indent
        yield self, indent
        if isinstance(self.right, self.__class__): yield from self.right.traverse(indent+1)
        else: yield self.right, indent

    def reduce(self):
        while self.reduce_action(): pass

    def reduce_action(self):
        for node, indent in self.traverse():
            if isinstance(node, self.__class__) and indent > 4:
                node.explode()
                return True
        for node, indent in self.traverse():
            if isinstance(node, Value) and node.value >= 10:
                node.split()
                return True
        return False

    def explode(self):
        left_neighbor = self.find_adjacent_node(True)
        right_neighbor = self.find_adjacent_node(False)
        if left_neighbor is not None: left_neighbor.value += self.left.value
        if right_neighbor is not None: right_neighbor.value += self.right.value
        replace_with_value = Value(0, self.parent)
        if self.parent.left == self: self.parent.left = replace_with_value
        else: self.parent.right = replace_with_value

    def find_adjacent_node(self, left):
        traverse_parents,traverse_children = self.parent,self
        while traverse_parents is not None:
            if left: next_neighbor = traverse_parents.left
            else: next_neighbor = traverse_parents.right

            if next_neighbor != traverse_children:
                candidate_node = next_neighbor
                while isinstance(candidate_node, Pair):
                    if left: candidate_node = candidate_node.right
                    else: candidate_node = candidate_node.left
                return candidate_node
            traverse_children, traverse_parents = traverse_parents, traverse_parents.parent
        return None

    def magnitude(self):
        return 3*self.left.magnitude() + 2*self.right.magnitude()

    def toString(self):
        return f'[{self.left.toString()},{self.right.toString()}]'



def parse_added(added):
    return Pair.parse_children(added, 0)

def add_snailfish(x, y):
    added = '[' + x.strip() + ',' + y.strip() + ']'
    root_pair = parse_added(added)
    root_pair.reduce()
    return root_pair.toString()

def solution(partOne):
    with open(sys.argv[1]) as f:
        input = f.readlines()

    if partOne:
        added_expression = input[0]
        for i in range(1, len(input)):
            added_expression = add_snailfish(added_expression, input[i])
        return parse_added(added_expression).magnitude()
    else:
        best_magnitude = 0
        for i in range(len(input)):
            for j in range(len(input)):
                if i == j: continue
                magnitude = parse_added(add_snailfish(input[i], input[j])).magnitude()
                if magnitude > best_magnitude: best_magnitude = magnitude
        return best_magnitude


if __name__ == "__main__":
    print("Solution part one: %d" % solution(True))
    print("Solution part two: %d" % solution(False))
