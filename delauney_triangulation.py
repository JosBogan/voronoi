from polygon_triangulation import random_points_in_polygon
from doubly_connected_edge_list import DoublyConnectedEdgeList

test_polygon = [[1, 1], [2, 5], [1, 7], [6, 8], [9, 7], [6, 6], [8, 6], [4, 2]]

def delauney_triangulation(points):
    structure = DoublyConnectedEdgeList()
    for x in range(3):
        structure.add_new_vert(points[x])
    for x in range(3):
        if x != 2:
            structure.add_new_edge(x, x + 1)
        else:
            structure.add_new_edge(x, 0)
    print(structure)

points = random_points_in_polygon(4, test_polygon)

#  ADD IN TRIANGLES TO DATA STRUCTURE WITH CIRCUMCIRCLES

delauney_triangulation(points)

