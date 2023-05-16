from data import Data


class Node:
    def __init__(self, name, value):
        self.id = name
        self.value = value
        self.left_child = None
        self.right_child = None

    def add_child(self, child):
        if child.value > self.value:
            if self.right_child is None:
                self.right_child = child
            else:
                self.right_child.add_child(child)
        else:
            if self.left_child is None:
                self.left_child = child
            else:
                self.left_child.add_child(child)

    def check_node(self, to_find):
        if self.value == to_find:
            return Data(self.id, self.value)
        else:
            if self.value < to_find:
                if self.right_child:
                    return self.right_child.check_node(to_find)
                else:
                    return -1
            else:
                if self.left_child:
                    return self.left_child.check_node(to_find)
                else:
                    return -1

    def return_children(self, array, id_array):
        if self.left_child:
            array.append(self.left_child.value)
            id_array.append(self.left_child.id)

        if self.right_child:
            array.append(self.right_child.value)
            id_array.append(self.right_child.id)

        if self.left_child:
            self.left_child.return_children(array, id_array)

        if self.right_child:
            self.right_child.return_children(array, id_array)


class BinaryTree:
    def __init__(self, root_value, name):
        self.root = Node(name, root_value)

    def add_node(self, node_name: int,  node_value: int):
        self.root.add_child(Node(node_name, node_value))

    def add_nodes(self, nodes_values_array: list):
        for i in range(len(nodes_values_array)):
            self.add_node(nodes_values_array[i].key, nodes_values_array[i].value)

    def search(self, to_find):
        return self.root.check_node(to_find)

    def print_tree(self):
        array = [self.root.value]
        id_array = [self.root.id]
        self.root.return_children(array, id_array)
        print(array)
        print(id_array)


def binary_tree_search(array, to_find):
    tree = BinaryTree(array[0].value, array[0].key)
    tree.add_nodes(array[1:])

    return tree.search(to_find)
