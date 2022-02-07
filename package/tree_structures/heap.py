class Heap():
    def _heapify(self, tree, size, root):
        largest = root
        left = root * 2 + 1
        right = root * 2 + 2
        tree_size = size
        if left < tree_size and tree[largest] < tree[left]:
            largest = left
        if right < tree_size and tree[largest] < tree[right]:
            largest = right
        if largest != root:
            tree[root], tree[largest] = tree[largest], tree[root]
            self._heapify(tree, size, largest)

    def heap_sort(self, array):
        n = len(array)
        for i in range(n//2 - 1, -1, -1):
            self._heapify(array, n, i)
        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self._heapify(array, i, 0)
