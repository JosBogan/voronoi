from polygon_triangulation import random_points_in_polygon
from doubly_connected_edge_list import DoublyConnectedEdgeList
from polygon_triangulation import calculate_triangle_area

test_polygon = [[1, 1], [2, 5], [1, 7], [6, 8], [9, 7], [6, 6], [8, 6], [4, 2]]

def delauney_triangulation(points):

    structure = DoublyConnectedEdgeList()
    # ? Adding the first three verticies, edges and triangle
    for x in range(3):
        structure.add_new_vert(points[x])
    for x in range(3):
        if x != 2:
            structure.add_new_edge(x, x + 1)
        else:
            structure.add_new_edge(x, 0)
    structure.add_new_triangle(0, 1, 2)
    # print(points)
    print(structure.triangles)
    # ? Looping through all the remaining points, looping again through each of the triangles in the 
    for p in range(3, len(points)):
        for tri in structure.triangles:
            triangle_data = [tri.vert_a.data, tri.vert_b.data, tri.vert_c.data]
            point = points[p]
            print(point, p)
            # ! Need to add the is in circumcircle condition here!
            if is_in_triangle(point, triangle_data):
                # structure.remove_triangle(tri)
                # new_vert = structure.add_new_vert(points[p])
                # # ! CURRENTLY INFINITLY LOOPING - Put this at the 
                # structure.add_new_edge(tri.vert_a.name, new_vert.name)
                # structure.add_new_edge(tri.vert_b.name, new_vert.name)
                # structure.add_new_edge(tri.vert_c.name, new_vert.name)
                # structure.add_new_triangle(tri.vert_a.name, tri.vert_b.name, new_vert.name)
                # structure.add_new_triangle(tri.vert_a.name, tri.vert_c.name, new_vert.name)
                # structure.add_new_triangle(tri.vert_c.name, tri.vert_b.name, new_vert.name)
                print('is in triangle')
                # ? Here the point is joined to all the verts and the old triangle is collapsed and three new triangles are made

                # break
            elif is_in_circumcircle(triangle_data, point):
                print('is in circumcircle but not triangle')
                # ? Here the point is joined to all the verts of the triangle and the edge that intersects with the old triangle is flipped, making a single new triangle and transforming the one already there
            else:
                print('point is totally external')
                # ? Here the point is joined to the verts of the triangle it can without passing through the triange, making a single new triangle

    # print(structure.triangles)
            # print(is_in_circumcircle(triangle, point))

def find_correct_triangles(point_data):
    


def is_in_triangle(point, triangle):

    # ? If what is coming is a dictionary calculate the areas of the big triangle and each triangle that connects to the point and compare
    triangle_area = calculate_triangle_area([triangle[0], triangle[1], triangle[2]])

    triangle_a_area = calculate_triangle_area([point, triangle[0], triangle[1]])
    triangle_b_area = calculate_triangle_area([point, triangle[1], triangle[2]])
    triangle_c_area = calculate_triangle_area([point, triangle[0], triangle[2]])

    check = triangle_a_area + triangle_b_area + triangle_c_area

    if check == triangle_area: 
        return True
    return False

def is_in_circumcircle(triangle, point):

    clockwise = (triangle[1][0] - triangle[0][0])*(triangle[2][1] - triangle[0][1])-(triangle[2][0] - triangle[0][0])*(triangle[1][1] - triangle[0][1]) <= 0
    ap = [triangle[0][0] - point[0], triangle[0][1] - point[1]]
    bp = [triangle[1][0] - point[0], triangle[1][1] - point[1]]
    cp = [triangle[2][0] - point[0], triangle[2][1] - point[1]]


    num = (ap[0] * ap[0] + ap[1] * ap[1]) * (bp[0] * cp[1] - cp[0] * bp[1]) - (bp[0] * bp[0] + bp[1] * bp[1]) * (ap[0] * cp[1] - cp[0] * ap[1]) + (cp[0] * cp[0] + cp[1] * cp[1]) * (ap[0] * bp[1] - bp[0] * ap[1])

    # print(clockwise, num)
    if clockwise:
        if num < 0:
            return True
        else:
            return False
    if num > 0:
        return True
    return False

# ! Actual test

# points = random_points_in_polygon(10, test_polygon)

# #  ADD IN TRIANGLES TO DATA STRUCTURE WITH CIRCUMCIRCLES

# delauney_triangulation(points)


# ! EASY TO VISUALISE TEST

test_points = [[1, 2], [3, 4], [3, 0], [2, 2], [4, 2], [6, 7], [7, 1], [3.5, 2.5], [2.5, 1]]


delauney_triangulation(test_points)