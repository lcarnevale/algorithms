def add_root(label='root'):
    tree = dict()
    tree[label] = {"parent": None, "left": None, "right": None}
    return tree

def add_child(tree, parent, new_node, side):
    if not new_node in tree and not tree[parent][side]:
        tree[parent][side] = new_node
        tree[new_node] = {"parent": parent, "left": None, "right": None}

def is_root(tree, node_name):
    return tree[node_name]['parent'] == None

def is_leaf(tree, node_name):
    return tree[node_name]['left'] == None and tree[node_name]['right'] == None

def get_children(tree, node_name):
    return [ 
        tree[node_name]['left'],
        tree[node_name]['right']
    ]


def depth(tree, node_name):
    if is_root(tree, node_name):
        return 1
    return 1 + depth(tree, tree[node_name]['parent'])

def height(tree, node_name):
    if is_leaf(tree, node_name):
        return 0
    #heights = list()
    #for child in get_children(tree, node_name):
    #    heights.append( height(tree, child) )
    #return 1+max(heights)
    return 1 + max( height(tree, child) for child in get_children(tree, node_name) )

def tree_search(tree, root, node_name):
    print("attraverso", root)
    if not root:
        print('non esiste')
        return root
    if root == node_name:
        print('trovato!')
        return root
    if node_name < root:
        return tree_search(tree, tree[root]['left'], node_name)
    else:
        return tree_search(tree, tree[root]['right'], node_name)

def sibling(tree, node_name):
    parent = tree[node_name]['parent']
    if parent is None:
        print("E' il nodo root")
        return None
    else:
        if node_name == tree[parent]['left']:
            return tree[parent]['right']
        else:
            return tree[parent]['left']

def preorder(tree, node_name, visited):
    if node_name != None:
        visited.append(node_name)
        left_child = tree[node_name]['left']
        right_child = tree[node_name]['right']
        if left_child is not None or right_child is not None:
            preorder(tree, left_child, visited)
            preorder(tree, right_child, visited)
        return visited

def postorder(tree, node_name, visited):
    if node_name != None:   
        left_child = tree[node_name]['left']
        right_child = tree[node_name]['right']
        if left_child is not None or right_child is not None:
            postorder(tree, left_child, visited)
            postorder(tree, right_child, visited)
        visited.append(node_name)
        return visited

def bfs(tree, node_name):
    queue, visited = list(), list()
    if is_root(tree, node_name):
        queue.append(node_name)
    while queue:
        current = queue.pop(0)
        visited.append(current)
        if tree[current]['left']:
            queue.append(tree[current]['left'])
        if tree[current]['right']:
            queue.append(tree[current]['right'])
    return visited

def inorder(tree, node_name, visited):
    if node_name != None:
        left_child = tree[node_name]['left']
        right_child = tree[node_name]['right']
        if left_child:
            inorder(tree, left_child, visited)
        visited.append(node_name)
        if right_child:
            inorder(tree, right_child, visited)
        return visited

def tree_min(tree, node_name):
    while tree[node_name]['left'] is not None:
        node_name = tree[node_name]['left']
    return node_name

def tree_max(tree, node_name):
    while tree[node_name]['right'] is not None:
        node_name = tree[node_name]['right']
    return node_name

def tree_successor(tree, node_name):
    if tree[node_name]['right']:
        return tree_min(tree, tree[node_name]['right'])
    parent = tree[node_name]['parent']
    while parent and node_name == tree[parent]['right']:
        node = parent
        parent = tree[parent]['parent']
        return parent

def tree_insert(tree, root, node_name):
    parent = None
    while root:
        parent = root
        if node_name < root:
            root = tree[root]['left']
        else:
            root = tree[root]['right']
    tree[node_name] = {'parent': parent, 'left': None, 'right': None}
    if parent and node_name < parent:
        tree[parent]['left'] = node_name
    else:
        tree[parent]['right'] = node_name
    return tree

def transplant(tree, old_node, new_node):
    print('travaso %d in %d' % (new_node, old_node))
    old_parent = tree[old_node]['parent']
    print('il genitore di %s è %s' % (old_node, old_parent))
    if not old_parent:
        tree[new_node]['parent'] = None
        if tree[old_node]['left']:
            tree[new_node]['left'] = tree[old_node]['left']
        if tree[old_node]['right']:
            tree[new_node]['right'] = tree[old_node]['right']
    elif old_node == tree[old_parent]['left']:
        print('here left')
        print('attacco %s come figlio sinistro di %s' % (new_node, old_parent))
        tree[old_parent]['left'] = new_node
    else:
        print('here right')
        tree[old_parent]['right'] = new_node
    if new_node is not None:
        tree[new_node]['parent'] = tree[old_node]['parent']
    del tree[old_node]

def tree_delete(tree, node_name):
    if not tree[node_name]['left']:
        print('travaso a destra')
        transplant(tree, node_name, tree[node_name]['right'])
    elif not tree[node_name]['right']:
        print('travaso a sinistra')
        transplant(tree, node_name, tree[node_name]['left'])
    else: # ci sono entrambi i figli
        node_min = tree_min(tree, tree[node_name]['right']) # prendo il successore
        if tree[node_min]['parent'] != node_name:
            tree[node_min]['right'] = tree[node_name]['right']
            print(tree)
            tree[tree[node_min]['right']]['parent'] = node_min
            print(tree)
            transplant(tree, node_min, tree[node_min]['right'])
            print(tree)  
        tree[node_min]['left'] = tree[node_name]['left']
        tree[tree[node_min]['left']]['parent'] = node_min
        transplant(tree, node_name, node_min)
    return tree


def main():
    """
    tree = add_root('book')
    add_child(tree, 'book', 'prefazione', 'left')
    add_child(tree, 'prefazione', 'ringraziamenti', 'left')
    add_child(tree, 'book', 'cap1', 'right')
    add_child(tree, 'cap1', 'sec1.1', 'left')
    add_child(tree, 'cap1', 'sec1.2', 'right')

    print(tree)
    #for key, value in tree.items():
    #    print(key, value)
    #print(tree)

    #print( depth(tree, 'cap1') )
    #print( is_root(tree, 'sec1.1') )
    #print( height(tree, 'book') )

    #print( sibling(tree, 'book') )

    print("#################")
    #print( preorder(tree, 'cap1', visited=list()) )
    #print( postorder(tree, 'cap1', visited=list()) )
    #print( bfs(tree, 'book') )
    print( inorder(tree, 'book', visited=list()) )
    """

    tree = add_root(15)
    add_child(tree, 15, 6, 'left')
    add_child(tree, 15, 18, 'right')
    add_child(tree, 6, 3, 'left')
    add_child(tree, 6, 7, 'right')
    add_child(tree, 3, 2, 'left')
    add_child(tree, 3, 4, 'right')
    add_child(tree, 7, 13, 'right')
    add_child(tree, 13, 9, 'left')
    add_child(tree, 18, 17, 'left')
    add_child(tree, 18, 20, 'right')
    #print(tree)

    #print( tree_search(tree, 15, 13) )
    #print( tree_min(tree, 18) )
    #print( tree_max(tree, 18) )
    #print( tree_successor(tree, 15) ) 

    tree = tree_insert(tree, root=15, node_name=14)
    tree = tree_delete(tree, 6)
    print (tree)

if __name__ == "__main__":
    main()