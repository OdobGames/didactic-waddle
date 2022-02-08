from typing import List, Tuple


class UnweightedGraph:

    def __init__(self, edges: List[Tuple[str]] = None) -> None:
        self.nodes = {}
        if edges is None:
            edges = []
        for start_node, end_node in edges:
            try:
                self.nodes[start_node].append(end_node)
            except KeyError:
                self.nodes[start_node] = [end_node]

    def insert(self, edges: List[Tuple[str]]):
        for start_node, end_node in edges:
            try:
                self.nodes[start_node].append(end_node)
            except KeyError:
                self.nodes[start_node] = [end_node]

    def search(self,
               start_node: str,
               end_node: str,
               path: list = None) -> List[List]:
        if path is None:
            path = []

        path = path+[start_node]

        if start_node == end_node:
            return [path]

        if start_node not in self.nodes.keys():
            return []

        paths = []

        for node in self.nodes[start_node]:
            if node not in path:
                new_paths = self.search(node, end_node, path)
                for p in new_paths:
                    paths.append(p)

        return paths
