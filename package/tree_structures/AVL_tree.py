class AVLTreeNode:
    def __init__(self, data) -> None:
        self._data = data
        self._left = None
        self._right = None
        self._height = 1


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
