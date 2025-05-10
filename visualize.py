from graphviz import Digraph
from roshen import Chocolate, build_chocolate_tree

def add_nodes(dot, node, counter):
    if not node:
        return counter

    node_id = f'node{counter}'
    label = f'{node.n}x{node.m}'
    dot.node(node_id, label)
    current_id = counter
    counter += 1

    if node.left:
        left_id = counter
        counter = add_nodes(dot, node.left, counter)
        dot.edge(f'node{current_id}', f'node{left_id}')
    
    if node.right:
        right_id = counter
        counter = add_nodes(dot, node.right, counter)
        dot.edge(f'node{current_id}', f'node{right_id}')

    return counter

def visualize_chocolate_tree(root, filename='chocolate_tree'):
    dot = Digraph()
    add_nodes(dot, root, 0)
    dot.render(filename, format='png', cleanup=True)

if __name__ == "__main__":
    root = Chocolate(3,4)
    build_chocolate_tree(root)
    visualize_chocolate_tree(root)
