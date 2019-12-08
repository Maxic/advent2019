from anytree import Node, search


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()
        nodes = {}

        # create dict with all children per node
        for line in content:
            node_ids = line.replace('\n', '').split(')')

            node_id_parent = node_ids[0]
            node_id_child = node_ids[1]

            if not nodes.__contains__(node_id_parent):
                nodes[node_id_parent] = [node_id_child]
            else:
                nodes[node_id_parent].append(node_id_child)

    # Create first node
    root = Node('COM', None)

    # fill tree (root node only has one child)
    add_children(nodes, nodes['COM'][0], root)

    # Get relevant nodes
    node_you = search.find_by_attr(root,"YOU")
    node_san = search.find_by_attr(root,"SAN")

    # remove irrelevant tree above the nodes we're interested in
    for node in set(node_you.ancestors).intersection(set(node_san.ancestors)):
        node.parent = None

    # count amount of ancestors, root node of this subtree should be removed in each list, so subtract two.
    print(node_you.depth-1 + node_san.depth-1)


# recursively add children, stop when reaching a leaf node.
def add_children(nodes, child_id, parent_node):
    node = Node(child_id, parent=parent_node)

    if child_id in nodes:
        for child in nodes[child_id]:
            add_children(nodes, child, node)


if __name__ == "__main__":
    main()
