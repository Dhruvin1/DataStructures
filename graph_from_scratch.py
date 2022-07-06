class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge:
    def __init__(self, value, from_node, to_node):
        self.value = value
        self.from_node = from_node
        self.to_node = to_node

class Graph:
    def __init__(self, nodes = [], edges = []):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)
        return

    def insert_edge(self, value, from_node, to_node):
        node_objects = {
            'from_node_object': None,
        'to_node_object' : None
        }
        for element in self.nodes:
            if element.value == from_node:
                node_objects['from_node_object'] = element
            elif element.value == to_node:
                node_objects['to_node_object'] = element
            if all(node_objects.values()):
                break
        if not node_objects['from_node_object']:
            new_node = Node(from_node)
            node_objects['from_node_object'] = new_node
            self.nodes.append(new_node)
        if not node_objects['to_node_object']:
            new_node = Node(to_node)
            node_objects['to_node_object'] = new_node
            self.nodes.append(new_node)
        new_edge = Edge(value,node_objects['from_node_object'], node_objects['to_node_object'])
        node_objects['from_node_object'].edges.append(new_edge)
        node_objects['to_node_object'].edges.append(new_edge)
        self.edges.append(new_edge)

    def get_node_list(self):
        mylist = []
        for element in self.nodes:
            mylist.append(element.value)
        return mylist

    def get_edge_list(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node, To Node)"""
        edge_list = []
        for element in self.edges:
            edge_list.append((element.value,element.from_node.value, element.to_node.value))
        return edge_list

    def get_adjacency_list(self):
        """Return a list of lists.
        The indecies of the outer list represent "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        adjucency_list = [[] for i in range(len(self.nodes)+1)]
        for nodes in self.nodes:
            for edges in nodes.edges:
                if nodes.value == edges.to_node.value:
                    adjucency_list[nodes.value].append((edges.from_node.value,edges.value))
                else:
                    adjucency_list[nodes.value].append((edges.to_node.value, edges.value))
        return adjucency_list

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        raw = len(self.nodes) + 1
        adjecency_metrix = [[0 for i in range(raw)] for j in range(raw)]
        for edge in self.edges:
            adjecency_metrix[edge.from_node.value][edge.to_node.value] = edge.value
            adjecency_metrix[edge.to_node.value][edge.from_node.value] = edge.value
        return adjecency_metrix

'''
Pictorial view of the graph

                     1
                   /   \
                2   ---  4
                  \    
                     3
'''

# driver code

if __name__ == "__main__":
    node_list = []
    for i in range(1,5):
        node_list.append(Node(i))
    mygraph = Graph(node_list)
    mygraph.insert_edge(10,1,2)
    mygraph.insert_edge(10, 1, 4)
    mygraph.insert_edge(10,2,4)
    mygraph.insert_edge(10, 2, 3)
    print("My graph nodes are: ",mygraph.get_node_list())
    print("My graph edges are: ",mygraph.get_edge_list())
    print("Adjacency list: ", mygraph.get_adjacency_list())
    print("Adjacency list: ", mygraph.get_adjacency_matrix())






