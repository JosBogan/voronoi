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

# test_Triangle = [
#     {
#         'point': [0, 0]
#     },
#     {
#         'point': [1, 6]
#     },
#     {
#         'point': [3, 5]
#     },
# ]

test_Triangle = [
    {
        'point': [1, 1]
    },
    {
        'point': [1, 5]
    },
    {
        'point': [4, 1]
    },
]

test_point = [2.5, 3.5]

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

# def choose_triangle(triangles):


def check_point(point, triangle):

    ac = {
        'x': triangle[2]['point'][0] - triangle[0]['point'][0],
        'y': triangle[2]['point'][1] - triangle[0]['point'][1]
    }
    ab = {
        'x': triangle[1]['point'][0] - triangle[0]['point'][0],
        'y': triangle[1]['point'][1] - triangle[0]['point'][1]
    }
    p = {
        'x': point[0] - triangle[0]['point'][0],
        'y': point[1] - triangle[0]['point'][1]
    }

    w1_top = (triangle[0]['point'][0] * ac['y']) + (p['y'] * ac['x']) - (point[0] * ac['y'])
    w1_bot = (ab['y'] * ac['x']) - (ab['x'] * ac['y'])

    if w1_bot != 0:
        w1 = w1_top / w1_bot
    else:
        w1 = w1_top

    # w1 = ((triangle[0]['point'][0] * ac['y'] + (p['y'] * ac['x']) - (point[0] * ac['y'])) / ((ab['y'] * ac['x']) - (ab['x'] * ac['y'])))

    w2_top = point[1] - triangle[0]['point'][1] - (w1 * ab['y'])
    w2_bot = triangle[2]['point'][1] - triangle[0]['point'][1]

    if w2_bot != 0:
        w2 = w2_top / w2_bot
    else:
        w2 = w2_top
        
    # w2 = (point[1] - triangle[0]['point'][1] - (w1 * ab['y'])) / (triangle[2]['point'][1] - triangle[0]['point'][1])


    print(w1, w2)

check_point(test_point, test_Triangle)
# random_point([[0, 1], [0, 5], [4, 2]])


