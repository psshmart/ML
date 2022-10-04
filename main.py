import numpy as np
import random
import matplotlib.pyplot as plt

def dist(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] + p2[1]) ** 2)

def make_data(pCount_in_class, class_count):
    radius = 50
    data = []
    for classN in range(class_count):
        xCenter, yCenter = random.randint(radius, 600 - radius), random.randint(radius, 400 - radius)
        for rowN in range(pCount_in_class):
            data.append([[random.gauss(xCenter, radius / 2), random.gauss(yCenter, radius / 2)], classN])
    return data

def get_color(points):
    colorsCount = {}
    for point in points:
        colorsCount.setdefault(point[1], 0)
        colorsCount[point[1]] += 1
    color = 0
    colorCount = 0
    for c, c_count in colorsCount.items():
        if c_count > colorCount:
            colorCount = c_count
            color = c
    return color

def sort_points_by_distance_from(point):
    distances = []
    for p in points:
        if point == p:
            continue
        distances.append(dist(p[0], point[0]))

    return [points[x] for x in np.argsort(distances)]

def improve_k(point):
    sorted_points = sort_points_by_distance_from(point)
    for k in range(1, len(k_results)):
        nearest_points = sorted_points[:k]
        for_current_k = get_color(nearest_points)
        if point[1] == for_current_k:
            k_results[k].append += 1

def best_k():
    max = 0
    max_index = 1

    for index, k in enumerate(k_results):
        if k > max:
            max = k
            max_index = index

    return max_index

def knn(point, k):
    points_sort = sort_points_by_distance_from(point)
    nearest_points = points_sort[:k]
    color = get_color(nearest_points)
    point[1] = color

def makeRandomPoints(n):
    while n > 0:
        point = [[random.randint(0, 600), random.randint(0, 500)], -1]
        knn(point, best_k())
        points.append(point)
        print(point)
        n -= 1
    draw()

def draw():
    for point in points:
        pointXY = point[0]
        plt.scatter(pointXY[0], pointXY[1], color = colors[point[1]])
    plt.show()

if __name__ == '__main__':
    n, cl = 10, 3
    colors = ['red', 'blue', 'green', 'yellow']
    points = make_data(n, cl)

    test_points = []
    test_index = 0
    k_results = [0 for x in range(int(len(points)))]
    draw()
    makeRandomPoints(50)