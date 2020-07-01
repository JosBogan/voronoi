class Vertex:
    def __init__(self, coords):
        self.coords = coords

    def __str__(self):
        return f'{self.coords[0]}, {self.coords[1]}'

    __repr__ = __str__

class Triangle:
    def __init__(self, vert_a, vert_b, vert_c, weight):
        self.vert_a = vert_a,
        self.vert_b = vert_b,
        self.vert_c = vert_c,
        self.weight = weight

    def __str__(self):
        return f'{self.vert_a},\n{self.vert_b},\n{self.vert_c},\nWeight: {self.weight}\n'
    
    __repr__ = __str__

class DecompDataStruct:
    def __init__(self):
        self.verts = []
        self.triangles = []

    def __str__(self):
        return f'{self.triangles}'

    def add_new_vert(self, coords):
        new_vert = Vertex(coords)
        self.verts.append(new_vert)

    def add_new_triangle(self, vert_a, vert_b, vert_c, weight):
        new_triangle = Triangle(vert_a, vert_b, vert_c, weight)
        self.triangles.append(new_triangle)