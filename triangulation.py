import random

from decomposed_data_struct import DecompDataStruct, Vertex, Triangle

from doubly_linked_list import Node, DoublyLinkedList


test_Triangle = [[1, 1], [1, 5], [4, 1]]

test_polygon = [[1, 1], [2, 5], [1, 7], [6, 8], [9, 7], [6, 6], [8, 6], [4, 2]]
test_polygon_bad = [[3, 1], [1, 5], [3, 2], [5, 5]]


# ? Creating the doubly linked list for triangulation
    
polygon_linked_list = DoublyLinkedList()

polygon_linked_list.insert_in_emptylist([1, 1])

for x in range(len(test_polygon)):
    if x != 0:
        polygon_linked_list.insert_at_end(test_polygon[x].copy())

polygon_linked_list.circularize()

# polygon_linked_list.traverse_list()

# ? Storing the triangluated polygon in a anew data structure

triangulated_polygon = DecompDataStruct()

for x in range(len(test_polygon)):
    triangulated_polygon.add_new_vert(test_polygon[x].copy())

# print(triangulated_polygon.verts)


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

    # ? If what is coming is a dictionary 
    triangle_area = calculate_triangle_area([triangle.data, triangle.nref.data, triangle.pref.data])
    triangle_a_area = calculate_triangle_area([point.data, triangle.data, triangle.nref.data])
    triangle_b_area = calculate_triangle_area([point.data, triangle.nref.data, triangle.pref.data])
    triangle_c_area = calculate_triangle_area([point.data, triangle.data, triangle.pref.data])
    check = triangle_a_area + triangle_b_area + triangle_c_area
    if check == triangle_area: 
        return True
    return False

def check_is_dog_ear(triangle):
    # print(triangle.data)
    determinate = (triangle.data[0] - triangle.pref.data[0]) * (triangle.nref.data[1] - triangle.data[1]) - (triangle.nref.data[0] - triangle.data[0]) * (triangle.data[1] - triangle.pref.data[1])
    if determinate > 0:
        return False
    # (b.x - a.x) * (c.y - b.y) - (c.x - b.x) * (b.y - a.y) > 0
    current_point = triangle
    while current_point != triangle.pref:
        if current_point is not triangle and current_point is not triangle.nref:
            if check_point(current_point, triangle):
                return False
            else:
                return True
            print(current_point.data)
        current_point = current_point.nref

# check_is_dog_ear(polygon_linked_list.start_node)

def triangulate(polygon, verts=None):
    verts = polygon.calculate_length()
    if verts <= 3:
        return

    current_vertex = polygon.start_node
    if check_is_dog_ear(current_vertex):
        if_dog_ear(current_vertex, polygon)
        verts -= 1

    # else:
    #     print(current_vertex.data, 'is not a dog ear')
    current_vertex = current_vertex.nref

    while verts > 3:
        if check_is_dog_ear(current_vertex):
            if_dog_ear(current_vertex, polygon)
            verts -= 1
        # else:
            # print(current_vertex.data, 'is not a dog ear')
        current_vertex = current_vertex.nref

    if_dog_ear(current_vertex, polygon)

def if_dog_ear(triangle, polygon):
    # print(triangle.data, 'is dog ear')
    polygon.remove_item(triangle)


    # print([x.coords for x in triangulated_polygon.verts])
    # vert_index = [triangle.data[0], triangle.data[1]] in triangulated_polygon.verts.coords
    # print(vert_index)

    vert_a = next(x for x in triangulated_polygon.verts if x.coords[0] == triangle.data[0] and x.coords[1] == triangle.data[1])
    vert_b = next(x for x in triangulated_polygon.verts if x.coords[0] == triangle.nref.data[0] and x.coords[1] == triangle.nref.data[1])
    vert_c = next(x for x in triangulated_polygon.verts if x.coords[0] == triangle.pref.data[0] and x.coords[1] == triangle.pref.data[1])

    triangle_area = calculate_triangle_area([triangle.data, triangle.nref.data, triangle.pref.data])

    # print(vert_a.coords, vert_b.coords, vert_c.coords, triangle_area)
    triangulated_polygon.add_new_triangle(vert_a, vert_b, vert_c, triangle_area)

    # also create a new data structure with all of the vertexes and edges


triangulate(polygon_linked_list)
# print('final check')
# polygon_linked_list.traverse_list()

print(triangulated_polygon)