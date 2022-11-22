import pygame
import pygame as pg
import sys
import sklearn.svm
import math

sc = pg.display.set_mode((300, 300))
sc.fill('black')
pg.display.update()

class Point:
    def __init__(self, x, y, point_class, color='black'):
        self.x = x
        self.y = y
        self.point_class = point_class
        self.color = color

def show_point(point):
    pg.draw.circle(sc, point.color, (math.fabs(point.x), math.fabs(point.y)), 5)
    pg.display.update()

def fit(points):
    x = [(point.x, point.y) for point in points]
    y = [point.point_class for point in points]
    svc = sklearn.svm.LinearSVC(random_state=42, tol=1e-5, max_iter=100000000)
    svc.fit(x, y)
    return svc.coef_[0][0], svc.coef_[0][1], svc.intercept_[0], svc

points = []
line = (0, 0, 0)

def count_x(line, y):
    return (-line[2] - line[1] * y) / line[0]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                point = Point(event.pos[0], -event.pos[1], 0, 'red')
                points.append(point)
                show_point(point)
            elif event.button == 3:
                point = Point(event.pos[0], -event.pos[1], 1, 'blue')
                points.append(point)
                show_point(point)
            elif event.button == 2:
                color = 'black'
                if line[1]*-event.pos[1] + line[0]*event.pos[0] + line[2] > 0:
                    point = Point(event.pos[0], -event.pos[1], 1, 'blue')
                    points.append(point)
                    show_point(point)
                else:
                    point = Point(event.pos[0], -event.pos[1], 0, 'red')
                    points.append(point)
                    show_point(point)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                line = fit(points)
                x1 = count_x(line, -599)
                x2 = count_x(line, 0)
                pg.draw.line(sc, 'white', (x1, 599), (x2, 0))


                pg.display.update()