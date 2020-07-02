import random, functools

from decomposed_data_struct import DecompDataStruct, Vertex, Triangle

from doubly_linked_list import Node, DoublyLinkedList


test_Triangle = [[1, 1], [1, 5], [4, 1]]

test_polygon = [[1, 1], [2, 5], [1, 7], [6, 8], [9, 7], [6, 6], [8, 6], [4, 2]]
test_polygon_bad = [[3, 1], [1, 5], [3, 2], [5, 5]]


# ? Creating the doubly linked list for triangulation
    
def create_linked_list(polygon_coords_list):
    polygon_linked_list = DoublyLinkedList()

    polygon_linked_list.insert_in_emptylist([polygon_coords_list[0][0], polygon_coords_list[0][1]])

    for x in range(len(polygon_coords_list)):
        if x != 0:
            polygon_linked_list.insert_at_end(polygon_coords_list[x].copy())

    polygon_linked_list.circularize()

    return polygon_linked_list

# polygon_linked_list.traverse_list()

# ? Storing the triangluated polygon in a anew data structure

def create_triangulated_data_structure(polygon_coords_list):

    triangulated_polygon = DecompDataStruct()

    for x in range(len(polygon_coords_list)):
        triangulated_polygon.add_new_vert(polygon_coords_list[x].copy())

    return triangulated_polygon

# ! Picks a random point within the triangle

def random_point(triangle):

    # ? Generate random number between 0 and 1
    w1 = random.random()

    # ? generate random number so that x + y <= 1
    w2 = random.uniform(0, 1 - w1)

    # ? plot the x as a percentage traversing down one of the sides of the triangle
    point_1 = [(triangle[1][0] - triangle[0][0]) * w1, (triangle[1][1] - triangle[0][1]) * w1]

    # ? plot the y as a percentage traversing down one of the sides of the triangle
    point_2 = [(triangle[2][0] - triangle[0][0]) * w2, (triangle[2][1] - triangle[0][1]) * w2]


    # ? Add them together to find the coordinates of the difference
    final_point = [point_1[0] + point_2[0], point_1[1] + point_2[1]]

    # ? Add the difference to the initial corner of the triangle used to find the final random point in space
    final_point_in_triangle = [triangle[0][0] + final_point[0], triangle[0][1] + final_point[1]]

    return final_point_in_triangle



# ! Picks a random triangle

def picking_random_triangle(decomp_polygon):
    list_of_triangles = decomp_polygon.triangles

    list_of_weighted_triangles = [[x] * x.weight for x in list_of_triangles]

    flat_list = [item for sublist in list_of_weighted_triangles for item in sublist]
    # print(flat_list)
    random_number = random.randint(0, len(flat_list))
    return flat_list[random_number - 1]


# ! Calculates triangle area

def calculate_triangle_area(triangle):
    area = triangle[0][0] * (triangle[1][1] - triangle[2][1]) + triangle[1][0] * ((triangle[2][1] - triangle[0][1])) + triangle[2][0] * ((triangle[0][1] - triangle[1][1]))
    return abs(area)

# ! Checks if point is within triangle

def check_point(point, triangle):

    # ? If what is coming is a dictionary calculate the areas of the big triangle and each triangle that connects to the point and compare
    triangle_area = calculate_triangle_area([triangle.data, triangle.nref.data, triangle.pref.data])

    triangle_a_area = calculate_triangle_area([point.data, triangle.data, triangle.nref.data])
    triangle_b_area = calculate_triangle_area([point.data, triangle.nref.data, triangle.pref.data])
    triangle_c_area = calculate_triangle_area([point.data, triangle.data, triangle.pref.data])

    check = triangle_a_area + triangle_b_area + triangle_c_area

    if check == triangle_area: 
        return True
    return False

def check_is_dog_ear(triangle):

    # ! Find the Determinate to check if the angle is over 180

    determinate = (triangle.data[0] - triangle.pref.data[0]) * (triangle.nref.data[1] - triangle.data[1]) - (triangle.nref.data[0] - triangle.data[0]) * (triangle.data[1] - triangle.pref.data[1])
    if determinate > 0:
        return False

    # ! Looping through the points to check if the input is a dog ear points (one of the other points of the polygon lies within)

    current_point = triangle
    while current_point != triangle.pref:
        if current_point is not triangle and current_point is not triangle.nref:
            if check_point(current_point, triangle):
                return False
            else:
                return True
            print(current_point.data)
        current_point = current_point.nref


def triangulate(polygon, triangulated_polygon, verts=None):
    # ! Initital check to see if the Polygon is a triangle and setting the while loop counter to the number of verts
    verts = polygon.calculate_length()
    if verts <= 3:
        return

    # ! doing the first rotation of the while loop

    current_vertex = polygon.start_node
    if check_is_dog_ear(current_vertex):
        if_dog_ear(current_vertex, polygon, triangulated_polygon)
        verts -= 1

    current_vertex = current_vertex.nref

    # ! Looping through the verticies, each time it reaches a dog ear, it executes the function and ticks down the counter and changing the current vertex to stay within the linked list
    while verts > 3:
        if check_is_dog_ear(current_vertex):
            if_dog_ear(current_vertex, polygon, triangulated_polygon)
            verts -= 1

        current_vertex = current_vertex.nref

    if_dog_ear(current_vertex, polygon, triangulated_polygon)


# def change_weighting(decomp_polygon):

#     # ! Mapping the weight value of each triangle to be bound by 1

#     list_of_triangles = decomp_polygon.triangles

#     weights = [x.weight for x in list_of_triangles]

#     polygon_area = functools.reduce(lambda x, y: x + y, weights)

#     for x in list_of_triangles:
#         x.weight = x.weight / polygon_area


def if_dog_ear(triangle, polygon, triangulated_polygon):

    # ! Removing the vertex from the linked_list
    polygon.remove_item(triangle)

    # ! Adding the triangle to the triangulated_polygon data structure

    vert_a = next(x for x in triangulated_polygon.verts if x.coords[0] == triangle.data[0] and x.coords[1] == triangle.data[1])
    vert_b = next(x for x in triangulated_polygon.verts if x.coords[0] == triangle.nref.data[0] and x.coords[1] == triangle.nref.data[1])
    vert_c = next(x for x in triangulated_polygon.verts if x.coords[0] == triangle.pref.data[0] and x.coords[1] == triangle.pref.data[1])

    triangle_area = calculate_triangle_area([triangle.data, triangle.nref.data, triangle.pref.data])

    triangulated_polygon.add_new_triangle(vert_a, vert_b, vert_c, triangle_area)


def random_point_in_triangle(triangle):

    triangle_coords = [triangle.vert_a[0].coords, triangle.vert_b[0].coords, triangle.vert_c[0].coords]
    
    point = random_point(triangle_coords)
    return(point)
    # print(point)

def random_points_in_polygon(num, polygon_coords_list):

    # ? Creating the data structures to hold the polgyon data
    polygon_linked_list = create_linked_list(polygon_coords_list)
    triangulated_polygon = create_triangulated_data_structure(polygon_coords_list)

    # ? Triangulating the Polyon
    triangulate(polygon_linked_list, triangulated_polygon)

    random_points = []

    # ? Picking random point in triangle

    for _ in range(num):
        point = random_point_in_triangle(picking_random_triangle(triangulated_polygon))
        random_points.append(point)

    # print(random_points)
    return random_points


# random_points_in_polygon(8, test_polygon)

# random_point([[1, 5], [9, 8], [6, 1]])
# print(picking_random_triangle(triangulated_polygon))

# change_weighting(triangulated_polygon)
# print(triangulated_polygon)