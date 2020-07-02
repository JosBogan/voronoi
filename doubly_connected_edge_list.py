class Vertex:
    def __init__(self, data, name):
        self.data = data
        self.name = name

    def __str__(self):
        return f'{self.name}'

    __repr__ = __str__

class Edge:
    def __init__(self, vert_a, vert_b):
        self.vert_a = vert_a
        self.vert_b = vert_b

    def __str__(self):
        return f'{self.vert_a} - {self.vert_b}'

    __repr__ = __str__

class DoublyConnectedEdgeList:
    def __init__(self):
        self.verts = []
        self.edges = []
        self.assignment = 'ABCDEFGHIJKLOMOPQRSTUVWXYZ'
        self.assignment_possition = 0
        self.assignment_rotation = 1

    def __str__(self):
        return f'{self.verts}\n{self.edges}'

    __repr__ = __str__

    def add_new_vert(self, data):
        name = self.assignment[self.assignment_possition] * self.assignment_rotation
        self.assignment_possition += 1
        if self.assignment_possition >= len(self.assignment):
            self.assignment_possition = 0
            self.assignment_rotation += 1
        new_vert = Vertex(data, name)
        self.verts.append(new_vert)

    def add_new_edge(self, vert_a, vert_b):
        if type(vert_a) == str:
            listed_vertex_a = next(x for x in self.verts if x.name == vert_a)
        elif type(vert_a) == int:
            listed_vertex_a = self.verts[vert_a]
        if type(vert_b) == str:
            listed_vertex_b = next(x for x in self.verts if x.name == vert_b)
        elif type(vert_b) == int:
            listed_vertex_b = self.verts[vert_b]
        new_edge = Edge(listed_vertex_a, listed_vertex_b)
        self.edges.append(new_edge)

# structure = DoublyConnectedEdgeList()

# for x in range(30):
# structure.add_new_vert(2)
# structure.add_new_vert(2)
# structure.add_new_vert(6)
# structure.add_new_vert(2)
# structure.add_new_vert(3)

# structure.add_new_edge('A', 'B')
# structure.add_new_edge('A', 'C')
# structure.add_new_edge('B', 'C')
# structure.add_new_edge('A', 'E')
# structure.add_new_edge('B', 'D')

# print(structure)