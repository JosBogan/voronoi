import random

list_of_triangles = [
    {
        coords: [],
        size: 1,
        weight: 1
    },

]

def random_point(triangle):
    # Generate random number between 0 and 1
    x = random.random()
    # generate random number so that x + y <= 1
    y = random.uniform(0, 1 - x)
    # plot the x as a percentage traversing down one of the sides of the triangle
    point_1 = [abs((triangle[0][0] - triangle[1][0]) * x), abs((triangle[0][1] - triangle[1][1]) * x)]
    # plot the y as a percentage traversing down one of the sides of the triangle
    point_2 = [abs((triangle[0][0] - triangle[2][0]) * y), abs((triangle[0][1] - triangle[2][1]) * y)]
    # Add them together to find the coordinates of the difference
    final_point = [point_1[0] + point_2[0], point_1[1] + point_2[1]]
    # Add the difference to the initial corner of the triangle used to find the final random point in space
    final_point_in_triangle = [triangle[0][0] + final_point[0], triangle[0][1] + final_point[1]]
    return final_point_in_triangle

def choose_triangle(triangles):



random_point([[0, 1], [0, 5], [4, 2]])