import random

list_of_triangles = [
    {
        'coords': [],
        'size': 1,
        'weight': 1
    },
]

weighted_list_of_triangles = [

]


test_Triangle = [[1, 1], [1, 5], [4, 1]]

test_polygon = [[1, 1], [2, 5], [1, 7], [6, 8], [9, 7], [6, 6], [8, 6], [4, 2]]

test_point = [2.2, 2]

class Node:
    def __init__(self, data):
        self.pref = None
        self.data = data
        self.nref = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")
    
    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def traverse_list(self):
        c = self.start_node
        while c is not None:
            print(c.data)
            c = c.nref
    
    def circularize(self):
        c = self.start_node
        while c.nref is not None:
            c = c.nref
        c.nref = self.start_node
        self.start_node.pref = c
    
polygon_linked_list = DoublyLinkedList()

polygon_linked_list.insert_in_emptylist([1, 1])

for x in range(len(test_polygon)):
    if x != 0:
        polygon_linked_list.insert_at_end(test_polygon[x].copy())

# polygon_linked_list.traverse_list()

polygon_linked_list.circularize()

def random_point(triangle):

    # ? Generate random number between 0 and 1
    x = random.random()

    # ? generate random number so that x + y <= 1
    y = random.uniform(0, 1 - x)

    # ? plot the x as a percentage traversing down one of the sides of the triangle
    point_1 = [abs((triangle[0][0] - triangle[1][0]) * x), abs((triangle[0][1] - triangle[1][1]) * x)]

    # ? plot the y as a percentage traversing down one of the sides of the triangle
    point_2 = [abs((triangle[0][0] - triangle[2][0]) * y), abs((triangle[0][1] - triangle[2][1]) * y)]

    # ? Add them together to find the coordinates of the difference
    final_point = [point_1[0] + point_2[0], point_1[1] + point_2[1]]

    # ? Add the difference to the initial corner of the triangle used to find the final random point in space
    final_point_in_triangle = [triangle[0][0] + final_point[0], triangle[0][1] + final_point[1]]

    return final_point_in_triangle

def calculate_triangle_area(triangle):
    area = triangle[0][0] * (triangle[1][1] - triangle[2][1]) + triangle[1][0] * ((triangle[2][1] - triangle[0][1])) + triangle[2][0] * ((triangle[0][1] - triangle[1][1]))
    return abs(area)

def check_point(point, triangle):

    # ? If what is coming is a List (OLD METHOD)
    # if type(triangle) is list:
    #     print('it is a list')
    #     triangle_area = calculate_triangle_area(triangle)
    #     triangle_a_area = calculate_triangle_area([point, triangle[0], triangle[1]])
    #     triangle_b_area = calculate_triangle_area([point, triangle[1], triangle[2]])
    #     triangle_c_area = calculate_triangle_area([point, triangle[0], triangle[2]])

    #     check = triangle_a_area + triangle_b_area + triangle_c_area

    #     if check == triangle_area: 
    #         return True
    #     return False

    # ? If what is coming is a dictionary 
    triangle_area = calculate_triangle_area([triangle.data, triangle.nref.data, triangle.pref.data])
    triangle_a_area = calculate_triangle_area([point.data, triangle.data, triangle.nref.data])
    triangle_b_area = calculate_triangle_area([point.data, triangle.nref.data, triangle.pref.data])
    triangle_c_area = calculate_triangle_area([point.data, triangle.data, triangle.pref.data])
    check = triangle_a_area + triangle_b_area + triangle_c_area
    if check == triangle_area: 
        return True
    return False

def check_dog_ear(triangle, polygon):
    current_point = triangle
    while current_point != triangle.pref:
        if current_point is not triangle and current_point is not triangle.nref:
            if check_point(current_point, triangle):
                print('Inside')
            else:
                print('Outside')
            print(current_point.data)
        current_point = current_point.nref

check_dog_ear(polygon_linked_list.start_node, polygon_linked_list)
# random_point([[0, 1], [0, 5], [4, 2]])

# polygon = Doubly_connected_edge_list()
# polygon_linked_list = Doubly_linked_list()
# check_dog_ear(Doubly_linked_list().list[0], polygon_linked_list)

# def choose_triangle(polygon):
#     if polygon

#     print(w1, w2)

