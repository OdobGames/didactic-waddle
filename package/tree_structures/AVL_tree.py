class AVLTreeNode:
    def __init__(self, data) -> None:
        self._data = data
        self._left = None
        self._right = None
        self._height = 1

    def __str__(self):
        return (f'{self._data} ->'
                + '[{self._left._data}, {self._right._data}]')

    def __repr__(self):
        return (f'{self._data}')


class AVLTree:

    def append(self, new_data, root):
        if root is None:
            return AVLTreeNode(new_data)
        elif new_data > root._data:
            root._right = self.append(new_data, root._right)
        else:
            root._left = self.append(new_data, root._left)

        root._height = 1 + max(self.height(root._left),
                               self.height(root._right))

        node_balance = self.balance(root)

        if node_balance > 1:
            if new_data < root._left._data:
                return self.right_rotate(root)
            else:
                root._left = self.left_rotate(root._left)
                return self.right_rotate(root)
        if node_balance < -1:
            if new_data > root._right._data:
                return self.left_rotate(root)
            else:
                root._right = self.right_rotate(root._right)
                return self.left_rotate(root)
        return root

    def height(self, node) -> int:
        return getattr(node, '_height', 0)

    def balance(self, node) -> int:
        try:
            left_weight = getattr(node._left, '_height', 0)
        except AttributeError:
            left_weight = 0
        try:
            right_weight = getattr(node._right, '_height', 0)
        except AttributeError:
            right_weight = 0
        return left_weight - right_weight

    def right_rotate(self, node):
        root = node._left
        horphan = root._right
        root._right = node
        node._left = horphan

        node._height = 1 + max(self.height(node._left),
                               self.height(node._right))
        root._height = 1 + max(self.height(root._left),
                               self.height(root._right))
        return root

    def left_rotate(self, node):
        root = node._right
        horphan = root._left
        root._left = node
        node._right = horphan

        node._height = 1 + max(self.height(node._left),
                               self.height(node._right))
        root._height = 1 + max(self.height(root._left),
                               self.height(root._right))
        return root

    def search(self, root, data):
        try:
            if data == root._data:
                return root
        except AttributeError:
            return root
        if data < root._data:
            return self.search(root._left, data)
        else:
            return self.search(root._right, data)

    def predecessor(self, root, data):
        try:
            if data > root._data:
                if data == root._right._data:
                    return root
                return self.predecessor(root._right, data)
            else:
                if data == root._left._data:
                    return root
                return self.predecessor(root._left, data)
        except AttributeError:
            return None

    def inorder(self, root):
        if root is not None:
            yield from self.inorder(root._left)
            yield root
            yield from self.inorder(root._right)

    def preorder(self, root):
        if root is not None:
            yield root
            yield from self.preorder(root._left)
            yield from self.preorder(root._right)

    def postorder(self, root):
        if root is not None:
            yield from self.postorder(root._left)
            yield from self.postorder(root._right)
            yield root


AVl = AVLTree()
root = None
root = AVl.append(50, root)
root = AVl.append(70, root)
root = AVl.append(30, root)
root = AVl.append(40, root)
root = AVl.append(20, root)

print('inorder', end=' ')
for x in AVl.inorder(root):
    print(repr(x), end=' ')
print('')

print('preorder', end=' ')
for x in AVl.preorder(root):
    print(repr(x), end=' ')
print('')

print('postorder', end=' ')
for x in AVl.postorder(root):
    print(repr(x), end=' ')
print('')
