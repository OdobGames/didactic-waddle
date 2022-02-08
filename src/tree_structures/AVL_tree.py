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

    def min_value_node(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current._left is not None):
            current = current._left

        return current

    def delete_node(self, root, key):

        # Base Case
        if root is None:
            return root

        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if key < root._data:
            root._left = self.delete_node(root._left, key)

        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif(key > root._data):
            root._right = self.delete_node(root._right, key)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root._left is None:
                temp = root._right
                root = None
                return temp

            elif root._right is None:
                temp = root._left
                root = None
                return temp

            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.min_value_node(root._right)

            # Copy the inorder successor's
            # content to this node
            root._data = temp._data

            # Delete the inorder successor
            root._right = self.delete_node(root._right, temp._data)

        root._height = 1 + max(self.height(root._left),
                               self.height(root._right))

        node_balance = self.balance(root)

        if node_balance > 1:
            if key < root._left._data:
                return self.right_rotate(root)
            else:
                root._left = self.left_rotate(root._left)
                return self.right_rotate(root)
        if node_balance < -1:
            if key > root._right._data:
                return self.left_rotate(root)
            else:
                root._right = self.right_rotate(root._right)
                return self.left_rotate(root)

        return root
