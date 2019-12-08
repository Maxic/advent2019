from anytree import Node, PreOrderIter


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()
        nodes = {}
        orbit_sum = 0

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

    # fill tree
    add_children(nodes, nodes['COM'][0], root)

    # sum all ancestors per node
    for node in PreOrderIter(root):
        orbit_sum += node.ancestors.__len__()

    print(orbit_sum)


def add_children(nodes, child_id, parent_node):
    node = Node(child_id, parent=parent_node)

    if child_id in nodes:
        for child in nodes[child_id]:
            add_children(nodes, child, node)


if __name__ == "__main__":
    main()
