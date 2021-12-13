import numpy as np

with open('12.in') as infile:
    input = infile.read()

lines = input.splitlines()


def find_nodes(lines):
    nodes_set = set()

    for line in lines:
        nodes_set.update(set(line.split('-')))

    nodes = np.array(list(nodes_set))

    start_index = np.where(nodes == 'start')[0][0]
    nodes[0], nodes[start_index] = nodes[start_index], nodes[0]

    end_index = np.where(nodes == 'end')[0][0]
    nodes[1], nodes[end_index] = nodes[end_index], nodes[1]

    return nodes


def find_edges(nodes, lines):
    edges = np.zeros((len(nodes), len(nodes)))

    for line in lines:
        lnodes = line.split('-')

        a_index = np.where(nodes == lnodes[0])[0][0]
        b_index = np.where(nodes == lnodes[1])[0][0]

        edges[a_index, b_index] = 1
        edges[b_index, a_index] = 1

    return edges


def count_routes(node, steps, nodes, edges):
    if node == 1:       # node index 1 is the end point
        return 1

    count = 0
    for new_node in range(1, len(nodes)):
        if edges[node][new_node] == 1:
            new_steps = np.copy(steps)

            if nodes[new_node].isupper():
                count += count_routes(new_node, new_steps, nodes, edges)
            else:
                if steps[new_node] == 0:
                    new_steps[new_node] += 1
                    count += count_routes(new_node, new_steps, nodes, edges)
                # part two
                elif steps[new_node] == 1 and np.count_nonzero(steps > 1) == 0:
                    new_steps[new_node] += 1
                    count += count_routes(new_node, new_steps, nodes, edges)

    return count


nodes = find_nodes(lines)
edges = find_edges(nodes, lines)
steps = np.zeros(len(nodes))


print(count_routes(0, steps, nodes, edges))
