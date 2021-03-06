import math
from typing import List
import numpy as np
vertex_number = int(input())
vertex = np.array([list(map(int, input().split())) for i in range(vertex_number)])

for i in range(0, round(1e10)):
    avg = round(np.sum(vertex[:, 0]) / vertex_number)
    if not avg - i in vertex[:, 0]:
        x = avg - i
        break
    elif not avg + i in vertex[:, 0]:
        x = avg + i
        break

for i in range(0, round(1e10)):
    round((np.max(vertex[:, 1]) + np.min(vertex[:, 1])) / 2)
    avg = round(np.sum(vertex[:, 1]) / vertex_number)
    if not avg - i in vertex[:, 0]:
        y = avg - i
        break
    elif not avg + i in vertex[:, 0]:
        y = avg + i
        break


center = [x, y]
f_area = 0


def GetAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return ang + 360 if ang < 0 else ang


def triangle(t1, t2, t3):
    x1, y1 = t1[0], t1[1]
    x2, y2 = t2[0], t2[1]
    x3, y3 = t3[0], t3[1]
    a = math.hypot(x1 - x2, y1 - y2)
    b = math.hypot(x2 - x3, y2 - y3)
    c = math.hypot(x3 - x1, y3 - y1)
    p = (a + b + c) / 2
    return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 4)


def add_or_not(n):
    n = n + vertex_number
    x, y = center[0], center[1]
    v_x, v_y = vertex[(n + 1) % vertex_number][0], vertex[(n + 1) % vertex_number][1]
    n_x, n_y = v_x - x, v_y - y
    c_x, c_y = vertex[n % vertex_number][0] - x, vertex[n % vertex_number][1] - y
    next_slope = n_y / n_x
    if not is_it_clockwise:
        if n_x > 0:
            if c_y < next_slope * c_x:
                return True
            else:
                return False
        elif n_x < 0:
            if c_y > next_slope * c_x:
                return True
            else:
                return False
        else:
            if c_x < next_slope * c_x:
                return True
            else:
                return False
    if is_it_clockwise:
        if n_x > 0:
            if c_y > next_slope * c_x:
                return True
            else:
                return False
        elif n_x < 0:
            if c_y < next_slope * c_x:
                return True
            else:
                return False
        else:
            if c_y < next_slope * c_x:
                return True
            else:
                return False


def is_clockwise():
    degree_list: List[float] = []
    for i in range(vertex_number):
        v1 = vertex[i]  # 1
        v2 = vertex[(i + 1) % vertex_number]  # 2
        v3 = vertex[(i + 2) % vertex_number]  # 3
        degree_list.append(GetAngle(v1, v2, v3))
    total_degree = round((sum(degree_list)), 2)
    if total_degree == 180 * (vertex_number - 2):
        return True
    else:
        return False


is_it_clockwise = is_clockwise()
triangle_add = [add_or_not(i) for i in range(vertex_number)]
triangle_areas = [triangle(center, vertex[j], vertex[(j + 1) % vertex_number]) for j in range(vertex_number)]
for p, a in zip(triangle_add,triangle_areas):
    f_area = eval(f"{f_area}{'+'if p else'-'}{a}")
print(abs(f_area))